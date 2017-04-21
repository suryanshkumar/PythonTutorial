#using function is python
'''
def functionName():
'''

#use of function without use of return command
def addTwoNumber(a, b):
    sum = a + b
    print ("The sum = " + str(sum))

#use of function with return command
def addTwoNumbers(a, b):
    sum = a+b
    return sum

#call the function now
a = 5
b = 10
addTwoNumber(a, b)

#use of return statement, take the return value and use if for other decisions
sum = addTwoNumbers(a, b)
if sum < 20:
    print("It works!!!")






