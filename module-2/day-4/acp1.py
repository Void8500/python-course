def decimal_binary(decimal_num):
    binary = ""
    temp = decimal_num

    while temp > 0:
        remainder = temp % 2
        temp = temp // 2

        new_binary = ""
        for i in str(remainder):
            new_binary += i
        for i in binary:
            new_binary += i

        binary = new_binary

    return binary if binary else "0"


num = int(input("Enter a decimal number: "))
print(f"Binary of {num} is {decimal_binary(num)}")
