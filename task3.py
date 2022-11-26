def get_fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return get_fib(n-2) + get_fib(n - 1)

print(get_fib(6))