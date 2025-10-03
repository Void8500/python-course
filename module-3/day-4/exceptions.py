try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("Result is : ", result)
    print("Result is : ", result1)

except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("You can not divide by zero")
except NameError as ex:
    print(ex)

finally:
    print("I will always run")