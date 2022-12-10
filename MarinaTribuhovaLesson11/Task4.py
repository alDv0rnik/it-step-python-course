# Задача 4 (I) Написать рекурсивную функцию get_fib(n: int) -> int поиска значения n-го числа
# Фибоначчи
# Input: get_fib(6)
# Output: 8


def get_fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return get_fib(n - 2) + get_fib(n - 1)


print(get_fib(6))