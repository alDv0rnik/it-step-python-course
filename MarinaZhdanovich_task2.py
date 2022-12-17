with open('data/unsorted_names.txt', 'r') as file:
    names = sorted(file.readlines())

with open('sorted_names.txt', 'w') as file:
    file.writelines(names)


