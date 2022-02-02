class User:
    def __init__(self, name, surname, age, sex, login_attempts):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.login_attempts = login_attempts
    def describe(self):
        print(f"Name: {self.name.title()}\nSurname: {self.surname.title()}\nAge: {self.age}\nSex: {self.sex}")
    def hellowUser(self):
        print(f"Hellow {self.surname.title()} {self.name.title()}!!")
    def increment_login_attempts(self):
        self.login_attempts +=1
        print(f"Login attempts is {self.login_attempts}!")
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login attempts is reset!")
class Admin(User):
    def __init__(self, name, surname, age, sex, login_attempts, previliges):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.login_attempts = login_attempts
        self.previliges =previliges
    def PrintPreviliges(self):
        for i in self.previliges:
            print(i)
u0 = User("bohdan", "horbenko", 16, "M", 0)
u1 = User("Vlad", "Vlad", 16, "M", 0)
u2 = User("vova", "vavo", 16, "M", 0)
u0.describe()
u0.hellowUser()
u1.describe()
u1.hellowUser()
u2.describe()
u2.hellowUser()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.reset_login_attempts()
admin = Admin('John', 'John', 45, "m", 0, ["Edit", "delete", "add"])
admin.PrintPreviliges()