import math

def f(x):
    if x > 0 and x != 1:
        numerator = x * math.sin(x)
        denominator = math.log(abs(x - x**2), 10)
        log4_x = math.log(x, 4)
        result = (numerator / denominator) + log4_x
        return result
    else:
        return "Невірне значення: x має бути додатним і не дорівнювати 1"

x_value = 2 
print(f"f({x_value}) = {f(x_value)}")
