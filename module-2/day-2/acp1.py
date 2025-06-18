base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1

if exponent == 0:
    result = 1
elif exponent > 0:
    for i in range(exponent):
        result *= base
else:
    for i in range(-exponent):
        result *= base
    result = 1 / result

print(f"{base} raised to the power {exponent} is {result}")