# Python Loops
# for [iterator] in [sequence]
# [sequence] = range(start, end, step)

print ("\nLoop with range with cool if-then-else")
evenodd = lambda n : "even" if n % 2 == 0 else "odd"
for i in range(1, 11):
    print (i, "is " + str(evenodd(i)))

print ("\nLoop in range with step")
for i in range(1, 11, 2):
    print (i, "is " + str(evenodd(i)))

print ("\nLoop through list")
flist = [0.1, 1.1, 2.1, 3.1, 4.1, 5.1]
for i in flist:
    print (i)
    
print ("\nLoop through range cast on a list")
for i in range(0, len(flist)):
    print (flist[i])

print ("\nLoop through range cast on a list")
for i in range(0, len(flist), 2):
    print (flist[i])

print ("\nNested Loop for matrix multiplication")
m1 = [1, 2, 3, 4] # single row matrix
m2 = [4, 3, 2, 1] # single column matrix
k = 0
if len(m1) != len(m2):
    print ("Incompatible matrix dimensions")
for i in range(0, len(m1)):
    for j in range(0, len(m2)):
        if i == j:
            k += m1[i] * m2[j]
            print (str(i+1) + "," + str(j+1) + ": " + str(m1[i]*m2[j]))
print ("Output: ", k)        

#flist = ['m','a','l','a','y','a','l','a','m']

print ("\nBrake for moose")
for i in m1:
    for j in m2:
        print (str(i) + "," + str(j))
        if i == j+1:
            print (str(i) + " is one greater than " + str(j) + ". Exiting")
            break # this only breaks out of the inner loop

print ("\nContinue for coons")
for i in m1:
    for j in m2:
        if i == j:
            continue
        print (str(i) + "," + str(j))

print ("\nIt's been a while ...")
flist = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
i = 1;
while i in flist:
    print ("i: " + str(i))
    i += 0.2

print ("\Quiz")
strlist = ["Anakin", "Vader", "Luke", "Leia", "Rey"]
for s in strlist:
    if len(s) < 5:
        print (s + ":" + str(len(s)))

i = 0
while (i < len(strlist)):
    if len(strlist[i]) < 5:
        print (len(strlist[i]))
    i += 1

print ("\nBalanced Braces")
# Given "[[[[][][]]]" return true if left braces match with closing right braces
#braces = "[[[[][][]]]"
#braces = "[[[[]]]][]["
#braces = "[[[[]]]]"
#braces = "]]]][[[["
braces = "[]][[]"
left = 0
right = 0
i = 0
brace_open = 0
while i < len(braces):
    # base case
    if i == 0 and braces[i] == "]":
        print ("False: starts with ]")
        right += 1
        break
    if (braces[i] == "["):
        left += 1
        brace_open += 1
    if (braces[i] == "]"):
        right += 1
        if brace_open >= 1:
            brace_open -= 1
    else:
        pass # don't care
    i += 1
if left != right or brace_open > 0:
    print ("False: Left:" + str(left) + " Right:" + str(right))
else:
    print ("True: Left:" + str(left) + " Right:" + str(right))

print ("\nSimpler code")
def check_balance(braces):
    check = 0
    for brace in braces:
        if brace == '[':
            check += 1
        elif brace == ']':
            check -= 1
        if check < 0:
            break
    return check == 0

#braces = "[[[[][][]]]"
#braces = "[[[[]]]][]["
#braces = "[[[[]]]]"
#braces = "]]]][[[["
#braces = "[]][[]"
ret = check_balance(braces)
if ret == True:
    print (braces + " is balanced")
else:
    print (braces + " is unbalanced")

print ("\nCheckSum to zero")
def check_sum(nlist):
    for num in nlist:
        for complement in nlist:
            if num + complement == 0:
                return True
    return False

numlist = [10, -14, 26, 5, -3, 13, -5]
#numlist = [10, -14, 26, 5, -3]
if check_sum(numlist):
    print ("Sum checks")
else:
    print ("Sum does not check")

# 0 1 1 2 3 5 8 13 21
print ("\nFibonacci with loops")
def fib(n):
    n1 = 0
    n2 = 1
    if (n < 1):
        return -1
    if (n == 1):
        return n1
    if (n == 2):
        return n2
    nth = 3
    # if you use for loop here, Py complains that val is uninitialized
    while (nth <= n):
        val = n1 + n2
        n1 = n2
        n2 = val
        nth += 1
    return val

print ("-1: " + str(fib(-1)))
print ("0: " + str(fib(0)))
print ("1: " + str(fib(1)))
print ("2: " + str(fib(2)))
print ("3: " + str(fib(3)))
print ("4: " + str(fib(4)))
print ("5: " + str(fib(5)))
print ("6: " + str(fib(6)))
print ("7: " + str(fib(7)))
            
