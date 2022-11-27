def search_value(i: int, lst: list) -> bool:
    if i in lst:
        return True
    else:
        for alement in lst:
            if type(alement) is list:
                return search_value(i, alement)
        return False


lst = [1, 2, [3, 4, [5, [6, []]]]]
print(search_value(3, lst))