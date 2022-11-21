from __future__ import annotations
from typing import List


def get_pairs(lst: list) -> List | None:
    lis = list()
    if len(lst) > 1:
        for i in lst[1:]:
            lisi = list()
            lisi.append(lst[lst.index(i) - 1])
            lisi.append(lst[lst.index(i)])
            lis.append(tuple(lisi))
    else:
        return None
    return lis


print(get_pairs(["artem", "ivan", "hanna", "enot", "bober", "andrey", "ursa"]))
print(get_pairs([1, 2, 3, 4, 5, 6]))
print(get_pairs(["artem"]))
