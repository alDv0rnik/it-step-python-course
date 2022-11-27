def search_value(i: int, lst=[]) -> bool:
    if i in lst:
        return True
    else:
        for j in lst:
            if type(j) == list:
                return search_value(i, j)
        return False


lst = [1, 2, [3, 4, [5, [6, []]]]]
print(search_value(3, lst))