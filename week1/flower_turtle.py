
import turtle

wn = turtle.Screen()
flower = turtle.Turtle()
flower.speed(0)
flower.pensize(5)


for aColor in ["yellow", "red", "purple", "blue", "hotpink", "orange", "green", "lightblue", "gold"]:
    flower.color(aColor)
    for _ in range(3):
        flower.left(25)
        flower.forward(50)
    flower.left(130)
    for _ in range(3):
        flower.forward(50)
        flower.left(25)

wn.exitonclick()