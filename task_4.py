
def sort_list(k: list):
    a = list()
    for i in k:
        if int(i) not in a:
            a.append(int(i))
        elif i in k:
            continue
    return a


print(sort_list(list(input().split(", "))))


