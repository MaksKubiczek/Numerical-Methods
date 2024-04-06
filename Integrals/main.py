from integration_methods import *
from functions import *
from plot_functions import *

def print_info(a, b, n, func):
    print("Integration interval: from", a, "to", b)
    print("Number of intervals:", n)
    print("Result using rectangle method:", integration_rectangle(a, b, n, func))
    print("Result using trapezoid method:", integration_trapezoid(a, b, n, func))
    print("Result using Simpson's method:", integration_Simpson(a, b, n, func))

def main():
    print("\n\nSin function")
    print_info(0.5, 2.5, 4, func_1)
    plot_convergence("sin", func_1, 0.5, 2.5)

    print("\n\nQuadratic function - x^2+2x+5")
    print_info(0.5, 5, 4, func_2)
    plot_convergence("quadratic", func_2, 0.5, 5)

    print("\n\nExponential function exp(x)")
    print_info(0.5, 5, 4, func_3)
    plot_convergence("exponential", func_3, 0.5, 5)

if __name__ == "__main__":
    main()
