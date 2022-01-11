import random
import matplotlib.pyplot as plt

def histogram():
    freq1 = 0
    freq2 = 0
    freq3 = 0
    freq4 = 0
    freq5 = 0
    freq6 = 0
    freq7 = 0
    freq8 = 0
    freq9 = 0
    num = [random.randint(0,1000) for i in range(1,100000)]
    for i in num:
        if i<100:
            if i//10 == 1:
                freq1 += 1
            elif i//10 == 2:
                freq2 += 1
            elif i//10 == 3:
                freq3 += 1
            elif i//10 == 4:
                freq4 += 1
            elif i//10 == 3:
                freq3 += 1
            elif i//10 == 4:
                freq4 += 1
            elif i//10 == 5:
                freq5 += 1
            elif i//10 == 6:
                freq6 += 1
            elif i//10 == 7:
                freq7 += 1
            elif i//10 == 8:
                freq8 += 1
            elif i//10 == 9:
                freq9 += 1
        else:
            if i//100 == 1:
                freq1 += 1
            elif i//100 == 2:
                freq2 += 1
            elif i//100 == 3:
                freq3 += 1
            elif i//100 == 4:
                freq4 += 1
            elif i//100 == 3:
                freq3 += 1
            elif i//100 == 4:
                freq4 += 1
            elif i//100 == 5:
                freq5 += 1
            elif i//100 == 6:
                freq6 += 1
            elif i//100 == 7:
                freq7 += 1
            elif i//100 == 8:
                freq8 += 1
            elif i//100 == 9:
                freq9 += 1
    return [freq1, freq2, freq3, freq4, freq5, freq6, freq7, freq8, freq9]

def showhist():
    x = [1,2,3,4,5,6,7,8,9]
    y = histogram()
    plt.bar(x,y)
    plt.xlabel('First Digit')
    plt.ylabel('Frequency')
    plt.title("Frequency of each first digit in a list of random number")
    plt.show()
#showhist()
    
def hist2():
    x = [1,2,3,4,5,6,7,8,9]
    data = open("population-of-towns.csv","r")
    string=data.read()
    finalStr = string.strip()[1:]
    dictt = {}
    for i in finalStr:
        lines = i.split(",")
        population = lines[2]
        if population[0] in dictt: 
           dicct[population[0]]+=1
        else:
            dicct[population[0]]=1
    return dictt
        
            
        
        
    