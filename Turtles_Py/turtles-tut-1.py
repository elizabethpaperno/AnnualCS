# Turtles - Basic

# References:
#    Turtle docs here:  https://docs.python.org/3/library/turtle.html
#    4 Turtles tutorial videos here: https://www.youtube.com/watch?v=p7CiFhiTdvY
#    Color names: http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

# Instructions: To run one of the Demo functions below, uncomment the execution line
#   for that Demo function (make sure all other Demo functions execution lines are commented)

import turtle
turtle.colormode(256)   # to allow r, g, b selection of colors, e.g. 

# ======================================================================
# Forget "Hello World!"... Let's draw a blue square.
def BlueSquareDemo():

    # create our little guy:
    LittleGuy = turtle.Turtle()

    # set his properties
    LittleGuy.color('blue')
    LittleGuy.pensize(4)
    LittleGuy.pd()

    # go go go
    for often in range(4):
        LittleGuy.fd(100)
        LittleGuy.rt(90)
    
#BlueSquareDemo()

# =====================================================================
# Create 3 turtles, draw 3 squares with different colors, and a filled circle
def ColorsAndFillDemo():

    theGroup = []
    theColors = ['maroon4','SpringGreen4','Dodger Blue2','coral2']
    
    # Create the group
    for i in range(3):
        aguy = turtle.Turtle()
        aguy.color(theColors[i])
        aguy.pensize(2)
        aguy.setheading(i*120)
        theGroup.append(aguy)
    
    # draw 3 squares
    for i in range(3):
        fred = theGroup[i]
        fred.pu()
        fred.fd(150)
        fred.lt(90)
        fred.pd()
        for j in range(4):
            fred.fd(50)
            fred.lt(90)
        fred.pu()
        fred.ht()  # hide the turtle

    # Create a filled circle, outline with a different color
    # Let's use one of our 3 turtles from theGroup
    circleNoid = theGroup[0]
    circleNoid.color('DodgerBlue2','salmon')  # outside is blue, inside is fish
    circleNoid.setx(50)
    circleNoid.sety(0)
    circleNoid.pd()
    circleNoid.begin_fill()
    circleNoid.circle(50)
    circleNoid.end_fill()
        
ColorsAndFillDemo()

# ===========================================================
# Using externally created shapes (.gif images).
# Note: An external shape cannot be rotated using the usual turtle rotation functions
# These 4 shapes were created using MSPaint...

def UseExternalShapesDemo():
    turtle.register_shape('arrow-1-up.gif')
    turtle.register_shape('arrow-1-right.gif')
    turtle.register_shape('arrow-1-down.gif')
    turtle.register_shape('arrow-1-left.gif')
    
    shifter = turtle.Turtle()
    shifter.pd()
    shifter.shape('arrow-1-right.gif')
    shifter.fd(100)
    shifter.lt(90)
    shifter.shape('arrow-1-up.gif')
    shifter.fd(100)
    shifter.lt(90)
    shifter.shape('arrow-1-left.gif')
    shifter.fd(100)
    shifter.lt(90)
    shifter.shape('arrow-1-down.gif')
    shifter.fd(100)
    shifter.lt(90)
    
#UseExternalShapesDemo()

