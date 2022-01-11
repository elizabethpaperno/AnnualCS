a = "hi there"
b = list(a)

bc = b
bc[0] = 15
print(b) #b has always changed

bc = b[:]
bc[0] = 100
print(b) #now it wont change

# abe,56
# john,34
# mary,89
names = ["abe" , "john", "mary"]
ages = [56, 34, 89]

names_ages = [ ["abe", 56], ["john", 34], ["mary", 89] ]

na = {"abe":56, "john":34, "mary":89} #sets of name value pairs
na["mary"] #name is the key value pair
print("mary" in na) #true
print("brooks" in na) #false, otherwise if tyou look it up it will return and error
na ["hdubz"] = 8 #adds to dict
del na["john"]

na["mary"]= [89,125.75]
na["mary"][1]

smallDict = {"age":89, "wage":125.75}
na["mary"]= smallDict
na["mary"]["wage"]

a = [2,4,2,5,6,7,6,6,3,4,9,8]

def freq1(lst):
    f = {}
    for anum in lst: 
        f[anum]=lst.count(anum)
    return f
print(freq1(a))

def freq2(lst):
    f ={}
    for anum in lst:
        if anum not in f:
            f[anum]=lst.count(anum)
    return f
print(freq2(a))

def freq3(lst):
    f ={}
    for anum in lst:
        if anum in f:
            f[anum]+=1
        else:
            f[anum] = 1
    return f
print(freq3(a))

g = freq3(a)
g[6] #3

        