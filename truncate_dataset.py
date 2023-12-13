import csv


def truncate_csv(input_file, output_file, label_column_index=1, max_lines=50000):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Assuming there's a header, adjust if not

        data_0 = []
        data_1 = []

        for row in reader:
            label = int(row[label_column_index])
            if label == 0 and len(data_0) < max_lines:
                data_0.append(row)
            elif label == 1 and len(data_1) < max_lines:
                data_1.append(row)

            if len(data_0) >= max_lines and len(data_1) >= max_lines:
                break

    truncated_data = data_0 + data_1

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(truncated_data)


if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output-100k.csv"
    truncate_csv(input_file, output_file)
