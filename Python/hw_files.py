infile = "names-1.txt"
readFile = open(infile, 'r') #'r' is to read and 'w' is to write
stringFile = readFile.read()
readFile.close()

listFile = stringFile.split('\n')

def mostMoney(lists):
    max_money = 0
    max_name = ""
    for aname in listFile:
        name = aname.split(',')
        try: 
            total_money = (float(name[3])-float(name[2])+1)*(float(name[1]))
            if total_money > max_money:
                max_money = total_money
                max_name = name[0]
        except:
            pass
    return [max_name,max_money]
print (mostMoney(listFile)) #['ZAMEEN', 1049.70]

def workedFewest(lists):
    fewest_days = 1000000 #some unreasonable number
    fewest_name = ""
    fewest_list = []
    for aname in listFile:
        name = aname.split(',')
        try: 
            total_worked = float(name[3])-float(name[2]) + 1
            if total_worked < fewest_days:
                fewest_days = total_worked
                fewest_name = name[0]
                
        except:
            pass
    for aname in listFile:
        name = aname.split(',')
        try: 
            total_worked = float(name[3])-float(name[2]) + 1
            if total_worked == fewest_days:
                fewest_list.append(name[0])
                fewest_list.append(total_worked)        
        except:
            pass
    return fewest_list
print (workedFewest(listFile)) #['SADAT', 3.0, 'FLORA', 3.0, 'MATTHEW', 3.0, 'YIHAN', 3.0, 'AISHWARJYA', 3.0, 'DONALD', 3.0, 'CHRIS', 3.0, 'VICKI', 3.0, 'JING HENG', 3.0]

def avgMoney(lists):
    total_total_money = 0
    counter = 0
    for aname in listFile:
        name = aname.split(',')
        try: 
            total_money = (float(name[3])-float(name[2])+1)*(float(name[1]))
            total_total_money += total_money
            counter += 1
        except:
            pass
    return (total_total_money/counter)
print (avgMoney(listFile)) #$373.5824369747899
