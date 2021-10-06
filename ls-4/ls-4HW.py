arr = ["Vlad", "Den", "Zhenya"]
print("//3.4>>>")
print(f"Preglashau - {arr[0]}")
print(f"Preglashau - {arr[1]}")
print(f"Preglashau - {arr[2]}")
print()
print()
print()


print("//3.5>>>")
print(f"{arr[-1]} ne samozet priyti((((")
del arr[-1]
arr.append("Vova")
print(arr)
print(f"Preglashau - {arr[0]}")
print(f"Preglashau - {arr[1]}")
print(f"Preglashau - {arr[2]}")
print()
print()
print()


print("//3.6>>>")
print("Teper nas bolyshe!!!")
arr.insert(0,"Egor")
arr.insert(2,"Sasha")
arr.append("Bohdan")
print(f"Preglashau - {arr[0]}")
print(f"Preglashau - {arr[1]}")
print(f"Preglashau - {arr[2]}")
print(f"Preglashau - {arr[3]}")
print(f"Preglashau - {arr[4]}")
print()
print()
print()


print("//3.7>>>")
print("Mesta hvatit tilko dlya 2 gostey")
arr.pop()
arr.pop()
arr.pop()
arr.pop()
print(f"Preglashau - {arr[0]}")
print(f"Preglashau - {arr[1]}")
del arr[1]
del arr[0]
print(arr)
print()
print()


print("//3.8>>>")
list = ['Ua','UK', 'Nig', 'Ger', 'USA']
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.reverse()
print(list)

