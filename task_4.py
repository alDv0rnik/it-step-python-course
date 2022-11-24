def generate_squares(i: int):
    dict_create = {}
    for num in range(1, i + 1):
        dict_create[num] = num**2
    return dict_create

print(generate_squares(25))

