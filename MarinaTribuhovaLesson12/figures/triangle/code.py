from math import sqrt

a = 7
b = 2
c = 8


def triangle_perimeter(d=a, e=b, f=c):
    return d + e + f


def triangle_area(d=a, e=b, f=c):
    p = 0.5 * (d + e + f)#полупериметр
    return round(sqrt(p * (p - d) * (p - e) * (p - f)), 2)


