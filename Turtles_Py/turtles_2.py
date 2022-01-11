# tree
MINLENGTH = 10
import turtle
t = turtle.Turtle()
t.pu()
t.setpos(0,-200)
t.setheading(90)
t.speed(0)

def tree(length):
    t.pd()
    if length < MINLENGTH:
        return
    t.fd(length)
    t.lt(30)
    tree(length*.75)
    t.rt(60)
    tree(length*.75)
    t.lt(30)
    t.bk(length)
#tree(100)
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
fact(5)