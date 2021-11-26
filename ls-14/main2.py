import random
n = int(input("n:"))
m = int(input("m:"))
massive = [[random.randint(0,9) for i in range(n)] for i in range(m)]
for i in massive:
    print(i)
