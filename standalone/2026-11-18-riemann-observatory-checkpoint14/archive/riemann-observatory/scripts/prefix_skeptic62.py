"""Cross-check the fixed-prefix constant by independent rational calculations."""

from fractions import Fraction
from math import comb


def moment_constant(m, b):
    matrix = [
        [(1 - b ** (i + j + 1)) / (i + j + 1) for j in range(m)]
        for i in range(m)
    ]
    vector = [-int(j == 0) + m * b ** (j + 1) / (j + 1) for j in range(m)]
    augmented = [row + [entry] for row, entry in zip(matrix, vector)]
    for j in range(m):
        pivot = augmented[j][j]
        augmented[j] = [value / pivot for value in augmented[j]]
        for i in range(j + 1, m):
            scale = augmented[i][j]
            augmented[i] = [
                left - scale * right
                for left, right in zip(augmented[i], augmented[j])
            ]
    solution = [Fraction(0)] * m
    for i in reversed(range(m)):
        solution[i] = augmented[i][-1] - sum(
            augmented[i][j] * solution[j] for j in range(i + 1, m)
        )
    return m * m * b + sum(v * x for v, x in zip(vector, solution))


def legendre_integral_constant(m, b):
    z = 2 * b / (1 - b)
    n = m - 1
    derivative = [
        Fraction(j * comb(n, j) * comb(n + j, j), 2**j)
        for j in range(1, n + 1)
    ]
    return m * m + 2 * sum(
        left * right * z ** (i + j + 1) / (i + j + 1)
        for i, left in enumerate(derivative)
        for j, right in enumerate(derivative)
    )


def main():
    prefixes = tuple(map(Fraction, ("0", "1/100", "1/7", "1/2", "7/9", "99/100")))
    for m in range(1, 13):
        previous = Fraction(m * m)
        for b in prefixes:
            c = moment_constant(m, b)
            assert c == legendre_integral_constant(m, b), (m, b, c)
            if m == 1:
                assert c == 1
            elif b > 0:
                assert c > previous
            if m == 2:
                assert c == 4 / (1 - b)
            if m == 3:
                assert c == 3 * (b**3 + 9 * b**2 + 3 * b + 3) / (1 - b) ** 3
            previous = c

    assert moment_constant(3, Fraction(1, 2)) == 165
    print("72 exact rational comparisons passed for m=1,...,12.")
    print("c_3(1/2)=165, exceeding proposed values 18 and 72.")


if __name__ == "__main__":
    main()
