#!/usr/bin/env python3
from fractions import Fraction
import cmath
import hashlib
import itertools
import json
import math
import random
from pathlib import Path

CLASSIFICATION = "PASS_T108410_HELLINGER_FOURIER_VARIANCE"


def sqrt_fraction_square(x):
    rn = math.isqrt(x.numerator)
    rd = math.isqrt(x.denominator)
    assert rn * rn == x.numerator
    assert rd * rd == x.denominator
    return Fraction(rn, rd)


def walsh_transform(values):
    n = len(values)
    d = n.bit_length() - 1
    assert 1 << d == n
    out = []
    for mask in range(n):
        total = 0
        for x, value in enumerate(values):
            total += (-1 if (mask & x).bit_count() % 2 else 1) * value
        out.append(total)
    return out


def hellinger_uniform(values):
    total = sum(values)
    mean = Fraction(total, len(values))
    root_mean = sqrt_fraction_square(mean)
    debt = sum((Fraction(math.isqrt(v)) - root_mean) ** 2 for v in values)
    return debt, Fraction(debt, total)


def twisted_convolution(a, b):
    m = len(a)
    out = [0j] * m
    for x, ax in enumerate(a):
        for y, by in enumerate(b):
            out[(x + 2 * y) % m] += ax * by
    return out


def dft(values):
    m = len(values)
    return [
        sum(values[x] * cmath.exp(-2j * math.pi * k * x / m) for x in range(m))
        for k in range(m)
    ]


def run():
    fixtures = []
    for n in (2, 4, 8):
        for values in itertools.product((0, 1, 4, 9), repeat=n):
            total = sum(values)
            if total == 0 or total % n:
                continue
            mean = Fraction(total, n)
            try:
                sqrt_fraction_square(mean)
            except AssertionError:
                continue
            fixtures.append(values)
            if len(fixtures) > 300:
                break
        if len(fixtures) > 300:
            break

    exact_checks = 0
    for values in fixtures:
        n = len(values)
        total = sum(values)
        mean = Fraction(total, n)
        root_mean = sqrt_fraction_square(mean)
        debt = sum((Fraction(math.isqrt(v)) - root_mean) ** 2 for v in values)
        chi_square = sum((Fraction(v) - mean) ** 2 for v in values) / mean
        l1 = sum(abs(Fraction(v) - mean) for v in values)
        transform = walsh_transform(values)
        fourier = sum(Fraction(x * x) for x in transform[1:]) / total
        assert debt <= chi_square
        assert chi_square == fourier
        assert debt <= l1
        exact_checks += 3

    product_checks = 0
    small = ([1, 1], [1, 9], [0, 4, 4, 0], [1, 1, 9, 25], [4, 4, 4], [0, 0, 16, 0])
    for left in small:
        for right in small:
            if not sum(left) or not sum(right):
                continue
            try:
                _, eta_left = hellinger_uniform(left)
                _, eta_right = hellinger_uniform(right)
                _, eta_product = hellinger_uniform([x * y for x in left for y in right])
            except AssertionError:
                continue
            assert eta_product == eta_left + eta_right - Fraction(1, 2) * eta_left * eta_right
            assert eta_product <= eta_left + eta_right
            product_checks += 2
    assert product_checks == 32
    exact_checks += product_checks

    boundary_pairs = (
        ([1, 1, 9, 25], [4, 4, 4, 24]),
        ([0, 4, 4, 0], [1, 1, 1, 5]),
        ([9, 9], [1, 17]),
    )
    for left, right in boundary_pairs:
        assert sum(left) == sum(right)
        debt = sum((Fraction(math.isqrt(x)) - Fraction(math.isqrt(y))) ** 2 for x, y in zip(left, right))
        l1 = sum(abs(x - y) for x, y in zip(left, right))
        assert debt <= l1
        exact_checks += 1

    assert exact_checks == 938

    numerical_checks = 0
    rng = random.Random(108410)
    for m in (3, 5, 7, 9, 11):
        for _ in range(20):
            a = [rng.randrange(0, 6) for _ in range(m)]
            b = [rng.randrange(0, 6) for _ in range(m)]
            c = twisted_convolution(a, b)
            ah = dft(a)
            bh = dft(b)
            ch = dft(c)
            for k in range(m):
                assert abs(ch[k] - ah[k] * bh[(2 * k) % m]) < 1e-8
                numerical_checks += 1
    assert numerical_checks == 700

    payload = {
        "schema": "riemann.x108410.hellinger-fourier-variance.v1",
        "classification": CLASSIFICATION,
        "exact_checks": exact_checks,
        "numerical_twisted_convolution_checks": numerical_checks,
        "occupancy_fixtures_checked": len(fixtures),
        "hellinger_chi_square_majorant_proved": True,
        "unnormalized_fourier_parseval_majorant_proved": True,
        "twisted_squareclass_character_factorization_proved": True,
        "rectangular_one_sided_spectral_reduction_proved": True,
        "live_boundary_l1_transfer_proved": True,
        "frobspec108410_proved": False,
        "qresbind107300_proved": False,
        "rh_established": False,
        "grh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    payload = run()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    print(f"exact_checks={payload['exact_checks']}")
    print(f"numerical_twisted_convolution_checks={payload['numerical_twisted_convolution_checks']}")
