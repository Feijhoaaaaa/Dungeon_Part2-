import math
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = b**2 - 4*a*c
if d>0:
    print((-b+math.sqrt(d))/2*a)
    print((-b-math.sqrt(d))/2*a)
elif d==0:
    print(-b/2*a)
else:
    print("net korney")
