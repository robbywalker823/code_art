import turtle

wn = turtle.Screen()
wn.title("Fibonacci Spiral")
wn.colormode(255)
wn.setup(700, 700)
wn.bgcolor(0, 0, 0)

t = turtle.Turtle()
t.speed(0)
t.pencolor(255, 255, 255)
t.pensize(2)


def polygon(n, l):
    for i in range(n):
        t.forward(l)
        t.right(360/n)


def fibonacci(r):
    previous = 0
    current = 1
    for x in range(r):
        t.circle(current, 90)
        following = current + previous
        previous = current
        current = following


def golden(r):
    previous = 0
    current = 1
    for x in range(r):
        polygon(4, current)
        t.backward(previous)
        following = current + previous
        previous = current
        current = following
        t.left(90)


golden(20)

t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()
t.pencolor(255, 0, 0)

fibonacci(20)

t.hideturtle()

wn.exitonclick()
