def sort_list(k: list):
    """
    This function takes values as a list as input, create empty list and add unique values from parameters.
    :param k: The input is a list only.
    :return: Order-preserving unique list.
    """

    a = list()
    for i in k:
        if int(i) not in a:
            a.append(int(i))
        elif i in k:
            continue
    return a


print(sort_list(list(input().split(", "))))