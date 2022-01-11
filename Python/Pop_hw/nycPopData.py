import matplotlib.pyplot as plt
year = []
man = []
brklyn = []
q = []
bx = []
si = []
def getData(filename):
    data=open(filename,'r')
    alldata=data.read()
    lines=alldata.strip().split("\n")
    for aline in lines[1:]:
        pieces=aline.split(',')
        year.append(int(pieces[0]))
        man.append(int(pieces[1]))
        brklyn.append(int(pieces[2]))
        q.append(int(pieces[3]))
        bx.append(int(pieces[4]))
        si.append(int(pieces[5]))
    return year, man, brklyn, q, si, bx

def oneB(bname, bname2):
    getData("nyc-population.csv")
    plt.plot(year,bname)
    plt.ylabel("Population"), plt.xlabel("Year")
    plt.title("Population of " + bname2 + " throughout 1790-2010")
    plt.show()
oneB(man, "Manhattan")

def allB():
    getData("nyc-population.csv")
    plt.plot(year,man,label="Manhattan")
    plt.plot(year,brklyn,label="Brooklyn")
    plt.plot(year,q,label="Queens")
    plt.plot(year,bx,label="Bronx")
    plt.plot(year,si,label="Staten Island")
    plt.ylabel("Population"), plt.xlabel("Year")
    plt.title("Population of NYC boroughs throughout 1790-2010")
    plt.legend()
    plt.show()
#allB()
    
