# Задание 6* (II). Представим, что есть программа, которая выполняет опрос пользователя. Его
# ответы программа сохраняет в виде списка. Внутри программы есть структура данных, которая
# хранит в себе правильные ответы. Правильные ответы являются неизменяемыми (Подумай,
# какую структуру данных здесь можно применить).
# Написать код, который сравнивает два списка: answers (ответы) и correct_answers (правильные
# ответы). В случае, если пользователь дает правильный ответ (или ответы), ему начисляется очко
# (score). Код долежн возвращать ответ в виде словаря со следующими ключами: ‘score’,
# ‘correct_answers’. Первый ключ хранит в себе значения полученных очков, второй список
# правильных ответов
list_answers = input("Enter your answers in the form of 5 digits from 1 to 9 separated by commas. ").split(",")
print(f"Your answers are {list_answers}")
correct_answers = tuple("13649")
print(f"Correct answers are {correct_answers}")
score = 0
for i in range(len(correct_answers)):
    if list_answers[i] == correct_answers[i]:
        score += 1
d = {score: list(correct_answers)}
print(f"Number of correct answers and correct answers {d}")
