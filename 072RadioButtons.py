# radio buttons = similar to checkbox, but you can only select one from the group

from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza")
    elif(x.get()==1):
        print("You ordered hamburger")
    elif(x.get()==2):
        print("You ordered hotdog")
    else:
        print("Invalid choice")

window = Tk()

pizzaImage = PhotoImage(file="G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\pizza072RadioButtons.png")
hamburgerImage = PhotoImage(file="G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\hamburger072RadioButtons.png")
hotdogImage = PhotoImage(file="G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\hotdog072RadioButtons.png")
foodImages = [pizzaImage,hamburgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton= Radiobutton(window,
                             text=food[index],  # adds text to radio buttons
                             variable=x,        # group radiobuttons  together if they share the same variable
                             value=index,       # assigns each radiobutton a different value
                             padx=25,           # add padding on x axis
                             font=('Impact',30),
                             image=foodImages[index],   #adds images to radiobuttons
                             compound='left',            #put image to left-side
                             indicatoron=0,     # eliminate circle indicators
                             width=375,         # set width of push button
                             command=order      # set command of radio buttons to function
                             )

    radiobutton.pack(anchor=W)


window.mainloop()
