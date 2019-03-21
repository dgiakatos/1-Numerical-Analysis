import math


def f(x):
    y = 94 * pow(math.cos(x), 3) - 24 * math.cos(x) + 177 * pow(math.sin(x), 2) - 108 * pow(math.sin(x), 4) - 72 * pow(math.cos(x), 3) * pow(math.sin(x), 2) - 65
    return y


def f1(x):
    y = - 282 * pow(math.cos(x), 2) * math.sin(x) + 24 * math.sin(x) + 354 * math.sin(x) * math.cos(x) - 432 * pow(math.sin(x), 3) * math.cos(x) + 216 * pow(math.cos(x), 2) * pow(math.sin(x), 3) - 144 * pow(math.cos(x), 4) * math.sin(x)
    return y


def f2(x):
    y = 564 * math.cos(x) * pow(math.sin(x), 2) - 282 * pow(math.cos(x), 3) + 24 * math.cos(x) + 354 * pow(math.cos(x), 2) - 354 * pow(math.sin(x), 2) - 1296 * pow(math.sin(x), 2) * pow(math.cos(x), 2) + 432 * pow(math.sin(x), 4) - 432 * math.cos(x) * pow(math.sin(x), 4) + 648 * pow(math.cos(x), 3) * pow(math.sin(x), 2) + 576 * pow(math.cos(x), 3) * pow(math.sin(x), 2) - 144 * pow(math.cos(x), 5)
    return y


a = 0
b = 2.5

if f(a) * f2(a) > 0:
    root = a
else:
    root = b


i = 0

while True:
    preRoot = root
    root = root - (f(root) / f1(root)) - ((pow(f(root), 2) * f2(root)) / (2 * pow(f1(root), 3)))
    i = i + 1
    if math.fabs(root - preRoot) < pow(10, -6)/2:
        break


#root = 2.0
print("The root is:", root)
print("The sum of loops are: ", i)
print("f(x) = ", f(root))
if f1(root) != 0:
    print(f2(root) / (2 * f1(root)))
