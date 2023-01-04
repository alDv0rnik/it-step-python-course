# Задание 2 (I). Написать класс User, у него будут в конструкторе определяться поля age, name,
# user_type, а метод будет access_database. Сделать метод таким, чтобы если
# self.user_type был равен “superuser”, то метод выводил в консоль “access granted”, в
# случае если это просто юзер, то выводило “access denied”. Для суперюзера сделать
# унаследованный класс SuperUser от User

class User:
    def __init__(self, age, name, user_type):
        self.__age = age
        self.__name = name
        self.__user_type = user_type.lower()

    def access_database(self):
        if self.__user_type == "superuser":
            print("Access granted")
        elif self.__user_type == "user":
            print("Access denied")
        else:
            print("Such a user is not defined")


class SuperUser(User):
    def __init__(self, age, name, user_type='superuser'):
        super().__init__(age, name, user_type)


user1 = User(25, "David", "Superuser")
user1.access_database()
user2 = User(36, "Inna", "USER")
user2.access_database()
user3 = User(55, "Roman", "player")
user3.access_database()
superuser1 = SuperUser(31, "John")
superuser1.access_database()

