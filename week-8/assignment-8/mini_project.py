import csv

path = "../data/messy_data.csv"

clean_data = []
skipped_rows = []
rows_attempted = 0

try:
    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file)  
        
        for row_number, row in enumerate(reader, start=1):
            rows_attempted += 1

            if None in row:
                skipped_rows.append(f"Row {row_number}: extra column detected - skipped")
                continue
            try:
                row["amount"] = float(row["amount"])
            except ValueError as e:
                skipped_rows.append(f"Row {row_number}: Value Error - {e}")
            except KeyError as e:
                 skipped_rows.append(f"Row {row_number}: Key Error - {e}")
            except TypeError as e:
                skipped_rows.append(f"Row {row_number}: Type Error - {e}")

            else:
                clean_data.append(row)
        

except FileNotFoundError:
    print(f"Error: {path} was not found.")


else:
    print("=== CSV Report ===")
    print(f"Rows attempted: {rows_attempted}")
    print(f"Rows Parsed: {len(clean_data)}")
    print(f"Rows skipped: {len(skipped_rows)}")
    
    print("\nSkipped rows:")
    
    for error in skipped_rows:
        print(f"    {error}")

    print("\nClean data:")
    for row in clean_data:
        print(f"{row['name']} | {row['category']} | ${row['amount']:.2f}")

