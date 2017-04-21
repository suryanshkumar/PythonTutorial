#how to use break

number = 20

for x in range(100):
    if x == 20:
        print ("the number = ", x)
        break
    else:
        print ("searching ...")


#how to use continue
numberList = [5, 10, 15]

for x in range(20):
    if x in numberList:
        continue
    else:
        print (x, "Not in the numberList")
