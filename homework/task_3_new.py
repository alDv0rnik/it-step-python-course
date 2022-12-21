class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} can fly"

    def walk(self):
        return f"{self.name} can walk"


class FlyingBird(Bird):
    def __init__(self, name, ration="berry"):
        super().__init__(name)
        self.ration = ration


class NonflyingBird(FlyingBird): # почему не нужно прописывать рацион
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        return f"{self.name} can't fly"


class SuperBird(FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return f"{self.name} can swim"

    def eat(self):
        return f"{self.name} eat only {self.ration}"


p = SuperBird("Сrane")
s = FlyingBird("Rooster")
f = NonflyingBird("Kivi")
k = Bird("woodi")
print(p.ration)
print(f.ration)
print(p.eat(), p.fly(), p.walk(), p.swim(), sep=" | ")
print(s.fly(), s.walk(), sep=" | ")
print(f.fly(), f.walk(), sep=" | ")
print(k.fly(), k.walk(), sep=" | ")
print(SuperBird.__mro__)
