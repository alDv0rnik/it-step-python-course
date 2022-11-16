
# Task 1
# keys = input()
# max_3 = {}
# l_keys = []
# l_count = []
# for i in keys:
#     l_keys.append(i)
# for j in l_keys:
#     l_count.append(l_keys.count(j))
# dict_new = dict(zip(l_keys, l_count))
# print(dict_new)
# max_val = max(dict_new.values())
# i = 1
# while i <= 3:
#     for k, v in list(dict_new.items()):
#         if v == max(dict_new.values()):
#             max_3[k] = v
#             del dict_new[k]
#             i += 1
#             break
# print(max_3)

# Task 2(1)

# dict_first = {
#     1: "Artem",
#     2: "Hanna",
#     3: "Alla",
#     4: "Irina",
#     5: "Marina"
# }
# print(id(dict_first))
# print(dict_first)
# del dict_first[1]
# del dict_first[2]
# del dict_first[3]
# del dict_first[4]
# del dict_first[5]
# dict_Art = {1: "Artem"}
# dict_AI = {3: "Alla", 4: "Irina"}
# dict_Mar = {5: "Marina"}
# dict_NV = {"new_key": "new_value"}
# dict_first.update(dict_Mar)
# dict_first.update(dict_AI)
# dict_first.update(dict_Art)
# dict_first.update(dict_NV)
# print(id(dict_first))
# print(dict_first)


# task 2(2)

# dict = {
#     1: "Artem",
#     2: "Hanna",
#     3: "Alla",
#     4: "Irina",
#     5: "Marina"
# }
# del dict[2]
# dict[1] = "Marina"
# dict[3] = "Alla"
# dict[4] = "Irina"
# dict[5] = "Artem"
# dict["new_key"] = "new_value"
# print(dict)

# Task 3(работает не правильно, скорее всего можно сортировать функцией)

# num = int(input())
# i = 0
# d = {}
# while i <= num - 1:
#     i += 1
#     buy_list = input()
#     a = buy_list.split()
#     d[a[0]] = a[1:3]
# print(d)

# task 4(1)

# keys = input()
# l_keys = []
# l_count = []
# for i in keys:
#     l_keys.append(i)
# for j in l_keys:
#     l_count.append(l_keys.count(j))
# print(l_keys)
# print(l_count)
# dict_new = dict(zip(l_keys, l_count))
# print(dict_new)

# task 4(2)
# через множество, чтоб элементы которые мы считаем не повторялись, остальной код не менял.
# keys = input()
# l_keys = []
# l_count = []
# for i in keys:
#     l_keys.append(i)
# for j in l_keys:
#     l_count.append(l_keys.count(j))
# dict_new = set(zip(l_keys, l_count))
# print(dict_new)

# task 5

# print("Пиши ответы на англ")
# correct_ans = ({"yes", "isdigit()", "isalpha()"})
# q_1 = input("Является ли функция 'sorted' встроенной ? ")
# q_2 = input("Какой метод проверяет строку на содержание цифр ? ")
# q_3 = input("Какой метод проверяет строку на содержание букв ? ")
# users_ans = list()
# users_ans.append(q_1)
# users_ans.append(q_2)
# users_ans.append(q_3)
# d = dict()
# a = correct_ans.copy().intersection(users_ans)
# print("Ваши ответы: " + str(users_ans))
# print("Даны правильные ответы: " + str(a))
# print("Tвой рекорд " + str(len(a)))
# d[len(a)] = list(a)
# print(d)
