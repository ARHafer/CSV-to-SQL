import csv

def validate_csv(filepath):
    with open(filepath) as file:
        reader = csv.reader(file)
        headers = next(reader)

        if not headers:
            raise EOFError
        else:
            num_headers = len(headers)

            for line, row in enumerate(reader, start = 2):
                if len(row) != num_headers:
                    raise ValueError(f"Error: Malformed data found at file line {line}.")

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