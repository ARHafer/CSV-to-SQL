import csv

def get_headers(filepath):
    with open(filepath) as file:
        reader = csv.reader(file)
        headers = next(reader)
        return headers

def stream_csv(filepath):
    with open(filepath) as file:
        reader = csv.DictReader(file)

        for row in reader:
            yield row