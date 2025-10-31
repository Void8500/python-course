count = int(input("Enter amount of numbers you want to multiply: "))

numbers = []

for i in range(count):
    n = int(input(f"Enter number {i+1}: "))
    numbers.append(n)

numbers = tuple(numbers)

product = 1
for num in numbers:
    product *= num

print("Product of all numbers:", product)
print(tuple(numbers))