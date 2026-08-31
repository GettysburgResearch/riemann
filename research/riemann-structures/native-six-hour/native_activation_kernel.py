#!/usr/bin/env python3
"""Bounded exact original-kernel Gram discovery for native activation paths."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha1
from itertools import product
from math import isqrt, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE_COMMIT = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
SOURCE_PATH = "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md"
SOURCE_BLOB = "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6"
ZERO = (F(0), F(0))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def q(a=0, b=0):
    return F(a), F(b)


def qa(a, b):
    return a[0] + b[0], a[1] + b[1]


def qm(a, b):
    return a[0] * b[0] + 2 * a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def qs(a, b):
    return a[0] * b, a[1] * b


def expr(constant=ZERO, logs=None):
    return constant, {
        F(key): value
        for key, value in (logs or {}).items()
        if value != ZERO and key != 1
    }


def ea(a, b):
    logs = dict(a[1])
    for key, value in b[1].items():
        logs[key] = qa(logs.get(key, ZERO), value)
    return expr(qa(a[0], b[0]), logs)


def es(a, value):
    return expr(
        qs(a[0], value),
        {key: qs(coefficient, value) for key, coefficient in a[1].items()},
    )


def sqrt_boundary(value):
    value = F(value)
    for factor in (1, 2):
        reduced = value / factor
        n, d = isqrt(reduced.numerator), isqrt(reduced.denominator)
        if n * n == reduced.numerator and d * d == reduced.denominator:
            return q(F(n, d), 0) if factor == 1 else q(0, F(n, d))
    raise ValueError("kernel boundary is not in Q(sqrt2)")


@lru_cache(maxsize=128, typed=True)
def gamma_square_ratio(ratio):
    require(
        type(ratio) in (int, F) and 0 < ratio <= 1000000,
        "bounded exact frequency ratio",
    )
    ratio = F(ratio)
    require(
        max(ratio.numerator.bit_length(), ratio.denominator.bit_length()) <= 64,
        "frequency ratio bit cap",
    )
    ratio = ratio if ratio >= 1 else 1 / ratio
    shift = ratio * ratio
    if shift >= 8:
        return expr()
    pieces = (
        (F(1), F(2), q(8), q(-4)),
        (F(2), F(4), q(-8, -8), q(0, 4)),
        (F(4), F(8), q(0, 8), q(-2)),
    )
    result = expr()
    for lo1, hi1, a, b in pieces:
        for lo2, hi2, c, d in pieces:
            lo, hi = max(lo1, shift * lo2), min(hi1, shift * hi2)
            if lo >= hi:
                continue
            constant_log = qm(a, c)
            square_root_term = qs(qa(qm(a, d), qs(qm(c, b), ratio)), 2 / ratio)
            linear_term = qs(qm(b, d), 1 / ratio)
            constant = qa(
                qm(square_root_term, qa(sqrt_boundary(hi), qs(sqrt_boundary(lo), -1))),
                qs(linear_term, hi - lo),
            )
            result = ea(result, expr(constant, {hi / lo: constant_log}))
    return result


def ia(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def im(a, b):
    values = [x * y for x in a for y in b]
    return min(values), max(values)


def inv(a):
    require(a[0] > 0 or a[1] < 0, "interval division away from zero")
    return F(1, a[1]), F(1, a[0])


def point(value):
    return F(value), F(value)


@lru_cache(maxsize=256, typed=True)
def log_interval(value, terms=48):
    require(type(value) in (int, F) and value > 0, "positive exact logarithm")
    require(type(terms) is int and 8 <= terms <= 64, "log series cap")
    value = F(value)
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= 128,
        "log input bit cap",
    )
    if value < 1:
        return neg(log_interval(1 / value, terms))
    k = 0
    while value >= 2:
        value /= 2
        k += 1
        require(k <= 128, "log range reduction cap")
    z = (value - 1) / (value + 1)
    current, total = z, F(0)
    for j in range(terms):
        total += 2 * current / (2 * j + 1)
        current *= z * z
    remainder = 2 * current / ((2 * terms + 1) * (1 - z * z))
    local = total, total + remainder
    if not k:
        return local
    z2 = F(1, 3)
    current, total = z2, F(0)
    for j in range(terms):
        total += 2 * current / (2 * j + 1)
        current *= z2 * z2
    remainder = 2 * current / ((2 * terms + 1) * (1 - z2 * z2))
    return ia(local, (k * total, k * (total + remainder)))


def qi(value):
    denominator = 10**40
    lower = isqrt(2 * denominator * denominator)
    sqrt2 = F(lower, denominator), F(lower + 1, denominator)
    return ia(point(value[0]), im(point(value[1]), sqrt2))


def ei(value):
    result = qi(value[0])
    for base, coefficient in value[1].items():
        result = ia(result, im(qi(coefficient), log_interval(base)))
    return result


def inner_expressions(left, right, divisors):
    result = expr()
    for a, n in zip(left, divisors, strict=True):
        for b, m in zip(right, divisors, strict=True):
            if a and b:
                result = ea(result, es(gamma_square_ratio(F(n, m)), a * b))
    return result


def kernel_gram(primes):
    require(
        type(primes) is tuple and len(primes) == 3 and len(set(primes)) == 3,
        "three distinct literal primes",
    )
    require(
        all(
            type(p) is int
            and 2 <= p <= 101
            and all(p % d for d in range(2, isqrt(p) + 1))
            for p in primes
        ),
        "bounded prime check",
    )
    signs = tuple(product((-1, 1), repeat=3))
    divisors = tuple(
        prod(p for p, sign in zip(primes, row, strict=True) if sign == 1)
        for row in signs
    )
    mean = (F(1, 8),) * 8
    odd = tuple(tuple(F(row[j], 8) for row in signs) for j in range(3))
    gram = tuple(tuple(inner_expressions(a, b, divisors) for b in odd) for a in odd)
    mean_energy = inner_expressions(mean, mean, divisors)
    cross = tuple(inner_expressions(mean, a, divisors) for a in odd)
    require(
        all(ei(value)[0] <= 0 <= ei(value)[1] for value in cross),
        "even-odd kernel symmetry",
    )
    return {
        "primes": primes,
        "K": prod(primes),
        "divisors": divisors,
        "gram": gram,
        "mean": mean_energy,
        "even_odd_cross": cross,
    }


def determinant(matrix):
    a, b, c = matrix
    first = im(a[0], ia(im(b[1], c[2]), neg(im(b[2], c[1]))))
    second = im(a[1], ia(im(b[0], c[2]), neg(im(b[2], c[0]))))
    third = im(a[2], ia(im(b[0], c[1]), neg(im(b[1], c[0]))))
    return ia(ia(first, neg(second)), third)


def cofactor(matrix, row, column):
    sub = [
        [matrix[i][j] for j in range(3) if j != column] for i in range(3) if i != row
    ]
    value = ia(im(sub[0][0], sub[1][1]), neg(im(sub[0][1], sub[1][0])))
    return value if (row + column) % 2 == 0 else neg(value)


def summarize_interval(value):
    return {
        "lower": str(value[0]),
        "upper": str(value[1]),
        "approximate_midpoint": float((value[0] + value[1]) / 2),
    }


def discover(primes):
    model = kernel_gram(primes)
    matrix = tuple(tuple(ei(value) for value in row) for row in model["gram"])
    det = determinant(matrix)
    require(det[0] > 0, "certified positive determinant")
    cofactors = tuple(tuple(cofactor(matrix, i, j) for j in range(3)) for i in range(3))
    rows = tuple(ia(ia(row[0], row[1]), row[2]) for row in cofactors)
    total = ia(ia(rows[0], rows[1]), rows[2])
    probabilities = tuple(im(row, inv(total)) for row in rows)
    uniform = point(0)
    for row in matrix:
        for value in row:
            uniform = ia(uniform, im(point(F(1, 9)), value))
    minimum = im(det, inv(total))
    improvement = ia(uniform, neg(minimum))
    gradient = tuple(
        im(point(F(1, 3)), ia(ia(row[0], row[1]), row[2])) for row in matrix
    )
    powers = tuple(
        max(1, round(1000 * float((value[0] + value[1]) / 2)))
        for value in probabilities
    )
    q_candidate = tuple(F(a, sum(powers)) for a in powers)
    candidate_energy = point(0)
    for i in range(3):
        for j in range(3):
            candidate_energy = ia(
                candidate_energy,
                im(point(q_candidate[i] * q_candidate[j]), matrix[i][j]),
            )
    return {
        "primes": primes,
        "K": model["K"],
        "gram": [[summarize_interval(x) for x in row] for row in matrix],
        "mean_energy": summarize_interval(ei(model["mean"])),
        "determinant": summarize_interval(det),
        "unconstrained_activation": [summarize_interval(x) for x in probabilities],
        "interior_certified": all(x[0] > 0 for x in probabilities),
        "uniform_gradient": [summarize_interval(x) for x in gradient],
        "uniform_minus_optimum": summarize_interval(improvement),
        "candidate_integer_power_schedule": powers,
        "uniform_minus_candidate": summarize_interval(
            ia(uniform, neg(candidate_energy))
        ),
        "normalization": "all energies here multiplied by K; fixed mean energy excluded from differences",
    }


def authenticate():
    raw = subprocess.run(
        ["git", "show", f"{SOURCE_COMMIT}:{SOURCE_PATH}"],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout
    require(
        0 < len(raw) < 65536
        and sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        == SOURCE_BLOB,
        "original kernel source authentication",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    authenticate()
    require(
        gamma_square_ratio(F(1)) == expr(q(-288), {F(2): q(384, 128)}),
        "exact native Gamma(0)",
    )
    output = {
        "source": {"commit": SOURCE_COMMIT, "path": SOURCE_PATH, "blob": SOURCE_BLOB},
        "models": [discover(primes) for primes in ((3, 5, 7), (2, 3, 5), (3, 11, 101))],
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
