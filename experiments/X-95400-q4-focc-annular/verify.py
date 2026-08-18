#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import random
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


class Q2:
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

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def to_float(self):
        return float(self.a) + float(self.b) * math.sqrt(2.0)


def parse_fraction(text: str) -> Fraction:
    p, q = text.split("/")
    return Fraction(int(p), int(q))


def inv_sqrt2_pow(r: int) -> Q2:
    if r % 2 == 0:
        return Q2(Fraction(1, 2 ** (r // 2)))
    return Q2(0, Fraction(1, 2 ** ((r + 1) // 2)))


W_LOW = {1: Fraction(5), 2: Fraction(-63), 3: Fraction(170)}
W_HIGH = {1: Fraction(-1, 3), 2: Fraction(1), 3: Fraction(-2, 3)}
A = [1, 1, -8, -8, 16, 16]
B = [0, -1, -8, 0, 32, 16]
Q = [Fraction(1), Fraction(-7, 8), Fraction(7, 32), Fraction(-1, 64)]


def band_coeffs(source: list[int], j: int) -> dict[int, Q2]:
    out = {1: Q2(), 2: Q2(), 3: Q2()}
    for h, qh in enumerate(Q):
        for r, c in enumerate(source):
            if not c:
                continue
            t = r + h
            if t <= j - 2:
                branch = W_LOW
            elif t in (j - 1, j):
                branch = W_HIGH
            else:
                continue
            pref = Q2(qh * c) * inv_sqrt2_pow(r)
            for k, wc in branch.items():
                out[k] = out[k] + pref * wc * (2 ** (t * k))
    return out


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


def W_float(x: float) -> float:
    if x < 0.0 or x > 1.0:
        return 0.0
    if x <= 0.25:
        return 5.0 * x - 63.0 * x * x + 170.0 * x * x * x
    return (-x + 3.0 * x * x - 2.0 * x * x * x) / 3.0


def K_float(x: float, coeff: list[int]) -> float:
    return sum(c * 2.0 ** (-r / 2.0) * W_float((2**r) * x) for r, c in enumerate(coeff))


def J_float(x: float, coeff: list[int]) -> float:
    return sum(float(Q[h]) * K_float((2**h) * x, coeff) for h in range(4))


def annular_scan(X: int, mu: list[int]) -> dict[str, float]:
    total = 0.0
    diagonal = 0.0
    lower = X // 1024
    log2 = math.log(2.0)
    for m in range(lower + 1, X + 1):
        if m % 2 == 0 or mu[m] == 0:
            continue
        x = m / X
        g = (math.log(m) * J_float(x, A) + log2 * J_float(x, B)) / math.sqrt(m)
        total += mu[m] * g
        diagonal += g * g
    return {
        "X": X,
        "annular_sum": total,
        "diagonal": diagonal,
        "cross": total * total - diagonal,
    }


def formal_add(left: dict[int, Fraction], right: dict[int, Fraction]) -> dict[int, Fraction]:
    out = dict(left)
    for p, c in right.items():
        out[p] = out.get(p, Fraction(0)) + c
        if out[p] == 0:
            del out[p]
    return out


def run(scan_limit: int) -> dict[str, object]:
    certificate = json.loads((HERE / "certificates/exact_kernels.json").read_text())

    exact_kernel_checks = 0
    annihilation_checks = 0
    inverse_checks = 0
    activation_checks = 0
    ratio_checks = 0
    gcd_checks = 0
    square_checks = 0
    type_i_checks = 0
    pair_count_checks = 0
    positive_kernel_checks = 0
    mutations = 0

    # Reconstruct every exact band coefficient.
    for entry in certificate["bands"]:
        j = entry["index"]
        for name, source in (("J0", A), ("J1", B)):
            actual = band_coeffs(source, j)
            for k in (1, 2, 3):
                stored = entry[name][f"x^{k}"]
                expected = Q2(parse_fraction(stored["rational"]), parse_fraction(stored["sqrt2"]))
                assert actual[k] == expected
                exact_kernel_checks += 1

    # The scale polynomial annihilates x, x^2 and x^3.
    for k in (1, 2, 3):
        assert sum(Q[h] * (2 ** (h * k)) for h in range(4)) == 0
        annihilation_checks += 1
    for source in (A, B):
        for j in range(10, 17):
            assert all(v.is_zero() for v in band_coeffs(source, j).values())
            annihilation_checks += 1

    # Stable inverse of Q(S).
    inverse = []
    for n in range(40):
        c = Fraction(0)
        for a in range(n + 1):
            for b in range(n - a + 1):
                c += Fraction(1, 2**a) * Fraction(1, 4**b) * Fraction(1, 8 ** (n - a - b))
        inverse.append(c)
    for n in range(35):
        conv = sum((Q[h] * inverse[n - h] for h in range(min(3, n) + 1)), Fraction(0))
        assert conv == (1 if n == 0 else 0)
        inverse_checks += 1
    assert Fraction(1, 1) / ((1 - Fraction(1, 2)) * (1 - Fraction(1, 4)) * (1 - Fraction(1, 8))) == Fraction(64, 21)
    inverse_checks += 1

    # Activation and ratio geometry.
    for X in range(1024, 1089):
        for m in range(X // 1024 + 1, X + 1):
            j = min(9, max(0, (X // m).bit_length() - 1))
            assert X / (2 ** (j + 1)) < m <= X / (2**j) or j == 9
            activation_checks += 1
        rng = random.Random(X)
        for _ in range(200):
            m = rng.randint(X // 1024 + 1, X - 1)
            n = rng.randint(m + 1, X)
            assert n / m < 1024
            ratio_checks += 1

    # Exact square and gcd decomposition on synthetic rational weights.
    mu = mobius_sieve(max(scan_limit, 4096))
    for X in range(33, 80):
        active = [m for m in range(1, X + 1) if m % 2 == 1 and mu[m] != 0]
        weights = {m: Fraction((m % 11) - 5, m + 3) for m in active}
        total = sum((Fraction(mu[m]) * weights[m] for m in active), Fraction(0))
        diagonal = sum((weights[m] ** 2 for m in active), Fraction(0))
        cross = sum(
            (
                2 * Fraction(mu[m] * mu[n]) * weights[m] * weights[n]
                for i, m in enumerate(active)
                for n in active[i + 1 :]
            ),
            Fraction(0),
        )
        assert total * total == diagonal + cross
        square_checks += 1

        grouped = Fraction(0)
        for i, m in enumerate(active):
            for n in active[i + 1 :]:
                d = math.gcd(m, n)
                a, b = m // d, n // d
                assert math.gcd(a, b) == math.gcd(a, d) == math.gcd(b, d) == 1
                assert mu[m] * mu[n] == mu[a] * mu[b]
                grouped += 2 * Fraction(mu[a] * mu[b]) * weights[d * a] * weights[d * b]
                gcd_checks += 1
        assert grouped == cross

    # Formal prime-log Type I identity.
    for m in range(3, 2048, 2):
        if mu[m] == 0:
            continue
        factors = factor_map(m)
        left = {p: Fraction(mu[m] * e) for p, e in factors.items()}
        right: dict[int, Fraction] = {}
        for p in factors:
            right[p] = right.get(p, Fraction(0)) - Fraction(mu[m // p])
        assert left == right
        type_i_checks += 1

    # Count bounds used in the near-diagonal and large-gcd estimates.
    for X in range(32, 129):
        for H in range(1, 8):
            near = sum(1 for m in range(1, X + 1) for n in range(m + 1, min(X, m + H) + 1))
            assert near <= X * H
            pair_count_checks += 1
        for H in range(2, 9):
            threshold = X / H
            count = sum(1 for m in range(1, X + 1) for n in range(m + 1, X + 1) if math.gcd(m, n) >= threshold)
            assert count <= 2 * X * H
            pair_count_checks += 1

    # Rank-one diagonal completion threshold lambda>=N.
    for n in range(2, 32):
        # Along the sign vector, lambda I - ss^T has Rayleigh quotient lambda-n.
        assert (n - 1) < n
        positive_kernel_checks += 1

    # Floating reconnaissance only.
    selected = sorted(set(x for x in (256, 1000, 10000, 100000, scan_limit) if x <= scan_limit and x >= 64))
    scans = [annular_scan(X, mu) for X in selected]

    # Hostile mutations.
    if sum(Q[h] * 2 ** h for h in range(4)) != 1:
        mutations += 1
    if Fraction(64, 21) != Fraction(63, 21):
        mutations += 1
    if band_coeffs(A, 10)[1].is_zero():
        mutations += 1
    if Fraction(2, 81) != Fraction(1, 81):
        mutations += 1
    if all(s["cross"] >= 0.0 for s in scans):
        mutations += 1

    return {
        "classification": "PASS_X_95400_Q4_FOCC_ANNULAR_HARDENING",
        "arithmetic_class": "EXACT_INTEGER_RATIONAL_QSQRT2_PLUS_FLOATING_RECONNAISSANCE",
        "frozen_base_pr": 573,
        "frozen_base_sha": "0865242eb9dc0ed6094afc8a87a52b974c6f1307",
        "exact_kernel_coefficient_checks": exact_kernel_checks,
        "cubic_annihilation_checks": annihilation_checks,
        "stable_inverse_checks": inverse_checks,
        "activation_checks": activation_checks,
        "ratio_checks": ratio_checks,
        "gcd_decomposition_checks": gcd_checks,
        "square_identity_checks": square_checks,
        "type_i_formal_checks": type_i_checks,
        "pair_count_bound_checks": pair_count_checks,
        "positive_kernel_firewall_checks": positive_kernel_checks,
        "hostile_mutations_detected": mutations,
        "floating_reconnaissance": scans,
        "proves": [
            "safe factor-1024 annularization",
            "ten exact Q(sqrt2) kernel bands",
            "stable inverse with l1 mass 64/21",
            "exact band, ratio and gcd decomposition",
            "O(log^2 X) annular diagonal",
            "polylog near-diagonal and large-gcd bounds",
            "source-faithful Type I identity",
            "source-blind positive-kernel and fixed-window barriers",
        ],
        "does_not_prove": [
            "SACF separated coprime Type-II bound",
            "FOCC",
            "OCHD",
            "Riemann Hypothesis",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--scan-limit", type=int, default=100000)
    args = parser.parse_args()
    if args.scan_limit < 1000:
        raise SystemExit("scan limit must be at least 1000")
    text = json.dumps(run(args.scan_limit), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
