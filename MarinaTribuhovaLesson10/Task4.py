# Задание 4 (II). Реализовать функцию get_pairs(lst: List) -> List[Tuple], которая возвращает список
# из кортежей, содержащих пары элементов. Пары следует формировать так, как показано в
# примере. Если в списке есть только один элемент, то вернуть None
# Вход: get_pairs([1, 2, 3, 8, 9])
# Выход: [(1, 2), (2, 3), (3, 8), (8, 9)]
# Вход: get_pairs(['need', 'to', 'sleep', 'more'])
# Выход: [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
from typing import Tuple, List

def get_pairs(lst: List) -> List[Tuple] | None:
    lst1 = []
    if len(lst) == 1:
        return None
    else:
        for i in range(len(lst) - 1):
            lst1.append((lst[i], lst[i + 1]))
        return lst1


print(get_pairs([10]))
print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))





