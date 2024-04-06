import numpy as np
import math

points = np.genfromtxt("input_points.txt", delimiter=" ", usemask=True)


def newton(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def poly(x, n):
    if n == 0:
        return 1
    result = 1
    for j in range(n):
        result *= (x - j)
    return result


def F(k, n, q):
    if q == 0:
        return 1
    SUM = 0
    for s in range(k + 1):
        SUM += math.pow((-1), s) * newton(k, s) * newton((k + s), s) * (poly(q, s) / poly(n, s))
    return SUM


def gram_calculate(m, points, x):
    ym = 0
    q = (x - points[0][0]) / (abs(points[1][0] - points[0][0]))
    n = len(points) - 1

    ck = 0
    n = len(points) - 1
    if m <= n:
        ym = 0
        for k in range(m + 1):
            ck = 0
            sk = 0
            for i in range(n + 1):
                ck += math.pow(F(k, n, i), 2)
                sk += points[i][1] * F(k, n, i)
            ym += (sk / ck) * F(k, n, q)
    return ym


def ck_sk(m, points, x):
    ym = 0
    q = (x - points[0][0]) / (abs(points[1][0] - points[0][0]))
    n = len(points) - 1

    ck = 0
    n = len(points) - 1
    if m <= n:
        ym = 0
        for k in range(m + 1):
            ck = 0
            sk = 0
            for i in range(n + 1):
                ck += math.pow(F(k, n, i), 2)
                sk += points[i][1] * F(k, n, i)
            ym += (sk / ck) * F(k, n, q)
            print("ck: ", round(ck, 5), "\tsk:", round(sk, 5))


print("Number of nodes: ", len(points))
print("\nCoefficients ck, sk:")
ck_sk(2, points, 0)
print()
for p in points:
    print("x = ", p[0], "   y = ", p[1], "\t==>\t", "x = ", p[0], "   Ym(x) = ", gram_calculate(2, points, p[0]))
print()
print("x = 2.5 ", "  y:", "Unknown", "\t==>\t", "x = 2.5", "   Ym(x) = ", gram_calculate(2, points, 2.5))
print("x = 6.5 ", "  y:", "Unknown", "\t==>\t", "x = 6.5", "   Ym(x) = ", gram_calculate(2, points, 6.5))
