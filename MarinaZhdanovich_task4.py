def func(value):
    result = []
    for i in value:
        if i not in result:
            result.append(i)
    return result


test = func([1, 15, 35, 4, 1, 15])
print(test)
