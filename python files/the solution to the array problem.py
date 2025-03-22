nameArray = []
for i in range(10):
    name = input("enter a name: ")
    nameArray.append(f"{i+1}. {name}")
    if i == 9:
        for i in range(10):
            print(nameArray[i])    