# clock using turtle
import turtle
import time

t = turtle.Turtle()
turtle.title("Clock")

# changing background color of window screen
t.screen.bgcolor("#ddccdd")

# improves speed
t.speed(0)
# bringing turtle to home cordinates (0, 0) and direction East (INITIAL POSITION)
t.home()
# to write co-ordinates on screen
# t.write((0, 0))

# writing below clock
t.penup()
t.right(90)
t.forward(130)
t.write("Running Clock", align = "center", font = 10)
t.home()

#---------------------------------------------------------#
# drawing outer circle
# no drawing when moving
t.penup()
t.goto(0, -100)
# drawing on moving
t.pendown()
# dark outer circle
t.pensize(3)
# Fill the shape drawn after the call begin_fill().
t.begin_fill()
t.fillcolor("skyblue")

t.circle(100)

# drawing inner circle
t.penup()
t.home()
t.goto(0, -60)
t.pendown()
t.pensize(1)
t.circle(60)

t.end_fill()

#---------------------------------------------------------#
# giving numbers in clock
t.penup()
t.home()
# moving head left 90 deg
t.left(90)
for i in range(12) :
    # moving turtle right by 30deg
    t.right(360/12)
    # moving forward
    t.forward(85)
    # writing number
    t.write(i+1)
    # going to center
    t.goto(0, 0)

#---------------------------------------------------------#
# draw arms
def draw_hour_arm():
    t.penup()
    t.home()
    t.right(180)
    t.pendown()
    t.pensize(5)
    t.forward(40)

def draw_minute_arm():
    t.penup()
    t.home()
    t.right(270)
    t.pendown()
    t.pensize(3)
    t.forward(70)

draw_hour_arm()
draw_minute_arm()

t.color("black")
t.pensize(2)
t.penup()
t.home()
t.left(90)

while True:
    # current time since while loop will take time to run
    start = time.time()
    t.pendown()
    t.forward(60)
    # waits for a second (subtracting some time to increase accuracy)
    time.sleep(1 - (time.time()-start))
    # removes drawed line
    t.undo()
    t.goto(0, 0)
    # moving second hand 12 deg right
    t.right(360/60)


#---------------------------------------------------------#
# to retain window open
turtle.done()
