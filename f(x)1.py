import math
x = float(input("Введіть х: "))

def function(x):
    if x >= -0.7:
        result = -6 * x**2 + math.sin(x)
    elif -9.9 < x < -0.7:
        result = math.log(abs(x+math.sin(x)))
    elif x <= -9.9:
        result = 12 + abs(math.sin(2*x))
    else:
        print("Обчислення виразу неможливе")
    return result

result = function(x)
print("f(x) = ", result)