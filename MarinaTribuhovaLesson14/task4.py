# Задание 4 (I). Файл data/students.csv хранит информацию о студентах в формате CSV: имена
# студентов, возраст и среднюю отметку.
# 1. Реализуйте функцию, которая получает путь к файлу и возвращает имена лучших
# учеников
# def get_top_performers(file_path, number_of_top_students=5):
# pass
# print(get_top_performers("students.csv"))
# >>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
# 2. Реализуйте функцию, которая получает путь к файлу с информацией srudents и записывает
# информацию о студенте в новый файл csv в порядке убывания возраста. Результат:
# student name,age,average mark
# Verdell Crawford,30,8.86
# Brenda Silva,30,7.53
# ...
# Lindsey Cummings,18,6.88
# Raymond Soileau,18,7.27

import csv
from operator import itemgetter


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, "r") as file_in:
        data = list(csv.reader(file_in, delimiter=","))
    rows = data[1:]  # список без шапки
    lst_mark_first = []
    for i in rows:
        lst_mark_first.append(list(reversed(i)))  # элементы списка в обратном порядке, чтобы сортировать по оценке - первому элементу
    for i in lst_mark_first.copy():
        i[0] = float(i[0])
    lst_mark_sort = reversed(sorted(lst_mark_first))
    lst_top_students = []
    for k in lst_mark_sort:
        #print(k)
        lst_top_students.append(k[2])
    return lst_top_students[:number_of_top_students]


def write_students_age(filepath):
    with open(filepath) as in_file, open('data/sort_age.csv', "w") as out_file:
        data = list(csv.reader(in_file, delimiter=","))
        col = data[0]  # шапка
        rows = data[1:]  # список без шапки
        lst_age_sort = sorted(rows, key=itemgetter(1), reverse=True)
        data_write = csv.writer(out_file, delimiter=',')
        data_write.writerow(col)
        for row in lst_age_sort:
            data_write.writerow(row)


print(get_top_performers("data/students.csv"))
write_students_age("data/students.csv")



