import random
import time
from tkinter import Tk, Button, DISABLED, Label
import tkinter.font as font


#------------ function to start game -------------------------------------
def start_game():
    welcome.destroy()
    start_button.destroy()
    for x in range(6):
        for y in range(4):
            # displaying buttons
            button = Button(command = lambda a=x, b=y : show_symbols(a,b), width=6, height=3, fg = 'red', bg = 'lightblue')
            button['font'] = font.Font(size=25)
            button.grid(column=x, row=y)
            # storing buttons details (cordinates and symbols)
            buttons[x,y] = button
            button_symbols[x, y] = symbols.pop()

#------------ function to show symbols on clicking ------------------------
def show_symbols(x, y):
    global first
    global previousx, previousy
    # showing symbol on button on click
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    # if first card is opening
    if first:
        previousx = x
        previousy = y
        first = False
    # if it is a second card
    elif previousx != x or previousy != y:
        # if both symbols are not same then again hide both
        if buttons[previousx, previousy]['text'] != buttons[x,y]['text']:
            time.sleep(0.5) # so that user can see the text for some time
            buttons[previousx, previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
        # if they are same disabled the buttons
        else:
            buttons[previousx, previousy].configure(bg='lightgreen', fg='blue')
            buttons[x,y].configure(bg='lightgreen', fg='blue')
            buttons[previousx, previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True
    # print("The width of Tkinter window:", win.winfo_width())
    # print("The height of Tkinter window:", win.winfo_height())

#-------------- Initializing the matchmaker ----------------------------------------------------
win = Tk()
win.title("Matchmaker")
win.geometry('744x572')
win.configure(bg='#00FFEF')
# remove option of resize window
win.resizable(width=False, height=False)

welcome = Label(win, text = 'Welcome to Matchmaker Game\n Click on below button to play game', font=('Helvetica 30'), bg='#00FFEF')
start_button = Button(command = lambda : start_game(), text='Start Game', width=20, height=4, font=('Helvetica 20'), bg = 'lightgreen')
welcome.pack(pady=50)
start_button.pack(pady=50)


# taking record of previous card or first card
first = True
previousx = 0
previousy = 0


# codes of some symbols (12 pairs)
symbols = [u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B', u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728',
        u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B', u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728']
# print(u'\u2702') code for scissor symbol

# shuffling symbols to get new cordinates in each round
random.shuffle(symbols)


# dictionary to store buttons and its symbols
buttons = { }
button_symbols = { }

# to remain window open
win.mainloop()