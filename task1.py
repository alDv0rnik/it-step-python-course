import time


def timer(function):
    def wrapper(i):
        start = time.time()
        val = function(i)
        end = time.time() - start
        print(f"Execution time for {function.__name__} is {end} sec")
        return val
    return wrapper


@timer
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


fib = int(input('Введите число Фиббоначи: '))
print(fibonacci(fib))