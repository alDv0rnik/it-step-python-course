

def search_value(i: int, lst: list) -> bool:
    if i in lst:
        return True
    else:
        for j in lst:
            if type(j) == list:
                return search_value(i, j)
        return False


print(search_value(6, [1, 2, [3, 4, [5, [11, 12, 13], 6, []]]]))