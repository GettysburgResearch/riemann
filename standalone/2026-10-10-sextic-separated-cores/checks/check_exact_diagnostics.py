#!/usr/bin/env python3
"""Finite exact diagnostics; no infinite analytic theorem is tested here."""

from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math


# Z[zeta_6], with zeta_6**2 = zeta_6 - 1. All arithmetic is integral.
ZERO = (0, 0)
ONE = (1, 0)
ROOTS = (ONE, (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def require(condition, detail="diagnostic check failed"):
    if not condition:
        raise RuntimeError(detail)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c + b * d


def scale(c, x):
    return c * x[0], c * x[1]


def conjugate(x):
    return x[0] + x[1], -x[1]


def norm2(x):
    y = mul(x, conjugate(x))
    require(y[1] == 0 and y[0] >= 0, 'check failed: y[1] == 0 and y[0] >= 0')
    return y[0]


def sum_values(values):
    ans = ZERO
    for v in values:
        ans = add(ans, v)
    return ans


def check_gcd_identities():
    """Every zero/sixth-root assignment on a three-prime squarefree model.

    Weights are prescribed finite samples of a smooth norm test, with the
    unit sample zero. The model is closed under every divisor used in the
    identities. It is not an assertion about ideal counts or mean squares.
    """
    prime_norms = (7, 13, 19)
    masks = range(8)
    norms = [
        math.prod(p for i, p in enumerate(prime_norms) if m >> i & 1)
        for m in masks
    ]
    mu = [(-1) ** m.bit_count() for m in masks]
    weights = (0, 2, -1, 3, 5, -2, 4, -3)
    gcd_cutoffs = (1, 2, 8, 14, 92)
    cross_cutoffs = (1, 7, 13, 19, 91, 2000)
    f_checks = covariance_checks = 0

    for phases in product((ZERO,) + ROOTS, repeat=3):
        eta = []
        for m in masks:
            z = ONE
            for i in range(3):
                if m >> i & 1:
                    z = mul(z, phases[i])
            eta.append(z)
        coeff = [scale(mu[m] * weights[m], eta[m]) for m in masks]
        for cutoff in gcd_cutoffs:
            B = [
                sum_values(coeff[m] for m in masks if norms[n & m] < cutoff)
                for n in masks
            ]
            fq = [
                sum_values(
                    scale(mu[a] * weights[q | a], mul(eta[a], B[q | a]))
                    for a in masks if not a & q
                )
                for q in masks
            ]

            # Independent expansion by t=(q,m), d=(a,m), then a0,m0.
            for q in masks:
                rhs = ZERO
                for t in masks:
                    if t & q != t:
                        continue
                    for d in masks:
                        if d & q or norms[t | d] >= cutoff:
                            continue
                        core = ZERO
                        for a0 in masks:
                            if a0 & (d | q):
                                continue
                            for m0 in masks:
                                if m0 & (d | q | a0):
                                    continue
                                factor = (
                                    mu[a0] * mu[m0]
                                    * weights[q | d | a0]
                                    * weights[d | t | m0]
                                )
                                core = add(core, scale(factor, mul(eta[a0], eta[m0])))
                        outer = scale(mu[t], mul(eta[t], mul(eta[d], eta[d])))
                        rhs = add(rhs, mul(outer, core))
                require(fq[q] == rhs, ("F_q identity", phases, cutoff, q))
                f_checks += 1

            z = [mul(coeff[n], B[n]) for n in masks]
            for threshold in cross_cutoffs:
                # Literal covariance with the two side-gcd restrictions.
                lhs = sum_values(
                    mul(z[n], conjugate(z[m]))
                    for n in masks for m in masks if norms[n & m] >= threshold
                )
                # Signed mu(e) square after exact cross-gcd inclusion-exclusion.
                rhs = 0
                for c in masks:
                    if norms[c] < threshold:
                        continue
                    for e in masks:
                        if e & c:
                            continue
                        q = c | e
                        if eta[q] != ZERO:
                            rhs += mu[e] * norm2(fq[q])
                require(lhs == (rhs, 0), ("cross-gcd identity", phases, cutoff, threshold))
                covariance_checks += 1
    return {
        "prime_norms": prime_norms,
        "phase_and_zero_assignments": 7 ** 3,
        "F_q_exact_identities": f_checks,
        "cross_gcd_covariance_identities": covariance_checks,
    }


def check_local_conductor():
    cases = 0
    for x, w, y, z in product((0, 1), repeat=4):
        multiplicity = x + w + y + z
        exponent = F(1) if multiplicity == 1 else F(0)
        if multiplicity == 2 and ((x and w) or (y and z)):
            exponent = F(1, 2)
        disjoint = abs(x - y) + abs(w - z)
        star = w + x * (1 - y) + y * (1 - x) + z * (1 - x)
        require(exponent <= disjoint, 'check failed: exponent <= disjoint')
        require(exponent <= star, 'check failed: exponent <= star')
        require(min(x, y, z) >= min(x, y) + min(x, z) - x, 'check failed: min(x, y, z) >= min(x, y) + min(x, z) - x')
        cases += 1
    row_residues = 0
    for m, delta in product(range(3), (0, 1)):
        j = (2 * m + delta) % 6
        require((j == 4) == (m == 2 and delta == 0), 'check failed: (j == 4) == (m == 2 and delta == 0)')
        row_residues += 1
    require(min(F(4, 3), 2 * F(4, 3) - 1) > 1, 'check failed: min(F(4, 3), 2 * F(4, 3) - 1) > 1')
    return {"four_tuple_prime_patterns": cases, "square_part_residue_classes": row_residues}


def affine(a=0, b=0):
    return F(a), F(b)


def plus(x, y):
    return x[0] + y[0], x[1] + y[1]


def times(c, x):
    return c * x[0], c * x[1]


def value(x, h):
    return x[0] + x[1] * h


def raw_terms(r, all_rows):
    return [
        affine(1, 1),
        plus(affine(F(5, 12), 2), times(F(7, 4), r)),
        plus(affine(F(2, 3), F(4, 3)), times(2, r)),
        plus(affine(2, F(1, 6) if all_rows else 0), times(-3, r)),
        plus(affine(F(4, 3), F(2, 3)), times(-2, r)),
        affine(0, 1),
    ]


def check_exponents():
    # Each difference is affine in h, so endpoint checks certify the full
    # stated closed interval in this finite rational optimization.
    regimes = [
        ("squarefree_low", False, F(0), F(19, 44),
         affine(F(4, 15), -F(4, 15)), affine(F(6, 5), F(4, 5))),
        ("squarefree_high", False, F(19, 44), F(19, 24),
         affine(F(1, 3), -F(8, 19)), affine(1, F(24, 19))),
        ("all_rows_low", True, F(0), F(38, 87),
         affine(F(4, 15), -F(7, 30)), affine(F(6, 5), F(13, 15))),
        ("all_rows_high", True, F(38, 87), F(19, 22),
         affine(F(1, 3), -F(22, 57)), affine(1, F(151, 114))),
    ]
    reports = []
    for name, all_rows, left, right, r, target in regimes:
        terms = raw_terms(r, all_rows)
        for h in (left, right):
            require(0 <= value(r, h) <= F(1, 3), 'check failed: 0 <= value(r, h) <= F(1, 3)')
            require(max(value(t, h) for t in terms) == value(target, h), 'check failed: max(value(t, h) for t in terms) == value(target, h)')
        reports.append({
            "regime": name, "height_interval": [str(left), str(right)],
            "cutoff_exponent_affine": list(map(str, r)),
            "energy_exponent_affine": list(map(str, target)),
            "all_six_terms_bounded_on_interval": True,
        })
    require(value(affine(1, F(151, 114)), F(114, 151)) == 2, 'check failed: value(affine(1, F(151, 114)), F(114, 151)) == 2')
    all_example = max(value(t, F(1, 2)) for t in raw_terms(affine(F(1, 3), -F(22, 57)), True))
    sf_example = max(value(t, F(1, 2)) for t in raw_terms(affine(F(1, 3), -F(8, 19)), False))
    require(all_example == F(379, 228), 'check failed: all_example == F(379, 228)')
    require(sf_example == F(31, 19), 'check failed: sf_example == F(31, 19)')
    require(F(25, 12) - all_example == F(8, 19), 'check failed: F(25, 12) - all_example == F(8, 19)')

    h, x, b = F(21, 20), F(7, 12), F(7, 8)
    a = 2 * b - 1
    phi = lambda t: max(F(0), t - F(5, 6) * h, (2 * t - h) / 3)
    old_native, old_classical = a * 2 * x, phi(3 * x)
    subset = a * x + phi(2 * x)
    require(old_native == old_classical == F(7, 8), 'check failed: old_native == old_classical == F(7, 8)')
    require(subset == F(623, 720), 'check failed: subset == F(623, 720)')
    require(min(old_native, old_classical) - subset == F(7, 720), 'check failed: min(old_native, old_classical) - subset == F(7, 720)')
    return {
        "raw_regimes": reports,
        "all_row_example": str(all_example),
        "squarefree_example": str(sf_example),
        "triangle_loss": str(subset),
        "triangle_saving": str(F(7, 720)),
    }


def main():
    report = {
        "status": "PASS",
        "scope": (
            "Finite exact divisor/zero-mask identities, local exponent inequalities, "
            "and rational optimizations only. No theta automorphy, large sieve, "
            "moment bound, zero-free region, or proof-assistant theorem is certified."
        ),
        "gcd_identities": check_gcd_identities(),
        "local_conductor": check_local_conductor(),
        "exponents": check_exponents(),
    }
    path = Path(__file__).with_name("exact_diagnostics.json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
