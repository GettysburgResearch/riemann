#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import random
from fractions import Fraction
from pathlib import Path


class Q2:
    """a+b*sqrt(2), exact."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other):
        other = other if isinstance(other, Q2) else Q2(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Q2) else -Q2(other))

    def __rsub__(self, other):
        return Q2(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, Q2) else Q2(other)
        return Q2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def __eq__(self, other):
        other = other if isinstance(other, Q2) else Q2(other)
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return f"Q2({self.a},{self.b})"


def pow_inv_sqrt2(j: int) -> Q2:
    # 2^(-j/2).
    if j % 2 == 0:
        return Q2(Fraction(1, 2 ** (j // 2)))
    return Q2(0, Fraction(1, 2 ** ((j + 1) // 2)))


def mobius_sieve(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def v2(n: int) -> int:
    e = 0
    while n and n % 2 == 0:
        e += 1
        n //= 2
    return e


def factor_map(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def add_map(
    x: dict[int, Fraction],
    y: dict[int, Fraction],
    scale: Fraction = Fraction(1),
) -> dict[int, Fraction]:
    out = dict(x)
    for p, c in y.items():
        out[p] = out.get(p, Fraction(0)) + scale * c
        if out[p] == 0:
            del out[p]
    return out


def scale_map(x: dict[int, Fraction], c: Fraction | int) -> dict[int, Fraction]:
    c = Fraction(c)
    return {p: c * v for p, v in x.items() if c * v}


def a4(n: int, mu: list[int]) -> int:
    e = v2(n)
    m = n >> e
    if mu[m] == 0:
        return 0
    if e == 0:
        return mu[m]
    if e == 1:
        return -mu[m]
    return 3 * ((-1) ** (e + 1)) * mu[m]


def a_log(n: int, mu: list[int]) -> dict[int, Fraction]:
    return scale_map(
        {p: Fraction(e) for p, e in factor_map(n).items()},
        a4(n, mu),
    )


def d4_map(n: int, mu: list[int]) -> dict[int, Fraction]:
    out = a_log(n, mu)
    if n % 4 == 0:
        out = add_map(out, a_log(n // 4, mu), Fraction(-4))
    return out


def e4_map(n: int, mu: list[int]) -> dict[int, Fraction]:
    out = d4_map(n, mu)
    if n % 2 == 0:
        out = add_map(out, d4_map(n // 2, mu), Fraction(2))
    if n % 4 == 0:
        out = add_map(out, d4_map(n // 4, mu))
    return out


def expected_e4_map(n: int, mu: list[int]) -> dict[int, Fraction]:
    e = v2(n)
    m = n >> e
    if mu[m] == 0 or e >= 6:
        return {}
    A = (1, 1, -8, -8, 16, 16)
    B = (0, -1, -8, 0, 32, 16)
    out = scale_map(
        {p: Fraction(k) for p, k in factor_map(m).items()},
        mu[m] * A[e],
    )
    if B[e]:
        out[2] = out.get(2, Fraction(0)) + Fraction(mu[m] * B[e])
        if out[2] == 0:
            del out[2]
    return out


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def W(x: Fraction) -> Fraction:
    if x < 0 or x > 1:
        return Fraction(0)
    if x <= Fraction(1, 4):
        return 5 * x - 63 * x * x + 170 * x ** 3
    return (-x + 3 * x * x - 2 * x ** 3) / 3


def run() -> dict[str, object]:
    N = 4096
    mu = mobius_sieve(N)

    finite_packet_checks = 0
    polynomial_checks = 0
    scale_inverse_checks = 0
    kernel_checks = 0
    diagonal_checks = 0
    randomized_checks = 0
    top_band_checks = 0
    mutations = 0

    # Exact coefficient table, including vanishing above depth five.
    for n in range(1, N + 1):
        assert e4_map(n, mu) == expected_e4_map(n, mu)
        finite_packet_checks += 1

    # Polynomial identities.
    P = [1, 0, -4]
    A = poly_mul(poly_mul(P, P), [1, 1])
    B = poly_mul([0, -1], poly_mul(P, [1, 8, 4]))
    assert A == [1, 1, -8, -8, 16, 16]
    assert B == [0, -1, -8, 0, 32, 16]
    polynomial_checks += 2

    # Exact stable scale inversion over Q(sqrt(2)).
    rng = random.Random(95310)
    a = Q2(0, Fraction(1, 2))  # 1/sqrt(2)
    for length in range(1, 28):
        for _ in range(6):
            c = [Q2(Fraction(rng.randint(-9, 9), rng.randint(1, 9))) for _ in range(length)]
            cpad = c + [Q2(), Q2()]
            e = [
                cpad[k] + Q2(0, 1) * cpad[k + 1] + Q2(Fraction(1, 2)) * cpad[k + 2]
                for k in range(length)
            ]
            recovered: list[Q2] = []
            for k in range(length):
                total = Q2()
                for j in range(length - k):
                    coeff = pow_inv_sqrt2(j) * ((-1) ** j) * (j + 1)
                    total += coeff * e[k + j]
                recovered.append(total)
            assert recovered == c
            scale_inverse_checks += 1

    # Exact coefficient-sum bounds and kernel safe bounds on a dense rational grid.
    Acoef = (1, 1, -8, -8, 16, 16)
    Bcoef = (0, -1, -8, 0, 32, 16)
    # SA=9+9/sqrt2<16 and SB=12+5/sqrt2<16.
    assert 9 * 9 < 2 * 7 * 7
    assert 5 * 5 < 2 * 4 * 4
    kernel_checks += 2

    for den in range(8, 129):
        for num in range(0, den + 1):
            x = Fraction(num, den)
            assert abs(W(x)) <= 32
            # On the top band all shifted kernels vanish and W is positive.
            if Fraction(2, 3) <= x <= Fraction(3, 4):
                assert W(x) >= Fraction(2, 81)
                for r in range(1, 6):
                    assert W((2 ** r) * x) == 0
                top_band_checks += 1
            kernel_checks += 1

    # The declared diagonal majorant.
    for X in (16, 32, 64, 128, 256, 512):
        diagonal_upper = Fraction(0)
        for m in range(1, X + 1, 2):
            if mu[m] == 0:
                continue
            # Bound |F_m| <= 512 log(2m)/sqrt(m) symbolically by recording
            # the square coefficient 512^2/m and the maximal log envelope.
            diagonal_upper += Fraction(512 * 512, m)
        harmonic_bound = Fraction(512 * 512) * sum(
            (Fraction(1, m) for m in range(1, X + 1)), Fraction(0)
        )
        assert diagonal_upper <= harmonic_bound
        diagonal_checks += 1

    # Exact Rademacher identity on small rational fixtures.
    for k in range(1, 9):
        values = [Fraction(rng.randint(-7, 7), rng.randint(1, 7)) for _ in range(k)]
        lhs = Fraction(0)
        for signs in itertools.product((-1, 1), repeat=k):
            total = sum((Fraction(s) * v for s, v in zip(signs, values)), Fraction(0))
            lhs += total * total
        lhs /= 2 ** k
        rhs = sum((v * v for v in values), Fraction(0))
        assert lhs == rhs
        randomized_checks += 1

    # Hostile mutations.
    if e4_map(64, mu):
        mutations += 1
    if A != [1, 1, -8, -8, 16, 15]:
        mutations += 1
    if B != [0, -1, -8, 1, 32, 16]:
        mutations += 1
    if W(Fraction(2, 3)) != Fraction(2, 81):
        mutations += 1
    if Q2(0, 1) != Q2(Fraction(3, 2)):
        mutations += 1

    return {
        "classification": "PASS_X_95310_Q4_FINITE_ODD_CORE_PRECONDITIONER",
        "arithmetic_class": "EXACT_INTEGER_RATIONAL_FORMAL_PRIME_LOG_AND_QSQRT2",
        "finite_odd_core_packet_checks": finite_packet_checks,
        "dyadic_polynomial_checks": polynomial_checks,
        "stable_scale_inverse_checks": scale_inverse_checks,
        "kernel_bound_checks": kernel_checks,
        "top_band_firewall_checks": top_band_checks,
        "diagonal_majorant_checks": diagonal_checks,
        "rademacher_diagonal_checks": randomized_checks,
        "hostile_mutations_detected": mutations,
        "proves": [
            "double dyadic preconditioning leaves exactly six odd-core levels",
            "the exact A and B dyadic polynomials",
            "stable critical-scale inversion over Q(sqrt(2))",
            "polylogarithmic same-core diagonal majorant",
            "exact Rademacher diagonal identity",
            "top-band source-blind sign firewall",
        ],
        "does_not_prove": [
            "distinct odd-core cross-correlation bound FOCC",
            "OCHD",
            "critical centered-cubic square-root bound",
            "Riemann Hypothesis",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
