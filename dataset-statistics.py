char_count = {}
file = input("dataset name: ")
with open(file, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            first_char = line[0]
            if first_char in char_count:
                char_count[first_char] += 1
            else:
                char_count[first_char] = 1

print("First character statistics:")
for char, count in char_count.items():
    print(f"'{char}': {count} times")
