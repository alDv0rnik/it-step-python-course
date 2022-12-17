import csv


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, "r") as file:
        data = list(csv.reader(file, delimiter=","))
    result = {}
    for row in data[1:]:
        result[row[0]] = float(row[2])
    final = sorted(result.items(), key=lambda item: item[1], reverse=True)
    return list(dict(final[0: number_of_top_students]))


print(get_top_performers("data/students.csv"))


def get_top_age(file_path):
    with open(file_path, "r") as file:
        data = list(csv.reader(file, delimiter=","))
    result = {}
    for row in data[1:]:
        result[row[0], row[2]] = int(row[1])
    final_age = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

    with open('sorted students.csv', 'w') as file:
        file.write(f'student name,age,average mark\n')
        for key, value in final_age.items():
            i, j = key
            file.write(f'{i},{value}, {j}\n')
    return final_age


print(get_top_age("data/students.csv"))






