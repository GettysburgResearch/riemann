#!/usr/bin/env python3
"""Independent Hermite-derivative check, distinct from triple-product expansion."""
import hashlib
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from flint import arb, ctx, __FLINT_VERSION__

ctx.prec = 192
n = 70
c = Fraction(13, 2)


def partial_exp(k):
    return sum((c ** (2 * j) / factorial(j) for j in range(k + 1)), Fraction())


def as_ball(q):
    return arb(q.numerator) / q.denominator


# Gaussian integration by parts: E[He_k Q_n²] = E[(Q_n²)^(k)].
# Since Q_n^(j) = c^j Q_(n−j), orthogonality leaves this single sum.
ratios = [c**k * sum((comb(k, j) * partial_exp(min(n-j, n-k+j))
                      for j in range(k+1)), Fraction()) / partial_exp(n)
          for k in range(5)]
sigma = (arb(2).log() / 2).sqrt()
s = arb(1) / (20 * sigma)
q = arb(7) / (12000 * sigma)
coefficients = [arb(1), -4*s+q, 6*s*s-s*q, -4*s**3, s**4]
value = sum((a * as_ball(r) for a, r in zip(coefficients, ratios)), arb(0))
assert value < arb('-0.00118')
print(json.dumps(dict(
    method='Gaussian integration by parts plus exact rational partial exponential sums',
    formal_only=True, arithmetic_supported_orders=list(range(5)),
    degree=n, formal_moments_used_through=2*n,
    hermite_shift=str(c), precision_bits=ctx.prec, flint=__FLINT_VERSION__,
    normalized_squared_formal_expectation=str(value),
    source_code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
), indent=2))
