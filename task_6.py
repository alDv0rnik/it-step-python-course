from __future__ import annotations
from typing import List


def split_by_index(s: str, indexes: List[int]):
    str_end = list()
    o = 0
    global i
    for i in indexes:
        if i < len(s):
            str_end.append(s[o:i])
            o = 0
            o += i
        elif len(s) == i:
            str_end.append(s[o:])
            break
        elif i > len(s):
            continue
    return str_end


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 10, 546, 12, 13, 666, 18, 21, 25, 26]))
