import eur
import rub
import usd
import sys


def runner():
    if len(sys.argv) == 3:
        first = int((sys.argv[1]))
        second = sys.argv[2].upper()
        if second == 'RUB':
            print(rub.exchange_rub(first))
        elif second == 'USD':
            print(usd.exchange_usd(first))
        elif second == 'EUR':
            print(eur.exchange_eur(first))
    else:
        print('Incorrect value')


if __name__ == '__main__':
    runner()