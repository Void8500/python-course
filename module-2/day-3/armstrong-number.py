num = int(input("Enter a number: "))

sum = 0

num_digits = len(str(num))

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")