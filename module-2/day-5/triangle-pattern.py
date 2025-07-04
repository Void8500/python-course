rows = int(input("Enter amount of rows: "))
for i in range(rows):
    for j in range(i + 1):
        print("*", end=' ')
    print()