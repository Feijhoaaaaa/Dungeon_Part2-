class Restaurant:
    def __init__(self, Restaurant_name, Cuisine_type, Number_served):
        self.Restaurant_name = Restaurant_name
        self.Cuisine_type = Cuisine_type
        self.Number_served = Number_served 
    def Restaurant_describe(self):
        print(f"Restaurant name:{self.Restaurant_name}\nCuisine type:{self.Cuisine_type}")
    def Restaurant_open(self):
        print(f"Restaurant {self.Restaurant_name} is open!")
    def set_number_served(self):
        self.Number_served = int(input("SAet number served:"))
        print(self.Number_served)
    def increment_numbers_served(self):
        self.Number_served += 10
        print(self.Number_served)

class IceCreamStand(Restaurant):
    def __init__(self, Restaurant_name, Cuisine_type, Number_served, flavors):
        self.Restaurant_name = Restaurant_name
        self.Cuisine_type = Cuisine_type
        self.Number_served = Number_served 
        self.flavors = flavors
    def printFlavors(self):
        for i in self.flavors:
            print(i)
IceCreamStand1 = IceCreamStand("Borshch", "UA", 0, ["Baunty", "Obamka", "Fistaschkowoje"])
restaurant0 = Restaurant("Sakura", "Asian", 0)
restaurant1 = Restaurant("Hamburger....", "USA", 0)
restaurant2 = Restaurant("Borshch", "UA", 0)
restaurant0.Restaurant_describe()
restaurant1.Restaurant_describe()
restaurant2.Restaurant_describe()
restaurant0.Restaurant_describe()
restaurant0.Restaurant_open()
restaurant0.set_number_served()
restaurant0.increment_numbers_served()
IceCreamStand1.printFlavors()
