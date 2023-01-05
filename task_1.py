class User:
    def __init__(self, name, age, user_type):
        self.name = name
        self.age = age
        self.user_type = user_type

    def access_database(self):
        if self.user_type == 'superuser':
            print('access granted')
        else:
            print('access denied')


class SuperUser(User):
    def __init__(self, name, age, user_type='superuser'):
        super().__init__(name, age, user_type)


