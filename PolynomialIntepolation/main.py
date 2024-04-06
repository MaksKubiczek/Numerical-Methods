# Given interpolation nodes and values at nodes
xi = [1, 2, 3, 4, 5, 6, 7, 8]
fi = [2, 4, 3, 5, 6, 9, 11, 11]

# Degree of the approximating polynomial
n = 1

# Weighting function
wi = [1] * len(xi)

# Calculation of the G matrix
G = []
for i in range(n+1):
    row = []
    for j in range(n+1):
        val = 0
        for k in range(len(xi)):
            val += wi[k] * (xi[k] ** i) * (xi[k] ** j)
        row.append(val)
    G.append(row)

# Calculation of the F vector
F = []
for i in range(n+1):
    val = 0
    for k in range(len(xi)):
        val += wi[k] * (xi[k] ** i) * fi[k]
    F.append(val)

# Solving the system of equations using Gauss method
for i in range(n+1):
    div = G[i][i]
    G[i] = [x / div for x in G[i]]
    F[i] /= div
    for j in range(i+1, n+1):
        mult = G[j][i]
        G[j] = [G[j][k] - mult * G[i][k] for k in range(n+1)]
        F[j] -= mult * F[i]

for i in range(n, -1, -1):
    for j in range(i-1, -1, -1):
        mult = G[j][i]
        G[j] = [G[j][k] - mult * G[i][k] for k in range(n+1)]
        F[j] -= mult * F[i]

# Displaying the results
print("Number of nodes:", len(xi))
print("Coefficients of the approximating polynomial:", F)
print("Interpolation nodes and values at nodes:")
for i in range(len(xi)):
    print(xi[i], fi[i], sum([F[j] * (xi[i] ** j) for j in range(n+1)]))
