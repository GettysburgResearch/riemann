#!/usr/bin/env python3
"""Exact finite diagnostics for CUBE_INVERSE; no analytic input is certified."""

import argparse
import hashlib
import itertools
import json
from fractions import Fraction as Q
from math import prod
from pathlib import Path


class CheckFailure(Exception):
    pass


def require(condition, message):
    if not condition:
        raise CheckFailure(message)


# Formal squarefree prime supports. These integers supply test norm labels only;
# this checker does not construct Eisenstein ideals or evaluate residue symbols.
PRIMES = (7, 13, 19)
MASKS = tuple(range(1 << len(PRIMES)))
MU = tuple((-1) ** mask.bit_count() for mask in MASKS)
NORMS = tuple(
    prod(p for i, p in enumerate(PRIMES) if mask & (1 << i))
    for mask in MASKS
)
SUBSETS = tuple(tuple(d for d in MASKS if d & mask == d) for mask in MASKS)

# Exact Z[omega], omega^2 + omega + 1 = 0. The ordered units are sixth roots.
ZERO, ONE = (0, 0), (1, 0)
ROOTS = (ONE, (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def scale(c, x):
    return (c * x[0], c * x[1])


def multiplicative_values(prime_values):
    values = []
    for mask in MASKS:
        value = ONE
        for i, prime_value in enumerate(prime_values):
            if mask & (1 << i):
                value = mul(value, prime_value)
        values.append(value)
    return tuple(values)


def shared_sides(lam1, lam2, excluded, w1, w2, poison_common_zero=False):
    """Equation (2.5), with arbitrary finite axis tests w_i(N(ell*s_i))."""
    lhs = ZERO
    for a, b in itertools.product(MASKS, repeat=2):
        if not (a & b or (a | b) & excluded):
            lhs = add(lhs, scale(MU[a] * MU[b] * w1[a] * w2[b],
                                 mul(lam1[a], lam2[b])))
    rhs = ZERO
    for ell in MASKS:
        if ell & excluded:
            continue
        sums = []
        for lam, weights in ((lam1, w1), (lam2, w2)):
            scalar = ZERO
            for s in MASKS:
                if not s & (excluded | ell):
                    scalar = add(scalar, scale(MU[s] * weights[ell | s], lam[s]))
            sums.append(scalar)
        common = mul(lam1[ell], lam2[ell])
        if poison_common_zero and common == ZERO:
            common = ONE
        rhs = add(rhs, scale(MU[ell], mul(common, mul(*sums))))
    return lhs, rhs


def check_shared_divisor():
    for a, b in itertools.product(range(6), repeat=2):
        require(mul(ROOTS[a], ROOTS[b]) == ROOTS[(a + b) % 6],
                "Sixth-root arithmetic failed")
    weights = (
        (tuple((n + 2 * m.bit_count()) % 7 - 3 for m, n in enumerate(NORMS)),
         tuple((3 * n + m.bit_count()) % 11 - 5 for m, n in enumerate(NORMS))),
        (tuple(int(m == 1) for m in MASKS),
         tuple(int(m == 1) for m in MASKS)),
    )
    cases = 0
    for a, b, zeros, variant in itertools.product(range(6), range(6), MASKS, range(2)):
        zeros2 = zeros if variant == 0 else ((zeros << 1) & 7) | (zeros >> 2)
        lam1 = multiplicative_values(tuple(
            ZERO if zeros & (1 << i) else ROOTS[(a + i) % 6] for i in range(3)))
        lam2 = multiplicative_values(tuple(
            ZERO if zeros2 & (1 << i) else ROOTS[(b + 2 * i) % 6] for i in range(3)))
        for excluded, (w1, w2) in itertools.product(MASKS, weights):
            lhs, rhs = shared_sides(lam1, lam2, excluded, w1, w2)
            require(lhs == rhs, f"Shared identity failed: {a,b,zeros,variant,excluded}")
            cases += 1

    # Both finite parts are one, while the common quadratic row character is
    # zero at the first prime. Replacing its extracted sixth power by one fails.
    lam = multiplicative_values((ZERO, ONE, ONE))
    delta = weights[1][0]
    lhs, rhs = shared_sides(lam, lam, 0, delta, delta)
    _, poisoned = shared_sides(lam, lam, 0, delta, delta, True)
    require(lhs == rhs == ZERO and poisoned == (-1, 0),
            "The literal-zero regression did not detect the incorrect unit value")
    return {
        "cases": cases,
        "coefficient_ring": "Z[omega], omega^2 + omega + 1 = 0",
        "prime_phase_grid": "a,b in 0..5; phases a+i and b+2i modulo 6",
        "zero_patterns": "all 8 masks; the second mask is equal or cyclically rotated",
        "exclusion_masks": 8,
        "axis_test_pairs": 2,
        "literal_zero_regression": {
            "forced_r1_and_r2": PRIMES[0],
            "expected": list(ZERO),
            "incorrect_principal_zero_replacement": list(poisoned),
        },
    }


def mask_expansion(e, g, h, f):
    """Expand e/g and e/h first; expand residual g'/h' by ell last."""
    first, full, poisoned = 0, 0, 0
    dj_terms, ell_terms, overlaps = 0, 0, 0
    for d, j in itertools.product(SUBSETS[e & g], SUBSETS[e & h]):
        if d & j or (d | j) & f:
            continue
        ep, gp, hp = e ^ (d | j), g ^ d, h ^ j
        fixed = f | d | j
        if ep & fixed or gp & fixed or hp & fixed:
            continue
        dj_terms += 1
        if not gp & hp:
            first += MU[gp] * MU[hp]
        for ell in SUBSETS[gp & hp]:
            gg, hh = gp ^ ell, hp ^ ell
            require(not (ell & fixed or (gg | hh) & (fixed | ell)),
                    "The explicitly retained squarefree/exclusion masks failed")
            term = MU[ell] * MU[gg] * MU[hh]
            full += term
            ell_terms += 1
            if ep & ell:
                overlaps += 1
            else:
                poisoned += term
    return first, full, poisoned, (dj_terms, ell_terms, overlaps)


def check_allocation_masks():
    cases = wrong_mask_failures = 0
    totals = [0, 0, 0]
    for e, g, h, f in itertools.product(MASKS, repeat=4):
        expected = MU[g] * MU[h] * int(
            not (e & g or e & h or g & h or f & (e | g | h)))
        first, full, poisoned, counts = mask_expansion(e, g, h, f)
        require(first == expected, f"Two-divisor mask identity failed: {e,g,h,f}")
        require(full == expected, f"Three-divisor mask identity failed: {e,g,h,f}")
        wrong_mask_failures += int(poisoned != expected)
        totals = [x + y for x, y in zip(totals, counts)]
        cases += 1
    first, full, poisoned, _ = mask_expansion(1, 1, 1, 0)
    require(first == full == 0 and poisoned == 1,
            "The e'=ell regression did not detect the forbidden extra mask")
    require(totals[2] > 0 and wrong_mask_failures > 0,
            "No shared ell/e' configurations were exercised")

    # Row and cubic zero masks factor exactly after e=d*j*e'. The pointwise
    # test is exhaustive on three formal primes, including every row zero.
    factor_cases = 0
    for e, f, k, n in itertools.product(MASKS, repeat=4):
        for d, j in itertools.product(SUBSETS[e], repeat=2):
            if d & j:
                continue
            ep = e ^ (d | j)
            row_left = int(not k & (e | f))
            row_right = int(not k & (d | j | f)) * int(not k & ep)
            cubic_left = int(not n & e)
            cubic_right = int(not n & (d | j)) * int(not n & ep)
            require(row_left == row_right and cubic_left == cubic_right,
                    "A row or cubic nonunit mask was lost under e=d*j*e'")
            factor_cases += 1
    return {
        "allocation_cases": cases,
        "admissible_d_j_terms": totals[0],
        "shared_ell_terms": totals[1],
        "terms_with_ell_sharing_e_prime": totals[2],
        "row_and_cubic_mask_factorizations": factor_cases,
        "cases_detecting_incorrect_e_prime_ell_exclusion": wrong_mask_failures,
        "minimal_extra_mask_regression": {
            "e": PRIMES[0], "g": PRIMES[0], "h": PRIMES[0], "f": 1,
            "expected": 0, "with_incorrect_e_prime_ell_exclusion": poisoned,
        },
        "retained_masks": [
            "(d,j)=1; (dj,f)=1; (e',djf)=1",
            "(g',fdj)=(h',fdj)=1, followed by the shared ell expansion",
            "(ell,fdj)=1; (g'',ell fdj)=(h'',ell fdj)=1",
            "(e',ell) is unrestricted",
        ],
    }


def check_rational_maxima():
    vertices = ((Q(0), Q(0)), (Q(1, 2), Q(0)), (Q(0), Q(1, 3)))
    output = []
    for beta in (Q(13, 24), Q(2, 3), Q(3, 4), Q(11, 12), Q(1)):
        require(Q(1, 2) < beta <= 1, "Beta lies outside the stated algebraic range")
        objectives = (
            ("first", 2 * beta - 3, 2 * beta - 2, Q(0)),
            ("middle", 2 * beta - 1, 2 * beta + 1, (2 * beta + 1) / 3),
            ("third", 2 * beta - 2, 2 * beta, 2 * beta / 3),
        )
        maxima = {}
        for name, a, b, expected in objectives:
            values = tuple(a * g + b * z for g, z in vertices)
            require(max(values) == expected, f"Vertex maximum failed: {beta,name}")
            if name == "first":
                certificate = {"g": -a, "z": -b}
            else:
                # For s=1-2g-3z, expected - a*g - b*z =
                # expected*s + (2*expected-a)*g, an exact nonnegative certificate.
                require(3 * expected == b, "Slack certificate z coefficient failed")
                certificate = {"slack": expected, "g": 2 * expected - a}
            require(all(c >= 0 for c in certificate.values()),
                    f"Nonnegative coefficient certificate failed: {beta,name}")
            maxima[name] = {
                "maximum": str(expected),
                "maximizing_vertices": [
                    [str(g), str(z)] for (g, z), v in zip(vertices, values) if v == expected
                ],
                "nonnegative_gap_certificate": {k: str(v) for k, v in certificate.items()},
            }
        middle = (1 + 2 * beta) / 3
        third = (2 + 2 * beta) / 3
        h = (5 - 2 * beta) / 6
        require(h <= 1 and h <= 1 - beta / 2, "The stated row threshold is not strongest")
        energy = (h + 1, 2 * h + middle, Q(4, 3) * h + third)
        require(max(energy) <= 2 and energy[1] == 2, "The exact target exponent failed")
        output.append({
            "beta": str(beta),
            "maxima": maxima,
            "balanced_column_exponents": [str(middle), str(third)],
            "row_threshold": str(h),
            "energy_exponents_at_threshold": [str(x) for x in energy],
        })
    return {
        "domain": "g>=0, z>=0, 2g+3z<=1; G=D^g, Z=D^z, B=D",
        "slack": "s=1-2g-3z>=0",
        "interpretation": "Exact rational linear inequalities; no analytic bound is checked",
        "cases": output,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {
        "schema": "cube-inverse-finite-algebra-v1",
        "status": "PASS_FINITE_ALGEBRA",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Finite formal prime-support identities and rational exponent algebra only.",
        "not_checked": [
            "Analytic scalar estimates, automorphy, cusp coefficients, or large sieves.",
            "The analytic exact cutoff, arbitrary rows, centered covariance, or any RH claim.",
        ],
        "formal_prime_norm_labels": list(PRIMES),
        "shared_divisor_identity": check_shared_divisor(),
        "allocation_masks": check_allocation_masks(),
        "rational_maximization": check_rational_maxima(),
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
