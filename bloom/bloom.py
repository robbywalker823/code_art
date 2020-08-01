import turtle

wn = turtle.Screen()
wn.title("Bloom")
wn.colormode(255)
wn.setup(700, 700)
wn.bgcolor(0, 0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

c_r = 0
c_g = 100
c_b = -100

r = 270
for i in range(350):
    petal_color = (abs(c_r), abs(c_g), abs(c_b))
    t.pencolor(255, 255, 255)
    t.fillcolor(petal_color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    r = 0.99 * r
    t.rt(137.5)

    c_r += 1
    if c_r > 255:
        c_r = 255

    c_g += 1
    if c_g > 255:
        c_g = 255

    c_b += 1
    if c_b > 255:
        c_b = 255

wn.exitonclick()
