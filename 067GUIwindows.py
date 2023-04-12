from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("450x450")
window.title("Wiru GUI Test")

icon = PhotoImage(file="G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\icontest067GUIwindows.png")
window.iconphoto(True,icon)
#window.config(background="black")
window.config(background="#5cfcff")

window.mainloop() # this place windows on computer screen, listen for events


