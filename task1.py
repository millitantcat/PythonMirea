import math
import cmath


def main(y, z):
    return (61 * y + (49 * z ** 3 - 80) ** 5) / \
           (z ** 5 + 81 * y ** 3) - \
           math.sqrt((80 * math.exp(y) ** 5 - z) /
                     (y ** 2 - (z ** 2 + 40 * z ** 3 + z / 74) ** 6))


print('{0:.2e}'.format(main(-0.71, 0.08)))
