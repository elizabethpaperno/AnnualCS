infile = "names-1.txt"
f = open(infile, 'r')
s = f.read()
len(s)
s[:30]
s[:100]
f.close()
a = s.split("\n")
len(a)
a[0]
