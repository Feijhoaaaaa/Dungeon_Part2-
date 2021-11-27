n = int(input("Your age:"))
if n<0:
    print("Baby")
elif n>=2 and n<4:
    print("Kid")
elif n>=4 and n<13:
    print("Child")
elif n>=13 and n<20:
    print("Teenager")
elif n>=20 and n<65:
    print("Adult")
elif n>=65:
    print("Old")
else:
    print("Age is incorrect")