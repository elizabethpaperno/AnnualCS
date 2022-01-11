#1a
def ToUpper(x):
    newString=""
    lower = "abcdefghijklmnaopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNAOPQRSTUVWXYZ"
    for i in range (len(x)):
        pos = lower.find(x[i])
        if pos == -1:
            newString += x[i]
        else:
            newString += upper[pos]
    return newString
            
print(ToUpper("Hi there, 2 you"))

#1b
def Encrypt (some_text):
    newString = ""
    Julius_before='defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC'
    Julius_after ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range (len(some_text)):
        pos = Julius_before.find(some_text[i])
        newString += Julius_after[pos]
    return newString
print(Encrypt('defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC')) #returns julius after


def Decrypt (some_text):
    newString = ""
    Julius_before='defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC'
    Julius_after ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range (len(some_text)):
        pos = Julius_after.find(some_text[i])
        newString += Julius_before[pos]
    return newString
print(Decrypt('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')) #returns julius before

#2a
def IsSameName(name1,name2):
    return name1.upper() == name2.upper()
print (IsSameName('John smith', 'JOHN Smith')) #true
print (IsSameName('John Smith', "John's Myth")) #false

#2b
def CapWord (word):
    return word[0].upper() + word[1:len(word)].lower()
print(CapWord("jOHN")) #John 

#2c
def CapName (name):
    spacePos= name.find(" ")
    return CapWord(name[:spacePos])+" "+CapWord(name[spacePos + 1:len(name)])
print (CapName("JoHn SmitH"))

#3a
def FirstLast (name):
    commaPos= name.find(",")
    return name[commaPos + 2: len(name)] + name[commaPos+1] + name[:commaPos]
print(FirstLast('Brooks, Peter')) #Peter Brooks

#3d
def FirstLastSequence (names):
    newString = ""
    prevSemi = -1
    for i in range (len(names)):
        if names[i].find(";") != -1:
            newString += FirstLast(names[prevSemi+1:i]) + names[i]
            prevSemi=i
    return newString
print (FirstLastSequence('Brooks, Peter;Holmes, David;Pascu, Ms.;'))

#4
def FileClassifier(filename):
    posPeriod = filename.rfind(".")
    suffix = filename[posPeriod + 1:len(filename)].upper()
    if suffix == "JPG" or suffix == "JPEG":
        return "picture"
    elif suffix == "MP3":
        return "music"
    elif suffix == "NLOGO":
        return "Netlogo"
    elif suffix == "PY":
        return "Python"
print (FileClassifier('StarSpangledBanner.Mp3'))
print (FileClassifier('Fred.mp3.JPEG.nlogo'))

#Triple Challenge
constraint= 26 #only 26 letters in alphabet
keyWords = ["giant", "mets", "nets", "islanders", "rangers", "knicks", "yankees", "jets"]

def decryptCeaserCypher(s,n):
    shiftedString = ""
    for i in range (len(s)):
        if 65 <= ord(s[i]) <= 90:
            shiftedString += chr((ord(s[i])+n-65) % constraint+65)
        elif 97 <= ord(s[i]) <= 122:
            shiftedString += chr((ord(s[i])+n-97) % constraint+97)
        else:
            shiftedString+=s[i]
    return shiftedString

def findKeyWords (s, words):
    for i in range (len(words)):
        if s.find(words[i]) != -1:
            return True
    return False

def findKeyWordsInLowerCase (s, words): #makes the search for the keywords not case senstive since we are not give the capitlization of the sports team name 
    return findKeyWords(s.lower(), words)

def TCP(s):
    for n in range (constraint + 1):
        shiftedString = decryptCeaserCypher (s,n)
        if findKeyWordsInLowerCase (shiftedString, keyWords): 
            break        
    return shiftedString 

print(TCP("Zw Z yrmv jvve wlikyvi zk zj sp jkreuzex fe kyv jyfcuvij fw Xzrekj."))

  



