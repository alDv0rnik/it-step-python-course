def revers_list(func):
    def wrapper(l1, l2):
        a = func(l1, l2)
        b = list(reversed(a))
        return b
    return wrapper


@revers_list
def transform(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(f'{i}+{j}')
    return result

l1 = [1, 2, 3]
l2 = [2, 3, 4]
print(transform(l1, l2))