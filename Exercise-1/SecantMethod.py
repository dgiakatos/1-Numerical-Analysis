import math


def f(x):
    y = 14 * x * pow(math.e, x - 2) - 12 * pow(math.e, x - 2) - 7 * pow(x, 3) + 20 * pow(x, 2) - 26 * x + 12
    return y


a = 1.5
b = 3

if f(a) * f(b) >= 0:
    exit(0)


i = 0
preRoot = a
root = b

while math.fabs(root - preRoot) > pow(10, -6):
    tempRoot = root - (f(root) * float(root - preRoot)) / (f(root) - f(preRoot))
    preRoot = root
    root = tempRoot
    i = i + 1


print("The root is:", root)
print("The sum of loops are: ", i)
