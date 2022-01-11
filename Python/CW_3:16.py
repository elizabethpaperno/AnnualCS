a = "abcdefghijklm"
print (len(a))
print (a[3]) #d

print (a[3:6])

print( a[-2]) #l

print (a[10:13]) #kml

print (a[-4:-1]) #jkl

print (a[-4:]) #if you leave off last number it goes to the end of the string
print (a[:3]) #starts at the beginning of the string
print(a[:]) #full string
print(a[3:3]) #nothing
print (a[10:1000]) #does not return an error, just goes as far as possible

a[1:10:2] #3rd parameter is skip value (move to very second position)
a[1:10:3] #move to every third position
a [10:5:-1] #goes through it backward