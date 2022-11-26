# Задание 6 (II). Реализовать функцию split_by_index(s: str, indexes: List[int]) -> List[str], которая
# делит строку s с помощью индексов, указанных в indexes. Неправильные индексы должны быть
# проигнорированы.
# Вход: split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# Выход: ["python", "is", "cool", ",", "isn't", "it?"]

from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    result = []
    i = 0
    for elem in indexes:
        #игнорируем неправильные индексы
        if elem < 0:
            continue
        result.append(s[i:elem])
        i = elem
    return result


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
# игнорируем нерпвильные индексы
print(split_by_index("pythoniscool,isn'tit?", [-3, 8, 12, -20, 18]))

