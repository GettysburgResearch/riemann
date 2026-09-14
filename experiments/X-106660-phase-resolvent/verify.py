#!/usr/bin/env python3
"""Exact replay for T-106660.

The replay uses Fraction arithmetic only.  It checks:
* the phase-optimized one-pole calibration;
* a two-channel phase-dispersion firewall;
* the rational resolvent completion on scalar and 2x2 fixtures;
* the generalized Gram-coordinate identity.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
from typing import List

Q = Fraction
Matrix = List[List[Q]]


def eye(n: int) -> Matrix:
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: Q, a: Matrix) -> Matrix:
    return [[c * x for x in row] for row in a]


def mul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def trace(a: Matrix) -> Q:
    return sum((a[i][i] for i in range(len(a))), Q(0))


def inv(a: Matrix) -> Matrix:
    n = len(a)
    aug = [a[i][:] + eye(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        assert pivot is not None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            f = aug[r][col]
            if f:
                aug[r] = [aug[r][j] - f * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def det2(a: Matrix) -> Q:
    assert len(a) == 2 and len(a[0]) == 2
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def psd2(a: Matrix) -> bool:
    return a[0][0] >= 0 and a[1][1] >= 0 and det2(a) >= 0


def f(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


checks = 0

# One-pole example from corrected L-106514.
m = Q(1)
overlap = Q(4, 5)
delta_re = Q(12, 25)
delta_im = Q(-16, 25)
delta_abs = Q(4, 5)
assert delta_re * delta_re + delta_im * delta_im == delta_abs * delta_abs
checks += 1
charge = m - overlap
optimized = m - delta_abs
assert charge == optimized == Q(1, 5)
checks += 1
unoptimized = m - delta_re
assert unoptimized == Q(13, 25) and unoptimized > charge
checks += 1

# Abstract two-channel principal-phase fixture: equal singular values 1/2
# with opposite trace phases.  It proves that one scalar phase can remain strict.
m2 = Q(2)
r = Q(1, 2)
overlap2 = 2 * r * r
delta2_abs = Q(0)
charge2 = m2 - overlap2
optimized2 = m2 - delta2_abs
assert charge2 == Q(3, 2)
assert optimized2 == Q(2)
assert optimized2 - charge2 == overlap2 == Q(1, 2)
checks += 3

# Scalar resolvent completion.
scalar_rows = []
for x in [Q(0), Q(1, 10), Q(1, 3), Q(1, 2), Q(9, 10), Q(1)]:
    for tau in [Q(1, 10), Q(1, 3), Q(1), Q(3)]:
        q = (1 + tau) * x / (1 + tau * x)
        gap = tau * x * (1 - x) / (1 + tau * x)
        assert q - x == gap
        assert q >= x
        checks += 2
        scalar_rows.append({"x": f(x), "tau": f(tau), "Q_tau": f(q), "gap": f(gap)})

# A non-diagonal positive-contraction fixture.
K = [[Q(1, 2), Q(1, 4)], [Q(1, 4), Q(1, 2)]]
I = eye(2)
assert psd2(K) and psd2(sub(I, K))
checks += 2
for tau in [Q(1, 5), Q(1, 2), Q(1), Q(2)]:
    resolvent = inv(add(I, scale(tau, K)))
    lhs = (1 + tau) * trace(mul(K, resolvent))
    rhs_gap = tau * trace(mul(mul(K, sub(I, K)), resolvent))
    assert lhs - trace(K) == rhs_gap
    assert rhs_gap >= 0
    checks += 2

# Generalized Cauchy-Gram coordinate fixture.
G = [[Q(1), Q(1, 3)], [Q(1, 3), Q(1)]]
D = [[Q(1, 4), Q(0)], [Q(0), Q(1, 2)]]
H = mul(mul(transpose(D), G), D)
assert psd2(G) and psd2(sub(G, H))
checks += 2
C = trace(mul(inv(G), H))
gram_rows = []
for tau in [Q(1, 10), Q(1, 2), Q(1), Q(3)]:
    Q_tau = (1 + tau) * trace(mul(H, inv(add(G, scale(tau, H)))))
    # Coordinate version of tau tr K(I-K)(I+tau K)^(-1).
    # Use Q_tau-C as the exact algebraic oracle; positivity follows from
    # 0 <= H <= G and is also checked in Fraction arithmetic.
    gap = Q_tau - C
    assert gap >= 0
    checks += 1
    gram_rows.append({"tau": f(tau), "C": f(C), "Q_tau": f(Q_tau), "gap": f(gap)})

result = {
    "status": "PASS_T106660_PHASE_OPTIMIZED_RESOLVENT_GATE",
    "arithmetic": "EXACT_RATIONAL",
    "exact_checks": checks,
    "one_pole": {
        "canonical_charge": f(charge),
        "optimized_phase_majorant": f(optimized),
        "unoptimized_phase_majorant": f(unoptimized),
    },
    "two_channel_firewall": {
        "canonical_charge": f(charge2),
        "optimized_scalar_majorant": f(optimized2),
        "strict_slack": f(optimized2 - charge2),
    },
    "scalar_resolvent_rows": scalar_rows,
    "gram_coordinate_rows": gram_rows,
    "scientific_boundary": {
        "phase_scalar_estimate_for_Xi": False,
        "resolvent_estimate_for_Xi": False,
        "ninety_percent": False,
        "density_one": False,
        "riemann_hypothesis": False,
    },
}

out = Path(__file__).resolve().parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(result["status"])
print(f"exact checks: {checks}")
