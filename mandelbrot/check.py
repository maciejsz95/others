"""

"""
from math import floor, exp
import numpy as np
from matplotlib import pyplot as plt

def checkC(z_0, C, it_max):
    for i in range(it_max):
        z_1 = z_0 ** 2 + C
        if abs(z_1) >= 2:
            break
        z_0 = z_1
    return i

def funkcja_mal():
    # Zbiór Mandelbrota
    # Zakres układu współrzędnych
    x_min = -2.5
    x_max = 1.5
    y_max = 1.25
    y_min = -1.25

    iterations = 50

    m = int(input('podaj szerokość:\n'))
    n = floor(m * (y_max - y_min) / (x_max - x_min))
    unit = (x_max - x_min) / m
    Mal = np.zeros((n, m, 3))

    C_0 = x_min + 1j*y_max
    C = C_0

    w1 = 50
    w2 = 50
    w3 = 50

    p1 = 2.2
    p2 = 2.2
    p3 = 2.2

    c1 = 1 / 4
    c2 = 1 / 2
    c3 = 3 / 4

    # f1 = @(x) exp(-w1 * abs(x - c1). ^ p1)
    # f1 = lambda x: exp(-w1 * abs(x - c1). ^ p1)
    # f2 = @(x) exp(-w2 * abs(x - c2). ^ p2)
    # f3 = @(x) exp(-w3 * abs(x - c3). ^ p3)

    for i in range(n):
        C = C - C.real + C_0.real
        for j in range(m):
            x = checkC(0, C, iterations) / iterations
            Mal[i, j, 0] = (exp(-w1 * abs(x - c1)** p1))
            Mal[i, j, 1] = (exp(-w2 * abs(x - c2)** p2))
            Mal[i, j, 2] = (exp(-w3 * abs(x - c3)** p3))
            # Mal[i, j, :] = x
            C = C + unit
        C = C - 1j*unit

    plt.imshow(Mal)
    plt.show()


if __name__ == "__main__":
    funkcja_mal()