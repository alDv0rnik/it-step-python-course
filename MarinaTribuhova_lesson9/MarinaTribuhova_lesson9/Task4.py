# Задание 4 (I). Напишите функцию func, которая принимает список и возвращает его уникальную
# копию в исходном порядке, то есть каждый элемент входит в список ровно один раз. Элементы в
# списке принимают значения от 0 до 100.
# Вход: [1, 15, 35, 4, 1, 15]
# Выход: [1, 15, 35, 4]

from random import randint


def func(list1: list):
    list_unique = []
    for i in list1:
        if i not in list_unique:
            list_unique.append(i)
    return list_unique


list2 = []
for i in range(20):
    list2.append(randint(0, 100))
print(f"Our list of random numbers is {list2}")
print(f"List of unique numbers is {func(list2)}")

