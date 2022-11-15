keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

result = dict(zip(keys, values))
# функция zip берет на вход несколько списков и создает из них список кортежей
print(result)