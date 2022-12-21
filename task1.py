class Cat:
    def __init__(self, color, cat_type, size='uncknown'):
        self.size = size
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == 'indoor':
            self.size = 'small'
        else:
            self.size = 'undefined'
        print(f'This cat is {self.size} size')


class Tiger(Cat):
    def __init__(self, color, cat_type, size='uncknown'):
        Cat.__init__(self,color, cat_type, size)

    def set_size(self):
        if self.cat_type == 'wild':
            self.size = 'big'
        else:
            self.size = 'undefined'
        print(f'This {self.color} tiger is {self.size} size')

murzick = Cat('black', 'indoor')
murzick.set_size()
barsick = Cat('white', 'outdoor')
barsick.set_size()
tiger = Tiger('yelow', 'wild')
tiger.set_size()
baby_tiger = Tiger('orenge', 'indoor')
baby_tiger.set_size()