a = [5, -7.5, 0, 3.5]

def sumList(alist):
    total = 0
    for i in range (len(alist)):
        total += alist[i]
    return total
print(sumList(a))

def sumlist2(alist):
    total = 0
    for fred in alist:
        total += fred
    return total
print(sumlist2(a)) 

sum(a)
max(a)
min(a)

def maxV(alist):
        maxValue = 0
        for i in alist:
            if i > maxValue:
                maxValue = i
        return maxValue
print(maxV(a))
print(maxV(""))