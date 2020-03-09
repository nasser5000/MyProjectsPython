# this code to create amotion by the turtle Object in python
import turtle
terry = turtle.Turtle()
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
terry.width(5)
terry.speed(0)
for color in rainbow:
    terry.color(color)
    for side in [1,2,3,4,5]:
        terry.forward(50)
        terry.right(144)
    terry.right(60)
    terry.penup()
    terry.forward(50)
    terry.pendown()
