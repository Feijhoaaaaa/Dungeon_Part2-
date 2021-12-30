class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def sus(self):
        print(f"Name:{self.name}\nSurname:{self.surname}\nAge:{self.age}")
class Student(Human):
    def study(self):
        print(f"Student:{self.name} is studing")
class Teacher(Human):
    pass




p1 = Student("Bohdan", "Horbenko", 12)
p1.sus()
p1.study()
