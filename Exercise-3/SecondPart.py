import math

def AT(A):
    B = [[None for j in range(len(A))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            B[j][i] = A[i][j]
    return B


def equal(A, AT):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] != AT[i][j]:
                print('A != AT')
                exit(1)
    return


def cholesky(A):
    equal(A, AT(A))
    L = [[0 for j in range(len(A))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            if i > j:
                temp = 0
                for k in range(0, j):
                    temp = temp + (L[j][k] * L[i][k])
                L[i][j] = (A[i][j] - temp) / L[j][j]
            elif i == j:
                temp = 0
                for k in range(0, j):
                    temp = temp + math.pow(L[i][k], 2)
                if A[i][i] - temp < 0:
                    print("A[i][i] - temp < 0")
                    exit(1)
                L[i][i] = math.sqrt(A[i][i] - temp)
    return L


C = [[4,12,-16],[12,37,-43],[-16,-43,98]]
print(cholesky(C))
