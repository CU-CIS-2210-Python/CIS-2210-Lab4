from turtle import *
mode('logo')
speed(9)

#This function draws a spiral,
# using the len parameter as
# the outside size of the spriral 
def spiral(len):
    if len > 0:
        forward(len)
        right(90)
        spiral(len - 10)

spiral(200)

exitonclick()