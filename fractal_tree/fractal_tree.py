import turtle
import random
from math import sqrt

wn = turtle.Screen()
wn.title("Fractal Tree")
wn.colormode(255)
wn.setup(700, 700)
wn.bgcolor(0, 0, 0)

t = turtle.Turtle()
t.speed(0)


def tree(length):
    if length < 2:
        t.pencolor(255, 100, 0)
    else:
        t.pencolor(10, int(50 + 12 * sqrt(length)), int(255 - 5 * sqrt(length)))
    if length < 1:
        return
    else:
        t.width(length/12)
        t.pendown()
        t.forward(length)
        t.left(30)
        tree(length/random.uniform(1, 2.5))
        t.right(60)
        tree(length/random.uniform(1, 2.5))
        t.left(30)
        t.penup()
        t.backward(length)


t.penup()
t.goto(0, -250)
t.left(90)
tree(150)

t.hideturtle()

wn.exitonclick()
