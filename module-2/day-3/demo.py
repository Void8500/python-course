number = int(input("Enter a number above 2: "))

# for i in range(2, number + 1, 2):
#    print(i)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"{number} is prime? {is_prime(number)}")