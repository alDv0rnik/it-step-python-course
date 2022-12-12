import csv
from operator import itemgetter


def get_top_performers(file_path, number_of_top_students=5):
    dict_of_students = {}
    with open(file_path, encoding='utf-8') as r_file:
        reader_object = csv.DictReader(r_file, delimiter=",")
        for row in reader_object:
            dict_of_students[row["student name"]] = float(row["average mark"])

    list_of_values = list(reversed(sorted(dict_of_students.values())))

    result = []
    for i in list_of_values:
        for k, v in dict_of_students.items():
            if v == i and k not in result:
                result.append(k)

    print(result[0:number_of_top_students])


def sort_age(filepath):
    list_ = []
    with open(filepath, encoding='utf-8') as file:
        for row in file:
            list_.append(row.replace('\n', '').split(','))

    sorted_list = sorted(list_, key=itemgetter(1), reverse=True)

    with open('sorted_students.csv', mode='w', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\r')
        for i in sorted_list:
            file_writer.writerow(i)


get_top_performers('students.csv')
sort_age("students.csv")




