from math import sqrt

a_1 = 7
b_1 = 2
c_1 = 8


def triangle_perimeter(a=a_1, b=b_1, c=c_1): return a + b + c


def triangle_area(a=a_1, b=b_1, c=c_1):
    p = 0.5 * (a + b + c)
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s
