class User:
    def __init__(self, name, age):
        self.__age = age
        self.name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            print(f"{age} is not valid")
        elif type(age) != int:
            print(f"{age} is not valid")
        elif age > 0:
            self.__age = age


u = User("artem", 24)
print(f"im {u.name} {u.age} years old")
u1 = User("artem", 6)
u1.age = 5
u1.age = 5.2
u1.age = -5
print(f"im {u1.name} {u1.age} years old")



