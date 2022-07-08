import math
import cmath


"""def main(x):
    sum1 = 0
    for i in range(1, len(x) + 1):
        sum1 += 68 * (math.log10(37 * x[math.ceil(i / 3 - 1)] ** 2 + 82)) ** 4
    return sum1 * 54


print('{0:.2e}'.format(main([-0.82, 0.59, 0.83, -0.39, 0.98, 0.48])))"""


def main(z, x, y):
    sum1 = 0

    for i in range(1, len(x) + 1):
        sum1 += 29 * math.tan(6 * y[math.ceil(i/3 - 1)] -
                              x[len(x)-i] ** 2 - z[math.ceil(i/2 - 1)] ** 3) ** 2

    return sum1 * 47


print('{0:.2e}'.format(main([0.95, 0.07, -0.34, -0.65],
                            [0.43, -0.43, -0.19, 0.06],
                            [-0.86, 0.43, 0.78, 0.26])))
