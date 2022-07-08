import math
import cmath


def main(n):
    if n == 0:
        return -0.19
    if n >= 1:
        return main(n-1) ** 4 / 85 + main(n-1) ** 9 + \
               math.cos(main(n-1)) / 8


print('{0:.2e}'.format(main(4)))
