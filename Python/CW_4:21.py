a = "fred,18"
b = a.split(",")
c = float(b[1])+2

e = "fred,18a"

def convInt(s):
    try:
        a = int(s)
    except: #if error 
        return [False, 0]
    return [True, a]