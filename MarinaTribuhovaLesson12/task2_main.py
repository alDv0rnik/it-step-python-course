# Задание 2 (I). Написать программу конвертер рублей в любые три валюты (обратное действие
# не требуется). На вход программа принимает сумму в бел. рублях и валюту, в которую нужно ее
# перевести (Например, EUR). Результат округлить до 2-х значимых цифр. Организовать функции
# в модули и пакет.

from package_task2 import transfer_to_euro
from package_task2 import transfer_to_dollars
from package_task2 import transfer_to_russian_rubles


sum_br = int(input("Enter the amount in belarusian rubles for the transfer: "))
cur = int(input("Select the currency to transfer:\n1 - euro\n2 - dollars\n3 - russian rubles\n"))
while cur < 1 or cur > 3:
    print("Incorrect input! Be careful!")
    cur = input("Select the currency to transfer:\n1 - euro\n2-dollars\n3-russian rubles\n")
if cur == 1:
    print(f"{sum_br} belarusian rubles = {transfer_to_euro.belrub_to_euro(sum_br)} euro")
elif cur == 2:
    print(f"{sum_br} belarusian rubles = {transfer_to_dollars.belrub_to_dollars(sum_br)} dollars")
else:
    print(f"{sum_br} belarusian rubles = {transfer_to_russian_rubles.belrub_to_russian_rubles(sum_br)} russian rubles")