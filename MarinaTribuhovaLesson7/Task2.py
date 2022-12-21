# Задание 2 (I). Напишите программу, которая считает количество символов в строке (игнорирует
# регистр) Для решения задачи можно использовать класс Counter из модуля collections
# (https://www.digitalocean.com/community/tutorials/python-counter-python-collections-counter )
# Вход: 'Oh, it is python'
# Выход: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
from collections import Counter
str1 = 'Oh, it is python'
str1 = str1.lower()
counter = Counter(str1)
print(counter)
