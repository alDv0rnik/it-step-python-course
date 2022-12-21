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