import turtle
import math

wn = turtle.Screen()
wn.bgcolor('lightgreen')
bob = turtle.Turtle()
bob.speed(10)
bob.fillcolor('brown')

# making box of house
for b in range(4):
    bob.forward(100)
    bob.left(90)

bob.left(90)
bob.forward(100)

# making the roof
bob.right(45)
dist = math.sqrt(100 * 100 / 2)
bob.forward(dist)
bob.right(90)
bob.forward(20)
bob.left(135)
bob.forward(16)
bob.right(90)
bob.forward(10)
bob.right(90)
bob.forward(23)
bob.left(45)
bob.forward(37)

# making the door
bob.right(45)
bob.forward(102)
bob.right(90)
bob.forward(30)
bob.right(90)
bob.forward(60)
bob.left(90)
bob.forward(30)
bob.left(90)
bob.forward(60)

wn.exitonclick()