def values(data, new_value):
    if type(data) == list:
        return data.append(new_value)
    elif type(data) == set:
        return data.add(new_value)
    elif type(data) == str:
        if type(new_value) != list:
            return data + str(new_value)
        else:
            return data
    else:
        return data


