from equations import diff_eq1, diff_eq2
from numerical_methods import euler_method, rk2_method, rk4_method

# Input data
x0 = 0
y0 = 0.1
x = 1
N = 10

# Equation 1
print("Equation 1:")
print("Initial condition:", f"y({x0}) =", y0)
print("End point:", f"x =", x)
print("Step size:", f"N =", N)

y_euler = euler_method(diff_eq1, x0, y0, x, N)
print("Solution using Euler's method at the end point:", f"y({x}) =", y_euler)

y_rk2 = rk2_method(diff_eq1, x0, y0, x, N)
print("Solution using RK2 method at the end point:", f"y({x}) =", y_rk2)

y_rk4 = rk4_method(diff_eq1, x0, y0, x, N)
print("Solution using RK4 method at the end point:", f"y({x}) =", y_rk4)

# Equation 2
print("\nEquation 2:")
print("Initial condition:", f"y({x0}) =", y0)
print("End point:", f"x =", x)
print("Step size:", f"N =", N)

y_euler = euler_method(diff_eq2, x0, y0, x, N)
print("Solution using Euler's method at the end point:", f"y({x}) =", y_euler)

y_rk2 = rk2_method(diff_eq2, x0, y0, x, N)
print("Solution using RK2 method at the end point:", f"y({x}) =", y_rk2)

y_rk4 = rk4_method(diff_eq2, x0, y0, x, N)
print("Solution using RK4 method at the end point:", f"y({x}) =", y_rk4)
