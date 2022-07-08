import math
import cmath


def main(x):
    if x < 121:
        return 1 + 47 * math.cos(1 + x / 12 + 37 * x ** 3) ** 4 \
               + 93 * x ** 5
    if (x >= 121) & (x < 200):
        return 92 * (x / 25 - x ** 2 - 93) ** 2 + \
               88 * math.tan(x) ** 5 + 68 * (6 * x ** 3 + 19 + x) ** 4
    if x >= 200:
        return (math.cos(96 * x ** 3) ** 5) / 89


print('{0:.2e}'.format(main(193)))
