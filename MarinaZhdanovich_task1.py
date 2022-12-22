class User:
    def __init__(self, age, name):
        self.__age = age
        self.name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or age % 1 != 0:
            print('Unvalid age')
        else:
            self.__age = age


user1 = User(35, "Petya")
user1.age = 36
print(user1.age)
user1.age = -35
user1.age = 35.4


