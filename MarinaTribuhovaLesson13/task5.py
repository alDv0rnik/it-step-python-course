# Задание 5(I). Пусть дана следующая функция:
# def transform(list1, list2):
# result = []
# for i in list1:
# for j in list2:
# result.append(f"{i} + {j}")
# return result
# Напишите декоратор @reverse_list, который будет возвращать список обратный списку из
# функции выше. Выполните оптимизацию функции transform(list1, list2), если это возможно.


from functools import wraps


def revers_list(func):
    @wraps(func)
    def wrapper(list_1, list_2):
        val = func(list_1, list_2)
        val.reverse()
        return val
    return wrapper


@revers_list
def transform(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(f"{i} + {j}")
    return result


a = [5, 8, 4]
b = [7, 6, 3]
print(transform(a, b))


#oптимизация для сложения элементов листов с одинаковыми индексами
@revers_list
def transform1(list1, list2):
    result = []
    for (i, j) in zip(list1, list2):
        result.append(f"{i} + {j}")
    return result


a = [5, 8, 4]
b = [7, 6, 3]
print(transform1(a, b))









