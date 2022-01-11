# this is a comment -- anything after the "#" character is not interpreted by Python

fred = 23  # the spaces around the "=" are not necessary, they just look better that way

print(fred+4)  # when you execute this set of commands, you should see a 27 in the shell below

# we can ask print() to print several things -- print(this,that,george), which could be a mixture of
#  strings (between double-quotes or between apostrophes), and numeric expressions...
print("This should also be a 27: ",fred+4,' See?')

# a function consists of the function declaration line that looks like:
#def func-name(arg0, arg1, ...)
# followed by the function body, which is indented at least one tab stop

def to_fahr(celsius):
    almost = celsius * 9/5
    return almost+32

print('Boiling point of water is ', to_fahr(100), 'degrees.')

harry = "hello world"

geroge = 'hello world'

ron= '''to be or not to be 
that is the question '''

