def func(list_of_nums: list):
    """функция принимает список и возвращает его уникальную копию
    list_of_nums: список с повтаряющимися эллементами"""
    return list(set(list_of_nums))


list_of_nums = [1, 2, 43, 12, 99, 99, 2, 43, 1, 2, 1]


print(func(list_of_nums))