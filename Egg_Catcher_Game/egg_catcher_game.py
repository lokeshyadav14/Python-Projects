from itertools import cycle
from random import randrange
from tkinter import Tk, Canvas, messagebox


# creating window and setting environment -------------------------------------------------------------------------------------------
canvas_width = 800
canvas_height = 400

win = Tk()
win.title('Egg Catcher')
win.resizable(width=False, height=False)

c = Canvas(win, width=canvas_width, height=canvas_height, background='deep sky blue')
# Ground - width=0 for no visible line of rectangle
c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill='sea green', width=0)
# SUN - widht=0 for no visible line of oval shape
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.pack()

# eggs--------------
color_cycle = cycle(['light blue', 'light pink', 'green', 'light yellow', 'violet', 'light green', 'red', 'blue', 'yellow', 'blue'])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 250
egg_interval = 5000
difficulty_factor = 0.95

# egg catcher-------------------
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height - catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_start_x2, catcher_start_y2, start=200, extent=140, style='arc', outline=catcher_color, width=3)

# scoring part------------------
score = 0
score_text = c.create_text(10, 10, anchor='nw', font=('Arial',16,'bold'), fill='darkblue', text='Score: '+str(score))

# Lives--------------------------
lives_remaining = 3
lives_text = c.create_text(canvas_width-10, 10, anchor='ne', font=('Arial',16,'bold'), fill='darkblue', text='Lives: '+str(lives_remaining) )


# ------------------------------------------------------------------------------------------------------
# creating eggs------------------ running continuously
eggs = []
def create_eggs():
    # generates eggs starting position
    x = randrange(30, 740)
    y = 20
    # next() function will return next color of cycle
    new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    # after egg_interval it will create an egg again
    win.after(egg_interval, create_eggs)

# falling eggs------------------- running continuously
def move_eggs():
    for egg in eggs:
        # to get coordinates of a shape 
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        # move egg by 5 considering its coordinates as 0
        c.move(egg, 0, 5)
        # if any egg reach to ground
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    # again move eggs after egg_speed time interval
    win.after(egg_speed, move_eggs)

# dropped eggs------------------
def egg_dropped(egg):
    # remove egg instance from eggs list
    eggs.remove(egg)
    # delete egg instance
    c.delete(egg)
    # update life_remaining
    lose_a_life()
    # if no lives remaning then display score and end the game
    if lives_remaining == 0:
        messagebox.showinfo('GAME OVER!', 'Final Score : ' + str(score))
        win.destroy()

# updates lives_remaining-------
def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text='Lives : ' + str(lives_remaining))

# catch checkig ---------------- running continuously
def catch_check():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher)
    # checking all eggs one by one is they in catcher or not
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    # checking again after 100 milisecond
    win.after(100, catch_check)

# increasing score after successful catch
def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text, text='Score : ' + str(score))

# ------------------------------------------------------------------------------------------------------
# functions to move catcher
def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    # giving gap of 10
    if x1 > 10:
        # moving left so -20 sign
        c.move(catcher, -20, 0)
    
def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    # giving gap of 10
    if x2 < canvas_width-10:
        # moving right so +20 sign
        c.move(catcher, 20, 0)

# bind function is used to bind keys with function
c.bind('<Left>', move_left)
c.bind('<Right>', move_right) 
# to sure that keys are pressed
c.focus_set()

# starting our game --------------------------------------------------------------------------------------
win.after(1000, create_eggs)
win.after(1000, move_eggs)
win.after(1000, catch_check)
# -------------------------------------------------------------------------------------------------------

win.mainloop()