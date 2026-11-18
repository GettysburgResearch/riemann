"""Compare three exact expressions for the rStation48 finite cost."""
from fractions import Fraction as Q
from math import comb


def moment_cost(m, b):
    rows = [
        [(1 - b ** (i + j + 1)) / (i + j + 1) for j in range(m)]
        + [-int(i == 0) + m * b ** (i + 1) / (i + 1)]
        for i in range(m)
    ]
    v = [row[-1] for row in rows]
    for i in range(m):
        pivot = rows[i][i]
        rows[i] = [entry / pivot for entry in rows[i]]
        for j in range(m):
            if j != i:
                multiplier = rows[j][i]
                rows[j] = [a - multiplier * b for a, b in zip(rows[j], rows[i])]
    return m * m * b + sum(a * row[-1] for a, row in zip(v, rows))


def legendre_cost(m, b):
    w = 1 / (1 - b)
    values = [m - 1 - m / w]
    for n in range(1, m):
        values.append(sum(
            (-1) ** (n - j) * comb(n, j) * comb(n + j, j)
            * (Q(m, j + 1) - 1) * w ** j
            for j in range(n + 1)
        ))
    return m * m * b + w * sum((2 * n + 1) * value ** 2 for n, value in enumerate(values))


def positive_coefficients(m):
    return [
        Q(m * (m - 1) * comb(m - 2, j) * comb(m + j, j), j + 1)
        for j in range(m - 1)
    ]


def polynomial_cost(m, b):
    s = b / (1 - b)
    coefficients = positive_coefficients(m)
    return m * m + sum(
        u * v * s ** (i + j + 1) / (i + j + 1)
        for i, u in enumerate(coefficients)
        for j, v in enumerate(coefficients)
    )


def main():
    samples = [Q(0), Q(1, 17), Q(1, 4), Q(1, 2), Q(7, 8), Q(99, 100)]
    for m in range(1, 13):
        values = [moment_cost(m, b) for b in samples]
        assert values == [legendre_cost(m, b) for b in samples]
        assert values == [polynomial_cost(m, b) for b in samples]
        if m == 1:
            assert all(v == 1 for v in values)
        elif m == 2:
            assert values == [4 / (1 - b) for b in samples]
        if m >= 2:
            assert all(u < v for u, v in zip(values, values[1:]))
            leading = positive_coefficients(m)[-1] ** 2 / (2 * m - 3)
            assert leading == 4 * (2 * m - 3) * comb(2 * m - 4, m - 2) ** 2
        print(f"m={m:2}  exact agreement on {len(samples)} points  c_m(1/4)={values[2]}")
    print("72 exact three-way comparisons passed")


if __name__ == "__main__":
    main()
