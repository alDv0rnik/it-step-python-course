import csv


def get_top_performers(file_path, number_of_top_students=5):
    students = dict()
    with open('data/students.csv', 'r') as rf:
        r_object = csv.DictReader(rf, delimiter=',')
        for row in r_object:
            students[row['student name']] = float(row['average mark'])

    list_val = list(reversed(sorted(students.values())))

    res = list()
    for _ in list_val:
        for k, v, in students.items():
            if v == _ and k not in res:
                res.append(k)

    print(res[0:number_of_top_students])


get_top_performers('students.csv')



