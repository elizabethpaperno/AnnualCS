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
    return [freq1/100000, freq2/100000, freq3/100000, freq4/100000, freq5/100000, freq6/100000, freq7/100000, freq8/100000, freq9/100000]

def showhist():
    x = [1,2,3,4,5,6,7,8,9]
    y = histogram()
    plt.bar(x,y)
    plt.xlabel('First Digit')
    plt.ylabel('Frequency')
    plt.title("Frequency of each first digit in a list of random number")
    plt.show()
showhist()
    
def hist2():
    x = [1,2,3,4,5,6,7,8,9]
    data = open("population-of-towns.csv","r")
    string=data.read()
    fStr = string.strip()
    Str=fStr.split("\n")
    finalStr = Str[1:]
    dictt = {}
    sorted_freq = []
    for i in finalStr:
        lines = i.split(",")        
        population = lines[2]
        if population[0] in dictt:
            dictt[population[0]]+=1
        else:
            dictt[population[0]]=1  
    sorted_freq = sorted(dictt.items(),key=lambda x: x[1], reverse=True)
    y = [sorted_freq[0][1], sorted_freq[1][1], sorted_freq[2][1], sorted_freq[3][1], sorted_freq[4][1], sorted_freq[5][1], sorted_freq[6][1], sorted_freq[7][1], sorted_freq[8][1]]
    plt.bar(x,y)
    plt.xlabel('First Digit')
    plt.ylabel('Frequency')
    plt.title("Frequency of each first digit in a list of town's populations")
    plt.show()
#hist2()      

def hist3():
    x = [1,2,3,4,5,6,7,8,9]
    data = open("vgsales.csv","r")
    string=data.read()
    fStr = string.strip()
    Str=fStr.split("\n")
    finalStr = Str[1:]
    dictt = {}
    sorted_freq = []
    for i in finalStr:
        lines = i.split(",")        
        sales = lines[10]
        #print(sales)
        if float(sales) >= 1:
            if sales[0] in dictt:
                dictt[sales[0]]+=1
            else:
                dictt[sales[0]]=1
        if float(sales) < 1:
            sales=sales.replace(".", "")
            sales=sales.replace("0", "")
            try:
                if sales[0] in dictt:
                    dictt[sales[0]]+=1
                else:
                    dictt[sales[0]]=1
            except:
                print(sales)
    sorted_freq = sorted(dictt.items(),key=lambda x: x[1], reverse=True)
    print(sorted_freq)
    print(dictt)
    y = [sorted_freq[0][1]/100000, sorted_freq[1][1]/100000, sorted_freq[2][1]/100000, sorted_freq[3][1]/100000, sorted_freq[4][1]/100000, sorted_freq[5][1]/100000, sorted_freq[6][1]/100000, sorted_freq[7][1]/100000, sorted_freq[8][1]/100000]
    plt.bar(x,y)
    plt.xlabel('Most Significant Figure')
    plt.ylabel('Frequency as a fraction')
    plt.title("Frequency of the Most Significant Figure in Global Sales of Video Games")
    plt.show()
#hist3()   
        
        
    