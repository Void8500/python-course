list1 = []
userleng = int(input("Enter the length of the list: "))
for i in range(userleng):
    elem = int(input("Enter element: "))
    list1.append(elem)
total = 0
for i in list1:
    total += i
print("The sum is: ", total)
    
maxi = max(list1)
mini = min(list1)
rever = list1[::-1]
leng = len(list1)
avg = total / leng

print("The minimum number in this list is: ", mini)
print("The maximum number in this list is: ", maxi)
print("The list reversed is: ", rever)
print("There are", leng, "elements in this list")
print("The average of these elements is: ", avg)
