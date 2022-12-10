# Задание 3(I). Написать декоратор @do_twice, который будет вызывать любую функцию дважды
import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@do_twice
def student(name):
    print(f"I am student {name}!")


student("Marina")


