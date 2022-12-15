import csv

# task 4-1


def get_top_performers(file_path, number_of_top_students=5):
    global final_dict
    with open(file_path, "r") as file:
        data = list(csv.reader(file, delimiter=","))
    rows = data[1:]
    names = {}
    bests = {}
    for row in rows:
        names[row[0]] = float(row[2])
    j = sorted(names.values(), reverse=True)

    for i in j:
        for k in names.keys():
            if names[k] == i:
                bests[k] = names[k]
        final_dict = [k for k, v in bests.items()]
    return final_dict[0: number_of_top_students]


# print(get_top_performers("data/for_task_4/students.csv"))


# task 4-2


def get_top_age(file_path):
    with open(file_path, "r") as file:
        data = list(csv.reader(file, delimiter=","))
    names = {}
    for row in data[1:]:
        names[row[0], row[2]] = int(row[1])
    name_rat = dict(sorted(names.items(), key=lambda x: x[1], reverse=True))

    with open('data/for_task_4/students_sort.csv', 'w') as file:
        file.write(f'Name,Age,Rating\n')
        for key, value in name_rat.items():
            n, r = key
            file.write(f'{n},{value}, {r}\n')
    return name_rat


print(get_top_age("data/for_task_4/students.csv"))
