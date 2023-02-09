from turtle import *
mode('logo')
speed(9)

#This function draws a spiral,
# using the len parameter as
# the outside size of the spriral 
def spiral(len):
    forward(len)
    right(90)
    spiral(len * .9)

spiral(300)