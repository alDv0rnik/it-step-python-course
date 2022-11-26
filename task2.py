def to_percent(num:float, round_digits = 0):
    p = float(num * 100)
    if round_digits:
        round_p = round(p, round_digits)
        return str(round_p) + '%'
    else:
        return str(int(p)) + '%'


num = float(input())
print(to_percent(num))
        