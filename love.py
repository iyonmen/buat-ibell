import math
import time
import turtle


def heart_function(t):
    return 16 * math.sin(t) ** 3


def heart_function_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)


def draw_heart():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.title("Precise Heart Shape")
    screen.bgcolor("#FFE4E1")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    t.penup()
    t.goto(heart_function(0) * 20, heart_function_y(0) * 20)
    t.pendown()
    t.color("#FF69B4")
    t.begin_fill()
    for i in range(360):
        x = heart_function(math.radians(i)) * 20
        y = heart_function_y(math.radians(i)) * 20
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(heart_function(0) * 17, heart_function_y(0) * 17)
    t.pendown()
    t.color("purple")
    t.begin_fill()
    for i in range(360):
        x = heart_function(math.radians(i)) * 17
        y = heart_function_y(math.radians(i)) * 17
        t.goto(x, y)
    t.end_fill()

    colors = ['#FFE4E1', 'pink', 'indigo', 'violet']
    t.penup()
    t.goto(0, -20)
    t.hideturtle()
    while True:
        for color in colors:
            t.color(color)
            t.write("I love u", align="center", font=("Arial", 56, "bold"))
            time.sleep(0.5)


draw_heart()
