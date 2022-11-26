# Задание 2 (I) Напишите рекурсивную функцию get_list(n: int, lst=[]) -> list, чтобы сгенерировать
# и вернуть список от 1 до N. Аргументом функции является только N.
# Input: get_list(4)
# Output: [1, 2, 3, 4]

import math

def get_list(n: int, lst=[]) -> list:
    if n == 0:
        return lst
    else:
        return get_list(n-1) + [n]


print(get_list(4))

