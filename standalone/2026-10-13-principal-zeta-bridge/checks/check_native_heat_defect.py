#!/usr/bin/env python3
"""Exact finite diagnostics for the native heat-defect proof note.

This checks all 7^4 character-value patterns with the exact residue-field
multiplicities. It is algebraic validation, not a short-row moment estimate
or an authenticated replay of the repository's original Poisson transform.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import itertools
import json
from math import isqrt
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# Q(zeta_6), represented by a+b*zeta, where zeta^2=zeta-1.
ZERO = (0, 0)
ONE = (1, 0)


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def sub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def mul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c + b * d)


def scale(c, z):
    return (c * z[0], c * z[1])


def conj(z):
    return (z[0] + z[1], -z[1])


def norm(z):
    a, b = z
    return a * a + a * b + b * b


def sumz(values):
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


def prodz(values):
    result = ONE
    for value in values:
        result = mul(result, value)
    return result


ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
VALUES = (ZERO,) + ROOTS
NORMS = (73, 109, 181, 277)
POINTS = tuple(itertools.product(range(7), repeat=4))
COLUMNS = tuple(frozenset(s) for s in itertools.combinations(range(4), 2))
COP_PAIRS = tuple((s, t) for s in COLUMNS for t in COLUMNS if not s & t)
RHO = tuple(Fraction(q - 1, q) for q in NORMS)
LOCAL_WEIGHTS = tuple(
    (Fraction(1, q),) + (Fraction(q - 1, 6 * q),) * 6 for q in NORMS
)


def monomial(point, subset):
    return prodz(VALUES[point[p]] for p in subset)


def column_polynomial(point, coefficients=None):
    if coefficients is None:
        coefficients = {s: 2 for s in COLUMNS}
    return sumz(scale(coefficients[s], monomial(point, s)) for s in COLUMNS)


def changed(point, p, value):
    result = list(point)
    result[p] = value
    return tuple(result)


def average_scalar(table, point, p):
    return sum(LOCAL_WEIGHTS[p][j] * table[changed(point, p, j)] for j in range(7))


def average_ring(table, point, p):
    return sumz(
        scale(LOCAL_WEIGHTS[p][j], table[changed(point, p, j)])
        for j in range(7)
    )


def cop_covariance(point, coefficients=None):
    if coefficients is None:
        coefficients = {s: Fraction(2) for s in COLUMNS}
    return sumz(
        scale(coefficients[s] * coefficients[t],
              mul(monomial(point, s), conj(monomial(point, t))))
        for s, t in COP_PAIRS
    )


def rational(value):
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--proof", type=Path,
        default=Path(__file__).with_name("NATIVE_HEAT_DEFECT_AND_PRIME_REMOVAL.md"),
    )
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).with_name("native_heat_defect_diagnostic.json"),
    )
    args = parser.parse_args()
    proof_hash = hashlib.sha256(args.proof.read_bytes()).hexdigest()
    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    for q, weights in zip(NORMS, LOCAL_WEIGHTS):
        require(q % 6 == 1, "Nonintegral sextic multiplicities")
        require(all(q % d for d in range(2, isqrt(q) + 1)), "Norm not prime")
        require(sum(weights) == 1, "Weights do not sum to one")
        require(sumz(scale(weights[j], VALUES[j]) for j in range(7)) == ZERO,
                "Local character not centered")
        require(sum(weights[j] * norm(VALUES[j]) for j in range(7)) == Fraction(q - 1, q),
                "Nonunit zero mass lost")

    require(len(COP_PAIRS) == 6, "Wrong native complementary-pair count")
    f_table = {point: column_polynomial(point) for point in POINTS}
    energy_table = {point: norm(value) for point, value in f_table.items()}
    cov_table = {point: cop_covariance(point) for point in POINTS}
    require(all(value[1] == 0 for value in cov_table.values()), "Covariance not real")

    counts = {"local_character_patterns": len(POINTS),
              "local_decomposition_checks": 0,
              "weighted_heat_checks": 0,
              "coprime_defect_checks": 0,
              "heat_intertwining_checks": 0,
              "mobius_gauge_checks": 0,
              "common_factor_mask_checks": 0}
    generator_choices = ((1, 1, 1, 1), (1, 2, 3, 4))

    for point in POINTS:
        f = f_table[point]
        gamma = []
        direct_energy_defect = []
        for p in range(4):
            f0 = sumz(scale(2, monomial(point, s)) for s in COLUMNS if p not in s)
            f1 = sumz(scale(2, monomial(point, s - {p})) for s in COLUMNS if p in s)
            require(add(f0, mul(VALUES[point[p]], f1)) == f,
                    "Squarefree decomposition failed")
            ep_energy = average_scalar(energy_table, point, p)
            require(ep_energy == norm(f0) + RHO[p] * norm(f1),
                    "Direct local expectation disagrees with decomposition")
            gp = (norm(VALUES[point[p]]) + RHO[p]) * norm(f1)
            require(gp >= 0, "Negative positive innovation")
            gamma.append(gp)
            direct_energy_defect.append(energy_table[point] - ep_energy)
            counts["local_decomposition_checks"] += 1

        for lambdas in generator_choices:
            af = sumz(
                scale(2 * sum(lambdas[p] for p in s), monomial(point, s))
                for s in COLUMNS
            )
            product = mul(conj(f), af)
            lhs = 2 * product[0] + product[1]
            rhs = sum(lambdas[p] * (gamma[p] + direct_energy_defect[p]) for p in range(4))
            require(lhs == rhs, "Weighted heat/defect identity failed")
            counts["weighted_heat_checks"] += 1

            # Independent coordinate averaging of the complete coprime kernel.
            measured_defect = sumz(
                scale(lambdas[p], sub(cov_table[point], average_ring(cov_table, point, p)))
                for p in range(4)
            )
            coefficient_derivative = sumz(
                scale(4 * (sum(lambdas[p] for p in s) + sum(lambdas[p] for p in t)),
                      mul(monomial(point, s), conj(monomial(point, t))))
                for s, t in COP_PAIRS
            )
            require(measured_defect == coefficient_derivative,
                    "Coprime covariance not wholly in physical defect")
            require(all(not (s & t) for s, t in COP_PAIRS),
                    "Positive innovation has a coprime coefficient")
            counts["coprime_defect_checks"] += 1

    # Apply the coordinate Markov kernels to the complete table, not the
    # predicted eigenvalue formula, then compare to filtered coefficients.
    noise = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5))
    smoothed = dict(cov_table)
    for p, r in enumerate(noise):
        previous = smoothed
        smoothed = {
            point: add(scale(r, previous[point]),
                       scale(1 - r, average_ring(previous, point, p)))
            for point in POINTS
        }
    filtered = {}
    for s in COLUMNS:
        coefficient = Fraction(2)
        for p in s:
            coefficient *= noise[p]
        filtered[s] = coefficient
    for point in POINTS:
        require(smoothed[point] == cop_covariance(point, filtered),
                "Exact coprime heat intertwining failed")
        counts["heat_intertwining_checks"] += 1

    # Include every degree, so the Mobius gauge also tests odd prime counts.
    subsets = tuple(frozenset(s) for j in range(5)
                    for s in itertools.combinations(range(4), j))
    for point in POINTS:
        shifted = tuple(0 if state == 0 else ((state - 1 + 3) % 6) + 1 for state in point)
        unsigned_shifted = prodz(add(ONE, VALUES[shifted[p]]) for p in range(4))
        mobius_original = sumz(scale((-1) ** len(s), monomial(point, s)) for s in subsets)
        require(unsigned_shifted == mobius_original, "Mobius CRT gauge failed")
        require(tuple(state == 0 for state in point) == tuple(state == 0 for state in shifted),
                "Gauge changed a nonunit mask")
        counts["mobius_gauge_checks"] += 1

    common_factors = tuple(frozenset(s) for j in range(3)
                           for s in itertools.combinations(range(4), j))
    for point in POINTS:
        diagonal = sum(4 * norm(monomial(point, s)) for s in COLUMNS)
        original_centered = energy_table[point] - diagonal
        reconstructed = ZERO
        for g in common_factors:
            residuals = tuple(s - g for s in COLUMNS if g <= s)
            primitive = sumz(
                scale(4 * (-1) ** (len(a) + len(b)),
                      mul(monomial(point, a), conj(monomial(point, b))))
                for a in residuals for b in residuals
                if not (a & b) and (a or b)
            )
            reconstructed = add(reconstructed,
                                scale(norm(monomial(point, g)), primitive))
        require(reconstructed == (original_centered, 0),
                "Common-factor decomposition lost the physical diagonal or a mask")
        counts["common_factor_mask_checks"] += 1

    unit = (1, 1, 1, 1)
    reciprocal_sum = sum(Fraction(1, q) for q in NORMS)
    gamma_unit = Fraction(288) - 36 * reciprocal_sum
    defect_unit = Fraction(288) + 36 * reciprocal_sum
    require(f_table[unit] == (12, 0), "Native unit value is wrong")
    require(energy_table[unit] == 144, "Native unit energy is wrong")
    require(cov_table[unit] == (24, 0), "Native coprime witness is wrong")
    require(gamma_unit + defect_unit == 576, "Unit defect split is wrong")
    require(sum(average_scalar({p: cov_table[p][0] for p in POINTS}, unit, j)
                for j in range(4)) == 0, "Coprime local means not zero")

    report = {
        "status": "PASS",
        "proof_sha256": proof_hash,
        "checker_sha256": script_hash,
        "arithmetic": "Exact integers and fractions in Q(zeta_6), zeta_6^2=zeta_6-1",
        "coverage": counts,
        "prime_norms": list(NORMS),
        "generator_weights_checked": [list(x) for x in generator_choices],
        "native_model": "Squarefree two-factor convolution of four singleton prime coefficients",
        "unit_tuple": {
            "polynomial_value": 12,
            "energy": 144,
            "coprime_off_product_covariance": 24,
            "positive_innovation_energy": rational(gamma_unit),
            "physical_defect_energy": rational(defect_unit),
            "coprime_positive_innovation": 0,
            "coprime_physical_defect": 96,
        },
        "not_proved": [
            "Transfer from complete CRT rows to the original Schwartz physical rows",
            "Any asymptotic native moment, signed comparison saving, or zero-free improvement",
            "Authenticated primitive replay of the imported signed auxiliary and Poisson identities",
        ],
    }
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "proof_sha256": proof_hash,
                      "checks": sum(counts.values()), "output": str(args.output)}, sort_keys=True))


if __name__ == "__main__":
    main()
