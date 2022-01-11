pi = 3.141592653589793

def eulerSum(n):
    myPi = 0.0
    for i in range (1, n+1):
        myPi += 1/i**2
    return  6*myPi**1/2

def Euler(teeny):
    i = 0
    while abs(eulerSum(i) - pi) > teeny:
        i += 1
        eulerSum(i)
    return eulerSum(i)

print(eulerSum(10000))