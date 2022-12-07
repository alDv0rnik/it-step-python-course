def reverse_list(func):
    def wrapper(*args, **kwargs):
        a = func(*args, *kwargs)
        b = list(reversed(a))
        return b
    return wrapper


@reverse_list
def transform(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(f"{i} + {j}")
    return result


l1 = [5, 10, 15]
l2 = [20, 25, 30]
print(transform(l1, l2))
