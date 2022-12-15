
def sorter():
    with open("data/for_task_2/unsorted_names.txt", "r", encoding="utf-8") as names:
        file = [i.strip() for i in names.readlines()]
        file.sort()
        f = file
    with open("data/for_task_2/sorted_names.txt", "w", encoding="utf-8") as alph_name:
        for j in f:
            alph_name.writelines("%s\n" % j)


sorter()
