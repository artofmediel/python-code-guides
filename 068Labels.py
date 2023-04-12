from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file="G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\pikachu068Labels.png")

label = Label(window,
              text="Hello wiru",
              font=('Arial',40,'bold'),
              fg='#00ff00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
label.pack()
#label.place(x=100,y=100)

window.mainloop()