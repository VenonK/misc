terminator1 = True
terminator2 = True

while terminator1 == True:
    num1 = float(input("input a number over 100 "))
    if num1 > 100:
        terminator1 = False


while terminator2 == True:
    num2 = float(input("input a number under 10 "))
    if num2 < 10:
        terminator2 = False

num3 = num1 / num2

print(f"the number {num2} is {num3} times smaller than {num1}")