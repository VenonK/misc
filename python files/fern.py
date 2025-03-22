array = [3,4,32,65,7,45,2,8,9,0,54]

for i in range(len(array)):
    elem = array[i]
    j = i-1
    while (j >= 0) and (array[j] > elem):
        array[j+1] = array[j]
        j = j-1
    array[j+1] = elem

print(array)