def increase_g():
    return g() + 1


def g():
    return (int(input("введите число: ")))


print(increase_g())