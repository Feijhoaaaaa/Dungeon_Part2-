arr = []
arr.append("1")
arr.append("2")
arr.append("3")
arr.append("4")
arr.append("5")
arr.append("6")
print(arr)
arr[2] = "mers"
print(arr)
arr.insert(2, "bmw")
print(arr)
del arr[3]
print(arr)
del_arr = arr.pop()
print(del_arr)
print(arr)

print("Vot vse mashyny ", arr)
print(f'vot vasha mashyna {arr[3].title()}')

print(f'vot vasha mashyna {arr[2].title()}')

print(f'vot vasha mashyna {arr[1].title()}')
del arr[3]
del arr[2]
del arr[1]
print(arr)