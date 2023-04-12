from tkinter import *

def submit():
    print("The temperaturee is: "+ str(scale.get()) +" degrees C")

window = Tk()

hotImage  = PhotoImage(file="G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\heat073Scale.png")
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # VERTIVAL or HORIZONTAL
              font=('Consolas',20),
              tickinterval=10,  # add numeric indicators for value
              #showvalue=0,      # hides or show current value
              resolution=5,     # increment of slider
              troughcolor="#69EAFF",
              fg='#FF1C00',
              bg='#111111'
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) # set current value of slider

scale.pack()

coldImage  = PhotoImage(file="G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\snowflake073Scale.png")
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()