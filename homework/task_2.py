
class Cat:
    def __init__(self, color, cat_type, size):
        self.size = size
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == "indoor":
            self.size = "small"
            return self.size
        else:
            self.size = "undefined"
            return self.size

# c = Cat("yellow", "indoor", "hz")
# print(c.set_size())


class Tiger(Cat):
    def __init__(self, color, cat_type, size):
        super().__init__(color, cat_type, size)

    def set_size(self):
        if self.cat_type == "wild":
            self.size = "big"
            return self.size
        else:
            self.size = "undefined"
            return self.size


# t = Tiger("yellow", "wifld", "hz")
# print(t.set_size())
