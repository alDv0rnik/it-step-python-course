# Задание 4* (II). Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е.
# ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся
# последовательности. Программа должна возвратить словарь из 3-х самых часто встречаемых
# чисел.
# Вход: 10591351
# Выход: {5: 2, 1: 3, 3: 1}

import random
str1 = ""
for i in range(10):
    str1 += str(random.randint(0, 9))
print(str1)
d = {int(item): str1.count(item) for item in str1}
print(d)
d_max = {}
count_max = 0 #подсчет максимальных значений
for key, value in d.copy().items():
    if value == max(d.copy().values()):
        d_max[key] = d.pop(key)
        count_max += 1
        if count_max == 3:
            break
#если макимальных меньше 3, значит остальные значения равны, берем 1 значение
# из получившего словаря без максимальных
if count_max < 3:
    for i in range(0, 3-count_max):
        for key, value in d().items():
            d_max[key] = d.pop(key)
print(d_max)


