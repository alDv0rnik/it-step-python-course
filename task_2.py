
def concat(num: int):
    i = 0
    new_str = str()
    while i < num:
        st = str(input())
        new_str += st
        i += 1
    return new_str


print(concat(int(input("Enter the number of str: "))))
