# Задание 4(I). Реализуйте декоратор @call_once, который запускает функцию или метод один раз
# и кэширует (сохраняет) результат. Все последовательные вызовы этой функции должны
# возвращать кэшированный результат независимо от аргументов
# @call_once
# def sum_of_numbers(a, b):
# return a + b
# print(sum_of_numbers(13, 42))
# >>> 55
# print(sum_of_numbers(999, 100))
# >>> 55

from functools import wraps


def call_once(func):
    lst = []#лист для хранения количества возвратов из функции

    @wraps(func)
    def wrapper(*args):
        val = func(*args)
        if len(lst) > 0:
            return lst[0]
        else:
            lst.append(val)
            return val
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))





