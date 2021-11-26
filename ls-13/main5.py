arr = [1,2,3,4,5,6,7,8,9,10]
arr_2 = ["true_2" if i%2==0 else "True_3" if i%3==0 else "Folse" for i in arr]
print(arr_2)