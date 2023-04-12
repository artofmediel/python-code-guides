from tkinter import *

def display():

    # if x is IntVar()
    #if(x.get()==1):
    #    print("You agree.")
    #else:
    #    print("You don't agree")
    #----------------------------
    # if x is StringVar()
    #if (x.get() == "YES"):
    #    print("You agree.")
    #else:
    #    print("You don't agree")
    #----------------------------
    # if x is BooleanVar()
    if (x.get()):
        print("You agree.")
    else:
        print("You don't agree")


window = Tk()

#x = IntVar() # onvalue = 1 , offvalue = 0
#x = StringVar() # onvalue = "YES" or any string, offvalue = "NO"
x = BooleanVar() # onvalue = True , offvalue = False

python_photo = PhotoImage(file='G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\pythonlogo071Checkbox.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial',20),
                           fg='#00ff00',
                           bg='black',
                           activeforeground='#00ff00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left')
check_button.pack()

window.mainloop()