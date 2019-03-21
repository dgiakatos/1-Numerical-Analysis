import math


def solverU(A, b):
    x = []
    for i in range(len(A)):
        x.append(None)
    for i in range(len(A) - 1, -1, -1):
        k = len(A) - 1
        temp = 0
        for j in range(len(A[0]) - 1, -1, -1):
            if x[k] is None:
                break
            temp = temp + A[i][j] * x[k]
            k = k - 1
        x[i] = (b[i] - temp) / A[i][i]
    return x


def solverL(A, b):
    x = []
    for i in range(len(A)):
        x.append(None)
    for i in range(len(A)):
        k = 0
        temp = 0
        for j in range(len(A[0])):
            if x[k] is None:
                break
            temp = temp + A[i][j] * x[k]
            k = k + 1
        x[i] = b[i] - temp
    return x


def multi(A, b):
    Ab = [0 for i in range(len(A))]
    if len(A[0]) != len(b):
        exit(1)
    for i in range(len(A)):
        for j in range(len(A[0])):
            Ab[i] = Ab[i] + A[i][j] * b[j]
    return Ab


def PLU(A):
    P = [[0 for j in range(len(A))] for i in range(len(A))]
    L = [[0 for j in range(len(A))] for i in range(len(A))]
    for i in range(len(A)):
        P[i][i] = 1
    for i in range(0, len(A)):
        maxElement = math.fabs(A[i][i])
        maxRow = i
        for j in range(i+1, len(A)):
            if math.fabs(A[j][i]) > maxElement:
                maxElement = math.fabs(A[j][i])
                maxRow = j
        for j in range(0, len(A)):
            temp = A[maxRow][j]
            A[maxRow][j] = A[i][j]
            A[i][j] = temp
            tempP = P[maxRow][j]
            P[maxRow][j] = P[i][j]
            P[i][j] = tempP
            tempL = L[maxRow][j]
            L[maxRow][j] = L[i][j]
            L[i][j] = tempL
        for j in range(i + 1, len(A)):
            g = A[j][i] / A[i][i]
            L[j][i] = g
            for k in range(i, len(A)):
                if i == k:
                    A[j][k] = 0
                else:
                    A[j][k] = - g * A[i][k] + A[j][k]
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                L[j][i] = 1
    U = A
    return P, L, U


def finalSolver(A, b):
    P, L, U = PLU(A)
    return solverU(U, solverL(L, multi(P, b)))


A = [[1, 2], [3, 4]]
B = [[-4], [4.5]]
C = [[1,2,3],[4,5,6],[7,8,9]]
D = [[10,11,12],[13,14,15],[16,17,18]]
F = [[2,4,1,-3], [-1,-2,2,4], [4,2,-3,5], [5,-4,-3,1]]
R = [[2,1,5],[4,4,-4],[1,3,1]]
Q = [[1, 0, 0], [1, 1, 0], [2, 3, 1]]
b = [4,5,6]

print(finalSolver(R, b))
