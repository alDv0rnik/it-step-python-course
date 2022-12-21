# Задание 2 (I). Написать класс, который описывает пользователя (class User), сделать ему
# приватный атрибут age, который передается в конструктор, публичный атрибут name, который
# так же передается в конструктор.
# 2.1 Написать getter и setter для атрибута age.
# 2.2 Добавить в setter проверку на валидный возраст (не отрицательное, целое число)

class User:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, x):
        if type(x) != int or x < 0:
            raise ValueError("The age is below eligibility criteria!!!")
        self.__age = x


user1 = User("Nina")
#сработает геттер
user1.age = 31
# сработает сеттер
print(user1.age)
#сработает геттер
user2 = User("Dima")
# не сработает сеттер из-зи ограничения по возрасту
user2.age = 26.3
print(user2.age)

# user3 = User("Fedor")
# user3.age = -36
# print(user3.age)





