def cube(n):
    return n ** 3

def isdivis(n):
    if n % 3 == 0:
        return cube(n)
    else:
        return f"{n} is not divisible by 3"

num = int(input("Enter a number: "))
print(isdivis(num))