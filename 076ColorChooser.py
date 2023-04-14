from tkinter import *
from tkinter import colorchooser # submodule

def click():
    color = colorchooser.askcolor()                 # assign color to a variable
    #print(color)
    colorHex = color[1]                             # assigns element at index 1 to a variable
    #print(colorHex)
    window.config(bg=colorHex[1])                   # change background color to test

    # this can be a simplified version of all codes above
    #window.config(bg=colorchooser.askcolor()[1])   # change background color to test

window = Tk()

window.geometry("450x450")

button = Button(text='click me',
                command=click)
button.pack()

window.mainloop()