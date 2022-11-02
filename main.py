from color import color_list
import turtle as t
import random




# set Attribute of turtle
kuya = t.Turtle()
kuya.shape('turtle')
kuya.color('darkgreen')
kuya.speed(6)
kuya.hideturtle() 
# Set the screen:
layar = t.Screen()
layar.colormode(255)

# Get Position :
def position():
    kuya.penup()
    kuya.setpos(-250.00, -250.00)
    kuya.pensize(20)

# Start To Draw dot
def draw(space, dot):
    for i in range(dot):
        for j in range(dot):
            kuya.color(random.choice(color_list))
            kuya.dot()
            kuya.penup()
            kuya.forward(space)
        kuya.backward(dot*space)
        kuya.left(90)
        kuya.forward(space)
        kuya.right(90)
    
position()
draw(50, 10)    

layar.exitonclick()

