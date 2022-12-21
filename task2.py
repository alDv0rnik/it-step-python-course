class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f'bird {self.name} can fly')

    def walk(self):
        print(f'bird {self.name} can walk')


class FlyingBird(Bird):
    def __int__(self, name, ration):
        self.ration = ration
        Bird.__init__(self, name)


class NoneflyingBird(Bird):
    def __init__(self, name, ration='worms'):
        self.ration = ration
        Bird.__init__(self, name)

    def fly(self):
        print(f'bird {self.name} can\'t fly')

    def eat(self):
        print(f'bird {self.name} can eat {self.ration}')



class SuperBird(FlyingBird, NoneflyingBird):
    def __init__(self, name, ration='bugs'):
        self.ration = ration
        FlyingBird.__init__(self, name)
        NoneflyingBird.__init__(self, name, ration)

    def swim(self):
        print(f'bird {self.name} can swim')


duck = Bird("duck")
duck.fly()
chicken = SuperBird("Ruti")
chicken_1 = SuperBird("Guti", "seeds")
chicken.eat()
chicken_1.eat()
ostrich = NoneflyingBird('Guga')
ostrich.eat()
ostrich.fly()