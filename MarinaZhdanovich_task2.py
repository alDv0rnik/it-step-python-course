import time


def timer(func):
    def wrapper(i):
        start = time.time()
        result = func(i)
        end = time.time() - start
        print(f'Execution time for {func.__name__} is {end} sec')
        return result
    return wrapper


@timer
def get_fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return get_fib(n-1) + get_fib(n-2)


print(get_fib(10))
