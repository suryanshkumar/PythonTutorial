# using function is python
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

#use of the return statement. Use the returned value and use it for other decisions
sum = addTwoNumbers(a, b)
if sum < 20:
    print("It works!!!")


#use addition for any number of arguments
sum = addNumbers(1.4, 1.3, 7, 6, 5)
print ("Total sum = " + str(sum))


