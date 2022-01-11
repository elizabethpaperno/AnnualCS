# Creating a polygon shape and storing its coords in a file

# To use:
#   Click, using the left mouse button on the polygon points, one after the other
#   You need not click on the first point to close the polygon, that last segment
#   will be added automatically when you click on the right mouse button to finish up

#   So, clicking on the right mouse button will add the last segment and ask for a filename
#   to store the polygon coords.

# To start: run this file, then you can call the function MakeOne(some-filename-here) repeatedly
#  from the shell, to create a set of shapes and store them in files.
# >> MakeOne(somefilename)


import turtle

SM_screen = None
SM_t = None
SM_xs = []
SM_ys = []
SM_filename = ''

def left_button(x,y):
    # add another segment to the polygon
    x = int(x)
    y = int(y)
    SM_t.setpos(x,y)
    if len(SM_xs) == 0:
        SM_t.color('red')
        SM_t.stamp()
        SM_t.color('black')
    else:
        SM_t.stamp()
    SM_xs.append(x)
    SM_ys.append(y)
    if len(SM_xs) > 1:
        SM_t.pu()
        SM_t.setpos(SM_xs[-2],SM_ys[-2])
        SM_t.pd()
        SM_t.setpos(SM_xs[-1],SM_ys[-1])
        SM_t.pu()
    
def right_button(x,y):
    # add the last (closing) segment 
    SM_t.setpos(SM_xs[0],SM_ys[0])
    SM_t.pd()
    SM_t.setpos(SM_xs[-1],SM_ys[-1])
    SM_t.pu()
    
    # write the segments to the file
    try:
        f = open(SM_filename,'w')
        for i in range(len(SM_xs)):
            f.write(str(SM_xs[i])+','+str(SM_ys[i])+'\n')
        f.close()
        print('Wrote polygon to '+SM_filename)
    except:
        print('Could not write to '+SM_filename)
        
    # Shut down the screen
    turtle.bye()
    
    # magic incantations from StackOverflow to reset the turtle environment
    # https://stackoverflow.com/questions/44249534/re-open-turtle-after-turtle-bye
    turtle.Turtle._screen = None
    turtle.TurtleScreen._RUNNING = True
    
def MakeOne(filename):
    global SM_t, SM_screen, SM_filename, SM_xs, SM_ys
    
    SM_filename = filename
    SM_screen = turtle.Screen()
    SM_xs = []
    SM_ys = []
    
    # make our drawing turtle
    SM_t = turtle.Turtle()
    SM_t.speed(0)
    SM_t.ht()
    SM_t.pu()
    
    # dispay instructions
    SM_t.setpos(-200,250)
    SM_t.write('Click with the left mouse button to add segments,',font=("Arial", 15, "normal"))
    SM_t.setpos(-200,220)
    SM_t.write('and right mouse button to finish.',font=("Arial", 15, "normal"))
    
    # small dots for vertices
    SM_t.shape('circle')
    SM_t.shapesize(.2,.2,.2)
    SM_t.speed(5)
    
    # listen for mouse clicks
    turtle.listen()
    
    turtle.onscreenclick(left_button,1)  # if the left button is clicked, execute the left_button function
    turtle.onscreenclick(right_button,2) # if the right button is clicked...
    
    SM_screen.mainloop()  #  sit, and wait for stuff to happen

# ======================================================================
#  Load a polygon, ready to register as a shape

# Use in the following way...
# Assume you have already created a polygon using MakeOne('fred.txt')
# You can register it later using:

#  import ShapeMaker
#  turtle.register_shape('harry', ShapeMaker.LoadPoly('fred.txt'))
#  turtle.shape('harry')
#  turtle.color('red','green')  # if you want to change the outline and fill colors

def LoadPoly(filename):
    try:
        f = open(filename,'r')
        lines = f.read().strip().split('\n')
        f.close()
        poly = []
        for aline in lines:
            parts = aline.split(',')
            if len(parts) != 2:
                print('Error in LoadPolygon, line should have 2 ints. line: ',aline)
                return
            x,y = parts
            if not SM_isnum(x) or not SM_isnum(y):
                print('Error in LoadPolygon, numbers should be numbers.  line: ',aline)
                return
            poly.append((float(x),float(y)))
        return tuple(poly)
    except:
        print('Error in LoadPolygon: cannot read file: ',filename)
        return None

def SM_isnum(s):
    try:
        f = float(s)
        return True
    except:
        return False
