#Задание 6 (I) Для функции из любой задачи написать аннотацию, используя правила docstring
def dictionary_of_lists(l1:list, l2:list):
    """
    This function returns a dictionary from 2 lists
    :param l1: list of letters
    :param l2: list of digits
    :return: dictionary
    """

    d = {}
    for i in range(len(l1)):
        d[l1[i]] = l2[i]
    return d


list_1 = ["a", "b", "c", "d"]
list_2 = [1, 2, 3, 4]
print(dictionary_of_lists(list_1, list_2))