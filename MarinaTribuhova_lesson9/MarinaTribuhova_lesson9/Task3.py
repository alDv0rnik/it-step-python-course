# Задание 3 (II). Напишите функцию 'increase_g`, которая будет возвращать результат выполнения
# функции `g` увеличенный на 1. Т.е. если функция g() возвращает 1, то ваша функция в таком
# случае будет возвращать 2.

def g(): return 1


def increase_g(): return g() + 1


print(increase_g())
