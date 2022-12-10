from decorators import fib_time


def fib(a):
    if a == 1 or a == 2:
        return a
    else:
        return fib(a - 2) + fib(a - 1)


# we call a help function to work out the recursion in it and calculate the time
# if not the decorator will count time each step of the recursion


@fib_time
def helper(b):
    fib(b)


helper(36)
