from turtle import *
mode('logo')
speed(9) #Go pretty fast

#Define a function that draws a square
def square(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)

#Draw a big square
square(200)

#Draw a little square
square(50)

exitonclick() #Keep the window with the drawing open until we click it.