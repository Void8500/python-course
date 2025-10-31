def square_filter(start, end):
    numbers = []
    squares = []
    even_squares = []
    odd_squares = []

    for i in range(start, end + 1):
        numbers.append(i)
        j = i * i
        squares.append(j)
        if j % 2 == 0:
            even_squares.append(j)
        else:
            odd_squares.append(j)

    print("Numbers:", numbers)
    print("Squares:", squares)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)

a = int(input("Enter starting number: "))
b = int(input("Enter end number: "))
square_filter(a, b)