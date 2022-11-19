def f(ls1: list, ls2: list):
    """
    This function takes two lists and outputs a dictionary with the key ls1 and the value ls2
    :param ls1, ls2: accept only lists
    :return: outputs a dictionary with the key ls1 and the value ls2
    """
    return dict(zip(ls1, ls2))



ls1 =  ["a", "b", "c", "d"]
ls2 = [1,2,3,4]
print(f(ls1, ls2))