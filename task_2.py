class HistoryDict:
    HISTORY = {}

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def set_value(self, key, value):
        self.dictionary = {key: value}
        self.HISTORY[key] = value

    def get_history(self):
        print(f'list of last ten keys: {list(self.HISTORY.keys())[:-11:-1]}')

d = HistoryDict({'foo', 42})
print(d.dictionary)
d.set_value('tes', 43)
d.set_value('tes 1', 44)
d.set_value('tes 2', 45)
d.set_value('tes 3', 46)
d.set_value('tes 4', 47)
d.set_value('tes 5', 48)
d.set_value('tes 6', 49)
print(d.dictionary)
d.set_value('tes 7', 50)
d.set_value('tes 8', 51)
d.set_value('tes 9', 52)
d.set_value('tes 10', 53)
d.set_value('tes 11', 54)
d.set_value('tes 12', 55)
print(d.dictionary)
d.get_history()