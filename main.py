from csv_reader import get_headers, stream_csv
from schema_handler import assign_schema
from sql_generator import generate_sql

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

table_name = input("\nEnter SQL table name: ")
csv_stream = stream_csv(filepath)
generate_sql(csv_stream, schema, table_name)