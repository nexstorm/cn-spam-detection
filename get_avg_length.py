import csv

def getAvgLength(input_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        data_0 = 0
        data_1 = 0
        data_0_count = 0
        data_1_count = 0


        for row in reader:
            label = row[1]
            if label == "0":
                data_0 += len(row[0])
                data_0_count += 1
            else:
                data_1 += len(row[0])
                data_1_count += 1
    print("Non-spam data average length: " + str(data_0 / data_0_count))
    print("Spam data average length: " + str(data_1 / data_1_count))


if __name__ == "__main__":
    input_file = "output.csv"
    getAvgLength(input_file)

#%%
