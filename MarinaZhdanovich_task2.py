class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f'Bird {self.name} can fly')

    def walk(self):
        print(f'Bird {self.name} can walk')


class FlyingBird(Bird):
    def __init__(self, name, ration='worms'):
        super(FlyingBird, self).__init__(name)
        self.ration = ration


class NonflyingBird(Bird):
    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def walk(self):
        print(f"Bird {self.name} can walk")


class SuperBird(FlyingBird, NonflyingBird):
    def __init__(self, name, ration='superfood'):
        FlyingBird.__init__(self, name)
        NonflyingBird.__init__(self, name)
        self.ration = ration

    def swim(self):
        print(f'Bird {self.name} can swim')

    def eat(self):
        print(f'Bird {self.name} eats {self.ration}')


bird = SuperBird('Donald Duck', 'superfood')
bird.walk()
bird.fly()
bird.eat()
bird.swim()

