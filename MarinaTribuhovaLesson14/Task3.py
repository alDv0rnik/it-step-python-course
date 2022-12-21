# Задание 3 (I). Реализовать функцию поиска наиболее распространенных слов в файле.
# Используйте файл data/lorem_ipsum.txt. ПРИМЕЧАНИЕ: Помните о точках, запятых, заглавных
# буквах и т.д.
# def most_common_words(filepath, number_of_words=3):
# pass
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']


#для подсчета количества и автоматического создания словаря
from collections import Counter
#для преобразования строки в список по нескольким разделителям
import re


def most_common_words(filepath, number_of_words=3):
    with open(filepath, 'r') as in_file:
        str_read = in_file.read().lower()
    lst_read = re.split(r'[,;. \n]+', str_read)  # разделит строку по символам
    counter = Counter(lst_read) # создаст oбъект Counter co словарем ключ-слово, значение-сколько раз повторяестя, по убыванию
    lst_max = counter.most_common()  # список из tuple
    lst_most_max = []
    for i in range(number_of_words):
        lst_most_max.append(lst_max[i][0])
    return lst_most_max


print(most_common_words('data/lorem_ipsum.txt'))


