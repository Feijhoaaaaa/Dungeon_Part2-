Name = {'Den':24, 'Vova':15, 'Zheka':17}
print(Name['Den'])
NameV2 = {'Egor':24, 'Anton':19, 'Danil':10}
Car = {'Porhe':1943, "Camaro":1984,"Ferrari":103,"Lada":2004,"Bugati":2000}
python = Name.copy()
python.update(Car)
print(python)
olds = Name | NameV2 | Car
print(olds)
print(Name.clear())
print(Name)


