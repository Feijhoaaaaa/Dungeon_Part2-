def FullTitleName(a, b):
    c = f"{a.title()} {b.title()}"
    return c
while True:
    a = str(input("Name:"))
    b = str(input("LastName:"))
    print("Enter 'q' to stop it.")
    if a=="q":
        break
    if b=="q": break
    print(FullTitleName(a,b))