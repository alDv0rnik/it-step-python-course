# Задание 2 (I). Написать класс Cat, создать ему атрибуты size, color, cat_type.
# 2.1. При создании объекта класса передавать в конструктор color и cat_type, которые
# записываются в соответсвующие атрибуты.
# 2.2. Сделать метод set_size, в котором если self.cat_type это indoor, то self.size =
# ‘small’ иначе self.size=’undefined’. Протестируйте разные варианты.
# 2.3. Сделать класс Tiger, унаследованный от класса Cat.
# 2.4. Переопределить метод set_size таким образом чтобы если self.cat_type это ‘wild’,
# то self.size = ‘big’ иначе self.size=’undefined’

class Cat:

    _size = None

    def __init__(self, color, cat_type):
        self._color = color
        self._cat_type = cat_type

    def set_size(self):
        if self._cat_type == "indoor":
            self._size = "small"
        else:
            self._size = "undefined"

    def get_size(self):
        return self._size


cat1 = Cat("white", "indoor")
cat1.set_size()
print(cat1.get_size())
cat2 = Cat("red", "street")
cat2.set_size()
print(cat2.get_size())


class Tiger(Cat):

    def __init__(self, color, cat_type):
        super().__init__(color, cat_type)

    def set_size(self):
        if self._cat_type == "wild":
            self._size = "big"
        else:
            self._size = "undefined"


tiger1 = Tiger('black_red', "wild")
tiger1.set_size()
print(tiger1.get_size())
tiger2 = Tiger("white_black", "zoo")
tiger2.set_size()
print(tiger2.get_size())
