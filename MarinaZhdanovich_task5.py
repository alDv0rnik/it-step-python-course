def revers_list(func):
    def wrapper(l1, l2):
        result = func(l1, l2)
        revers = list(reversed(result))
        return revers
    return wrapper


@revers_list
def transform(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(f"{i} + {j}")
    return result


print(transform([1, 2, 3], [4, 5, 6]))


@revers_list
def transform1(list1, list2):
    return [f"{i} + {j}" for i in list1 for j in list2]


print(transform1([1, 2, 3], [4, 5, 6]))



