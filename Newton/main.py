from newton import newton_interpolation, read_data

# Function to display results
def print_results(n, nodes, values, x, y, b):
    print("Number of nodes: ", n)
    print("Interpolation nodes and function values at nodes:")
    for i in range(n):
        print(nodes[i], "\t", values[i])
    print("Point at which the polynomial value is calculated: ", x)
    print("Value of the Newton polynomial at the given point: ", y)
    print("Coefficients of the Newton polynomial:")
    for i in range(n):
        print("b", i, " = ", b[i])

# Main function
def main():
    # Read data from text file
    n, nodes, values = read_data("data1.txt")

    # Compute the value of the polynomial at a selected point
    x = float(input("Enter the point at which you want to calculate the polynomial value: "))
    y, b = newton_interpolation(x, nodes, values)

    # Display results
    print_results(n, nodes, values, x, y, b)

    # Compute the value of the polynomial for selected points
    x1 = 2.5
    y1, _ = newton_interpolation(x1, nodes, values)
    print("Value of the Newton polynomial for x = 2.5: ", y1)

    x2 = 3.5
    y2, _ = newton_interpolation(x2, nodes, values)
    print("Value of the Newton polynomial for x = 3.5: ", y2)

    # Read data from another text file
    na, nodesa, valuesa = read_data("data2.txt")

    # Compute the value of the second polynomial at a selected point
    xa = float(input("Enter the point at which you want to calculate the polynomial value: "))
    ya, ba = newton_interpolation(xa, nodesa, valuesa)

    # Display results for the second polynomial
    print_results(na, nodesa, valuesa, xa, ya, ba)

    # Compute the value of the second polynomial for selected points
    x3 = -1
    y3, _ = newton_interpolation(x3, nodesa, valuesa)
    print("Value of the Newton polynomial for x = -1: ", y3)

    x4 = 2
    y4, _ = newton_interpolation(x4, nodesa, valuesa)
    print("Value of the Newton polynomial for x = 2: ", y4)

if __name__ == "__main__":
    main()
    