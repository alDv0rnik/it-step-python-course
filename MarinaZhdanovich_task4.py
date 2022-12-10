def call_once(func):
    list_res = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(list_res) > 0:
            return list_res[0]
        else:
            list_res.append(result)
        return result
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))



