# Задание 3 (I). Напишите фунцкию to_percent(num: float), которая будет принимать вещественное
# число и представлять его в виде процентов. Так, например, 0.1 это 10%, а 1.052 это 105.2%.
# Пускай функция будет принимать один необязательный параметр round_digits. Который будет
# указывать на количество цифр после запятой в числе процентов, при этом незначащие нули нужно
# опускать. Если он не указан, пускай ваша функция округляет результат до целого процента.


def to_percent(num: float, round_digits=0):
    num_percent: float = num*100
    if round_digits:
        num_percent = round(num_percent, round_digits)
# незначащие нули нужно опускать
        while num_percent > 0 and num_percent % 10 == 0:
            num_percent = num_percent / 10
        return str(num_percent) + ' %'
    else:
        return str(int(num_percent)) + ' %'

#опускаем незначащие нули в 1 вызове
print(to_percent(1.38599979, 2))
print(to_percent(1.38528979))

