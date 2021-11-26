x = int(input("x:"))
y = 0
for i in range(1, x+1):
    y += 1/2**i
print(y)