import turtle
import random

def RandomSquare(sidelength, color_name):
    turt = turtle.Turtle()
    turt.pu()
    randomX = random.randint(-700, 700) #abt the width in px of my scree
    randomY = random.randint(-300, 300) #abt the length in px of my scree
    turt.goto(randomX,randomY)
    turt.color(color_name)
    turt.pd()
    for i in range(4):
        turt.rt(90)
        turt.fd(sidelength)
    turt.ht()
RandomSquare(100, "blue")


def FilledHexagon(sidelength,border_color,fill_color):
    turt = turtle.Turtle()
    turt.pu()
    turt.goto(-0.5 *sidelength,(sidelength*3**0.5)/2)
    turt.color(border_color,fill_color)
    turt.pd()
    turt.begin_fill()
    for i in range(6):
        turt.fd(sidelength)
        turt.rt(60)
    turt.end_fill()
    turt.ht()
FilledHexagon(100,"blue","red")    
        

        