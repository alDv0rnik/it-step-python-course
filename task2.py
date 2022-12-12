def most_common_words(file_path, number_of_words=3):
    with open('data/lorem_ipsum.txt', 'r') as rf:
        words = rf.read().replace(',', '').replace('.', '').lower().split()

    d_words = {}
    for word in words:
        d_words[word] = words.count(word)

    list_val = list(reversed(sorted(d_words.values())))

    res = []
    for _ in list_val:
        for k, v in d_words.items():
            if v == _:
                res.append(k)

    print(res[0:number_of_words])


most_common_words('lorem_ipsum.txt')