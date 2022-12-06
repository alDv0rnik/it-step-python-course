import random


def do_twice(func):
    def wrapper(i):
        a = func(i)
        b = func(i)
        return a, b
    return wrapper



@do_twice
def random_number(n):
    print(random.randint(0, n))


random_number(25)