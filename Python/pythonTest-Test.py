def RPS (player1, player2) :
    if player1 == player2: 
        return ("tie")
    elif player1 == "rock":
        if player2 == "scissors":
            return ("player 1: rock")
        else:
            return ("player 2: paper")
    elif player1 == "scissors":
        if player2 == "rock":
            return ("player 2: rock")
        else:
            return ("player 1: scissors")
    else:
        if player2 == "rock":
            return ("player 1: paper")
        else:
            return ("player 2: scissors")
print (RPS ("rock", "paper"))          

def transcribe(DNA):
    DNA_code = "GCAT"
    mRNA = "CGUA"
    transcript = ""
    for i in DNA:
        pos = DNA_code.find(i)
        transcript += mRNA[pos]
    return transcript
print(transcribe("GCATTGU"))
        
def snake(camel):
    snake_case = [camel[0].lower()]
    for camelCase in camel[1:]:
        if camelCase.isupper():
            snake_case.append("_")
            snake_case.append(camelCase.lower())
        else:
            snake_case.append(camelCase)
    return "".join(snake_case) 
print(snake("helloMyFriend"))

def snake2(camel):
    snake_case = ""
    snake_case += camel[0].lower()
    for camelCase in camel[1:]:
        if camelCase.isupper():
            snake_case += "_"
            snake_case += camelCase.lower()
        else:
            snake_case += camelCase
    return "".join(snake_case) 
print(snake2("helloMyFriend"))

def camel(snake):
    camelCase = snake.split("_")
    result = ""
    for word in camelCase:
        result += word[0].upper() + word [1:]
    return result
print(camel("snake_camel_hi"))

def schoolID(name):
    commaPos = name.find(",")
    return name[0].lower()+ name[commaPos +1:].lower()
print(schoolID("ELIXjfkkj,papeNO"))        

def moreIDs (names):
    newString = ""
    prevSpace = -1
    for i in range (len(names)):
        if names[i].find(" ") != -1:
            newString += schoolID(names[prevSpace+1:i]) + names[i] #can also add space
            prevSpace=i
    return newString
print(moreIDs("ELIZabeth,pAperNo hArry,PottER "))
    

birthdays = '''08/30/2000
06/05/2002
10/29/2009
11/06/2009
03/02/2011
04/05/2011
12/06/2011
03/08/2016
11/10/2020
11/09/2020'''



def howMany (birthdays):
    return len(birthdays.split("\n"))
print(howMany(birthdays))
    
    
def mostRecent (birthdays):
    closestYr = 0
    closestMonth = 0
    closestDate = 0
    birthdays2 = birthdays.split("\n")
    for date in birthdays2:
        dates = date.split("/")
        if int(dates[2]) > closestYr:
            closestYr = int(dates[2])
            closestMonth = int(dates[0])
            closestDate = int(dates[1])
        elif int(dates[2]) == closestYr:
            if int(dates[0]) == closestMonth:
                if int(dates[1]) > closestDate:
                    closestYr = int(dates[2])
                    closestMonth = int(dates[0])
                    closestDate = int(dates[1])
                else:
                    break
            elif int(dates[0]) > closestMonth:
                closestYr = int(dates[2])
                closestMonth = int(dates[0])
                closestDate = int(dates[1])
    return ([closestMonth, closestDate, closestYr])

print(mostRecent(birthdays))

def mostRecent2 (birthdays): 
    birthdays2 = birthdays.split("\n")
    closestEvery = ""
    newDate = ""
    for date in birthdays2:
        dates = date.split("/")
        newDate = dates[2]+dates[0]+dates[1]
        if newDate >= closestEvery:
          closestEvery = newDate
    return [closestEvery[4:6], closestEvery[6:], closestEvery[:4]]
print(mostRecent2(birthdays))