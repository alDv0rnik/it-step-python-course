def to_percent(num: float, round_digit = 0):
    percent = num * 100
    if round_digit:
        round_percent = round(percent, round_digit)
        return f'{round_percent}%'
    else:
        return f'{round(percent)}%'


a = 1.514784362
b = 2
print(to_percent(a, b))

