def doolittle(filename):
    # Reading data from the file
    with open(filename, 'r') as f:
        data = [[float(num) for num in line.split(' ')] for line in f.readlines()]

    n = len(data)

    # Creating the augmented matrix
    A = []
    for i in range(n):
        row = []
        for j in range(n + 1):
            row.append(data[i][j])
        A.append(row)

    # LU decomposition - Doolittle's algorithm
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    for i in range(n):
        L[i][i] = 1.0

    for j in range(n):
        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A[i][j] - s1

        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (A[i][j] - s2) / U[j][j]

    # Determining the Y vector
    Y = [0.0] * n
    for i in range(n):
        s = sum(L[i][j] * Y[j] for j in range(i))
        Y[i] = A[i][n] - s

    # Determining the X vector
    X = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(U[i][j] * X[j] for j in range(i + 1, n))
        X[i] = (Y[i] - s) / U[i][i]

    # Checking if there is zero on the diagonal of the matrix
    for i in range(n):
        if U[i][i] == 0:
            print("There is zero on the diagonal of the matrix!")
            return None

    # Displaying the results
    print("Augmented matrix:")
    for row in A:
        print(row)

    print("\nMatrix L:")
    for row in L:
        print(row)

    print("\nMatrix U:")
    for row in U:
        print(row)

    print("\nVector Y:")
    print(Y)

    print("\nVector X:")
    print(X)

    return X


result = doolittle("data.txt")
