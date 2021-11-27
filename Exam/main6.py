MyDishes = ["Pizza", "Falafel", "Carrot cake"]
FriendDishes = MyDishes.copy()
Dishes = str(input("Friend dishes:"))
FriendDishes.append(Dishes)
print("Friend dishes is:")
print("_"*60)
for i in FriendDishes:
    print(i)