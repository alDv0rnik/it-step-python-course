# периметр треугольника равен P = a + b + c
# площадь треугольника равна S = 0.5 * a * h

A = 7
B = 2
C = 8


def triangle_perimetr(a=A, b=B, c=C):
    p = round(a + b + c, 2)
    return f"Периметр треугольника равен: {p}"


def triangle_area(a=A):
    h = int(input('Введите высоту треугольника: '))
    s = round(0.5 * a * h, 2)
    return f"Площадь треугольника равна: {s}"
