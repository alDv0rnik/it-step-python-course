# Задание 3 (I) Даны два списка одинаковой длины. Необходимо создать из них словарь таким
# образом, чтобы элементы первого списка были ключами, а элементы второго — соответственно
# значениями нашего словаря.
# Вход: [“a”, “b”, “c”, “d”]
# [1, 2, 3, 4]
# Выход: {“a”: 1, “b”: 2, “c”: 3, “d”: 4}
l1 = ["a", "b", "c", "d"]
l2 = [1, 2, 3, 4]
d = {}
for i in range(len(l1)):
    d[l1[i]] = l2[i]
print(d)
