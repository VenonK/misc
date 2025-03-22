def factorial(num):
    if num <= 0:
        myError = ValueError("This is less than 0")
        raise myError
    
    product = 1
    
    for i in range(1,num+1):
        product = product * i


    return product


print(factorial(9))
