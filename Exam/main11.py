Dict = {'a':1, 'b':2, 'c':3, 'd':4}
print(Dict)
for x,y in Dict.items():
    if Dict[x]%2==0:
        Dict[x] = "Even"
    else:
        Dict[x] = "odd"
print(Dict)
        