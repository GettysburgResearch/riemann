"""Numerical controls for contour signs and the complex-character Mellin factor."""

import mpmath as mp

mp.mp.dps = 45
critical = mp.mpf("0.5")
ell = mp.mpf("2.3")
poles = [
    (critical, 2, mp.mpc(1, 2)),
    (critical + mp.j * mp.mpf("0.72"), 1, mp.mpc(-1, 1)),
    (critical - mp.j * mp.mpf("1.27"), 1, mp.mpc(2, -3)),
]
heights = list(map(mp.mpf, ("-1.75", "-0.90", "-0.19", "0.31", "0.53", "1.02")))


def reciprocal(z):
    return 1 + sum(coefficient / (z - rho) ** order for rho, order, coefficient in poles)


def integrate_edge(integrand, start, end):
    return (end - start) * mp.quad(lambda v: integrand(start + (end - start) * v), [0, 1])


def corners(low, high):
    left = mp.mpf("0.34")
    right = mp.mpf("0.65")
    return [left + low * mp.j, right + low * mp.j, right + high * mp.j, left + high * mp.j]


def contour_integral(integrand, low, high):
    vertices = corners(low, high)
    return sum(
        integrate_edge(integrand, start, end)
        for start, end in zip(vertices, vertices[1:] + vertices[:1])
    )


def check_complete_cells():
    for ordinate in map(mp.mpf, ("-1.31", "-0.36", "0.09", "0.42", "0.80", "1.44")):
        s = critical + mp.j * ordinate
        U = 1 / reciprocal(s)

        def integrand(z):
            return reciprocal(z) * mp.expm1(ell * (z - s)) / (z - s) ** 2

        split = 0
        expected_sum = 0
        for low, high in zip(heights, heights[1:]):
            expected = 0
            for rho, order, coefficient in poles:
                if low < rho.imag < high:
                    r = coefficient / (s - rho) ** order
                    tapered = coefficient * mp.quad(
                        lambda x: x ** (order - 1)
                        * (1 - x / ell)
                        * mp.exp((rho - s) * x)
                        / mp.factorial(order - 1),
                        [0, ell],
                    )
                    expected += U * (r - tapered)
            observed = int(low < ordinate < high) - U * contour_integral(
                integrand, low, high
            ) / (2j * mp.pi * ell)
            assert abs(observed - expected) < mp.mpf("1e-37"), (s, low, observed, expected)
            split += observed
            expected_sum += expected

        telescoped = int(heights[0] < ordinate < heights[-1]) - U * contour_integral(
            integrand, heights[0], heights[-1]
        ) / (2j * mp.pi * ell)
        assert abs(split - telescoped) < mp.mpf("1e-37")
        assert abs(expected_sum - telescoped) < mp.mpf("1e-37")
    print("30 complete-cell checks and 6 asymmetric telescoping checks passed")


def check_character_mellin():
    character = (0, 1, mp.j, -mp.j, -1)
    upper = 2500
    alpha = mp.mpf(1) / 7
    for s in (
        critical + mp.j * mp.mpf("1.23"),
        critical - mp.j * mp.mpf("1.23"),
        critical,
    ):
        direct = mp.fsum(
            -sum(character[1:n % 5 + 1])
            * ((alpha / n) ** s - (alpha / (n + 1)) ** s) / s
            for n in range(1, upper)
        )
        lvalue = 5 ** (-s) * mp.fsum(
            character[a] * mp.zeta(s, mp.mpf(a) / 5) for a in range(1, 5)
        )
        expected = -(alpha ** s) * lvalue / s
        tail_bound = 2 * (alpha / upper) ** s.real / s.real
        assert abs(direct - expected) <= tail_bound
    print("3 complex-character Mellin controls passed with explicit truncation bounds")


if __name__ == "__main__":
    check_complete_cells()
    check_character_mellin()
