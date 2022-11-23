from typing import Tuple, List
def get_pairs(lst: List) -> List[Tuple]:
    l = []
    if len(lst) == 1:
        return None
    else:
        for i in range(len(lst) - 1):
            l.append((lst[i], lst[i + 1]))
        return l


pairs = input('Enter list: ')
print(get_pairs(pairs))

















