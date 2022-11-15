from collections import Counter

print(dict(Counter([int(num) for num in input()]).most_common(3)))
# функция most_common() возвращает список наиболее
# встречаемых элементов и их количество


