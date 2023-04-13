from tkinter import *
from tkinter import messagebox # import messagebox library

def click():
    #messagebox.showinfo(title='This is an info message box',message='wiru 123 123')
    #messagebox.showwarning(title='WARNING!', message='wiru wiru')
    #messagebox.showerror(title='ERROR', message='something went wrong')

    #if messagebox.askokcancel(title='ask ok cancel',message='do you know my name?'):
    #   print('chosen yes')
    #else:
    #    print('chosen no')

    #if messagebox.askretrycancel(title='ask retry cancel',message='do you want to try again?'):
    #    print('chosen yes')
    #else:
    #    print('chosen no')

    #if messagebox.askyesno(title='ask yes or no',message='do you like?'):
    #    print('me likey')
    #else:
    #    print('feelsbadman')

    #answer = messagebox.askquestion(title='ask question',message='do you like pie?')
    #if(answer == 'yes'):
    #    print('me too')
    #else:
    #    print('too bad')

    answer = messagebox.askyesnocancel(title='yes no cancel',message='do you like to code',icon='error')
    # icon = 'info','warning','error
    if(answer==True):
        print('you like to code')
    elif(answer==False):
        print('why not')
    else:
        print('cancelled')

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()