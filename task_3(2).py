# создаем функцию g(a) заранее

def g(a): return a


def increase_g(): return g(int(input())) + 1


print(increase_g())