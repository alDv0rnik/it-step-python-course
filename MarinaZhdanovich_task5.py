import csv

with open('data/in.csv', 'r') as file:
    result = 0
    errors = 0
    data = csv.reader(file, delimiter=",")
    for row in data:
        try:
            result += float(row[int(row[0])])
        except:
            errors += 1

print(f'Result = {result}')
print(f'error-lines = {errors}')
