import turtle
import random

wn = turtle.Screen()
wn.title("Tiny Planet")
wn.colormode(255)
wn.setup(700, 700)
wn.bgcolor(0, 0, 0)

t = turtle.Turtle()
t.speed(0)


def tree(l):
    if l < 1:
        return
    else:
        t.width(l/15)
        t.forward(l)
        t.left(30)
        tree(l/random.uniform(1, 3))
        t.right(60)
        tree(l/random.uniform(1, 3))
        t.left(30)
        t.backward(l)


dist = random.uniform(50, 150)

t.penup()
t.rt(90)
t.fd(dist)
t.lt(90)
t.pendown()
for i in range(random.randint(30, 70)):
    t.penup()
    t.circle(dist, random.uniform(0, 360))
    t.rt(90)
    t.pendown()
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tree(random.uniform(10, 70))
    t.lt(90)
    t.pencolor(0, 0, 0)

t.hideturtle()

wn.exitonclick()
