def f(ls1: list, ls2: list):
    return dict(zip(ls1, ls2))



ls1 =  ["a", "b", "c", "d"]
ls2 = [1,2,3,4]
print(f(ls1, ls2))