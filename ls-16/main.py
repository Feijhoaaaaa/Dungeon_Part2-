import math
class Circle:
    Num = 0
    def __init__(self, R):
        self.R = R
        Circle.Num+=1
    def S(self):
        print(f"S={2*math.pi*R}")
    def P(self):
        print(f"P={math.pi*R**2}")
        print(Circle.Num)

         
R = int(input("R:"))
C = Circle(R)
print(C.S())
print(C.P())
