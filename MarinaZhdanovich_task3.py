def to_percent(num: float, round_digits=0):
    percent = num * 100
    if round_digits:
        round_percent = round(percent, round_digits)
        return str(round_percent) + "%"
    else:
        return str(int(percent)) + "%"


print(to_percent(0.1))





