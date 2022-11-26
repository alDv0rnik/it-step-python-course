def  get_list(n: int, lst = []) -> list:
    if n == 0:
        return lst 
    else:
        return get_list(n - 1) + [n]


print(get_list(4))