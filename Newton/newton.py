# Function to compute the value of the Newton polynomial
def newton_interpolation(x, nodes, values):
    n = len(nodes)
    b = values.copy()
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            b[j] = (b[j] - b[j-1]) / (nodes[j] - nodes[j-i])
    y = b[n-1]
    for i in range(n-2, -1, -1):
        y = b[i] + (x - nodes[i]) * y
    return y, b

# Function to read data from a text file
def read_data(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        nodes = [0] * n
        values = [0] * n
        for i in range(n):
            line = file.readline().split()
            nodes[i] = float(line[0])
            values[i] = float(line[1])
    return n, nodes, values 