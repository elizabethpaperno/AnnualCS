def readNumbers(filename):
    f = open(filename,'r')
    s = f.readline()
    lst =[]
    while s != '':
       word = s.strip()   
       if word.isdigit():  
          lst.append(int(word))
       s = f.readline()
    return lst

def MinMaxList(filename):
    lst = readNumbers(filename)
    f ={}
    for anum in lst:
        if anum in f:
            f[anum]+=1
        else:
            f[anum] = 1
    sorted_freq = sorted(f.items(),key=lambda x: x[1], reverse=True)
    max_f="Max number " + str(sorted_freq[0][0]) + " appears "+ str(sorted_freq[0][1])+ " times"
    min_f ="Min number " + str(sorted_freq[len(sorted_freq)-1][0])+ " appears "+ str(sorted_freq[len(sorted_freq)-1][1]) + " times"
    return max_f + "\n" + min_f 
            
print(MinMaxList("randomNums.txt"))
    
def readMacbeth(filename):
    f = open(filename,'r')
    s = f.read().strip()
    start=s.find("THE TRAGEDY OF HAMLET, PRINCE OF DENMARK")
    end = s.find("*** END OF THE PROJECT GUTENBERG EBOOK HAMLET ***")
    string = s[start-1:end-1].strip()
    return string

def MinMaxList(filename):
    string = readMacbeth(filename).lower()
    f ={}
    for char in string:
        if ord(char) <= 127: 
            if char in f:
                f[char]+=1
            else:
                f[char] = 1
    sorted_freq = sorted(f.items(),key=lambda x: x[1], reverse=True)
    max3_f= [(sorted_freq[0][0], sorted_freq[0][1]), (sorted_freq[1][0], sorted_freq[1][1]), (sorted_freq[2][0], sorted_freq[2][1])]
    min3_f = [(sorted_freq[len(sorted_freq)-3][0], sorted_freq[len(sorted_freq)-3][1]), (sorted_freq[len(sorted_freq)-2][0], sorted_freq[len(sorted_freq)-2][1]), (sorted_freq[len(sorted_freq)-1][0], sorted_freq[len(sorted_freq)-1][1])]
    return max3_f, min3_f
print(MinMaxList("macbeth.txt"))
    

