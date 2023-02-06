from turtle import *    #Tell Python we want to use all the functions from
                        # the "Turtle Graphics" Library

mode('logo')    #Put the turtle into 'logo' mode, where it starts facing north

speed(1)    #Tell the turtle to move slowly, it will remember this speed until
            #we call the speed function again to change the speed.

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

#❓ Your code here:




exitonclick() #Keep the window with the drawing open until we click it.