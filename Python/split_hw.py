arr = '''FOMIN,SAQIF
PAPERNO,XINNI
WILLIAMS,SKAI
GINDIS,MOZEN
MORSE,ANDREA
LOW,ARIEL
ZAMAN,ALEXANDRIA
HUMAIDEE,AFIA
SHAN,NATALIA
SHAHID,EDWARD
TEDESCO,CARINA
HLINKA,ZAMIN
STACY,JIA
SHIN,JIAYI
ZHAN,MALIKA
LETON,HEPZIBAH
KUCHINAD,VIANA
LEUSSING,REGINA
CHEN,EBTESHAM
AUDHY,ELAINE
WIELAARD,ANI
MARUF,VIOLETA
CUNNINGHAM,TANISHA
TAMEEM,AQIB
BISTA,ANGELA
KHALIQUE,RAMEZ
LOU,CYRUS
PERAZZO,KRIPAMOYE
FRID,JOSEPH
HAQUE,ANNE
FANTOZZI,ALVI
LANDA,ISABELLE
VALLEJO,VICKY
XHETANI,ZAINAB
LAKUSTA,MANVEER
FIROOZAN,OLIVIER
KARIM,SOPHIA
SCHWARZ,ESTEAK
KROP-SIEGMUND,TAASEEN
MUI,YE-HEE
SHAPIRO,MIM
GUTKOVICH,JAY
CHIU,HUMAIRA
BAHUTSKI,KAIDEN
FUKUOKA,RIFAH
CASTLE,SHAFKATH
VAYSBURD,KAZI
ANDREWS,MICHA
CAOTHIEN,DREW
RABINOVICH,DANIEL
OR,LUCINDA
KABWA,WEIBIN
MEDINA,SAKURA
ANANT,TERREN
RUZZIER,GITAE
SY,IQRA
PULAWSKA,ROXY
REN,YUVAL
BACCHUS,OLUWATOBI
JEA,FLORENCE
BAE,IRENE
HUGHES,LEON
COWAN,INARA
SHEN,KEN
ILYANOK,CHENHUI
COLLINS,SELENA
MIKHALEVSKY,MADELYN
MAI,NAFISA
GRAEBER,SAYAN
BOIS,ALIND
TSAHALIS,MANOLEE
GALAI,QINA
ROHAN,ALFAYED
KRONMAN,MORRIS
KYI,GRETA
TAWHID,INFINITY
KRANICH,WAI
KOLENOVIC,DORIN
LEUNG,XINQING
BELL,SAARAH
TYLO,MISA
TASNEEM,DAVALYNN
AZIZ,MELODY
SOIEFER,KANJUDA
FUENTES,MENDY
SAI,CALISTA
BACON,ANIKAH
ALLEN,KHUJISTA
JIA,KEIRA
LEVINE,TAMARA
EISEN,PULINDU
ASHIKIN,FATIHA
LAMANY,AIDEN
SCHWARTZ,ATHENA
RUSSO,FARIHAH
KATARI,SUBYETA
ZOARDAR,MISHEL
HAMEED,YVETTE
HARVEY,CALVIN
SELECTOR,DANTE'''

def numberOfNames (arr):
    return len(arr.split('\n'))
print(numberOfNames(arr))

def listofFn(arr):
    firstNames = []
    x=arr.replace(",", "\n")
    firstAndLast = x.split("\n")
    for i in range (len(firstAndLast)):
        if i%2!=0:
            firstNames.append(firstAndLast[i])
    return firstNames
#print(listofFn(arr))

def listofLn(arr):
    lastNames = []
    x=arr.replace(",", "\n")
    firstAndLast = x.split("\n")
    for i in range (len(firstAndLast)):
        if i%2==0:
            lastNames.append(firstAndLast[i])
    return lastNames
#print(listofLn(arr))

def longestFN (arr):
    firstNames = listofFn(arr)
    max_length = 0
    longestName = ""
    for x in firstNames:
        if len(x) > max_length:
            max_length = len(x)
            longestName = x
    return longestName
print(longestFN(arr))
print(len(longestFN(arr)))

def secondFn (arr):
    firstNames = listofFn(arr)
    firstNames.remove(longestFN(arr))
    max_length = 0
    secondNames = []
    for x in firstNames:
        if len(x) > max_length:
            max_length = len(x)
    for i in firstNames:
        if len(i)==max_length:
            secondNames.append(i)
    return secondNames
print(secondFn(arr))

def longestLn (arr):
    lastNames = listofLn(arr)
    max_length = 0
    longestName = ""
    for x in lastNames:
        if len(x) > max_length:
            max_length = len(x)
            longestName = x
    return longestName, max_length
print(longestLn(arr))

def secongLn(arr):
    lastNames = listofLn(arr)
    max_length = 0 
    sec_length = 0
    for x in lastNames:
        if len(x) > max_length:
            sec_length = max_length
            max_length = len(x)
    return sec_length
print (secongLn(arr))