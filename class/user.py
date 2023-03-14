class user:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name =  last_name
        self.login_attempt = 0
    def describe(self):
        describe = f'my name is {self.first_name} {self.last_name}, nice to meet you'
        return describe
    def greeting(self):
        greet = f'nice to meet you {self.first_name}'
        return greet
    def increment_login_attempt(self):
        self.login_attempt+=1
    def reset_login_attempt(self):
        self.login_attempt = 0
user1 = user('Yeabsira', 'Nigusse')
print(user1.describe())
print(user1.greeting()) 
print(user1.login_attempt)
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
print(user1.login_attempt)
user1.reset_login_attempt()
print(user1.login_attempt)
#inheritance
class Admin(user):
    def __init__(self,first,last):
        super().__init__(first,last)
    privilage = ['can delate post','can ban user', 'can add post']
    def show_privilage(self):
        for privilage in privilage():
            print(privilage.title())
yeab = Admin('Yeabsira','Nigusse')
yeab.show_privilage()