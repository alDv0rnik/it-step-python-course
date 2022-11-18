numbers = [1, 15, 35, 4, 1, 15]

def func(numbers):
        unique = []
        for number in numbers:
            if number not in unique:
                unique.append(number)
        return unique
print(func(numbers))