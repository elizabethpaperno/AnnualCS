#1
def sum_squares (low, high):
    sum_sq=0
    while low <= high:
        tracker=low**2
        sum_sq += tracker
        low +=1
    return (sum_sq)
#print(sum_squares (2,4)) #29

#2
def sum_powers (low, high, power):
    sum_pow = 0
    while low <= high:
        tracker=low**power
        sum_pow += tracker
        low +=1
    return (sum_pow)
#print(sum_powers (8, 10, 3)) #2241

#3
def SUM_POWERS (a, b, power):
    if a<=b:
        return sum_powers (a, b, power)
    else:
        return sum_powers (b, a, power)
#print(SUM_POWERS (10, 8, 3)) #2241

#4
def fizzbuzz (n):
    counter = 1
    while counter <= n:
        if counter%5==0 and counter%3==0:
            print ("fizzbuzz")
        elif counter%3==0:
            print ("fizz")
        elif counter%5==0:
            print ("buzz")
        else:
            print (counter)
        counter += 1
#fizzbuzz (15)

#5
def num_digits (n):
    numOfDigits = 0
    while n > 0:
        n = n // 10
        numOfDigits += 1
    return numOfDigits
print (num_digits(105)) #3
#print (num_digits(8)) #1
            

        