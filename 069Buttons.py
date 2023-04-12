from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count+=1
    print(count)
    #print("You clicked the button!")

window = Tk()

photo = PhotoImage(file="G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\likebuton069Buttons.png")

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00ff00",
                bg="black",
                activeforeground="#00ff00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='top')

# state = active disabled/ this enable or disable the button

button.pack()

window.mainloop()