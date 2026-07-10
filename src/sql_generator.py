def generate_sql(csv_stream, schema, table_name):
    build_insert_statement(schema, table_name)

    # If a row is being read, print the previous row with a comma (if not first) and store the current.
    # If the last row was already read, print the stored row with a semicolon.
    first = True
    for row in csv_stream:
        if first:
            first = False
            buffer = row
        else:
            formatted_row = format_row(buffer, schema)
            print(f"({formatted_row}),")
            buffer = row

    formatted_row = format_row(buffer, schema)
    print(f"({formatted_row});")

def build_insert_statement(schema, table_name):
    columns = list()

    for header in schema:
        columns.append(header)

    sql_columns = ", ".join(columns)
    print(f"\nINSERT INTO {table_name} ({sql_columns}) VALUES")

def format_row(row, schema):
    formatted_data = list()

    for header, data in row.items():
        if schema[header] == "quoted":
            formatted_data.append(f"'{data}'")
        else:
            formatted_data.append(data)

    return ", ".join(formatted_data)

