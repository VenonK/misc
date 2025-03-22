def DPS(damage: int,time: int,timebase: str):
    if damage < 0:
        myError = ValueError("This should be a positive number")
        raise myError
    
    if time < 0:
        myError = ValueError("This should be a positive number")
        raise myError
    
    if timebase == "second":
        totalDamage = damage * time
    elif timebase == "minute":
        totalDamage = damage * time * 60
    else:
        totalDamage = damage * time * 3600

    return totalDamage

