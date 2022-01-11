def sumHarmonic (n):
    total = 0.0
    for i in range (1, n+1):
        total += 1/i
    return total
print(sumHarmonic(100)) #returns about 5.19
 
def sumHarmonic2(n):
    total=0
    i = 0
    while total < n:
        i += 1
        total=sumHarmonic(i) 
    return i
print(sumHarmonic2(10)) #returns 12367


pi = 3.141592653589793
def LeiSum(n):
    myPi = 0.0 
    for i in range (n+1):
        myPi += (-1.0)**i/(2.0*i+1.0)
    return 4*myPi
 
def Leibniz(teeny):
    i = 0
    counter = 0 
    while abs(LeiSum(i) - pi) > teeny:
        i += 1
        counter += 1
    return counter
print(Leibniz(0.001))

def WallisProduct(n):
    myPi = 1.0
    num = 2.0
    den = 1.0
    for i in range (1, n + 1): 
        myPi *= (num/den)
        if (i%2)== 1:
            den += 2.0
        else:
            num += 2.0 
    return myPi * 2
     
def Wallis(teeny):
    i = 0
    counter = 0
    while abs(WallisProduct(i) - pi) > teeny:
        i += 1
        counter += 1
    return counter
print(Wallis(0.001))

def eulerSum(n):
    myPi = 0.0
    for i in range (1, n + 1):
        myPi += 1/i**2
        
    return (6 * myPi)**(1/2)

def Euler(teeny):
    i = 0
    counter = 0 
    while abs(eulerSum(i) - pi) > teeny:
        i += 1
        counter += 1
    return counter

print(Euler(.001))


    

