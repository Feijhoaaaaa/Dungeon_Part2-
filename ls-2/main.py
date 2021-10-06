import math 

a = int(input("Сторона a:"))
b = int(input("Сторона b:"))
c = int(input("Сторона c:"))
p = (a + b + c)/2
r = int(p*(p-a)*(p-b)*(p-c))
print(p)
input()
r = math.sqrt(r)
print(r)
input()