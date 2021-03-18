# Python Functions
print ("\nPython Functions");

def myprinter():
    print ("\nThis is my printer")
myprinter()

def mycompare(first, second):
    if (first < second):
        print (first)
    else:
        print (second)
mycompare(10, 15)
mycompare(15, 10)

print ("\nImmutable parameters")
scoper = 25
def myreturn(first, second):
    scoper = 20
    print ("Scoper in:", scoper)
    if (first < second):
        return first;
    return second
ret = myreturn(10, 15)
print (ret)
print ("Scoper out:", scoper)
ret = myreturn(15, 10)
print (ret)

scoperstr = "Python"
print (scoperstr)
def myreturnstr (mystr):
    scoperstr = "Learning"
    print ("Scoper str in:", scoperstr)
    return mystr
ret = myreturnstr(scoperstr)
print ("Scoper str out:", scoperstr)
print (ret)

print ("\nMutable parameters")
nlist = [10, 20, 30, 40, 50]
print (nlist)
def x10_elements5 (mylist):
    mylist[0] *= 10
    mylist[1] *= 10
    mylist[2] *= 10
    mylist[3] *= 10
    mylist[4] *= 10
x10_elements5 (nlist)
print (nlist)
    
print ("\nString functions - Find")
print (scoperstr.find("Py")) # first instance at index 0
print (scoperstr.find("py")) # find is case sensitive
print (scoperstr.find("Py", 3,6)) # find in the range
print (scoperstr.find("Py", 0,4)) # find in the range
print (scoperstr.find("on"))

print ("\nString functions - Replace")
mystr = "learning Python"
newstr = mystr.replace("Python", "Perl")
newstr = mystr.upper()
print (newstr)

print ("\nCasts")
print (int("12"))
print (int(True))
print (int(23.9874))

print (ord('a')) # convert to unicode value
print (ord('0'))

print (float(24))
print (float(False))

print (str(False))
print (str(1.234) + ' is a string');

print (bool(10))
print (bool(25.3419))
print (bool(""))
print (bool ("Hello"))

print ("\nLambda functions - anonymous function that returns some form of data")
# fn_name = lambda <comma separated parameters> : <expr that returns something>

tres = lambda num : num * 3 # assign lambda to a variable
print (tres(10)) # calling lambda function with a parameter

sumo = lambda n1, n2, n3 : n1 + n2 + n3
print (sumo(10, 20, 30))

comp = lambda n1, n2 : n1 if (n1 > n2) else n2
print (comp(10, 20))

print ("\nLambda functions - usage example - Calculator")
def add (n1, n2):
    return n1 + n2
def substract (n1, n2):
    return n1 - n2
def multiply (n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1 / n2

def calculator (operation, n1, n2):
    return operation(n1, n2)

result = calculator(multiply, 10, 20)
print ("Calculator result for 10 x 20: ", result)
print ("Calculator result for 10 + 20: ", calculator(add, 10, 20))

# Anonymous lambda function
print ("Calculator with lambda: ", lambda n1, n2: n1 + n2, 10, 20)

# Lambda mapped to a named function
print ("\nMap() function")
nlist = [10, 20, 30, 40, 50]
double_the_list = map(lambda n : n * 2, nlist)
print ("List elements doubled: ", list(double_the_list))

print ("\nFilter() function")
filter_the_list = filter(lambda n : n > 10, nlist)
print ("List elements filtered > 10: ", list(filter_the_list))

print ("\nRecursive functions")
def recursive_count(number):
    print (number);
    # base case
    if number == 0:
        return 0;
    recursive_count(number - 1) # recursive call with a different argument
    print (number)

recursive_count(5)
# 1. rec(5) -> print 5
# 2. rec(4) -> print 4
# 3. rec(3) -> print 3
# 4. rec(2) -> print 2
# 5. rec(1) -> print 1
# 6. rec(0) -> print 0
# 7. return to rec(1) - print 1
# 8. return to rec(2) - print 2
# 9. return to rec(3) - print 3
# 10. return to rec(4) - print 4
# 11. return to rec(5) - print 5
# the extra numbers after 0 are because of the print statement
# if you changed it to print only if number > 0, then you won't see it
# but the return stack will still execute.

print ("\nRecursive Fibonacci function - return nth number in the sequence")
# 0 1 1 2 3 5 8 13 21 34 55 89

def fib(n):
    # base case
    if (n <= 1):
        return 0
    elif (n == 2):
        return 1
    else:
        print (n)
        return fib (n - 1) + fib (n - 2)

print (fib(5))
# 1. fib(4)                   + fib(3)
# 2. fib(3)          + fib(2) + fib(2) + fib(1)
# 3. fib(2) + fib(1) + 1      + 1      + 0
# 4. 1      + 0      +  
# base case: the first two values are 0 and 1 - this is the stopping condition.
# if n > 2, then it is the sum of the two numbers before it.

print ("\nQuiz")
mystr = "Hello"
def exclmn(mystr):
    mystr = "!!" + mystr + "!!"
    return mystr
exclmn(mystr)
print (mystr)
print (exclmn(mystr))

print ("\nQuiz - repeat concat")
def rep_cat(x, y):
    return ((10 * str(x)) + (5 * str(y)))
print(rep_cat(3, 4))

print ("\nQuiz - factorial")
# factorial(n) = n * (n - 1) * (n - 2) * ... * 1
def factorial(n):
    # base case
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print (factorial(4))
print (factorial(-5))
