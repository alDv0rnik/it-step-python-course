def generate_squares(i: int) -> dict:
    d = {i: i ** 2 for i in range(1, i + 1)}
    return d

i = int(input())
print(generate_squares(i))