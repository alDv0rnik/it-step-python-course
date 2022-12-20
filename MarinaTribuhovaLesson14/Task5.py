# Задание 5 (II). Текстовый файл in.csv (текстовые данные, разделенные запятой) содержит
# некоторую последовательность строк с любым числом элементов в каждой строке. Пусть
# начальный элемент любой строки имеет индекс 0. Его значение определяет индекс элемента в
# строке, с которым вы должны работать.
# 1. Рассчитайте сумму элементов, определяемых нулевыми элементами. Выведите этот результат
# в консоли. Формат вывода приведен в примерах ниже.
# 2. Вывести количество строк с "ошибками"
# Input: Input:
# 3,qw,4,5.2,2.7 3,qw,4,-3.1,2.7
# 15,,,k,5 1,-1,fgh,5
# 1,-3.14,fgh,5
# 0,,e1,2,3
# 2.3,a,b,c
# b,b,e
# Output: Output:
# Result (5.2 - 3.14 + 0.0) = 2.06 Result (-3.1 - 1) = -4.1
# error-lines = 3 error-lines = 0

import csv


with open('data/in.csv') as in_file:
    sum_elem = 0
    error_lines = 0
    data = list(csv.reader(in_file, delimiter=","))
    for i in data:
        try:
            sum_elem += float(i[int(i[0])])
        except:
            error_lines += 1

print(f'The sum of the elements is equal to {sum_elem}')
print(f'Number of rows with "errors" {error_lines}')

