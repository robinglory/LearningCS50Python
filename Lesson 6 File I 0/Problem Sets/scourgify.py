import sys
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, newline='') as infile:
            reader = csv.DictReader(infile)
            students = []
            
            for row in reader:
                last, first = row["name"].split(", ")  # Split into first and last name
                students.append({"first": first, "last": last, "house": row["house"]})
        
        with open(output_file, mode='w', newline='') as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
    
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


if __name__ == "__main__":
    main()
