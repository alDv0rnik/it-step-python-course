# Задание 3 (I). Создайте иерархию для класса birds из 4 классов:
# 3.1 Класс Bird с атрибутом name и методами fly и walk.
# 3.2 Класс FlyingBird с атрибутами name и ration (должен иметь значение по-умолчанию)
# и такими же методами
# 3.3 Класс NonflyingBird с такими же характеристиками, но без метода fly
# 3.4 Класс SuperBird, который может делать все: ходить, летать, плавать и есть
# Обратите внимание на метод eat


class Bird:
    def __init__(self, name):
        self._name = name

    def fly(self):
        print(f"Bird {self._name} flies")

    def walk(self):
        print(f"Bird {self._name} walks!")


bird1 = Bird("titmouse")
bird1.fly()
bird1.walk()


class FlyingBird(Bird):
    def __init__(self, name, ration="seed"):
        super().__init__(name)
        self._ration = ration


fly_bird1 = FlyingBird("bullfinch")
fly_bird1.fly()
fly_bird1.walk()


class NonflyingBird:
    def __init__(self, name, ration='seed'):
        self._name = name
        self._ration = ration

    def walk(self):
        print(f"Bird {self._name} walks!")


non_flying_bird1 = NonflyingBird("ostrich")
non_flying_bird1.walk()


class SuperBird(NonflyingBird, FlyingBird):
    def __init__(self, name, ration):
        super().__init__(name, ration)

    def swim(self):
        print(f"Birn {self._name} swims!")

    def eat(self):
        print(f"Bird {self._name} eats {self._ration}!")


super_bird = SuperBird("duck", "bread")
super_bird.fly()
super_bird.walk()
super_bird.swim()
super_bird.eat()









