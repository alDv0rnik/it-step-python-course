def rec_list(n: int, lst=[]) -> list:
    res = []
    if n:
        res = rec_list(n - 1) + [n]
    return res


print(rec_list(4))

