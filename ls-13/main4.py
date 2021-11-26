arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
arr_2 = [i if i>5 else "Error" for i in arr]
#for i in arr:
#    if i>5:
#        arr_2.append(i)
#    else:
#        arr_2.append("Error")
print(arr_2)