try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise Exception("Invalid age")
    print("Valid age")
    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")
except ValueError:
    print("Please enter a valid whole number")
except Exception as e:
    print(e)