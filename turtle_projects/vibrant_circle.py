# a vibrating circle using turtle
import turtle

# setting turtle
t = turtle.Turtle()
turtle.title("Vibrant Circle")

s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")

# speed 0 to 10 - 0 for max speed
t.speed(0.5)

t.hideturtle()

t.penup()
t.goto(0, 200)
t.pendown()

a = 0; b = 0
while True:
    t.forward(a)
    t.right(b)
    # to get ratio of 3:1
    a += 3
    b += 1
    # to break this loop
    if b == 216: break

# to retain window open
turtle.done()