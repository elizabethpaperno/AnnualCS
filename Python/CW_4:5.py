a = "Hi There"

b = a.upper()

a.upper().find("TH") #make it not case snesitive

up = "ABCDEFGHIJKLMNAOPQRSTUVWXYZ"

def shift(ch,n):
    pos=up.find(ch)
    return up[(pos+n) % 26]

b = "word1;alkf;que;"
def printwords(s):
    while len(s) > 0:
        pos=s.find(";")
        print(s[:pos])
        s=s[pos+1:]