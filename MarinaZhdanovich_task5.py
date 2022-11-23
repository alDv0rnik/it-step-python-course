def generate_squares(i: int) -> dict:
    return {num: num**2 for num in range(1, i + 1)}


print(generate_squares(5))




