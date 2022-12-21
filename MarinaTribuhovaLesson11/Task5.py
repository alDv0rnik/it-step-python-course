# Задание 5 (II) Напишите функцию search_value(i: int) -> bool, которая рекурсивно ищет в
# сложном объекте значение. Сложный объект - это будет список списков списков. Например, [1,
# 2, [3, 4, [5, [6, []]]]]. Функция должна рекурсивно заходить внутрь вложенных массивов, а если это
# другой тип данных игнорировать его. Возвращать логическое значение
# Input: search_value(3)
# Output: True


def search_value(i: int, lst=[]) -> bool:
    if i in lst:
        return True
    for check_list in lst:
        if type(check_list) == list:
            return search_value(i, check_list)
    return False


print(search_value(3, [1, 2, [3, 4, [5, [6, []]]]]))


