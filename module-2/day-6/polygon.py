import turtle    #importing library
turtle.Screen().bgcolor("red")
turtle.Screen().setup(700,500)
polygon = turtle.Turtle() #defined variable
 
num_sides = 3 #variable
side_length = 100
angle = 360.0 / num_sides
#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)
polygon.penup()
polygon.left(90)
polygon.forward(50)
polygon.pendown()
polygon.right(90)
for i in range(num_sides):
    polygon.forward(100)
    polygon.right(120)
    
turtle.done()