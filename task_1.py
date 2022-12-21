class User:
    def __init__(self, age, name):
        self.__age = age
        self.name = name


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, age):
        self.__age = age


    @age.getter
    def age(self):
        return self.age

    def set_age(self, age):
            if age > 0 and age % 1 == 0:
                self.__age = age
            else:
                print('InvalidAge')

    def get_age(self):
        return self.__age




Marck = User(25, 'Marck')
print(Marck.get_age())
Marck.set_age(30)
print(Marck.name)
print(Marck.get_age())
Marck.set_age(31.5)
Marck.set_age(0)
print(Marck.get_age())
Marck.name = 'Marckus'
print(Marck.name, Marck.get_age())