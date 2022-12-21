class HistoryDict:
    HISTORY = {}

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def set_value(self, key, value):
        self.dictionary = {key: value}
        self.HISTORY[key] = value

    def get_history(self):
        print(f'list of last ten keys: {list(self.HISTORY.keys())[:-11:-1]}')


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()
