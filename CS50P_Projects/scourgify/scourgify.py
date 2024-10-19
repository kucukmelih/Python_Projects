import csv
import os
import sys

def func(before, after):
    try:
        with open(before, mode='r', newline='') as infile:
            reader = csv.DictReader(infile)

            new_headers = ['first', 'last', 'house']
            with open(after, mode='w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=new_headers)
                writer.writeheader()

                for row in reader:
                    if row:
                        name_column = row['name']
                        house_column = row['house']

                        if ',' in name_column:
                            last_name, first_name = name_column.split(', ', 1)
                        else:
                            last_name, first_name = name_column, ''

                        new_row = {
                            'first': first_name,
                            'last': last_name,
                            'house': house_column
                        }
                        writer.writerow(new_row)
                    else:
                        print("Empty row encountered")  

        print(f"Data from {before} has been transformed and saved to {after}")

    except Exception as e:
        sys.exit(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")
    before = sys.argv[1]
    after = sys.argv[2]
    if before.endswith(".csv") and after.endswith(".csv"):
        if os.path.exists(before):
            func(before, after)
        else:
            sys.exit("Input file does not exist")
    else:
        sys.exit("Both arguments must be CSV files")

if __name__ == "__main__":
    main()
