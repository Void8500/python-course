def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):    
        if n % i == 0:
            return False
    return True

lowrange = int(input("Enter the lower range: "))
uprange = int(input("Enter the upper range: "))

for j in range(lowrange, uprange + 1):
    if is_prime(j):
        continue
    print(j)