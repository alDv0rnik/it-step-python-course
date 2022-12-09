import time

def timer(func):
    def wrapper(i):
        st = time.time()
        val = func(i)
        end = time.time() - st 
        print(f"Time for {func.__name__} is {end} sec")
        return val 
    return wrapper 



@timer
def fib(n):
    fib1 = fib2 = 1
    while n-2 > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    print(fib2)


fib(10)