class HistoryDict:
    HISTORY = dict()

    def __init__(self, dictionary):
        self.dct = dictionary

    def set_value(self, key, value):
        self.dct = {key, value}
        self.HISTORY[key] = value

    def get_history(self):
        print(list(self.HISTORY.keys())[: -11: -1])


d = HistoryDict({'t1', 1})
print(d.dct)
d.set_value('t2', 2)
d.set_value('t3', 3)
d.set_value('t4', 4)
d.set_value('t5', 5)
d.set_value('t6', 6)
d.set_value('t7', 7)
print(d.dct)
d.set_value('t8', 8)
d.set_value('t9', 9)
d.set_value('t10', 10)
d.set_value('t11', 11)
print(d.dct)
d.get_history()
