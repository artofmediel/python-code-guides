from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED) # this disable the entry box


def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Arial",50),
              fg="#00ff00",
              bg="black",
              show="*")
# show = used to hide text for password entry
# you can also separate the parameter setting by typing this
# entry.config(show="*")

entry.insert(0,'default text')
entry.pack(side=LEFT)

submit_button = Button(window,
                       text="submit",
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="delete",
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                       text="backspace",
                       command=backspace)

backspace_button.pack(side=RIGHT)

window.mainloop()