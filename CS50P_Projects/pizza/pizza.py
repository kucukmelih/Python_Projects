from tabulate import tabulate
import csv
import sys
import os

def display(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    print(tabulate(data, headers='firstrow', tablefmt='grid'))

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        if filename.endswith(".csv"):
            if os.path.exists(filename):
                display(filename)
            else:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CSV file")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()
