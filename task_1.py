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
def fibonachy(n):
    fib1 = fib2 = 1
    while n-2 > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    print("Значение этого элемента:", fib2)


fibonachy(25)