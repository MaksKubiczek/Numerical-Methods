from Jacobi import *

# Reading data
n, A, b = read_file('data.txt')

# Checking if matrix is weakly diagonally dominant
if not is_diagonally_dominant(n, A):
    print("The matrix is not diagonally weakly dominant ")

# Calculate matrix Lower-Upper and D^-1
LU, Dinv = decompose(n, A)

# Showing Results - LU matrix and D^1 matrix
print("L+U =")
for row in LU:
    print(row)
print("D^-1 =")
for row in Dinv:
    print(row)

# User input - max possibly number of iteration
max_iter = int(input("max number of iteration: "))

# Calling Jacobi method
x = jacobi(n, A, b, max_iter)

# Showing Results
print(f"\nNumber of iterations: {max_iter}")
print("Solution:")
for i in range(n):
    print(f"x[{i}] = {round(x[i], 4)}")

# Task 2
print("\n--Task nr 2--")


# Implementation of the stop condition in the form |x(i+1) - x(i)| < epsilon
def stop_condition(x, x_new, epsilon):
    for i in range(len(x)):
        if abs(x_new[i] - x[i]) >= epsilon:
            return False
    return True


# Task 1 (with slight modifications)
def jacobi_stop(n, A, b, epsilon, max_iter):
    x = [0.0] * n
    for iter in range(max_iter):
        x_new = [0.0] * n
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if stop_condition(x, x_new, epsilon):
            print(f"Warunek stopu został spełniony po {iter + 1} iteracjach.")
            return x_new
        x = x_new
    print(f"Maksymalna liczba iteracji ({max_iter}) została osiągnięta.")
    return x


# Reading input from file
n, A, b = read_file('data.txt')

# Checking if matrix is weakly diagonally dominant
if not is_diagonally_dominant(n, A):
    print("matrix is not weakly diagonally dominant")

# Calculate matrix Lower-Upper and D^-1
LU, Dinv = decompose(n, A)

# Calculate matrix Lower-Upper and D^-1
print("L+U =")
for row in LU:
    print(row)
print("D^-1 =")
for row in Dinv:
    print(row)

# User input - max possibly number of iteration
max_iter = int(input("Input max possibly iterations: "))

# Calculate solution for epsilon = 0.001
epsilon1 = 0.001
print(f"\nCalculations epsilon = {epsilon1}\n")
x1 = jacobi_stop(n, A, b, epsilon1, max_iter)

# Showing results
print(f"\nSolution for epsilon = {epsilon1}:")
for i in range(n):
    print(f"x[{i}] = {round(x1[i], 4)}")

# Calculate solution for epsilon  = 0.000001
epsilon2 = 0.000001
print(f"\nCalculations for epsilon = {epsilon2}\n")
x2 = jacobi_stop(n, A, b, epsilon2, max_iter)

# Showing results
print(f"\nSolution for epsilon = {epsilon2}:")
for i in range(n):
    print(f"x[{i}] = {round(x2[i], 4)}")
