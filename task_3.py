# определяем фунуцию g() в increase_g()
def increase_g():
    def g(a): return a
    return g(int(input())) + 1


print(increase_g())