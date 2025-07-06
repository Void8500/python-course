rows = int(input("Enter amount of rows: "))
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=' ')
    for k in range(i + 1):
        print("*", end=' ')
    print()