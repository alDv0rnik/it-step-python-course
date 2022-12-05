# Периметр квадрата равен P = a * 4
# Площадь квадрата равна S = a**2

A = 15


def square_perimetr(a=A):
    p = round(a * 4, 2)
    return f"Периметр квадрата: {p}"


def square_area(a=A):
    s = round(a**2, 2)
    return f"Площадь квадрата: {s}"


