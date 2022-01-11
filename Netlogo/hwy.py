a ="abcdefgh"
a[1]

def evenOrOdd(n):
    if n==0:
        return "niether"
    elif n%2==0:
        return "even"
    else:
        return "odd"


# 1+1/2+1/3...1/n
def sumHarmonic (n):
    sum1 = 0 
    for i in range (1, n+1):
        sum1 += 1/i #sum = sum + 1/n sum+= 1 sum= sum +1
    return sum1
print(sumHarmonic(2))

def sumHarmonic2(n):
    total = 0
    counter = 0 
    while total < n:
        counter += 1
        total = sumHarmonic(counter)
    return i 
        
def toUpper (x):
    newString = ""
    lower = "abcdefghijklmnaopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNAOPQRSTUVWXYZ"
    for i in range(len(x)):
        pos = lower.find(x[i])
        if pos == -1:
            newString += x[i]
        else:
            newString += upper[pos]
    return newString

def CapWord (word):
    return word[0].upper() + word[1:].lower()
#"JOhn" -> John

def CapName (name):
    spacePos= name.find(" ")
    return CapWord(name [:spacePos]) + name[spacePos] +  CapWord(name [spacePos+1:])

def FirstLast (name):
    commaPos = name.find(",")
    return name[commaPos +2:] + " " + name[:commaPos]

def fileClass (name):
    posPeriod = name.rfind(".")
    suffix = name [posPerios +1:].upper()
    if suffux=="JPG" or suffix=="JPEG":
        return "picture"
    elif suffix == "MP3":
        return "music"
    elif suffix == "NLOGO":
        return "Netlogo"
    elif suffix == "PY":
        return "Python"


        
    

