from collections import OrderedDict

dct = OrderedDict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
print('изначальный id нашего словаря: ', id(dct))

first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last = False) #Элемент перемещается в правый конец,
# если аргумент last=True (по умолчанию), или в начало, если last=False.

second = list(dct.items())[1]
del dct[second[0]]

dct['new_key'] = 'new_value'

print(dct)
print('конечный id нашего словаря: ', id(dct))
