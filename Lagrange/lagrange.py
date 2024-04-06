import math

def lagrange_interpolation_with_file(filename, x):

    data = []       # creating a list to store information about nodes
    with open(filename, "r") as file:
        for line in file:
            x_i, y_i = map(float, line.split())     # splitting each line into node and its assigned value
            data.append((x_i, y_i))         # adding values to the list

    n = len(data)

    L = 0.0
    for i in range(n):

        number_up = 1.0     # assigning initial value to the numerator product
        number_down = 1.0   # assigning initial value to the denominator product
        for j in range(n):
            if j != i:
                number_up *= x - data[j][0]  # x - x_j
                number_down *= data[i][0] - data[j][0]  # x_i - x_j

        L += data[i][1] * number_up / number_down

    # Displaying the result as instructed:
    """
    c) The program outputs:
• Number of nodes
• Data: interpolation nodes and function values at the nodes
• The point at which we calculate the value of the polynomial
• The value of the Lagrange polynomial at that point
    
    """
    print("Number of interpolation nodes:", n)
    print("\nData:")
    for i in range(n):
        print("{:.6f} {:.6f}".format(data[i][0], data[i][1]))
    print("\nThe point at which we calculate the value of the polynomial:", x)
    print("\nThe value of the Lagrange interpolation polynomial at point", x, "is:", L)

    return L


def lagrange_interpolation(x, x_values, y_values):

    n = len(x_values)
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result


def main():
    lagrange_interpolation_with_file("data.txt", -1)
    lagrange_interpolation_with_file("data.txt", 0.5)

    x = 50
    x_values = [27, 64, 125, 216]
    y_values = [math.pow(x, 1/3) for x in x_values]
    result = lagrange_interpolation(x, x_values, y_values)
    print(f"\nThe cubic root of 50 is approximately {result:.4f}.\n")


if __name__ == "__main__":
    main()
