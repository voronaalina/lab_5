import math 
def spil_dilnyk (x1, x2, x3, y):
    return x1 % y == 0 and x2 % y == 0 and x3 % y ==0

x1 = int(input("Введіть x1: "))
x2 = int(input("Введіть x2: "))
x3 = int(input("Введіть x3: "))
y = int(input("Введіть y: "))

if spil_dilnyk(x1, x2, x3, y):
    print(y, "- спільний дільник чисел ", x1, x2, x3)
else:
    print(y, "не є спільним дільником чисел ", x1, x2, x3)