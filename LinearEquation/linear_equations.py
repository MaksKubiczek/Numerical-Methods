def solve_linear_equations(filename):
    # Reading data from file
    with open(filename, 'r') as file:
        Ab = [[float(num) for num in line.split()] for line in file]

    n = len(Ab)  # matrix size

    # Printing matrix
    print("Matrix:")
    for row in Ab:
        print(row)

    # Partial row pivoting
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(Ab[j][i]) > abs(Ab[max_row][i]):
                max_row = j
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]

    # Gauss elimination method
    for i in range(n - 1):
        for j in range(i + 1, n):
            factor = Ab[j][i] / Ab[i][i]
            for k in range(i, n + 1):
                Ab[j][k] = Ab[j][k] - factor * Ab[i][k]

    # Solving the system of equations
    x = [0] * n
    x[n - 1] = Ab[n - 1][n] / Ab[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += Ab[i][j] * x[j]
        x[i] = (Ab[i][n] - s) / Ab[i][i]

    # Printing matrix v2
    print("Matrix after computations:")
    for row in Ab:
        print(row)

    # Printing the solution
    print("\nSolution of the system of equations:")
    for i in range(n):
        print("x{} = {:.2f}".format(i, x[i]))


def solve_linear_equations_crout(filename):
    # Reading data from file
    with open(filename, 'r') as file:
        Ab = [[float(num) for num in line.split()] for line in file]

    n = len(Ab)  # matrix size

    # Printing the extended matrix before computations
    print("Extended matrix before computations:")
    for row in Ab:
        print(row)

    # Creating a vector of column numbers
    column_order = list(range(n))
    for i in range(n):
        max_col = i
        for j in range(i + 1, n):
            if abs(Ab[i][max_col]) < abs(Ab[i][j]):
                max_col = j
        if max_col != i:
            column_order[i], column_order[max_col] = column_order[max_col], column_order[i]

    # Printing the vector of column numbers
    print("Vector of column numbers:")
    print(column_order)

    # Gauss-Crout elimination method with partial column pivoting
    for k in range(n):
        max_row = k
        for i in range(k + 1, n):
            if abs(Ab[i][column_order[k]]) > abs(Ab[max_row][column_order[k]]):
                max_row = i
        Ab[k], Ab[max_row] = Ab[max_row], Ab[k]

        for i in range(k + 1, n):
            factor = Ab[i][column_order[k]] / Ab[k][column_order[k]]
            Ab[i][column_order[k]] = factor
            for j in range(k + 1, n + 1):
                if j < n:
                    Ab[i][column_order[j]] -= factor * Ab[k][column_order[j]]

        # Adding zero elements below the diagonal
        for i in range(k + 1, n):
            Ab[i][column_order[k]] = 0

    # Printing the extended matrix after the first stage of computations
    print("Extended matrix after the first stage of computations:")
    for row in Ab:
        print(row)

    # Solving the system of equations
    x = [0] * n
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += Ab[i][column_order[j]] * x[j]
        x[i] = (Ab[i][n] - s) / Ab[i][column_order[i]]

    # Swapping column_order[3] with column_order[4]
    column_order[3], column_order[4] = column_order[4], column_order[3]

    # Printing the solution
    print("Solution of the system of equations:")
    for i in range(n):
        print("x = {:.2f}".format(x[i]))

    print("Vector of column numbers:")
    print(column_order)


if __name__ == "__main__":
    solve_linear_equations("MN-6-1.txt")
    solve_linear_equations_crout("MN-6-2.txt")
