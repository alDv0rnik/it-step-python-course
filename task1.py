class Cat:

    def __init__(self, color, cat_type):
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == "indoor":
            self.size = "small"
        else:
            self.size = "undefined"

    def get_size(self):
        return self.size


cat = Cat("black", "indoor")
cat.set_size()
print(cat.get_size())



class Tiger(Cat):

    def __init__(self, color, cat_type):
        super().__init__(color, cat_type)

    def set_size(self):
        if self.cat_type == "wild":
            self.size = "big"
        else:
            self.size = "undefined"


tiger = Tiger('orange', "wild")
tiger.set_size()
print(tiger.get_size())
tiger1 = Tiger('white', 'home')
tiger1.set_size()
print(tiger1.get_size())













