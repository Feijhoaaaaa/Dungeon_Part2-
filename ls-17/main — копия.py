class Animal:
    def __init__(self, age, kind, color, name,time, data):
        self.age = age
        self.kind = kind
        self.color = color
        self.name = name
        self.time = time
        self.data = data
    def data(self):
        print(f"Dog is {2021-self.data}")
    def sus(self):
        print(f"Age:{self.age}\nKind:{self.kind}\nColor:{self.color}")
class Dog(Animal):
    def bark(self):
        print(f"Dog {self.name} is barking")
    def dogeat(self):
        print(f"Dog {self.name} eat at {self.time}")   
class Cat(Animal):
    def washing(self):
        print(f"Cat {self.name} the cat is washing")
    def sitting():
        print(f"Cat {self,name} is sitting on windows")
class Frog(Animal):
    def bark(self):
        print(f"Frog {self.name} is barking")


dog = Dog(5, dog, black, barsik, dogdata)
cat = Cat(3, cat, white, loh, catdata)
frog = Frog(1, frog, green, noname, frogdata)

dogdata = int(input("Dog:"))
catdataa = int(input("cat:"))
frogdata = int(input("frog:"))
dog.bark()
dog.dogeat()
cat.washing()
cat.sitting()
frog.bark()
dog.data()
cat.data()
frog.data()
