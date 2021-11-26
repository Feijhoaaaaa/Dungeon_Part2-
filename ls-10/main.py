arr = ["block", "Water", "Grass", "Ferum"]
arr2 = []
while arr:
    a = arr.pop()
    print("Element",a,"was kiked((")
    arr2.append(a)
for i in arr2:
    print(i,"was added11")
print(arr2)