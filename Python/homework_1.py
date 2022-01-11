def fahr_to_cel(temp):
    return (temp - 32) * (5 / 9)

#print('Freezing point of water is: ',fahr_to_cel(32), 'and the boiling point is: ',fahr_to_cel(212))
#print('The temp in Celsius at -40 degrees Fahrenheit is: ',fahr_to_cel(-40))

def dist (x, y):
    return (x**2 + y**2) ** (1/2)
#print('This should be 5: ',dist(3,4))

def eval_quad (a, b, c, x):
    y = a*(x**2) + (b*x) + c
    return y
            
#print (eval_quad(1,1,1,2))
#print (eval_quad(0,2,1,4)) 