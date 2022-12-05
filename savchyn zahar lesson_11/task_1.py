def get_list(n: int, lst = []) -> list:
    if n > 0:
        lst = get_list(n-1) + [n]
    return lst

print(get_list(4))