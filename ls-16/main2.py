class Human:
    def __init__(self, name, surname, place, year):
        self.name = name
        self.surname=surname
        self.place=place
        self.year=year
        print("Human created")
    def sus(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\nPlase: {self.place}\nYears: {self.year}")
    def susee(self):
        print(f"Years:{2021 - int(self.year)}")


p1 = Human("Den","Dmitriev","ua","1997")
p1.sus()
p2 = Human("Bohdan", "Horbenko", "ua", "2005")
p3 = Human("Vlad", "Tkachenko", "ua", "2005")
p2.susee()