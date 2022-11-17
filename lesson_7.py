# Task 1
# s = 'pythonist'
# d = {i: (s.count(i)) for i in s}
# print(d)

# Task 2
# s = 'Oh, it is python'
# d = {i: (s.count(i)) for i in s}
# print(d)

# Task 3
# a = ["a", "b", "c", "d"]
# b = [1, 2, 3, 4]
# c = {}
# for i in range(len(b)):
#     c[a[i]] = b[i]
# print(c)

# Task 4
# str_ = input("ввудите набор чисел от 0 до 9 одно за другим: ")
# nums = '0123456789'
# dict_ = {}
# for a in nums:
#     count = str_.count(a)
#     if count > 0:
#         dict_.update({int(a): count})
# sorted_values = sorted(dict_.values())
# dict_sorted = {}
# for i in sorted_values:
#     for k in dict_.keys():
#         if dict_[k] == i:
#             dict_sorted[k] = dict_[k]
#             break
# ls = list(dict_sorted.items())
# dict_last_3 = dict(ls[-3:])
# print(dict_last_3)


# Task 5
# dict_1 = {"a": 1, "b": 2, "c": [3, 4 , 4], "d": 4, "e": 5}
# k, v = dict_1.popitem()
# del dict_1["a"]
# d = {}
# d[k] = v
# dict_1["a"] = 1
# dict_1, d = d, dict_1
# dict_1.update(d)
# del dict_1["b"]
# dict_1["new_key"] = "new_value"
# print(dict_1)

# Tasck 6
# a = input("Введите сталицу Беларуси: ")
# b = input("Город Беларуси Г..ь: ")
# c = input("Город Беларуси Б...: ")
# answers = [a, b, c]
# correct_answers = ["Минск", "Гомель", "Брест"]
# dict_ = {}
# score = 0
# for i in range(len(correct_answers)):
#     if answers[i] == correct_answers[i]:
#         score += 1
# dict_['score'] = score
# dict_['correct_answers'] = correct_answers
# print(dict_)












































