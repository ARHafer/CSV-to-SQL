from csv_reader import get_headers, stream_csv, validate_csv
from schema_handler import assign_schema
from sql_generator import generate_sql

# Game Plan:
# 1) Prompt user for .csv file path and data type of each header.
# 2) Use data type info to create "schema" dictionary. Key = header, value = data type.
# 3) Parse .csv file into a stream of dictionaries. Key = header, value = column data.
# 4) Use schema to determine if a column's data is printed in 'single quotes' or not.
# 5) Generate SQL table insert command with parsed .csv file and print into console.
# Ready, break!

while True:
    filepath = input("Enter .csv file path: ")

    try:
        validate_csv(filepath)
        break
    except FileNotFoundError:
        print("File not found, please enter a valid file path.\n")
    except EOFError:
        print("File is empty, please enter the path of a valid file.\n")
    except ValueError as error:
        print(error)
        print("Please enter the path of a valid file.\n")

headers = get_headers(filepath)
schema = assign_schema(headers)
csv_stream = stream_csv(filepath)

table_name = input("\nEnter SQL table name: ")
generate_sql(csv_stream, schema, table_name)