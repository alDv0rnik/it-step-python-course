# Длина окружности С = 2*pi * r**2
# Площадь окружности s = pi * r**2
from math import pi

DEFAULT_RADIUS = 5


def circle_perimetr(r=DEFAULT_RADIUS):
    c = round(2 * (pi * r**2), 2)
    return f"Длина окружности равна: {c}"


def circle_area(r=DEFAULT_RADIUS):
    s = round(pi * r**2, 2)
    return f"Площадь окружности равна: {s}"
