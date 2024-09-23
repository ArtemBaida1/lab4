import math

def F(x, a, b):
    if abs(x**2 + 0.7) > 0:
        part1 = x * math.tan(x) * math.exp(a - b)
        log_part = math.log(abs(x**2 + 0.7), 4)
        result = part1 + log_part
        return result
    else:
        return "Невірне значення: x^2 + 0.7 має бути додатним"

x_value = 2
a_value = 1
b_value = 0.5
print(f"F({x_value}, {a_value}, {b_value}) = {F(x_value, a_value, b_value)}")