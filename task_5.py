

def generate_squares(num: int) -> dict:
    squares = list()
    numbers = list()
    for i in range(1, num+1):
        numbers.append(i)
        squares.append(i**2)
    return dict(zip(numbers, squares))


print(generate_squares(5))
print(generate_squares(0))
