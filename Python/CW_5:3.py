fred = '''Name,day-wage,start-day,end-day
EMMANUEL,19.16,14,26
RAHMA,23.80,14,33
ALIF,27.85,1,10
JAVOHIR,34.43,12,27
NAKIB,25.71,9,34
SAQIF,29.22,6,12
ZARIN,22.31,6,21
MENDAKA BINETH,16.75,2,13
AHNAF,34.81,2,26
ABDAL,22.68,14,27'''

a = 'Zarin'
0 < fred.find(a.upper())
a.upper() in fred #yes or no q

"absedsbs".count("bs") #count how many times a substring occurs
fred.count(a.upper())
[1,3,4,2,1,3].index(3)

b="abe"


"aces" < "ace" #is case sensitive, but while return what comes first alphabetically 

print(sorted([1,3,2,4,6,5]))
print(sorted(["Zarin", "ace", "aces", "zarin"]))

sorted([ [10, "ace"], [10, "abe"], [7,"abe"]])

def sortbywage(l):
    a= l.split("\n")[1:-1]
    masterList = []
    for i in a:
        words = i.split(",")
        words = [float(words[1])] + words
        masterList.append(words)
    return(sorted(masterList))
print(sortbywage(fred))
    