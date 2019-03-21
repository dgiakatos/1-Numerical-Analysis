import math
import random


def f(x):
    y = 94 * pow(math.cos(x), 3) - 24 * math.cos(x) + 177 * pow(math.sin(x), 2) - 108 * pow(math.sin(x), 4) - 72 * pow(math.cos(x), 3) * pow(math.sin(x), 2) - 65
    return y


a = 0
b = 3

root = random.uniform(a, b)
i = 1

while True:
    if f(root) == 0:
        break
    elif (f(root) * f(a)) < 0:
        b = root
    else:
        a = root
    preRoot = root
    root = random.uniform(a, b)
    i = i + 1
    if math.fabs(root - preRoot) < pow(10, -6)/2:
        break

print("The root is:", root)
print("The sum of loops are: ", i)