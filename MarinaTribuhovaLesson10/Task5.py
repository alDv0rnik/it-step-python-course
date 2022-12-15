# Задание 5 (I). Реализовать функцию generate_squares(i: int) -> dict(int: int), которая принимает
# число в качестве аргумента и возвращает словарь, где ключ - это число, а значение - квадрат этого
# числа.
# Вход: print(generate_squares(5))
# Выход: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
from typing import Dict


def generate_squares(i: int) -> Dict:
    d = {i: i ** 2 for i in range(1, i + 1)}
    return d


a = int(input("Enter the number of dictionary elements: "))
print(generate_squares(a))


