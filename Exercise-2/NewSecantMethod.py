import math


def f(x):
    y = 94 * pow(math.cos(x), 3) - 24 * math.cos(x) + 177 * pow(math.sin(x), 2) - 108 * pow(math.sin(x), 4) - 72 * pow(math.cos(x), 3) * pow(math.sin(x), 2) - 65
    return y


a = 0
b = 3

if f(a) * f(b) >= 0:
    exit(0)


i = 0
x = 0
x1 = 0.5
x2 = 1.5
q = f(x) / f(x1)
r = f(x2) / f(x1)
s = f(x2) / f(x)

while math.fabs(x2 - x1) > pow(10, -6)/2:
    x3 = x2 - ((r * (r - q) * (x2 - x1) + (1 - r) * s * (x2 - x)) / (q - 1) * (r - 1) * (s - 1))
    x = x1
    x1 = x2
    x2 = x3
    i = i + 1


print(f(x2))
print("The root is:", x2)
print("The sum of loops are: ", i)
