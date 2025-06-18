base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (n): "))

result = 1

if exponent == 0:
    result = 1
elif exponent > 0:
    for i in range(exponent):
        result *= base
else:
    # For negative exponent, calculate positive power then invert
    for i in range(-exponent):
        result *= base
    result = 1 / result

print(f"{base} raised to the power {exponent} is {result}")