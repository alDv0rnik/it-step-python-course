from math import pi

default_radius = 5


def circle_perimeter(radius=default_radius):
    return round(2 * pi * radius, 2)


def circle_area(radius=default_radius):
    return round(pi * radius ** 2, 2)
