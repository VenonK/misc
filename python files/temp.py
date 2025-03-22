array = [123,435,543,6546,26326,34562]

finder = int(input("what to find fuck nigga "))

first = 0
last = len(array) -1

while first <= last:
    midpoint = (first+last) // 2
    
    if finder == array[midpoint]:
        print("found")
        break
    elif finder < array[midpoint]:
        last = midpoint - 1
    else:
        first = midpoint + 1

