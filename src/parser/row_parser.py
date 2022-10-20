class TableRowParser:
    def __init__(self, tr):
        self.tr = tr

    def get_artist(self):
        return self.tr.find('td', class_='artist').get_text()

    def get_title(self):
        title_data = self.tr.find('td', class_='title')
        return title_data.find('a', recursive=False).get_text()

    def get_label(self):
        return self.tr.find('td', class_="label").get_text()

    def get_country(self):
        return self.tr.find('td', class_="country").get_text()

    def get_year(self):
        return self.tr.find('td', class_="year").get_text()
