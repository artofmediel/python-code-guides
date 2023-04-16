from tkinter import *

def doSomething(event):
    print("Mouse coordinates :  (" + str(event.x) + " , " + str(event.y) + ")")

window = Tk()

#window.bind(event,function)
#window.bind("<Button-1>",doSomething) # Button-1 = left click
                                       # Button-2 = click mouse wheel
                                       # Button-3 = right click

#window.bind("<ButtonRelease>",doSomething) # mouse release
#window.bind("<Enter>",doSomething) # mouse enter the window
#window.bind("<Leave>",doSomething) # mouse leave the window
window.bind("<Motion>",doSomething) # mouse while in motion

window.mainloop()