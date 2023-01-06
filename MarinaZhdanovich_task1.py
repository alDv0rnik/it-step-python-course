class User:
    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.user_type = user_type.lower()

    def access_database(self):
        if self.user_type == 'superuser':
            print('access granted')
        elif self.user_type == 'user':
            print('access denied')
        else:
            print('unknown user type')


class SuperUser(User):
    def __init__(self, age, name, user_type='superuser'):
        super(SuperUser, self).__init__(age, name, user_type)


user1 = User(30, 'Petya', 'User')
user1.access_database()
user2 = User(32, 'Vasya', 'user123')
user2.access_database()
user3 = User(33, 'Hagi_Vagi', 'superuser')
user3.access_database()
superuser1 = SuperUser(31, 'kisi_Misi')
superuser1.access_database()
