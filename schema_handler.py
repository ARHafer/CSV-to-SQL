def assign_schema(headers):
    schema = dict()

    for header in headers:
        while True:
            print(f"\nSelect data type for header:\n\"{header}\"\n")
            print("[1]: String or Date/Time (Quoted)\n"
                  "[2]: Numeric or Boolean (Plain)\n")

            selection = input("> ").strip()
            if selection == "1":
                schema[header] = "Quoted"
                print(f"\n\"{header}\" values will be entered as 'quoted' text.")
                break
            elif selection == "2":
                schema[header] = "Plain"
                print(f"\n\"{header}\" values will be entered as plain text.")
                break
            else:
                print("\nInvalid selection. Please type \"1\" or \"2\".")

    return schema