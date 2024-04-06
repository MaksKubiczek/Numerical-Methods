import matplotlib.pyplot as plt
from integration_methods import integration_rectangle, integration_trapezoid, integration_Simpson


def plot_convergence(func_name, func, a, b):
    xs = []
    ys_rect = []
    ys_trap = []
    ys_simp = []
    for n in range(4, 130, 2):
        xs.append(n)
        ys_rect.append(integration_rectangle(a, b, n, func))
        ys_trap.append(integration_trapezoid(a, b, n, func))
        ys_simp.append(integration_Simpson(a, b, n, func))
    fig, ax = plt.subplots()
    ax.plot(xs, ys_rect, label="Rectangle method")
    ax.plot(xs, ys_trap, label="Trapezoid method")
    ax.plot(xs, ys_simp, label="Simpson's method")
    ax.set_xlabel("Number of intervals")
    ax.set_ylabel("Integration value")
    ax.set_title(f"Convergence plot of integration methods for {func_name} function")
    ax.legend()
    plt.savefig(f"{func_name}_convergence.png")
