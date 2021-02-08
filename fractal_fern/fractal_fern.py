import turtle
from math import sqrt

wn = turtle.Screen()
wn.title("Fractal Fern")
wn.colormode(255)
wn.setup(700, 700)
wn.bgcolor(0, 0, 0)

t = turtle.Turtle()
t.speed(0)


def fern(length, angle):
    if length < 2:
        t.pencolor(0, 255, 255)
    else:
        t.pencolor(255, int(50 + 10 * sqrt(length)), 10)
    if length < 1:
        return
    else:
        t.width(length/15)
        t.pendown()
        t.forward(length)
        t.left(90)
        fern(length/3, max(angle, 180-angle))
        t.right(angle)
        fern(length*4/5, angle)
        t.right(180-angle)
        fern(length/3, min(angle, 180-angle))
        t.left(90)
        t.penup()
        t.backward(length)


t.penup()
t.goto(0, -250)
t.left(102)
fern(120, 98)

t.hideturtle()

wn.exitonclick()
