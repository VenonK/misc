import random


craCounter = 0
armCounter = 0

while True:
    var = random.randint(1,100000000000)
    if var % 2 == 0:
        craCounter += 1 
    else:
        armCounter += 1


    if craCounter == 10:
        print("cradily")
        break
    
    if armCounter == 10:
        print("armaldo")
        break