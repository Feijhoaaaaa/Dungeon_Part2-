import random

x = int(input("X:"))
y = int(input('Y:'))
s = int(input('p:'))
p = int(input('s:'))
TwoDArr = [[random.randint(0,9) for i in range(x)] for i in range(y)]
print('_'*60)
for i in TwoDArr:
    print(i)
print('_'*60)
print(len(TwoDArr))
Diag = [TwoDArr[i][i] for i in range(0,len(TwoDArr))]
Diag2 = [TwoDArr[s+i][p+i] for i in range(-s,len(TwoDArr)-p)]
print(Diag)
print(Diag2)