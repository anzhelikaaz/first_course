import turtle

color_wn = input('Color background: ')
wn = turtle.Screen()
wn.bgcolor(color_wn)

tess = turtle.Turtle()
color_tess = input('Color Tess: ')
tess.shape('turtle')
tess.color(color_tess)

distance = 10
angle = 36
# tess.penup
count_loop = int(input('Count of loop iterations: '))
for t in range(count_loop):
    tess.stamp()
    tess.forward(distance)
    tess.left(angle)
    distance = distance + 5
    # angle = angle - 3

wn.exitonclick()

