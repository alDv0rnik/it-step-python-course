from decorators import revers


@revers
def transform(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(f"{i} + {j}")
    return result


transform(["arten", "hanna"], ["vitali", "alla"])


def transform(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(f"{i} + {j}")
    return result


print(transform(["arten", "hanna"], ["vitali", "alla"]))