
def buy_count(num):
    i = 0
    d = {}
    while i <= int(num) - 1:
        i += 1
        buy_list = input("buyer, product, quantity separated by a space")
        a = buy_list.split()

        if a[0] not in d.keys():
            d[a[0]] = {a[1]: int(a[2])}
        elif a[0] in d.keys() and a[1] not in d[a[0]].keys():
            d[a[0]].update({a[1]: int(a[2])})
        elif a[0] in d.keys() and a[1] in d[a[0]].keys():
            d[a[0]][a[1]] = int(d[a[0]][a[1]]) + int(a[2])
    return d


print(buy_count(3))




