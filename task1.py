class User:
    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.user_type = user_type


    def data_base(self):
        if self.user_type == "superuser":
            print("access granted")
        elif self.user_type == "user":
            print("access denied")
        else:
            print("unknow user")


class SuperUser(User):
    def __init__(self, age, name, user_type="user_type"):
        super().__init__(age, name, user_type)


u1 = User(35, "John", "superuser")
u1.data_base()
u2 = User(37, "Vadim", "user")
u2.data_base()
u3 = User(48, "Mick", "USER123")
u3.data_base()
superuser = SuperUser(35, "Lora")
superuser.data_base()




