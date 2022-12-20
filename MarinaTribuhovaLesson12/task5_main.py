# Задание 5 (II). Создайте пакет 'figures', состоящий из трех подпакетов: 'triangle', 'circle', 'square'.
# В каждом подпакете будем иметь файл code.py, где создадим ряд функций:
#  для пакета 'circle': функции circle_perimeter() – вычисляет длину окружности, circle_area()
# - вычисляет площадь окружности. Еще заведем переменную default_radius = 5, которая
# будет скрыта при импорте модуля. Ее назначение – дефолтный радиус для окружности,
# если пользователь не введет свой. Обе функции принимают на вход только радиус.
#  для пакета 'triangle': функции triangle_perimeter() – вычисляет периметр треугольника,
# triangle_area() – вычисляет площадь фигуры. Дополнительно создадим три переменные
# (длины сторон треугольника): a = 7, b = 2, c = 8, которые также не будут видны при
# импорте.
#  На вход функциям передается длина трех сторон (если пользователь ничего не введет, то
# используются значения по умолчанию).
#  для пакета 'square': функции square_perimeter() – вычисляет периметр квадрата,
# square_area() – вычисляет площадь фигуры. Дополнительная переменная a = 15 не
# доступна при импорте и принимается функциями, если пользователь не предоставил свои
# размеры стороны квадрата.
# Ваша итоговая задача – позволить человеку, загрузившему ваш пакет, иметь возможность
# напрямую импортировать все функции из подпакетов. Например, он может написать так: 'from
# figure import circle_area'.

from figures import circle_area
from figures import circle_perimeter
from figures import triangle_area
from figures import triangle_perimeter
from figures import square_area
from figures import square_perimeter


print(f"circle area = {circle_area()}")
print(f"circle perimeter = {circle_perimeter()}")
print(f"triangle area = {triangle_area()}")
print(f"triangle perimeter = {triangle_perimeter(5,6,8)}")
print(f"square area = {square_area(8)}")
print(f"square perimeter = {square_perimeter()}")




