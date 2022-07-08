import math
import cmath


'''def main(a, m, p, b):
    sum1 = 0
    sum2 = 0

    for i in range(1, m+1):
        prv = 1
        for c in range(1, a+1):
            prv *= 29 * i - 2 * math.atan(31 * p ** 3 + 72 * c) ** 4
        sum1 += prv

    for k in range(1, b+1):
        for i in range(1, a+1):
            sum2 += 17 * (i ** 2 + 10 + 83 * k) ** 2 - k ** 3

    return sum1 - sum2


print('{0:.2e}'.format(main(2, 4, -0.98, 4)))'''


def main(m, b, y, n, a):
    res1 = 1
    res2 = 0
    sum1 = 0

    for k in range(1, b+1):
        sum1 = 0
        for i in range(1, m + 1):
            sum1 += y/85 + (k ** 2 - 95 * i - 1) ** 3 + 71
        res1 *= sum1

    for j in range(1, m+1):
        for k in range(1, a + 1):
            for c in range(1, n + 1):
                res2 += ((89 * k) ** 4) / 21 - 54 * math.cos(c ** 3) ** 3 - j ** 21 / 60

    return res1 - res2


print('{0:.2e}'.format(main(6, 2, -0.76, 5, 5)))
