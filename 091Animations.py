from tkinter import *

import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\outerspace091Animations.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file='G:\\William\\python-projects\\PycharmProjects\\PythonTestFiles\\ufo091Animations.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)

    # check if x position of image is greater than the width of the canvas or less than 0
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        # reverse the velocity
        xVelocity = -xVelocity
    # check if y position of image is greater than the width of the canvas or less than 0
    if (coordinates[1] >= (HEIGHT-image_height) or coordinates[1]<0):
        # reverse the velocity
        yVelocity = -yVelocity

    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()