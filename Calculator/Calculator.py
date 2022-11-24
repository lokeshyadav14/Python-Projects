from tkinter import *
#variable to store expression to evaluate
exp = ""
#-----------------defining functions-------------#

def press(c):
    global exp
    exp += str(c)
    #updating exp entry widget
    equation.set(exp)

def solve():
    try:
        global exp
        #eval function evaluate the expression
        total = str(eval(exp))
        equation.set("Result = " + total)
        exp = ""
    except:
        equation.set(" Error ")
        exp = ""

def clear():
    global exp
    exp = ""
    equation.set("")

def delete():
    global exp
    exp = exp[0:-1]
    equation.set(exp)

#--------------starting program------------------#

window = Tk()
window.title("Calculator")

#creating widgets
equation = StringVar()
exp_field = Entry(window, textvariable = equation, border = 5)

button1 = Button(window, text = ' 1 ', command = lambda:press(1), height = 2, width = 7, bg = "light green", activebackground="green")
button2 = Button(window, text = ' 2 ', command = lambda:press(2), height = 2, width = 7, bg = "light green", activebackground="green")
button3 = Button(window, text = ' 3 ', command = lambda:press(3), height = 2, width = 7, bg = "light green", activebackground="green")

button4 = Button(window, text = ' 4 ', command = lambda:press(4), height = 2, width = 7, bg = "light green", activebackground="green")
button5 = Button(window, text = ' 5 ', command = lambda:press(5), height = 2, width = 7, bg = "light green", activebackground="green")
button6 = Button(window, text = ' 6 ', command = lambda:press(6), height = 2, width = 7, bg = "light green", activebackground="green")

button7 = Button(window, text = ' 7 ', command = lambda:press(7), height = 2, width = 7, bg = "light green", activebackground="green")
button8 = Button(window, text = ' 8 ', command = lambda:press(8), height = 2, width = 7, bg = "light green", activebackground="green")
button9 = Button(window, text = ' 9 ', command = lambda:press(9), height = 2, width = 7, bg = "light green", activebackground="green")

button0 = Button(window, text = ' 0 ', command = lambda:press(0), height = 2, width = 7, bg = "light green", activebackground="green")

button_plus = Button(window, text = ' + ', command = lambda:press('+'), height = 2, width = 7, bg = "light green", activebackground="green")
button_minus = Button(window, text = ' - ', command = lambda:press('-'), height = 2, width = 7, bg = "light green", activebackground="green")
button_multiply = Button(window, text = ' x ', command = lambda:press('*'), height = 2, width = 7, bg = "light green", activebackground="green")
button_divide = Button(window, text = ' / ', command = lambda:press('/'), height = 2, width = 7, bg = "light green", activebackground="green")

button_back = Button(window, text = ' <- ', command = lambda:delete(), height = 2, width = 16, bg = "light green", activebackground="green")
button_clear = Button(window, text = ' Cancel ', command = lambda:clear(), height = 2, width = 16, bg = "light green", activebackground="green")
button_equal = Button(window, text = ' = ', command = lambda:solve(), height = 2, width = 16, bg = "light green", activebackground="green")


#------------------griding all stuff------------------------#

exp_field.grid(row = 0, columnspan = 4, ipadx = 55, ipady = 10, pady = 10, padx = 5)


button_clear.grid(row = 1, column = 0, columnspan=2)
button_back.grid(row = 1, column = 2, columnspan=2)


button9.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button7.grid(row = 2, column = 2)
button_plus.grid(row = 2, column = 3)

button6.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button4.grid(row = 3, column = 2)
button_minus.grid(row = 3, column = 3)

button3.grid(row = 4, column = 0)
button2.grid(row = 4, column = 1)
button1.grid(row = 4, column = 2)
button_multiply.grid(row = 4, column = 3)

button0.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan = 2)
button_divide.grid(row = 5, column = 3)

#showing window
window.mainloop()
