class Ask():
    def __init__(self, age, data, name, surname, education):
        self.age = age
        self.data = data
        self.name = name
        self.surname = surname
        self.education = education
    def Sus(self):
        print(f"Name:{self.name}\nSurname:{self.surname}\nAge:{self.age}\nData:{self.data}\nEducation:{self.education}")

name = str(input("Name:"))
surname = str(input("Surname:"))
age = int(input("Age:"))
data = int(input("Data:"))
education = str(input("Education:"))

user1 = Ask(age, data, name, surname, education)
user1.Sus()
