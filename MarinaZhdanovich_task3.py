def increase_g(value):
    def g(value1):
        return value1 + 1
    return g


test = increase_g(1)
print(test(1))

