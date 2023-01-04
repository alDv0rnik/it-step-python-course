# Задание 3 (I). Реализовать пользовательский словарь (в виде класса), который будет запоминать
# 10 последних измененных ключей. Используя метод "get_history" вернуть эти ключи. Подумайте
# какой подход здесь лучше использовать.
# d = HistoryDict({"foo": 42})
# d.set_value("bar", 43)
# d.get_history()
# >>> ["bar"]


class HistoryDict(dict):
    def __init__(self, dict1):
        self.__dict1 = dict1
        #использую лист для сохранения упорядоченности ключей, т.к. словарь не упорядоченный
        self.__lst = list(self.__dict1.keys())

    def set_value(self, key1, value1):
        self.__dict1[key1] = value1
        self.__lst.append(key1)

    def get_history(self):
        return self.__lst[-10:]


d = HistoryDict({"foo": 42})
d.set_value("bar1", 43)
d.set_value("bar2", 44)
d.set_value("bar3", 45)
d.set_value("bar4", 46)
d.set_value("bar5", 47)
d.set_value("bar6", 48)
d.set_value("bar7", 49)
d.set_value("bar8", 50)
d.set_value("bar9", 51)
d.set_value("bar10", 52)
d.set_value("bar11", 53)
d.set_value("bar12", 53)
print(d.get_history())

