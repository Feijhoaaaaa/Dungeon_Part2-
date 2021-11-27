import random
n = int(input("How many:"))
arr = []
for i in range(n):
    arr.append(random.randint(0,15))
print(arr)
print(f"First:{arr[0]} \nLast:{arr[-1]}")