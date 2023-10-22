# The 1000th 'first program' in Python - let us hope it is the last first
"""Alternative commenting in Python"""
print ("Hello World!")
print ("Python 3", end="")
print ("Coding")

# Basic datatypes
print ("\nDish out some integers!")
print (10)
print (-3000)
num = 4000
print (num)
num = -1600
print (num)

print ("Fillet some floating points")
print (1.0005)
print (-85.601)
fltpt = 1.234
print (fltpt)

print ("\nCollate some complex numbers")
print ("Complex(real, imaginary) (a + bj)")
print (complex(10, 20))
cplx = complex(2, 0)
cplx2 = complex(0, 2)
# Python does not like this string
# print ("Cplx: " + cplx + "  Cplx2: " + cplx2)
# Python does not mind the semicolons - perhaps worth using it
print (cplx);
print (cplx2)

print ("\nBelt out Booleans!")
print (True)
maqbool = False
print (maqbool)
# the following won't work - first letter needs to be capital
# maqbool = false

print ("\nSwing some Strings")
lp = 'Learning Python in single quotes'
print (lp)
print ("&")
empty = ""
print (empty)
print (len(lp))
lp = "Learning Python in double quotes"
print (lp)
print (len(lp))
print (lp[9])
print (lp[len(lp) - 1])
# the following will error
# print (lp[len(lp)])
print ("Reverse indexing using [-idx], get P in Python")
print (lp[-1])  # same as len[len(lp)-1]
print (lp[-23]) # same as lp[9]

print ("\nStep 'em Strings")
print (lp[9:15:2])
print (lp[9::2])

print ("\nReverse 'em Strings - unique to Python")
print (lp[::-1])
print (lp[15:2:-1])
print (lp[18:0:-2])

print ("\nSlice 'em Strings - unique to Python")
print (lp[9:15])
print (lp[8:len(lp)])
print (lp[:9])
print (lp[9:])

print ("\nPEMDAS arithmetic Operators")
print (10 + 5)
print (10 - 5)
print (10 * 5)
print (10 / 5)
print (11 // 5) # floor division - floored to nearest smaller integer
print (14.9999 // 5)
print (10 % 5)
print (-10 % 3)
print (10 % -3) # remainder is -ve only if rhs operand is -ve
print (14 % 5)
print (14.9999 % 5)

print ("\nComparison operators")
print (10 < 5)
print (5 < 10)
print (5 == 5)
print (5 <= 10)
print (5 != 10)
## print (5 is not 10)
## print (10/2 is 5)
## print (10/2 is not 6)

print ("\nLogical operators")
print ((10 < 5) and (5 < 10))
print ((10 < 5) or (5 < 10))
print (not (10 < 5))

print ("\nBitwise operators")
n1 = 10 #0000 1010
n2 = 20 #0001 0100
print (n1 & n2) #0000 0000
print (n1 | n2) #0001 1110
print (n1 ^ n2) #0001 1110
print (~n1)     #1111 0101
print (n1 << 3) #0101 0000
print (n2 >> 3) #0000 0101

print ("\nString comparison operators")
s1 = 'Learning'
s2 = 'Python'
print (s1 < s2) # string first in the dictionary has smaller value
s3 = s2
print (s2 == s3) 
print (s3 < s1)
print (s1 >= s3)

print ("\nString concat and find - Important")
print (s1 + " " + s2)
print (s2 * 3)
print ('Py' in s2)
print ('Learn' in s1)

print ("\nGrouping operator - unique to Python")
print (s1, s2, n1, n2, 10*5)
mylist = [s1, s2, n1, n2, 10*5]
print (mylist)
print (mylist[3])
print (len(mylist))

print ("\nMixed type operations - unique to Python")
print (True + 5) # True gets a value 1, False 0
x = 20; y = 5;
print ((x + True) / (4 - y * False))

print ("\nQuiz")
mystr = "0123456789"
print (mystr[2:6:2])
print (mystr[-2])
print (mystr[-4])
print (mystr[-2:-8])
print (mystr[-2:-8:-2])

print ("Educative IO Exercise Gravitational Force between earth and moon")
print ("Compute GMm/r^2 with inputs G=6.67*10^-11, M=6.0*10^24, m=7.34*10^22, r=3.84*10^8")
G = 6.67 * (10 ** -11)
M = 6.0 * (10 ** 24)
m = 7.34 * (10 ** 22)
r = 3.84 * (10 ** 8)

Fg = (G * M * m)/(r ** 2)
print (Fg)

print ("\nEmpty (pass) statement")
if (G < 1):
    pass
    print ("Enter more code above")
    
print ("\nConditional Statements")
if (G < 1):
    newG = G
    print ("G is less than 1")
    print (newG)
else:
    print ("G is more than 1")
# Scoping sucks in Python
print (newG)

out = "G is less than 1" if (G < 1) else "G is more than 1"
print (out)

if (G < 1):
    print ("G is less than 1")
elif (G > 1):
    print ("G is more than 1")
else:
    print ("G is 1")

print ("\nEducative IO Exercise Discounted Price")
price = 200
final_price = price
if (price >= 300):
    final_price = price * ((100 - 30)/100) # 30% discount
elif (price >= 200):
    final_price = price * ((100 - 20)/100) # 20% discount
elif (price >= 100):
    final_price = price * ((100 - 10)/100) # 10% discount
elif (price > 0):
    final_price = price * ((100 - 5)/100)  # 5% discount
else:
    print ("Error in price")
print ("Price: " + str(price) + " Final price: " + str(final_price))