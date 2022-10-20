from time import sleep
import requests
from bs4 import BeautifulSoup
from parser.dataset_writer import DatasetWriter

from parser.row_parser import TableRowParser


class PageScrapper:
    base_url = "https://www.discogs.com/es"
    category = 'artist'
    artist = '15885-Michael-Jackson'
    type = 'Releases'
    subtype = 'Singles-EPs'
    url = f'{base_url}/{category}/{artist}?type={type}&subtype={subtype}'

    dataset = DatasetWriter()
    total_results = 0

    def scrape(self):
        self.dataset.init()

        page_num = 1

        while True:
            page = self._fetch_page(page_num)

            if page.status_code != 200:
                print(f'Finished! Results: {self.total_results}')
                break

            print(f'--- Scrapping page {page_num} ---')

            self._scrape_page(page)
            page_num += 1
            sleep(2)

        return

    def _scrape_page(self, page):
        soup = self._get_soup(page)

        results = soup.find('table').find_all('tr', class_='card')

        print(f'Results: {len(results)} ')

        for tr in results:
            parser = TableRowParser(tr)

            title = parser.get_title()
            artist = parser.get_artist()
            year = parser.get_year()
            country = parser.get_country()
            label = parser.get_label()

            self.dataset.write_row([title, artist, year, country, label])

        self.total_results += len(results)

    def _fetch_page(self, page_num):
        headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
        return requests.get(f'{self.url}&page={page_num}', headers=headers)

    def _get_soup(self, page):
        return BeautifulSoup(page.content, 'html.parser')
