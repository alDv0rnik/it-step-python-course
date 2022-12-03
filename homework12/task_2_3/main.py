from convert_pack import eur, usd, kzt
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print((sys.argv[0]))
        if sys.argv[1] == "usd":
            print(usd.conv_usd(int(sys.argv[2])))
        elif sys.argv[1] == "eur":
            print(eur.conv_eur(int(sys.argv[2])))
        elif sys.argv[1] == "kzt":
            print(kzt.conv_kzt(int(sys.argv[2])))
    if len(sys.argv) == 1:
        v = str(input("Enter currency: eur, usd, kzt "))
        if v == "usd":
            print(usd.conv_usd(float(input("Summa in byn: "))))
        elif v == "eur":
            print(eur.conv_eur(float(input("Summa in byn: "))))
        elif v == "kzt":
            print(kzt.conv_kzt(float(input("Summa in byn: "))))



