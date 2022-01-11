#5
def fib(n):
    count = 0
    n1 = 0
    n2 = 1
    while count < n:
        nth = n1 + n2
        n1=n2
        n2=nth
        count += 1
    return n1
print(fib(6))
print(fib(1000))

#6
def fibSeq (n):
    count = 0
    n1 = 0
    n2 = 1
    myList = []
    while count <= n:
        myList.append(n1)
        nth = n1 + n2
        n1=n2
        n2=nth
        count += 1
    return myList
print(fibSeq(7))

#7
def Hailstone(seed):
    HailList = [seed]
    while seed > 1: 
        if seed%2 == 0: 
          seed= seed//2 
        else: 
          seed = 3*seed + 1
        HailList.append(seed)
    return HailList
print(Hailstone(5))
print(Hailstone(26))
#8
def HailstoneSummary (low_seed, high_seed):
    max_length = 0
    max_seed = 0
    results = []
    for i in range (low_seed, high_seed + 1):
        length = 1
        seed = i
        while seed != 1:
            if seed % 2 == 0:
                seed = seed // 2
                length += 1
            else:
                seed = (seed * 3) + 1
                length += 1
        if length > max_length:
            max_length = length
            max_seed = i
    results.append(max_seed)
    results.append(max_length)
    return results
print(HailstoneSummary(2,10))
print(HailstoneSummary(2,100))            
print(HailstoneSummary(1,1000000))  #challenge calculation    
        