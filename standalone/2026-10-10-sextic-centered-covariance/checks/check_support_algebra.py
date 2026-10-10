#!/usr/bin/env python3
"""Exact finite predicates used by the reunited-cusp support proof.

This checks all matrices in SL_2(O/(3)), the fixed-unit cusp reduction,
the standard-frequency projection, the full local Ramanujan reunion,
and rational exponent bookkeeping. It does not check theta automorphy,
Mellin contour shifts, infinite cancellation, or a moment asymptotic.
No floating point or optimization-sensitive assert statements are used.
"""

import itertools
import json
from fractions import Fraction


checks = 0


def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise RuntimeError(message)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def conjugate(x):
    return x[0] - x[1], -x[1]


def norm(x):
    return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]


def power(x, n):
    result = (1, 0)
    for _ in range(n):
        result = mul(result, x)
    return result


def divides(d, x):
    z = mul(x, conjugate(d))
    q = norm(d)
    return z[0] % q == 0 and z[1] % q == 0


def mod3(x):
    return x[0] % 3, x[1] % 3


def matmul(a, b):
    return tuple(
        mod3(add(mul(a[2 * i], b[j]), mul(a[2 * i + 1], b[2 + j])))
        for i in range(2)
        for j in range(2)
    )


zero, one = (0, 0), (1, 0)
lam = (1, 2)
units = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]
ring = list(itertools.product(range(3), repeat=2))
unit_residues = {mod3(u) for u in units}
require(len(unit_residues) == 6, "six distinct global units modulo 3")
require(
    unit_residues == {x for x in ring if (x[0] + x[1]) % 3 != 0},
    "global units represent every unit in O/(3)",
)
for u in units:
    require(norm(u) == 1, "unit norm")
    require(mul(u, conjugate(u)) == one, "unit inverse")
    require(divides(power(lam, 4), mul(u, power(lam, 4))), "unit preserves lattice")

matrix_count = 0
cusp_counts = {"zero_lower_left": 0, "ramified_lower_left": 0, "unit_lower_left": 0}
identity = (one, zero, zero, one)
for a, b, c, d in itertools.product(ring, repeat=4):
    if mod3(add(mul(a, d), neg(mul(b, c)))) != one:
        continue
    matrix_count += 1
    a_matrix = (a, b, c, d)
    ramified = (c[0] + c[1]) % 3 == 0
    target = a if ramified else c
    candidates = [u for u in units if mod3(mul(target, u)) == one]
    require(len(candidates) == 1, "unique normalizing global unit")
    u = candidates[0]
    u_inverse = conjugate(u)
    diagonal = (mod3(u), zero, zero, mod3(u_inverse))
    normalized = matmul(a_matrix, diagonal)
    aa, bb, cc, dd = normalized
    if ramified:
        require(aa == one, "top-left normalized")
        t = mod3(neg(bb))
    else:
        require(cc == one, "bottom-left normalized")
        t = mod3(neg(dd))
    translation = (one, t, zero, one)
    final = matmul(normalized, translation)
    if ramified:
        require(cc in {zero, mod3(lam), mod3(neg(lam))}, "three ramified residues")
        expected = (one, zero, cc, one)
        key = "zero_lower_left" if cc == zero else "ramified_lower_left"
    else:
        expected = (aa, mod3(neg(one)), one, zero)
        key = "unit_lower_left"
    cusp_counts[key] += 1
    require(final == expected, "prescribed fixed cusp representative")
    h_inverse = (expected[3], mod3(neg(expected[1])), mod3(neg(expected[2])), expected[0])
    require(matmul(final, h_inverse) == identity, "Gamma(3) remainder")
require(matrix_count == 648, "complete SL_2(O/(3)) coverage")

# On the source cubic support, x=lambda^4 ell=lambda^(m+4) u n b^3.
# Primary n,b are 1 modulo 3. Representative ranges below contain
# nontrivial lifts, all units, and each valuation m=-4,...,12.
projection_cases = 0
for m, u, r, s, t, v in itertools.product(
    range(-4, 13), units, range(-1, 2), range(-1, 2), range(-1, 2), range(-1, 2)
):
    n = (1 + 3 * r, 3 * s)
    b = (1 + 3 * t, 3 * v)
    x = mul(power(lam, m + 4), mul(u, mul(n, power(b, 3))))
    actual = divides(power(lam, 3), add(x, neg(lam)))
    expected = m == -3 and u == one
    require(actual == expected, "standard-face congruence selects valuation and primary unit")
    projection_cases += 1

# Multiply the Ramanujan identity by sqrt(Na) so every comparison is
# an integer. Check all divisibility profiles, with no artificial
# condition that a negative-choice prime avoid the frequency.
prime_norms = [7, 13, 19, 31]
ramanujan_cases = 0
for divisor_flags in itertools.product((0, 1), repeat=len(prime_norms)):
    selected = [q for q, chosen in zip(prime_norms, divisor_flags) if chosen]
    for frequency_flags in itertools.product((0, 1), repeat=len(selected)):
        left = 1
        for q, divides_frequency in zip(selected, frequency_flags):
            left *= -1 + q * divides_frequency
        right = 0
        for positive_flags in itertools.product((0, 1), repeat=len(selected)):
            mu_g = (-1) ** (len(selected) - sum(positive_flags))
            norm_h = 1
            h_divides = 1
            for q, positive, divides_frequency in zip(selected, positive_flags, frequency_flags):
                if positive:
                    norm_h *= q
                    h_divides *= divides_frequency
            right += mu_g * norm_h * h_divides
        require(left == right, "exact reunited Ramanujan product")
        ramanujan_cases += 1

# The vertices are the complete feasible polygon e+f+g=1,
# e,f,g>=0, g<=1/2. Affine exponent maxima occur at these vertices.
vertices = [
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(1, 2), Fraction(0), Fraction(1, 2)),
    (Fraction(0), Fraction(1, 2), Fraction(1, 2)),
]
exponent_records = []
for beta in [Fraction(1), Fraction(11, 12), Fraction(7, 8), Fraction(3, 4)]:
    target_row_exponent = Fraction(5, 4) - beta / 2
    maxima = [
        max(e + (2 * beta - 2) * g for e, f, g in vertices),
        max((2 * beta - 1) * g - 2 * f for e, f, g in vertices),
        max(Fraction(2, 3) - 2 * f + (2 * beta - 2) * g for e, f, g in vertices),
    ]
    require(maxima == [Fraction(1), beta - Fraction(1, 2), Fraction(2, 3)],
            "component exponent maxima")
    require(target_row_exponent + maxima[0] <= 2, "first component at target")
    require(2 * target_row_exponent + maxima[1] == 2, "middle component at target")
    require(Fraction(4, 3) * target_row_exponent + maxima[2] <= 2,
            "third component at target")
    exponent_records.append({
        "beta": str(beta),
        "dual_row_cutoff_exponent": str(target_row_exponent),
        "middle_D_exponent": str(maxima[1]),
    })

print(json.dumps({
    "status": "PASS",
    "arithmetic": "exact integers and rational numbers",
    "predicates": checks,
    "sl2_mod3_matrices": matrix_count,
    "cusp_class_counts": cusp_counts,
    "standard_projection_cases": projection_cases,
    "ramanujan_reunion_cases": ramanujan_cases,
    "exponent_records": exponent_records,
    "scope": "finite algebra only; no theta, contour, cancellation, or moment certification",
}, indent=2, sort_keys=True))
