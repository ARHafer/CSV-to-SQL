import csv

def get_headers(filepath):
    with open(filepath) as file:
        reader = csv.reader(file)
        headers = next(reader)
        return headers