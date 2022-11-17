from collections import Counter
number = input('Enter numbers: ')
sorted = Counter([int(i) for i in number])
print(dict(sorted.most_common(3)))




