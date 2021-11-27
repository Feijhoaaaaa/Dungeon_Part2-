arr = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
print(arr)
for i in arr:
    if i <30 and i%3==0:
        arr.remove(i)
print(arr)
print(f"Sum is:{sum(arr)}")
