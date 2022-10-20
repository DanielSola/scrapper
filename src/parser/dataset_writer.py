import csv


class DatasetWriter:
    headers = ['title', 'artist', 'year', 'country', 'label']

    def init(self):
        with open('dataset.csv', 'w') as dataset:
            writer = csv.writer(dataset)
            writer.writerow(self.headers)

    def write_row(self, row):
        with open('dataset.csv', 'a') as dataset:
            writer = csv.writer(dataset)
            writer.writerow(row)

