from tkinter import *

# define movements
def move_up(event):
    # ---------------------------------------------------
    # PART 1 :moving images with keys on window
    #label.place(x=label.winfo_x(), y=label.winfo_y()-10)
    # ---------------------------------------------------
    # PART 2 :moving images with keys on a canvas
    canvas.move(myimage,0,-10)

def move_down(event):
    # ---------------------------------------------------
    # PART 1 :moving images with keys on window
    #label.place(x=label.winfo_x(), y=label.winfo_y()+10)
    # ---------------------------------------------------
    # PART 2 :moving images with keys on a canvas
    canvas.move(myimage, 0, 10)

def move_left(event):
    # ---------------------------------------------------
    # PART 1 :moving images with keys on window
    #label.place(x=label.winfo_x()-10, y=label.winfo_y())
    # ---------------------------------------------------
    # PART 2 :moving images with keys on a canvas
    canvas.move(myimage, -10, 0)

def move_right(event):
    # ---------------------------------------------------
    # PART 1 :moving images with keys on window
    #label.place(x=label.winfo_x()+10, y=label.winfo_y())
    # ---------------------------------------------------
    # PART 2 :moving images with keys on a canvas
    canvas.move(myimage, 10, 0)

window = Tk()
# ---------------------------------------------------
# PART 1 :moving images with keys on window
# window.geometry("500x500")
# ---------------------------------------------------
# PART 2 :moving images with keys on a canvas
canvas = Canvas(window,width=500,height=500)
canvas.pack()

# ---------------------------------------------------
# PART 1 and 2:moving images with keys on window and canvas
# movements w s a d
window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

# ---------------------------------------------------
# PART 1 and 2:moving images with keys on window and canvas
# movements arrow keys
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

# ---------------------------------------------------
# PART 1: :moving images with keys on window
# character
#myImage = PhotoImage(file='G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\junimo090MoveImageWithKey.png')
#label = Label(window,image=myImage)
#label.place(x=0,y=0)
# ---------------------------------------------------
# PART 2: :moving images with keys on a canvas
# character
photoimage = PhotoImage(file='G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\junimo090MoveImageWithKey.png')
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

window.mainloop()

