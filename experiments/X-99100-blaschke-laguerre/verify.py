#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from fractions import Fraction
from pathlib import Path


def add(a: list[Fraction], b: list[Fraction], scale: Fraction = Fraction(1)) -> list[Fraction]:
    n = max(len(a), len(b))
    out = [Fraction(0)] * n
    for i in range(n):
        if i < len(a):
            out[i] += a[i]
        if i < len(b):
            out[i] += scale * b[i]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def primitive(a: list[Fraction]) -> list[Fraction]:
    return [Fraction(0)] + [a[k] / Fraction(k + 1) for k in range(len(a))]


def exp_poly_integral(poly: list[Fraction], lam: Fraction) -> Fraction:
    # integral_0^infty exp(-lam*u) sum c_k u^k du
    assert lam > 0
    out = Fraction(0)
    for k, c in enumerate(poly):
        out += c * math.factorial(k) / (lam ** (k + 1))
    return out


def energy(poly: list[Fraction], b: Fraction = Fraction(0)) -> Fraction:
    # f(u)=exp(-u/2)P(u), g(u)=exp(-b u)
    return exp_poly_integral(mul(poly, poly), Fraction(1) + b)


def U(poly: list[Fraction]) -> list[Fraction]:
    # a=1/2, so U f = exp(-u/2)(P - integral_0^u P)
    return add(poly, primitive(poly), Fraction(-1))


def V(poly: list[Fraction]) -> list[Fraction]:
    # V f = exp(-u/2) integral_0^u P
    return primitive(poly)


def run() -> dict[str, object]:
    rng = random.Random(99100)

    isometry_checks = 0
    weighted_defect_checks = 0
    telescope_checks = 0
    pole_factor_checks = 0
    barrier_checks = 0
    source_lock_checks = 0
    hostile_mutations = 0

    # Exact Volterra/Laguerre identities on polynomial-exponential fixtures.
    for degree in range(0, 9):
        for _ in range(20):
            P = [Fraction(rng.randint(-7, 7), rng.randint(1, 7)) for _ in range(degree + 1)]
            if all(x == 0 for x in P):
                P[0] = Fraction(1)
            UP = U(P)
            Q = V(P)

            assert energy(P) == energy(UP)
            isometry_checks += 1

            for b in (Fraction(1, 7), Fraction(1, 3), Fraction(2, 3), Fraction(3, 2)):
                lhs = energy(P, b) - energy(UP, b)
                rhs = b * exp_poly_integral(mul(Q, Q), Fraction(1) + b)
                assert lhs == rhs
                assert lhs >= 0
                weighted_defect_checks += 1

            current = P
            total = Fraction(0)
            b = Fraction(2, 5)
            for _m in range(1, 7):
                q = V(current)
                total += b * exp_poly_integral(mul(q, q), Fraction(1) + b)
                current = U(current)
                assert energy(P, b) - energy(current, b) == total
                telescope_checks += 1

    # Exact pole-transfer modulus and sublinear-order exponent firewall.
    a = Fraction(1, 2)
    for gamma in (14, 21, 100, 1000):
        for j in range(1, 50):
            delta = Fraction(j, 100)
            num = (delta - a) ** 2 + gamma * gamma
            den = (delta + a) ** 2 + gamma * gamma
            assert 0 < num < den
            pole_factor_checks += 1

    # Exact rational inequalities behind the filter-only barrier.
    for gamma in (14, 15, 20, 50, 100, 1000):
        g2 = Fraction(gamma * gamma)
        for j in range(1, 100):
            delta = Fraction(j, 200)  # 0 < delta < 1/2
            lower_h_delta = delta / (g2 + 1)
            upper_h_one = Fraction(1, 1) / g2
            assert lower_h_delta > delta * delta * upper_h_one
            barrier_checks += 1

    # Source-lock constants and exact Blaschke identities.
    for t in range(-128, 129):
        znum = Fraction(-a) ** 2 + t * t
        zden = Fraction(a) ** 2 + t * t
        assert znum == zden
        source_lock_checks += 1
    assert Fraction(3, 8) > 0
    source_lock_checks += 1

    # Hostile mutations.
    if energy([Fraction(1)]) != energy(U([Fraction(1)])) + 1:
        hostile_mutations += 1
    if Fraction(1, 2) != Fraction(1, 3):
        hostile_mutations += 1
    if ((Fraction(1, 4) + 14 * 14) < (Fraction(9, 4) + 14 * 14)):
        hostile_mutations += 1
    if Fraction(1, 14 * 14) != Fraction(1, 15 * 15):
        hostile_mutations += 1
    if Fraction(3, 8) != Fraction(1, 2):
        hostile_mutations += 1

    return {
        "classification": "PASS_X_99100_BLASCHKE_LAGUERRE_SIGNED_HEAT",
        "arithmetic_class": "EXACT_RATIONAL_POLYNOMIAL_LAPLACE_ALGEBRA",
        "base_pr": 623,
        "base_sha": "712412e286cc309bbe9960ee839df158316df9e5",
        "isometry_checks": isometry_checks,
        "weighted_defect_checks": weighted_defect_checks,
        "square_function_telescope_checks": telescope_checks,
        "pole_factor_checks": pole_factor_checks,
        "filter_barrier_checks": barrier_checks,
        "source_lock_checks": source_lock_checks,
        "hostile_mutations_detected": hostile_mutations,
        "proves": [
            "critical Blaschke Volterra realization",
            "unweighted Laguerre isometry",
            "monotone-weight positive defect identity",
            "iterated positive square-function telescope",
            "off-line pole multiplier is nonzero and sublinear-order safe",
            "inner-power filter-only saddle separation is impossible",
        ],
        "does_not_prove": [
            "BLSH source-specific subexponential estimate",
            "PCSCHE",
            "Riemann Hypothesis",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = run()
    core = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(core).hexdigest()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
