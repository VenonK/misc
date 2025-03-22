def hashit(hashKey,numOfSlots):
    hashvalue = hashKey % numOfSlots
    return hashvalue

print(hashit(31971,48))
print(hashit(43219,48))
print(hashit(56342,48))
print(hashit(96756,48))