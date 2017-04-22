# using function is python
'''
def functionName():
'''

<<<<<<< HEAD
=======
#use of function without use of return command
def addTwoNumber(a, b):
    sum = a + b
    print ("The sum = " + str(sum))

#use of function with return command
def addTwoNumbers(a, b):
    sum = a+b
    return sum

#use function to pass any number of arguments

def addNumbers(*args):
    sum = 0
    for s in args:
        sum += s
    return sum


#call the function now
a = 5
b = 10
addTwoNumber(a, b)

#use of return statement, take the return value and use if for other decisions
sum = addTwoNumbers(a, b)
if sum < 20:
    print("It works!!!")
>>>>>>> 3423923a1b8f72c3007e48489d4f3be195e2a1ff

# 1. use of function without use of return command
def addTwoNumber1(a, b):
    s = a + b
    print ("The sum = " + str(s))

#use the addtion for any number of arguments
sum = addNumbers(1.4, 1.3, 7, 6, 5)
print ("Total sum = " + str(sum))

# 2. use of function with return command
def addTwoNumber2(a, b):
    s = a + b
    return s


# call the function now
a = 5
b = 10
addTwoNumber1(a, b)

# 2. use of return statement, take the return value and use if for other decisions
t = addTwoNumber2(a, b)
if t < 20:
    print("It works!!!")
