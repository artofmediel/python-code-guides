from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="G:\\William\\python-projects\\PycharmProjects\\PythonCodes",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("text file",".txt"),
                                        ("html file",".html"),
                                        ("All files",".*")
                                    ])

    if file in None:
        return
    #filetext = str(text.get(1.0,END))
    filetext = input("Enter some text I guess: ")
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()
