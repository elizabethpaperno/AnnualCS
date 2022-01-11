import ShapeMaker
import turtle

t=turtle.Turtle()
turtle.register_shape("voldy", ShapeMaker.LoadPoly("george.txt"))
t.shape("voldy")
t.shapesize(.5,.5,3)
t.lt(45)
t.color("red","green")