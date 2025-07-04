import turtle  # Import turtle graphics module

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("light blue")  # Set background color
screen.title("Turtle Drawing")

# Create the turtle
pen = turtle.Turtle()

# Initial size
size = 0

# Infinite loop to draw shapes
while True:
    for i in range(4):  # Draw a square
        pen.forward(size + 1)
        pen.left(90)
        size -= 5  # Decrease size within the loop
    size += 1  # Slowly increase size to create a dynamic pattern