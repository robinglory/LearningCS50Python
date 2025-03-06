import sys
import os
import csv
from tabulate import tabulate

def read_csv(filename):
    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            data = list(reader)  # Convert CSV to a list of rows
    except FileNotFoundError:
        sys.exit("File does not exist")

    return data

def main():
    # Validate command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")

    filename = sys.argv[1]

    # Check if the file has a .csv extension
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Read CSV data
    data = read_csv(filename)

    # Print formatted table using tabulate (grid format)
    print(tabulate(data, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
