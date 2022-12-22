class HistoryDict:
    def __init__(self, dictionary):
        self.__dictionary = dictionary
        self.__list = list(self.__dictionary.keys())

    def set_value(self, key, value):
        self.__dictionary[key] = value
        self.__list.append(key)

    def get_history(self):
        print(self.__list[-10:])


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.set_value("bar 1", 44)
d.set_value("bar 2", 45)
d.set_value("bar 3", 46)
d.set_value("bar 4", 47)
d.set_value("bar 5", 48)
d.set_value("bar 6", 49)
d.set_value("bar 7", 50)
d.set_value("bar 8", 51)
d.set_value("bar 9", 52)
d.get_history()
