#!/usr/bin/env python3
"""Exact finite algebra checks for the source-normalized anchor-flow identity.

These are algebra/normalization checks, not a computation of actual xi data
or proof of an unbounded source estimate. Standard library only.
"""
from fractions import Fraction as F
import json


def transpose(a):
    return [list(c) for c in zip(*a)]


def mul(a, b):
    bt = transpose(b)
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in bt] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def check(n, g):
    size = n+1
    gram = [[g[abs(j-k)] for k in range(size)] for j in range(size)]
    shift = [[F(0) for _ in range(size)] for _ in range(size)]
    for j in range(size):
        if j < n:
            shift[j+1][j] = F(j+1, 2)
        if j:
            shift[j-1][j] = F(-j, 2)
    r = [g[n+1-j] for j in range(size)]
    boundary = [[F(n+1, 2)*((r[k] if j == n else 0)
                            +(r[j] if k == n else 0))
                 for k in range(size)] for j in range(size)]
    derivative = [g[1]]+[F(k+1, 2)*g[k+1]-F(k-1, 2)*g[k-1]
                        for k in range(1, n+1)]
    expected = [[derivative[abs(j-k)] for k in range(size)]
                for j in range(size)]
    internal = add(mul(transpose(shift), gram), mul(gram, shift))
    actual = add(internal, boundary)
    if actual != expected:
        raise ArithmeticError(('matrix transport failed', n))
    if sum(actual[j][j] for j in range(size)) != (n+1)*g[1]:
        raise ArithmeticError(('trace failed', n))
    # A missing factor of two at the shared corner must be rejected.
    wrong = [row[:] for row in boundary]
    wrong[n][n] /= 2
    if g[1] and add(internal, wrong) == expected:
        raise ArithmeticError(('mutation was not rejected', n))
    # Exact characteristic invariants of the rank-two boundary spectrum.
    norm2 = sum(x*x for x in r)
    trace = sum(boundary[j][j] for j in range(size))
    trace2 = sum(boundary[j][k]*boundary[k][j]
                 for j in range(size) for k in range(size))
    if trace != (n+1)*r[n]:
        raise ArithmeticError('boundary trace')
    if trace2 != F((n+1)**2, 2)*(r[n]**2+norm2):
        raise ArithmeticError('boundary squared trace')


cases = 0
for n in range(1, 25):
    for family in range(4):
        if family == 0:
            g = [F(1, k+1) for k in range(n+2)]
        elif family == 1:
            g = [F((-1)**k*(k+2), 2*k+3) for k in range(n+2)]
        elif family == 2:
            g = [F((7*k*k+11*k+3) % 19-9, k+1) for k in range(n+2)]
        else:
            g = [F(k == 1) for k in range(n+2)]
        check(n, g)
        cases += 1
print(json.dumps({
    'status': 'PASS',
    'arithmetic': 'exact rational',
    'matrix_cases': cases,
    'maximum_dimension': 25,
    'checks': ['complete transport identity', 'trace identity',
               'shared-corner mutation rejection', 'rank-two spectral invariants'],
    'scope': 'finite algebra only; no actual xi coefficient or global sign check'
}, indent=2))
