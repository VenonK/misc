def doSomething(n):
    if n == 1:
        return 0
    else:
        return 1+ doSomething(n // 2)
    
print(doSomething(100))