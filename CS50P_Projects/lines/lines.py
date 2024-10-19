import sys
import os

def count_code_lines(filename):
    code_lines = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith("#"):
                    code_lines += 1
    except FileNotFoundError:
        print(f"File '{filename}' does not exist")
    return code_lines

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        if filename.endswith(".py"):
            if os.path.exists(filename):
                num_lines = count_code_lines(filename)
                print(num_lines)
            else:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a Python file")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()
