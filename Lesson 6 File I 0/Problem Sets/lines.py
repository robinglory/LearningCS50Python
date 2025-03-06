import sys
import os

def count_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    count = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line == "" or stripped_line.startswith("#"):
            continue
        count += 1
    print(count)

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    count_lines(filename)

if __name__ == "__main__":
    main()