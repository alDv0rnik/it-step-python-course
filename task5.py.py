from collections import OrderedDict

dct = OrderedDict({'one' : 1, 'two' :2, 'three' : 3, 'four' : 4, 'five' : 5})
print('изначальный id: ', id(dct))

first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last = False) 
second = list(dct.items())[1]
del dct[second[0]]
dct['new_key'] = 'new_value'

print(dct)
print('id: ', id(dct))