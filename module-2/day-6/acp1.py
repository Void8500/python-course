import turtle 

screen = turtle.Screen()
screen.bgcolor("light blue") 
screen.title("Turtle Square")
numsides = 4
angle = 360.0 / numsides
pen = turtle.Turtle()

# Simplified using loops
for i in range(numsides):
    pen.forward(100)
    pen.right(angle)

turtle.done()