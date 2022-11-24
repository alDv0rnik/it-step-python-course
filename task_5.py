from typing import List

def split_by_index(s: str, indexes: List[int]):
    result = []
    counter = 0
    for i in indexes:
        result.append(s[counter:i])
        counter = i
    result.append(s[counter:])
    return result


s = "pythoniscool,isn'tit?"
indexes = [6, 8, 12, 13, 18]
print(split_by_index(s, indexes))
