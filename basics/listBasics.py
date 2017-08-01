#declare list of numbers
num = [53, 12, 11, 22, 99]
print (num)
#accessing the elements of the list, indexing starts with 0
print(num[2])

#modify the entries of the list
num[2] = 0
print(num)

#add the elements to the available list
num = num + [6, 7, 8, 9]
print(num)
#or
num.append(1000)
print(num)

#remove the elements from the list
num[1:2] = []
print(num)
#remove specific element
num.remove(1000)
print(num)
#remove the entire list
num[:] = []
print(num)
