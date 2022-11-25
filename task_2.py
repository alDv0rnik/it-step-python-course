

def get_list(n: int, lst=list()) -> list:
    if n > 0:
        get_list(n - 1)
        lst.append(n)
    return lst


print(get_list(5))





