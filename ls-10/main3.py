def Menu(Size, *Type):
    print(f"Yor Pizza is {Size} \n Type:")
    for i in Type:
        print(i)
a = int(input("Wich size?:"))
Menu(a,"4 ocean")
Menu(a,"4 ocean", "Hawai", "Maxico")