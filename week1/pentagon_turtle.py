#drawing a regular pentagon
import turtle


wn = turtle.Screen()
pol = turtle.Turtle()
pol.color('darkgreen')
pol.speed(15)

for p in range(5):
    pol.forward(100)
    pol.left(72)