def increase_g(x):
    def g(x):
        return x + 1

    y = g(x)
    print(x, y)

increase_g(1)

