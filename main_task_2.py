def most_common_words(filepath, number_of_words=3):
    with open(filepath, 'r') as file:
        list_of_words = file.read().replace(',', '').replace('.', '').lower().split()

    dict_of_words = {}
    for i in list_of_words:
        dict_of_words[i] = list_of_words.count(i)

    list_of_values = list(reversed(sorted(dict_of_words.values())))

    result = []
    for i in list_of_values:
        for k, v in dict_of_words.items():
            if v == i:
                result.append(k)

    print(result[0:number_of_words])

most_common_words('lorem_ipsum.txt')






