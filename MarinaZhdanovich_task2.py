def get_list(n: int) -> list:
    lst = []
    if n > 0:
        lst = get_list(n - 1)
        lst.append(n)
    return lst


print(get_list(4))


