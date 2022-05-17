#drawing some flower by turtle
import turtle


wn = turtle.Screen()
flower = turtle.Turtle()
flower.speed(0)
flower.color('pink')
wn.bgcolor('green')
flower.pensize(5)

for f_ in range(10):
    for _ in range(3):
        flower.left(25)
        flower.forward(50)
    flower.left(130)
    for _ in range(3):
        flower.forward(50)
        flower.left(25)

wn.exitonclick()