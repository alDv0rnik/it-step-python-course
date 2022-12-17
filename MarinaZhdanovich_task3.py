from collections import Counter


def most_common_words(filepath, number_of_words=3):
    with open(filepath, 'r') as file:
        words = file.read().replace(',', '').replace('.', '').lower().split()
        final = Counter(words).most_common(number_of_words)
        return list(dict(final))


print(most_common_words('data/lorem_ipsum.txt'))



