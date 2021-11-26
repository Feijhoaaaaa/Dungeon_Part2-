arr = ["Block", "Water","Grass", "Axe"]
arr2 = []
def DelElement():
    while arr:
        a = arr.pop()
        print("Elem", a,"was kiked((")
        arr2.append(a)
def ShowElement():
    for i in arr2:
        print(i,"was added))")
DelElement()
ShowElement()
