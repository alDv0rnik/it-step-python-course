
class User:
    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.user_type = user_type

    def access_database(self):
        if self.user_type == "superuser":
            return "access granted"
        else:
            return "access denied"


class Superuser(User):
    def __init__(self, age, name, user_type):
        super().__init__(age, name, user_type)

    def ama(self):
        return "am a superuser"


u = User(14, "Artem", "superuser")
su = Superuser(18, "Andrey", "justuser")
print(u.access_database())
print(su.access_database())
