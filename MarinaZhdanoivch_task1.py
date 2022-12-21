class Cat:
    def __init__(self, color, cat_type, size=None):
        self.color = color
        self.cat_type = cat_type
        self.size = size

    def set_size(self):
        if self.cat_type == 'indoor':
            self.size = 'small'
        else:
            self.size = 'undefined'
        return self.size


class Tiger(Cat):
    def __init__(self, color, cat_type, size=None):
        super().__init__(color, cat_type)
        self.size = size

    def set_size(self):
        if self.cat_type == 'wild':
            self.size = 'big'
        else:
            self.size = 'undefined'
        return self.size


cat1 = Cat('black', 'indoor')
print(cat1.set_size())
cat2 = Cat('grey', 'outdoor')
print(cat2.set_size())
tiger1 = Tiger('white', 'wild')
print(tiger1.set_size())
tiger2 = Tiger('yellow', 'adult')
print(tiger2.set_size())
