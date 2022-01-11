a = 'Abc 2493290/ sjadh i'

b = a.upper() #converts to uppercase
print(b)

c = 'How are you George?'

c.find('w') #in position 2
c.find('o') #returns the first postion its found
c.find('x') #return -1 because its not there

c.find('you') #returns the position of the first letter

c.find('yeo') #will not find it (has to be exact match)

c.rfind("o") #find from the right

#c.find("string", ignores everything up to and in including this numner)

c.find('o', 2) #will return 9

def upper(x):
    if ord(x) > 96 and ord(x) < 123: 
        return chr(ord(x) - 32)
    else:
        return c
print(upper("F"))

def upper2(x):
    lower = "abcdefghijklmnaopqrstuvwxyz"
    pos = lower.find(x)
    if lower.find(x) == -1:
        return x
    upper = "ABCDEFGHIJKLMNAOPQRSTUVWXYZ"
    return upper[pos]

    upper 