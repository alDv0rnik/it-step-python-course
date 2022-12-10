import time

# for task_2


def fib_time(func):
    def wrapper(a):
        start = time.time()
        res = func(a)
        print(f"Time for function work =  {time.time() - start}")
        return res

    return wrapper


# for task_3


def mult(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        # print(func(*args, **kwargs), func(*args, **kwargs))
    return wrapper


# for task_4

def cash_clean():
    """
    if you will call this func, it will clear the values written to memory (myfile.txt) each time
    """
    with open('myfile.txt', 'w+') as clean_list:
        clean_list.seek(0)


def call_once(func):
    def wrapper(*a):
        val = func(*a)
        with open("myfile.txt", "a") as cash:
            cash.write("%s\n" % val)
        with open("myfile.txt", "r") as cash:
            cash_list = [i.strip() for i in cash.readlines()]
            print(f"cash memory: {cash_list}")
            return int(cash_list[0])

    return wrapper


# for task_5


def revers(func):
    reversed_list = []

    def wrapper(list1=list, list2=list):
        val = func(list1, list2)
        for i in val:
            reversed_list.insert(0, i)
        print(reversed_list)

    return wrapper



