def search_value(i: int, lst=[]) -> bool:
    if i in lst:
        return True
    for check_list in lst:
        if type(check_list) == list:
            return search_value(i, check_list)
    return False


print(search_value(3, [1, 2, [3, 4, [5, [6, []]]]]))