#!/usr/bin/env python3
"""Exact finite principal-block identities; not an analytic theorem checker."""
from fractions import Fraction
from itertools import product
from math import prod
from pathlib import Path
import argparse
import hashlib
import json

if not __debug__:
    raise RuntimeError("Assertions are required; do not run this checker with -O.")

PRIMES = (7, 61, 67, 19, 73, 79, 97, 103, 127, 139)


def norm(v):
    return prod(p**e for p, e in zip(PRIMES, v))


def kernel(v, w):
    if any((a-b) % 6 for a, b in zip(v, w)):
        return Fraction(0)
    return prod((Fraction(p-1, p) for p, a, b in zip(PRIMES, v, w)
                 if a or b), start=Fraction(1))


def centered(left, right):
    return sum((a*b*kernel(v, w) for v, a in left.items()
                for w, b in right.items() if v != w), start=Fraction(0))


def difference(left, right):
    return {v: left.get(v, 0)-right.get(v, 0) for v in left.keys() | right.keys()}


def long_coefficient(exponents, cutoff):
    return sum((-1)**sum(h) for h in product(
        *((0, 1) if e else (0,) for e in exponents))
        if norm(h) > cutoff)


def run():
    left_product = (3, 6, 0)+(0,)*7
    right_product = (3, 0, 6)+(0,)*7
    raw_product = (0, 0, 0)+(1,)*7
    lower = norm(left_product)
    assert lower <= norm(raw_product) <= 2*lower
    assert lower <= norm(right_product) <= 2*lower
    density = Fraction(23760, 28609)
    assert kernel(left_product, right_product) == density
    assert kernel(raw_product, left_product) == 0
    assert kernel(raw_product, right_product) == 0
    d_left = (1, 2, 0)+(0,)*7
    d_right = (1, 0, 2)+(0,)*7
    assert long_coefficient(d_left, 100) == 1
    assert long_coefficient(d_right, 100) == 1

    p1, p2 = {raw_product: 1}, {raw_product: 2}
    t1 = {left_product: 1, right_product: 2}
    t2 = {left_product: 3, right_product: -1}
    s1, s2 = difference(p1, t1), difference(p2, t2)
    value = 5*density
    matrix = [[centered(s1, s2), centered(s1, t2)],
              [centered(t1, s2), centered(t1, t2)]]
    assert matrix == [[value, -value], [-value, value]]
    assert sum((x for row in matrix for x in row), start=Fraction(0)) == 0
    assert centered(p1, p2) == 0

    separation_checks = 0
    for j0 in product(range(3), repeat=3):
        j = j0+(0,)*7
        d = tuple(2*e for e in j)
        for cutoff in (1, 7, 13, 49, 61, 91, 100, 169, 200, 1000):
            c = long_coefficient(d, cutoff)
            if c:
                assert norm(j) > cutoff
                assert norm(d)**3 > cutoff**6
            separation_checks += 1

    # Sharp endpoint: raw unit and tail p^6, arising from d=p^2.
    unit = (0,)*10
    square = (2,)+(0,)*9
    sixth = (6,)+(0,)*9
    assert long_coefficient(square, 6) == -1
    assert kernel(unit, sixth) == Fraction(6, 7)
    assert long_coefficient(square, 7) == 0
    assert norm(sixth) == 7**6

    return {
        "status": "PASS",
        "scope": "Finite rational principal kernels, actual product centering, and divisor support only.",
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "separation_checks": separation_checks,
        "common_annulus": [lower, 2*lower],
        "raw_squarefree_norm": norm(raw_product),
        "alias_product_norms": [norm(left_product), norm(right_product)],
        "principal_alias_density": str(density),
        "four_block_matrix": [[str(x) for x in row] for row in matrix],
        "sharp_cutoff": {"prime_norm": 7, "c_at_R_6": -1, "c_at_R_7": 0},
        "not_verified": [
            "The analytic R^-1 bound or uniform Fourier remainder",
            "The source's individual Gauss phases",
            "A complete finite-height covariance or moment",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("short_long_principal_checks.json"))
    parser.add_argument("--manuscript", type=Path,
                        default=Path(__file__).with_name("PRINCIPAL_SHORT_LONG_COVARIANCE.md"))
    parser.add_argument("--expected-manuscript-sha256")
    args = parser.parse_args()
    digest = hashlib.sha256(args.manuscript.read_bytes()).hexdigest()
    if args.expected_manuscript_sha256 is not None and digest != args.expected_manuscript_sha256:
        raise RuntimeError("The manuscript does not match the expected SHA-256.")
    report = run()
    report["manuscript_sha256"] = digest
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
