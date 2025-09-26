def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def mult(num1, num2):
    return num1 * num2

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
opt = input("Enter Operator: ")
if opt == "+":
   # ans = add(num1, num2)
    #print(ans)
    print(add(num1, num2))
elif opt == "-":
    print(sub(num1, num2))
elif opt == "/":
    print(divide(num1, num2))
elif opt == "*" or "x":
    print(mult(num1, num2))
else:
    print("Invalid Operator")