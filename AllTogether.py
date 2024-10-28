### Part Four -- your code goes here. 
import random
rand = []

for i in range(10):
    rand.append(random.randint(1, 100))

print("Origianl list",rand)
for x in rand[:]:
    while x % 2 == 0 and x in rand:
        index = rand.index(x)
        rand.pop(index)

print("Final list",rand)

