def func(data, new_value):
    if isinstance(data, list):
        data.append(new_value)
    elif isinstance(data, set):
        data.add("37")
    elif isinstance(data, str):
        if isinstance(new_value, list):
            return new_value
        else:
            data += new_value
    elif isinstance(data, int|dict|bool):
        return data
    else:
        raise ValueError("Изменений нету для типа данных")
    return data


list_1 = ["v", "a", "d"]
print(func(list_1, "37"))
set_1 = {"b", "v", "3"}
print(func(set_1, "37"))
str_1 = "Python!"
print(func(str_1, "37"))
print(func(str_1, ["v", "a", "d"]))
int_1 = 38
print(func(int_1, 37))
bool_1 = False
print(func(bool_1, "37"))
dict_1 = {1: "v", 2: "a", 3: "d"}
print(func(dict_1, "37"))



        