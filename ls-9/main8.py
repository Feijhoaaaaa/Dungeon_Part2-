def FullTitleName(a, b):
    c = f"{a.title()} {b.title()}"
    return c
a = str(input("Name:"))
b = str(input("LastName:"))
print(FullTitleName(a,b))