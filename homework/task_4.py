from decorators import call_once, cash_clean


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(25, 26))
# cash_clean()
# before use cash_clean() read her description
