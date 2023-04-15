from tkinter import *

def create_window():
    #new_window = Toplevel()     # Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
    new_window = Tk()           # Tk() = new independent window1

    old_window.destroy()        # close out of old window

old_window = Tk()

Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop()