def call_once(func):
    s = []
    def wrapper(*args):
        res = func(*args)
        if len(s) > 0:
            return s[0]
        else:
            s.append(res)
            return res
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(2, 8))
print(sum_of_numbers(10, 15))










