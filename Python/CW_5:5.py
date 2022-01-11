satscores=open("2012_SAT_Results.csv", "r")
data = satscores.read()
lines= data.split("\n")

def scoreMedian(L):
    masterList = []
    for aline in lines[1:]:
        values = aline.split(",")
        try:
            length = int(len(values))
            totalScore = [int(values[length-1])+ int(values[length-2]) + int(values[length-3])]
            values = totalScore + values
            masterList.append(values)
        except:
            pass
    return masterList[int(((len(masterList)-1)/2)+1)]
print(scoreMedian(lines))

        
        