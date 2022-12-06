def call_once(func):
    l = []
    def wrapper(*args):
        a = func(*args)
        if len(l) > 0:
            return l[0]
        else:
            l.append(a)
            return a
    return wrapper


@call_once
def sum(a, b):
    return a + b


print(sum(5, 2))
print(sum(81, 95))