# Задание 5* (II). Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами
# первый и последний элемент объекта. Удалите второй элемент. Добавьте в конец ключ «new_key»
# со значением «new_value». Выведите на печать итоговый словарь. Важно, чтобы словарь остался
# тем же (имел тот же адрес в памяти).

d = dict(one=1, two=2, three=3, four=4, five=5)
print(f"Dictionary before the change is {d}")
print(f"Аddress before the change of the dictionary is {id(d)}")
# print(d["one"])
temp1 = d.pop("one")
temp2 = d.pop("two")
temp3 = d.pop("three")
temp4 = d.pop("four")
temp5 = d.pop("five")
d["five"] = temp5
d["two"] = temp2
d["three"] = temp3
d["four"] = temp4
d["one"] = temp1
print(f"Dictionary after the change is {d}")
print(f"Аddress after the change of the dictionary is {id(d)}")


