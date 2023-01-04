# Задание 3 (I). Написать функцию, которая принимает 2 параметра data и new_value. Если data
# это список или множество, то добавить в него элемент new_value, если строка, то
# сконкатенировать (за исключением, если new_value не список, иначе вернуть не измененную
# data), а если это число, логическое значение или словарь, то вернуть не измененную data.


def func1(data, new_value):
    if isinstance(data, list):
        data.append(new_value)
    elif isinstance(data, set):
        data.add("44")
    elif isinstance(data, str):
        if isinstance(new_value, list):
            return data
        else:
            data += new_value
    elif isinstance(data, int | bool | dict):
        return data
    else:
        raise ValueError("No changes for this data type")
    return data


list1 = ['a', 'e', 'i']
print(func1(list1, "44"))
set1 = {"a", "s", "5"}
print(func1(set1, "44"))
str1 = "Hello world!!!"
print(func1(str1, "44"))
print(func1(str1, ["a", 'b', 'c']))
int1 = 55
print(func1(int1, 44))
bool1 = False
print(func1(bool1, "44"))
dict1 = {1: "one", 2: "two", 3: "three"}
print(func1(dict1, "44"))
#проверка, если data tuple
# tuple1 = ('t', "u", "p")
# print(func1(tuple1, "44"))



