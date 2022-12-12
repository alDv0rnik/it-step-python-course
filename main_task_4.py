import csv


with open('in.csv', encoding='utf-8') as file:
    errors = 0
    result = 0
    reader_object = csv.reader(file, delimiter=",")
    for row in reader_object:
        try:
            result += float(row[int(row[0])])
        except:
            errors += 1



print(f'Result = {result}')
print(f'error_liens = {errors}')