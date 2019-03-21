import math

def genA(n):
    A = [[-2 for j in range(n)] for i in range(n)]
    for i in range(n):
        A[i][i] = 5
    return A


def genb(n):
    b = [1 for i in range(n)]
    b[0] = 3
    b[n - 1] = 3
    return b


def GaussSeidel(A, b):
    x = [[None for j in range(len(A))] for i in range(2)]
    flag = True
    r = [None for i in range(len(A))]
    for i in range(len(A)):
        temp = 0
        for j in range(len(A)):
            if i != j:
                temp = temp + math.fabs(A[i][j])
        if math.fabs(A[i][i]) < temp:
            flag = False
    if flag:
        for i in range(len(A)):
            x[0][i] = 0
    else:
        for i in range(len(A)):
            x[0][i] = 1
    while True:
        for i in range(len(A)):
            left = 0
            right = 0
            count = 0
            for j in range(len(A)):
                if i > j:
                    left = left + A[i][j] * x[1][count]
                    count = count + 1
                elif i < j:
                    right = right + A[i][j] * x[0][count]
                    count = count + 1

            x[1][i] = (b[i] - left - right) / A[i][i]
        for i in range(len(A)):
            r[i] = math.fabs(x[1][i] - x[0][i])
        m = max(r)
        if m <= math.pow(10, -4) / 2:
            break
        for i in range(len(A)):
            temp = x[1][i]
            x[0][i] = temp
    return x, m


def max(A):
    m = A[0]
    for i in range(1, len(A)):
        if A[i] > m:
            m = A[i]
    return m


n = 10
E = [[8,1,1],[1,8,1],[1,1,8]]
b = [10,10,10]
x, m = GaussSeidel(genA(n), genb(n))
#x, m = GaussSeidel(E, b)

for i in range(0, 2):
    print(x[i])
print("r = ", m)