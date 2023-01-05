
def dataS(data, new_value):
    if type(data) == list:
        data.append(new_value)
        return data
    elif type(data) == set:
        data.update(new_value)
        return data
    elif type(data) == str:
        if type(new_value) == list:
            return data
        elif not type(new_value) == list:
            data += str(new_value)
            return data
    elif type(data) == dict or type(data) == bool or type(data) == int:
        return data


a = ["1", "d", "3"]
b = {1, "3", "f", "5"}
c = {1: "s", 2: "d", 3: "f"}
d = 1
e = "Artem"
i = True
print(type(a), type(b), type(c), type(d))
print(dataS(a, 5))
print(dataS(b, "5"))
print(dataS(d, a))
