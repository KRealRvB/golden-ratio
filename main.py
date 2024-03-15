import math

a = 0
b = 1
epsilon = 0.02

def function_of_x(x):
    return x**3 - math.sin(x)

x1 = (a + (3 - math.sqrt(5)) / 2) * (b - a)
x2 = (a + (math.sqrt(5) - 1) / 2) * (b - a)

epsilon_n = abs(x2 - x1)

while epsilon_n > epsilon:
    if function_of_x(x1) < function_of_x(x2):
        b = x2
        x2 = x1
        x1 = a + b - x2
    else:
        a = x1
        x1 = x2
        x2 = a + b - x1
    epsilon_n = abs(x2 - x1)
x_end = (a + b) / 2
print(x_end, function_of_x(x_end))