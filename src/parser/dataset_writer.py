import csv

#Class to handle dataset
class DatasetWriter:
    headers = ['title', 'artist', 'year', 'country', 'label']

    # Create the dataset CSV file and write its headers
    def init(self):
        with open('dataset.csv', 'w') as dataset:
            writer = csv.writer(dataset)
            writer.writerow(self.headers)

    # Append a row to dataset file
    def write_row(self, row):
        with open('dataset.csv', 'a') as dataset:
            writer = csv.writer(dataset)
            writer.writerow(row)

