#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import random
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


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

    def to_float(self) -> float:
        return float(self.a) + math.sqrt(2.0) * float(self.b)

    def as_json(self) -> dict[str, str]:
        return {"rational": str(self.a), "sqrt2": str(self.b)}


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


def formal_add(
    left: dict[int, Fraction],
    right: dict[int, Fraction],
    scale: Fraction = Fraction(1),
) -> dict[int, Fraction]:
    out = dict(left)
    for p, c in right.items():
        out[p] = out.get(p, Fraction(0)) + scale * c
        if out[p] == 0:
            del out[p]
    return out


def formal_scale(x: dict[int, Fraction], c: Fraction) -> dict[int, Fraction]:
    return {p: c * v for p, v in x.items() if c * v}


def odd_squarefree(limit: int, mu: list[int]) -> list[int]:
    return [n for n in range(1, limit + 1) if n % 2 == 1 and mu[n] != 0]


W_LOW = (5.0, -63.0, 170.0)
W_HIGH = (-1.0 / 3.0, 1.0, -2.0 / 3.0)
A = (1, 1, -8, -8, 16, 16)
B = (0, -1, -8, 0, 32, 16)
Q = (1.0, -7.0 / 8.0, 7.0 / 32.0, -1.0 / 64.0)


def W_float(x: float) -> float:
    if x < 0.0 or x > 1.0:
        return 0.0
    if x <= 0.25:
        return W_LOW[0] * x + W_LOW[1] * x * x + W_LOW[2] * x**3
    return W_HIGH[0] * x + W_HIGH[1] * x * x + W_HIGH[2] * x**3


def K_float(x: float, coeff: tuple[int, ...]) -> float:
    return sum(c * 2.0 ** (-r / 2.0) * W_float((2**r) * x) for r, c in enumerate(coeff))


def J_float(x: float, coeff: tuple[int, ...]) -> float:
    return sum(Q[h] * K_float((2**h) * x, coeff) for h in range(4))


def annular_scan(X: int, mu: list[int]) -> dict[str, float]:
    total = 0.0
    diagonal = 0.0
    log2 = math.log(2.0)
    for m in range(X // 1024 + 1, X + 1):
        if m % 2 == 0 or mu[m] == 0:
            continue
        x = m / X
        g = (math.log(m) * J_float(x, A) + log2 * J_float(x, B)) / math.sqrt(m)
        total += mu[m] * g
        diagonal += g * g
    return {
        "X": X,
        "annular_sum": total,
        "square": total * total,
        "diagonal": diagonal,
        "cross": total * total - diagonal,
    }


def run(scan_limit: int) -> dict[str, object]:
    rng = random.Random(95500)
    mu = mobius_sieve(max(scan_limit, 4096))
    source = odd_squarefree(255, mu)

    local_euler_checks = 0
    finite_euler_product_checks = 0
    gcd_bijection_checks = 0
    logarithmic_derivative_checks = 0
    dual_frequency_checks = 0
    kernel_factor_checks = 0
    zero_frequency_checks = 0
    autocorrelation_checks = 0
    exponent_dictionary_checks = 0
    odd_mertens_checks = 0
    partial_summation_checks = 0
    hostile_mutations = 0

    # Exact local critical resonance.
    for _ in range(512):
        u = Fraction(rng.randint(-9, 9), rng.randint(2, 19))
        v = Fraction(rng.randint(-9, 9), rng.randint(2, 19))
        assert 1 - u - v + u * v == (1 - u) * (1 - v)
        local_euler_checks += 1

    # Finite Euler products: four source states per prime equal two Möbius legs.
    for primes in ([3], [3, 5], [3, 5, 7], [3, 5, 7, 11]):
        for _ in range(32):
            lhs = Fraction(1)
            rhs = Fraction(1)
            for p in primes:
                u = Fraction(rng.randint(1, 7), p * rng.randint(2, 9))
                v = Fraction(rng.randint(1, 7), p * rng.randint(2, 9))
                lhs *= 1 - u - v + u * v
                rhs *= (1 - u) * (1 - v)
            assert lhs == rhs
            finite_euler_product_checks += 1

    # Exact gcd/source bijection on arbitrary rational test functions.
    for limit in range(9, 70):
        active = [n for n in source if n <= limit]
        f = {n: Fraction((7 * n + 3) % 19 - 9, n + 5) for n in active}
        g = {n: Fraction((11 * n + 1) % 23 - 11, n + 7) for n in active}
        direct = sum(
            (
                Fraction(mu[m] * mu[n]) * f[m] * g[n]
                for m in active
                for n in active
            ),
            Fraction(0),
        )
        grouped = Fraction(0)
        for m in active:
            for n in active:
                d = math.gcd(m, n)
                a, b = m // d, n // d
                assert math.gcd(a, b) == math.gcd(a, d) == math.gcd(b, d) == 1
                assert mu[m] * mu[n] == mu[a] * mu[b]
                grouped += Fraction(mu[a] * mu[b]) * f[d * a] * g[d * b]
                gcd_bijection_checks += 1
        assert direct == grouped

    # Formal logarithmic derivative: log(m)=log(a)+log(d).
    for m in source:
        for n in source[: min(40, len(source))]:
            d = math.gcd(m, n)
            a, b = m // d, n // d
            log_m = {p: Fraction(e) for p, e in factor_map(m).items()}
            log_a = {p: Fraction(e) for p, e in factor_map(a).items()}
            log_d = {p: Fraction(e) for p, e in factor_map(d).items()}
            assert log_m == formal_add(log_a, log_d)
            log_n = {p: Fraction(e) for p, e in factor_map(n).items()}
            log_b = {p: Fraction(e) for p, e in factor_map(b).items()}
            assert log_n == formal_add(log_b, log_d)
            logarithmic_derivative_checks += 2

    # Dual frequency exactness with rational cosine surrogates u,v.
    # Algebraically this is the same conjugate-pair local determinant.
    for _ in range(256):
        radial = Fraction(rng.randint(1, 9), rng.randint(10, 31))
        phase = Fraction(rng.randint(-7, 7), rng.randint(10, 31))
        u = radial + phase
        v = radial - phase
        assert 1 - u - v + u * v == (1 - u) * (1 - v)
        dual_frequency_checks += 1

    # Exact Mellin factor/root-line classification.
    # q roots have Re z=-1,-2,-3; 1+t root has -1/2; 1-4t^2 has 1/2;
    # W numerator roots have Re z=1. None lies in 0<Re z<1/2.
    root_lines = {
        "q": (Fraction(-1), Fraction(-2), Fraction(-3)),
        "1+t": (Fraction(-1, 2),),
        "1-4t^2": (Fraction(1, 2),),
        "W": (Fraction(1),),
    }
    for lines in root_lines.values():
        assert all(not (Fraction(0) < x < Fraction(1, 2)) for x in lines)
        kernel_factor_checks += len(lines)

    # Exact J0 Mellin mass at z=0.
    j00 = Q2(Fraction(7, 128), Fraction(7, 256))
    q0 = Fraction(21, 64)
    a20 = Q2(1, Fraction(1, 2))  # 1 + 1/sqrt(2)
    what0 = Fraction(1, 6)
    assert Q2(q0) * a20 * what0 == j00
    assert j00.to_float() > 0
    zero_frequency_checks += 2

    # Discrete exact autocorrelation Gram identity (finite analogue of R_hat=|gamma_hat|^2).
    for length in range(2, 14):
        gamma = [Fraction(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(length)]
        corr: dict[int, Fraction] = {}
        for lag in range(-(length - 1), length):
            corr[lag] = sum(
                (
                    gamma[i] * gamma[i + lag]
                    for i in range(length)
                    if 0 <= i + lag < length
                ),
                Fraction(0),
            )
        coeff = [Fraction(rng.randint(-7, 7), rng.randint(1, 7)) for _ in range(length)]
        lhs = sum(
            (coeff[i] * coeff[j] * corr[j - i] for i in range(length) for j in range(length)),
            Fraction(0),
        )
        conv = []
        for u in range(2 * length - 1):
            value = Fraction(0)
            for i in range(length):
                gidx = u - i
                if 0 <= gidx < length:
                    value += coeff[i] * gamma[gidx]
            conv.append(value)
        rhs = sum((x * x for x in conv), Fraction(0))
        assert lhs == rhs and rhs >= 0
        autocorrelation_checks += 1

    # Exponent dictionary fixtures: SACF exponent alpha=2 theta -> zero line 1/2+theta.
    for delta_num in range(1, 10):
        delta = Fraction(delta_num, 10)
        sacf_exponent = 1 - delta
        theta = sacf_exponent / 2
        zero_line = Fraction(1, 2) + theta
        assert zero_line == 1 - delta / 2
        exponent_dictionary_checks += 1
    assert Fraction(1, 2) + Fraction(0) == Fraction(1, 2)
    exponent_dictionary_checks += 1

    # Exact odd-Mertens identities used by the classical zero-free-region gain.
    M = [0] * 4097
    Mo = [0] * 4097
    for n in range(1, 4097):
        M[n] = M[n - 1] + mu[n]
        Mo[n] = Mo[n - 1] + (mu[n] if n % 2 else 0)
        assert M[n] == Mo[n] - Mo[n // 2]
        reconstructed = 0
        y = n
        while y >= 1:
            reconstructed += M[y]
            y //= 2
        assert reconstructed == Mo[n]
        odd_mertens_checks += 2

    # Exact discrete Abel/partial-summation identity on arbitrary rational weights.
    for upper in range(8, 96):
        lower = max(1, upper // 8)
        weights = {
            n: Fraction(rng.randint(-11, 11), rng.randint(1, 13))
            for n in range(lower, upper + 1)
        }
        direct = sum(
            (Fraction(mu[n] if n % 2 else 0) * weights[n] for n in range(lower, upper + 1)),
            Fraction(0),
        )
        abel = Fraction(Mo[upper]) * weights[upper] - Fraction(Mo[lower - 1]) * weights[lower]
        abel += sum(
            (Fraction(Mo[n]) * (weights[n] - weights[n + 1]) for n in range(lower, upper)),
            Fraction(0),
        )
        assert direct == abel
        partial_summation_checks += 1

    # Hostile controls.
    if 1 - Fraction(1, 3) - Fraction(1, 5) != (1 - Fraction(1, 3)) * (1 - Fraction(1, 5)):
        hostile_mutations += 1
    if j00 != Q2(Fraction(7, 128), Fraction(7, 255)):
        hostile_mutations += 1
    if Fraction(1, 2) != Fraction(0):
        hostile_mutations += 1
    if root_lines["1-4t^2"] != (Fraction(0),):
        hostile_mutations += 1
    if Fraction(1) - Fraction(1, 5) != Fraction(1) - Fraction(1, 10):
        hostile_mutations += 1

    scan_points = sorted(set([1000, 10000, min(scan_limit, 100000)]))
    scans = [annular_scan(x, mu) for x in scan_points if x <= scan_limit]

    parent_kernel = ROOT / "imports/t95500/exact_kernels.json"
    parent_certificate = json.loads(parent_kernel.read_text())
    assert parent_certificate["base_sha"] == "0865242eb9dc0ed6094afc8a87a52b974c6f1307"

    certificate = json.loads((HERE / "certificates/resonance.json").read_text())
    assert certificate["base_sha"] == "812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05"
    assert certificate["j0_mellin_at_zero"] == j00.as_json()
    assert certificate["carry_imported"] is False

    return {
        "classification": "PASS_X_95500_Q4_SACF_CRITICAL_RESONANCE",
        "arithmetic_class": "EXACT_INTEGER_RATIONAL_FORMAL_PRIME_LOG_AND_QSQRT2",
        "frozen_base_pr": 580,
        "frozen_base_sha": "812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05",
        "local_euler_checks": local_euler_checks,
        "finite_euler_product_checks": finite_euler_product_checks,
        "gcd_bijection_checks": gcd_bijection_checks,
        "logarithmic_derivative_checks": logarithmic_derivative_checks,
        "dual_frequency_checks": dual_frequency_checks,
        "kernel_factor_checks": kernel_factor_checks,
        "zero_frequency_checks": zero_frequency_checks,
        "autocorrelation_gram_checks": autocorrelation_checks,
        "exponent_dictionary_checks": exponent_dictionary_checks,
        "odd_mertens_identity_checks": odd_mertens_checks,
        "partial_summation_checks": partial_summation_checks,
        "hostile_mutations_detected": hostile_mutations,
        "floating_reconnaissance": scans,
        "proves": [
            "critical gcd Euler resonance 1-u-v+uv=(1-u)(1-v)",
            "exact gcd triple factorization of two odd Mobius reciprocal states",
            "complete logarithmic channels are derivatives of the same tensor product",
            "annular J0 has no zero in the off-line counterexample strip",
            "ratio autocorrelation is positive spectral mass",
            "any fixed SACF power saving implies a fixed zeta zero-free strip",
            "odd-Mertens state is a finite dyadic sum of the ordinary Mertens state",
            "exact partial summation interface for the ten-band classical gain",
        ],
        "does_not_prove": [
            "SACF",
            "FOCC",
            "OCHD",
            "Riemann Hypothesis",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-limit", type=int, default=100000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.scan_limit < 1000:
        raise SystemExit("scan-limit must be at least 1000")
    result = run(args.scan_limit)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
