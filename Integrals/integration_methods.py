import math

def calculate_dx(a, b, n):
    return (b - a) / n

def integration_rectangle(a, b, n, func):
    total = 0.0
    dx = calculate_dx(a, b, n)
    for i in range(0, n):
        total += func((a + (i * dx)))
    return dx * total

def integration_trapezoid(a, b, n, func):
    dx = (b - a) / n
    total = (func(a) + func(b)) / 2
    for i in range(1, n):
        x = a + i * dx
        total += func(x)
    return dx * total

def integration_Simpson(a, b, n, func):
    dx = (b - a) / n
    total = func(a) + func(b)
    subtotal_sum_1 = 0
    subtotal_sum_2 = 0

    for i in range(0, n, 2):
        x = a + i * dx
        subtotal_sum_1 += func(x)

    for i in range(1, n - 1, 2):
        x = a + i * dx
        subtotal_sum_2 += func(x)
    return dx * (total + 4 * subtotal_sum_1 + 2 * subtotal_sum_2) / 3
