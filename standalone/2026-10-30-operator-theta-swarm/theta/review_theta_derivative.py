#!/usr/bin/env python3
"""Reviewer cross-check: formal exp polynomial versus the author's Bell recurrence.

Shares the reviewed rational interval primitive, but not the derivative recurrence.
No numerical special-function package is needed. This authenticates eight finite
prefix derivatives; the infinite tail is reviewed in the accompanying prose.
"""
import contextlib
import argparse
from fractions import Fraction as F
from io import StringIO
import json
from math import factorial
from pathlib import Path
import runpy

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('verifier', type=Path,
                    help='Path to the author verify_polya_obstruction.py')
path = parser.parse_args().verifier.resolve()
with contextlib.redirect_stdout(StringIO()):
    source = runpy.run_path(str(path))
I, PI = source['I'], source['PI']


def multiply(a, b, degree=8):
    result = [I(0) for _ in range(degree+1)]
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            if j+k <= degree:
                result[j+k] += x*y
    return result


def formal_derivative(r, A, B):
    # Coefficients of h(t)/h(0) = exp(r t - A(e^(2t)-1) + B(e^(-2t)-1)).
    exponent = [I(0)] + [((r if j == 1 else 0) - A*2**j + B*(-2)**j)
                         /factorial(j) for j in range(1, 9)]
    power = [I(1)] + [I(0) for _ in range(8)]
    total = power[:]
    for k in range(1, 9):
        power = multiply(power, exponent)
        for j in range(9):
            total[j] += power[j]/factorial(k)
    return total[8]*factorial(8)*source['exp_interval'](-A+B)


count = 0
for n in range(1, 5):
    A, B = PI*(n*n-1), PI
    for r in [F(9, 2), F(5, 2)]:
        independent = formal_derivative(r, A, B)
        author = source['derivative'](r, A, B, 8)
        if max(independent.lo, author.lo) > min(independent.hi, author.hi):
            raise ArithmeticError('disjoint independent derivative intervals')
        count += 1

print(json.dumps({
    'status': 'PASS_REVIEWER_FORMAL_EXPONENTIAL_CROSSCHECK',
    'finite_derivatives_compared': count,
    'independent_method': 'sum of truncated powers of the exponent polynomial',
    'shared_component': 'reviewed outward-rational interval and exponential primitives',
    'scope': 'Finite theta prefix derivative cross-check; infinite tail checked in prose; no RH result.'
}, sort_keys=True, indent=2))
