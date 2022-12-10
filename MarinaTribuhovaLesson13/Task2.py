# Задание 2(I). Напишите декоратор @timer для функции поиска n-го числа Фибоначчи, который
# будет выводить время выполнения программы.

from time import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(i):
        start = time()
        val = func(i)
        end = time()
        print(f"Execution time for {val} {func.__name__} is {end - start} sec")
        return val
    return wrapper


@timer
def get_fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return get_fib(n - 2) + get_fib(n - 1)


a = int(input("Enter the sequence number of the fibonacci number: "))

print(f"{a} number of the fibonacci is {get_fib(a)}")

