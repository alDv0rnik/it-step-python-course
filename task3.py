class User:
    def __init__(self, age, name):
        self.verify_age(age)

        self.__age = age
        self.name = name

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 1:
            raise TypeError("Возраст должен быть целым числом и больше 0")


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age


u = User(37, "Vadim")
# u1 = User(35.5, "Mick")
print(u.age, u.name)
# print(u1.age, u1.name)
