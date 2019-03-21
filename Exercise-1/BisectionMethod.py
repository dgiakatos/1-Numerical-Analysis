import math


def f(x):
    y = 14 * x * pow(math.e, x - 2) - 12 * pow(math.e, x - 2) - 7 * pow(x, 3) + 20 * pow(x, 2) - 26 * x + 12
    return y


a = 1.5
b = 3
N = (math.log10(b - a) - math.log10((1/2)*pow(10, -6))) / math.log10(2)

for i in range(math.ceil(N)):
    m = (a + b) / 2.0
    if f(m) == 0:
        break
    elif (f(m) * f(a)) < 0:
        b = m
    else:
        a = m

print("The root is:", m)
print("The sum of loops are: ", i+1)
