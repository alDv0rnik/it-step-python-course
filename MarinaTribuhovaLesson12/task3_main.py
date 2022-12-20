# Задание 3 (I). Для предыдущей задачи создайте точку входа в программу, чтобы ее можно было
# запускать из консоли. Позаботьтесь, чтобы программа могла принимать на вход аргументы из
# консоли. Для этого воспользуйтесь модулем sys.

import sys
from package_task2.transfer_to_euro import belrub_to_euro
from package_task2.transfer_to_dollars import belrub_to_dollars
from package_task2.transfer_to_russian_rubles import belrub_to_russian_rubles


def runner():
    if len(sys.argv) == 3:
        first = int(sys.argv[1])#сумма в белорусских
        second = sys.argv[2]#указать валюту (EUR, USD, RUB)
        if second == "eur":
            print(f"{first} belarusian rubles = {belrub_to_euro(first)} euro")
        elif second == "usd":
            print(f"{first} belarusian rubles = {belrub_to_dollars(first)} dollars")
        else:
            print(f"{first} belarusian rubles = {belrub_to_russian_rubles(first)} russian rubles")
    else:
        print("Two arguments are needed!!!")


if __name__ == "__main__":
    runner()


