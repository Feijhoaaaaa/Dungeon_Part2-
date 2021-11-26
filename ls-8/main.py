import math
import numba
print(numba.__version__)
a = []
t = 0
while True:
    t+=1
    a.append(math.factorial(math.factorial(t)))
    print(a[-1])
print(a)