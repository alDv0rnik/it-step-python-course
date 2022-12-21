class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"Птица {self.name} умеет летать")

    def walk(self):
        print(f"Птица {self.name} умеет ходить")


bird = Bird("Утка")
bird.fly()
bird.walk()


class FlyingBird(Bird):
    def __init__(self, name, ration="мясо"):
        super().__init__(name)
        self.ration = ration


fly_bird = FlyingBird("Орел")
fly_bird.fly()
fly_bird.walk()


class NonFlyingBird:

    def __init__(self, name, ration="grass"):
        self.name = name
        self.ration = ration

    def walk(self):
        print(f"Птица {self.name} не летает")


non_fly = NonFlyingBird("Страус")
non_fly.walk()


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration):
        super().__init__(name, ration)

    def swimm(self):
        print(f"Птица {self.name} умеет плавать")


    def eat(self):
        print(f"Птица {self.name} eats {self.ration}")


super_bird = SuperBird("Гусь", "Зерно")
super_bird.fly()
super_bird.walk()
super_bird.swimm()
super_bird.eat()















