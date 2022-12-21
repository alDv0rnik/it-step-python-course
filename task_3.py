
class UserDict:
    def __init__(self, start_dict: dict):
        self.__liss = list(start_dict.keys())
        self.start_dict = start_dict
        self.__ud = dict(start_dict)

    def set_value(self, key: str, value):
        self.__ud[key] = value
        if len(self.__liss) < 10:
            self.__liss.append(key)
        elif len(self.__liss) >= 10:
            self.__liss.remove(self.__liss[0])
            self.__liss.append(key)
        return self.__ud

    def get_value(self):
        return f"len of list keys {len(self.__liss)}\nlist keys =  {self.__liss}"


u = UserDict({"foo": 42, "1": 45, "2": 22, "3": 55, "4": 44, "5": 84, "6": 89, "7": 65})
u.set_value("8", 5)
u.set_value("9", 5)
u.set_value("10", 5)
u.set_value("11", 5)
u.set_value("12", 5)
u.set_value("13", 5)
print(u.get_value())



