arrStr = ['Day','month','Year','Second','Hour','Minute']
arrInt = [1,3,5,9,31,12,30]
Dict = {}
a = int(input('Raised to power:'))
for i in range(len(arrStr)):
    Dict[arrStr[i]] = arrInt[i]**a
print(Dict)
