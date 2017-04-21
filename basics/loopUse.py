#for loop demonstration

print("For loop demo")
foods = ['egg', 'mango', 'apple', 'wine', 'yogurt']

for i in foods:
    print(i)
    print(len(i))

#loop 10 times
print("standard one step loop")
for x in range(5):
    print ("hi there")

#loop in range with two numbers
print("range increment loop")
for x in range(10, 15):
    print (x)

#change the step size from 1 to any value
print("step increment loop")
for x in range(10, 20, 2):
    print (x)


#while loop demo

print ("While loop demo")
n = 5
while n < 10:
    print(n)
    n += 1
