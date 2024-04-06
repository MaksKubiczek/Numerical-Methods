def f(x):
    return -x ** 3 + 10 * x + 5


def f_derivative(x):
    return -3 * x ** 2 + 10


def secant_method(f, x_minus1, x0, iterations):
    print("Secant Method:")
    print("f(x) =", f.__name__)

    x_minus1_value = f(x_minus1)
    x0_value = f(x0)

    print("Iteration 0: x =", x_minus1, "f(x) =", x_minus1_value)
    print("Iteration 1: x =", x0, "f(x) =", x0_value)

    for i in range(2, iterations + 1):
        x_next = x0 - (f(x0) * (x0 - x_minus1)) / (f(x0) - f(x_minus1))
        x_next_value = f(x_next)
        print("Iteration", i, ": x =", x_next, "f(x) =", x_next_value)

        x_minus1 = x0
        x0 = x_next


def newton_method(f, f_derivative, x0, iterations):
    print("Newton's Method:")
    print("f(x) =", f.__name__)

    x = x0
    print("Iteration 0: x =", x, "f(x) =", f(x))

    for i in range(1, iterations + 1):
        x -= f(x) / f_derivative(x)
        print("Iteration", i, ": x =", x, "f(x) =", f(x))


# Input data
x0 = float(input("Enter the initial point x0: "))
iterations = int(input("Enter the number of iterations: "))
x_minus1 = x0 - 0.1

# Secant Method
secant_method(f, x_minus1, x0, iterations)

# Newton's Method
newton_method(f, f_derivative, x0, iterations)
