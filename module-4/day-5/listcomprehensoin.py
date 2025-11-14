n = int(input("Enter a number: "))
odds1 = [i for i in range(n) if i%2]
odds2 = [i for i in range(n+1) if i%2]
print(odds1, odds2)

fruits = ["apple","banana","mango","grape"]
updated = [f.capitalize() for f in fruits]
print(updated)