
def most_common_words(filepath, number_of_words=3):
    atr = ["/", "-", "=", "+", "_", "*", "!", "&", "?", "#", "$", ";", " ", "(", ")", "\n"]
    lis = []
    with open(filepath, "r", encoding="utf-8") as names:
        file = names.read()
        com = file.lower().replace(",", " ").replace(".", " ")
        split_file = com.split(" ")
        search_list = [i for i in split_file]
        for j in search_list:
            if search_list.count(j) >= number_of_words and j not in lis and j not in atr:
                lis.append(j)
    return lis[1:]


print(most_common_words("data/for_task_3/file.txt"))
