def do_twice(func):
    def wrapper(*args, **kwargs):
        result1 = func(*args, **kwargs)
        result2 = func(*args, **kwargs)
        return result1, result2
    return wrapper


@do_twice
def say_hello(name):
    print(f'Hello {name}')


say_hello('Marina')


