# using function is python
'''
def functionName():
'''


# 1. use of function without use of return command
def addTwoNumber1(a, b):
    s = a + b
    print ("The sum = " + str(s))


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
