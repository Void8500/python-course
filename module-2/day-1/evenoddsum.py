num = int(input("Enter a number: "))
sum = 0
if num % 2 == 0:
    print(f"{num} is even number")
    for i in range(num, 0, -2):
        print(f"{i} ", end = "")
        sum += i
    print(f"\nEven sum: {sum}")
else:
    print(f"{num} is odd number")
    for i in range(num, 0, -2):
        print(f"{i} ", end = "")
        sum += i
    print(f"\nOdd sum: {sum}")
