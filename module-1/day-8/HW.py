num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

maximum = num1
minimum = num1

if num2 > maximum:
    maximum = num2
if num3 > maximum:
    maximum = num3

if num2 < minimum:
    minimum = num2
if num3 < minimum:
    minimum = num3
    
print("Maximum number:", maximum)
print("Minimum number:", minimum)
