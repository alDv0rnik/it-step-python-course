from converter import EUR, USD, RUB
import sys

def main_converter():
    if len(sys.argv) == 3:
        if sys.argv[1] == 'eur':
            print(EUR.conv_eur(int(sys.argv[2])))
        elif sys.argv[1] == 'usd':
            print(USD.conv_usd(int(sys.argv[2])))
        elif sys.argv[1] == 'rub':
            print(RUB.conv_rub(int(sys.argv[2])))
        else:
            print('error')
    else:
        print('error')


if __name__ == '__main__':
    main_converter()