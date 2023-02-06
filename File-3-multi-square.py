from turtle import *
mode('logo')
speed(9) #Go pretty fast

#Define a function that draws a square
def square():
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)

#Draw six squares, turning a little each time
square()
left(60)
square()
left(60)
square()
left(60)
square()
left(60)
square()
left(60)
square()
left(60)

exitonclick() #Keep the window with the drawing open until we click it.