# Reading data from file
def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    n = int(lines[0])
    A = []
    b = []

    for line in lines[1:]:
        row = list(map(float, line.strip().split()))
        A.append(row[:-1])
        b.append(row[-1])

    return n, A, b


# Checking if matrix is weakly diagonally dominant
def is_diagonally_dominant(n, A):
    for i in range(n):
        row_sum = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= row_sum:
            return False
    return True


# Calculate matrix Lower-Upper and D^-1
def decompose(n, A):
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]
    Dinv = [[0.0] * n for i in range(n)]

    for i in range(n):
        Dinv[i][i] = 1.0 / A[i][i]
        for j in range(n):
            if i == j:
                L[i][j] = 0.0
                U[i][j] = 0.0
            elif i < j:
                U[i][j] = A[i][j]
                L[i][j] = 0.0
            else:
                L[i][j] = A[i][j]
                U[i][j] = 0.0

    LU = [[L[i][j] + U[i][j] for j in range(n)] for i in range(n)]

    return LU, Dinv


# Jacobi Method
def jacobi(n, A, b, max_iter):
    x = [0.0] * n
    for iter in range(max_iter):
        x_new = [0.0] * n
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        x = x_new
    return x
