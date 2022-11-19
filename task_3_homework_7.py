num = input("Enter the number: ")
i = 0
d = {}
if num.isalpha():
    print("\U0001F914 " + "I SAID ENTER THE NUMBER!")
else:
    while i <= int(num) - 1:
        i += 1
        buy_list = input()
        a = buy_list.split()

        if a[2].isalpha():
            print("\U0001F92D " + "Something wrong " + "with " + str(a[0]))
        elif a[0] not in d.keys():
            d[a[0]] = {a[1]: int(a[2])}
        elif a[0] in d.keys() and a[1] not in d[a[0]].keys():
            d[a[0]].update({a[1]: int(a[2])})
        elif a[0] in d.keys() and a[1] in d[a[0]].keys():
            d[a[0]][a[1]] = int(d[a[0]][a[1]]) + int(a[2])

    for j in sorted(d.keys()):
        print("\U0001f600 " + j + ':')
        for c in sorted(d[j].keys()):
            print(c, d[j][c])

# 7
# Mike Milk 2
# Jane Coffee 1
# Mike Milk 4
# Bob Milk 7
# Jane Сookie 2
# Mike Bread 1
# Bob Coffee 4