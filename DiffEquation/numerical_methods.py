def euler_method(diff_eq, x0, y0, x, N):
    h = (x - x0) / N
    xi = x0
    yi = y0

    for _ in range(N):
        yi += h * diff_eq(xi, yi)
        xi += h

    return yi

def rk2_method(diff_eq, x0, y0, x, N):
    h = (x - x0) / N
    xi = x0
    yi = y0

    for _ in range(N):
        k1 = h * diff_eq(xi, yi)
        k2 = h * diff_eq(xi + h/2, yi + k1/2)
        yi += k2
        xi += h

    return yi

def rk4_method(diff_eq, x0, y0, x, N):
    h = (x - x0) / N
    xi = x0
    yi = y0

    for _ in range(N):
        k1 = h * diff_eq(xi, yi)
        k2 = h * diff_eq(xi + h/2, yi + k1/2)
        k3 = h * diff_eq(xi + h/2, yi + k2/2)
        k4 = h * diff_eq(xi + h, yi + k3)
        yi += (k1 + 2*k2 + 2*k3 + k4) / 6
        xi += h

    return yi
