from csv_reader import get_headers
from schema_handler import assign_schema

# Game Plan:
# 1) Prompt user for .csv file path and data type of each header.
# 2) Use data type info to create "schema" dictionary. Key = header, value = data type.
# 3) Parse .csv file into a stream of dictionaries. Key = header, value = column data.
# 4) Use schema to determine if a column's data is printed in 'single quotes' or not.
# 5) Generate SQL table insert command with parsed .csv file and print into console.
# Ready, break!

filepath = input("Enter .csv file path: ")
headers = get_headers(filepath)
schema = assign_schema(headers)

print(schema)