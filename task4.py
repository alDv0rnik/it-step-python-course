def main_test():
    """функция принимает список ответов на вопросы
    и возвращает словарь с колличеством набранных очков
    и списком верных ответов"""
    answers = antering_answers()
    correct_answers = ["Минск", "Гомель", "Брест"]
    score = counting_score(answers, correct_answers)
    create_dict_of_score_and_answers(score, correct_answers)


def antering_answers():
    a = input("Введите столицу Беларуси: ")
    b = input("Город Беларуси Г..ь: ")
    c = input("Город Беларуси Б...т: ")
    return [a, b, c]


def counting_score(answers, correct_answers):
    score = 0
    for i in range(len(correct_answers)):
        if answers[i] == correct_answers[i]:
            score += 1
    return score


def create_dict_of_score_and_answers(score, correct_answers):
    dict_ = {}
    dict_['score'] = score
    dict_['correct_answers'] = correct_answers
    print(dict_)


main_test()