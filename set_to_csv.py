import csv

input_file_path = input("name of dataset")
output_file_path = 'output.csv'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['Text', 'Label'])
    for line in input_file:
        label, text = line.split('   ', maxsplit=1)
        text = text.strip()
        label = 1 if label.lower() == 'y' else 0
        csv_writer.writerow([text, label])
print(f'Conversion completed. CSV file saved at: {output_file_path}')
