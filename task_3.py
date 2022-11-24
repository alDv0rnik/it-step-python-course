from typing import Tuple


def get_pairs(lst: list) -> list[Tuple]:
    dct = {}
    count = 0
    if len(lst) == 1:
        return None
    else:
        for i in lst:
            if count < len(lst) - 1:
                dct[i] = lst[count + 1]
                count += 1
            else:
                return list(dct.items())

test_1 = [1, 2, 3, 8, 9]
test_2 = ['need', 'to', 'sleep', 'more']
print(get_pairs(test_2))


