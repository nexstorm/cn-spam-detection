import sys

def remove_duplicates(input_file, output_file):
    seen_lines = set()

    with open(output_file, 'w') as out_file:
        with open(input_file, 'r') as in_file:
            for line in in_file:
                if line not in seen_lines:
                    out_file.write(line)
                    seen_lines.add(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 removeduplicates.py input_file")
    else:
        input_file = sys.argv[1]
        output_file = "output.csv"
        remove_duplicates(input_file, output_file)
