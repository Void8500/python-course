print("Enter the three numbers:")

values = [0, 0, 0]

for i in range(3):
    values[i] = int(input(f"Value {i + 1}: "))

print("Numbers input")
print("Values:", values)

corrected = [values[1], values[2], values[0]]

print("Numbers swapped")
print("Values:", corrected)