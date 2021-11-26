Users = {"Zhenia":['Task0','Task1','Task2','Task3','Task4'],
        "Maciej":['Task0','Task1','Task2'],
        "Sasha":['Task0','Task1'],
        "Den":['Task0','Task1','Task2','Task3']}
for x,y in Users.items():
    print("_"*60)
    print(f"Her name is{x}, he completed:")
    for i in y:
        print(f"\t\/{i}")
    print("_"*60)