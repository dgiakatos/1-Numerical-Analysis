import math


def f(x):
    y = 14 * x * pow(math.e, x - 2) - 12 * pow(math.e, x - 2) - 7 * pow(x, 3) + 20 * pow(x, 2) - 26 * x + 12
    return y


def f1(x):
    y = 2 * pow(math.e, x - 2) + 14 * x * pow(math.e, x - 2) - 21 * pow(x, 2) + 40 * x - 26
    return y


def f2(x):
    y = 16 * pow(math.e, x - 2) + 14 * x * pow(math.e, x - 2) - 42 * x + 40
    return y


a = 1.5
b = 3

if f(a) * f2(a) > 0:
    root = a
else:
    root = b


i = 0

while True:
    preRoot = root
    root = root - (f(root) / f1(root))
    i = i + 1
    if math.fabs(root - preRoot) < pow(10, -6):
        break


print("The root is:", root)
print("The sum of loops are: ", i)
if f1(root) != 0:
    print(f2(root) / (2 * f1(root)))
