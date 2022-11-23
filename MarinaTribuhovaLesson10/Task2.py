# Задание 2 (I). Напишите функцию concat, которая будет принимать произвольное число строк и
# объединять их в одну.


def concat(*string: str) -> str:
    return "".join(string)


print(concat("abc", "defg", "hi"))

