from tkinter import *
import Telephone_book_database as db
    
def delete_command():
    db.delete(mobile_number.get())
    list.delete(0, END)
    list.insert(END, (mobile_number.get() + ' --Deleted'))


def add_command():
    respond = db.add(full_name.get(), mobile_number.get(), address.get(), email.get(), genre.get())
    list.delete(0, END)
    if respond == True:
        list.insert(END, (full_name.get(), mobile_number.get(), address.get(), email.get(), genre.get()))
    else :
        list.insert(END, 'Mobile number must be INSERTED!')

def view_command():
    # deletes all data in list
    list.delete(0, END)
    for row in db.view_all():
        list.insert(END, row)

def search_command():
    list.delete(0, END)
    for row in db.search(full_name.get(), mobile_number.get(), address.get(), email.get(), genre.get()):
        list.insert(END, row)

win = Tk()
win.title('Telephone Book')

l1 = Label(win, text='Full Name')
l1.grid(row=0, column=0)
l2 = Label(win, text='Mobile Number')
l2.grid(row=0, column=2)
l3 = Label(win, text='Address')
l3.grid(row=1, column=0)
l4 = Label(win, text='E-mail')
l4.grid(row=1, column=2)
l5 = Label(win, text='Genre')
l5.grid(row=2, column=0)

full_name = StringVar()
e1 = Entry(win, textvariable=full_name)
e1.grid(row=0, column=1)
mobile_number = StringVar()
e2 = Entry(win, textvariable=mobile_number)
e2.grid(row=0, column=3)
address = StringVar()
e3 = Entry(win, textvariable=address)
e3.grid(row=1, column=1)
email = StringVar()
e4 = Entry(win, textvariable=email)
e4.grid(row=1, column=3)
genre = StringVar()
e5 = Entry(win, textvariable=genre)
e5.grid(row=2, column=1)

list = Listbox(win, height=10, width=55)
list.grid(row=3, column=1, rowspan=5, columnspan=3)

sb = Scrollbar(win)
sb.grid(row=2, column=4, rowspan=5)

b1 = Button(win, text='SAVE', width=12, pady=5, command=add_command)
b1.grid(row=3, column=0)
b2 = Button(win, text='SEARCH', width=12, pady=5, command=search_command)
b2.grid(row=4, column=0)
b1 = Button(win, text='DELETE', width=12, pady=5, command=delete_command)
b1.grid(row=5, column=0)
b1 = Button(win, text='VIEW ALL', width=12, pady=5, command=view_command)
b1.grid(row=6, column=0)
b1 = Button(win, text='CLOSE', width=12, pady=5, command=win.destroy)
b1.grid(row=7, column=0)

instructions = Label(win, font=('Calibri', 12, 'normal'), justify=LEFT, anchor="w", text='1. Insert details then Press SAVE to add contact.\n'+
                    '2. Enter any detail(s) Press SEARCH to get details.\n'+
                    '3. Enter mobile number then press DELETE to delete contact.\n'+
                    '4. Click VIEW ALL to view all saved contacts\n'+
                    '5. Click CLOSE to exit.')
instructions.grid(row=8, column=0, columnspan=4, pady=10, padx=10)
win.mainloop()