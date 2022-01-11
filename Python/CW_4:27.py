def conv(s):
    try:
        a = int(s)
        return a 
    except:
        return "wrong"
        
#if conv(s) == "wrong":
    #take evasive action

fred = 56
print("Fred can eat " + str(fred) + " pumpkins")

infile = "names-1.txt"
f = open(infile, 'r') #'r' is to read and 'w' is to write
s = f.read()
f.close()
print(len(s)) #long
s[:100]
fred = s.split('\n')
fred[:3]
fred[len(fred)-3:]

s = False
while not s:
    try:
        fname = input("filename: ")
        f = open(fname, 'r')
        s = true
    except:
        print ("Sorry, try again")
print ("Ok, continue")

        