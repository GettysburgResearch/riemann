#!/usr/bin/env python3
"""Exact finite-CRT checks for the minimum-degree mark projection.

Standard library only; every acceptance condition is an explicit exception.
This does not test the asymptotic distribution of primes or a zero-free claim.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import comb, gcd, prod
import json


def require(condition, description):
    if not condition:
        raise RuntimeError(description)


def mean(values):
    return sum(values, F(0)) / len(values)


def subproduct(values, indices):
    return prod((values[i] for i in indices), start=F(1))


def all_subsets(n):
    return [s for j in range(n + 1) for s in combinations(range(n), j)]


def derivative_moments(primes, rho):
    # Direct independent Bernoulli law; separate from residue enumeration.
    first, second = F(0), F(0)
    for bits in product((0, 1), repeat=len(primes)):
        probability = prod(
            (F(1, p - 1) if bit else F(p - 2, p - 1)
             for p, bit in zip(primes, bits)), start=F(1)
        )
        count = sum(bits)
        mark = F(count) * rho ** (count - 1) if count else F(0)
        first += probability * mark
        second += probability * mark * mark
    return first, second / first**2


def run_case(bands, rho):
    primes = [p for band in bands for p in band]
    require(len(set(primes)) == len(primes), "bands are disjoint")
    modulus = prod(primes)
    residues = [a for a in range(modulus) if gcd(a, modulus) == 1]
    n = len(bands)
    moments = [derivative_moments(band, rho) for band in bands]
    qs = [1 / r for _, r in moments]
    values = []
    for a in residues:
        row = []
        for band, (normalizer, _) in zip(bands, moments):
            count = sum((a + 2) % p == 0 for p in band)
            mark = F(count) * rho ** (count - 1) if count else F(0)
            row.append(mark / normalizer)
        values.append(row)
    for i, (_, second) in enumerate(moments):
        require(mean([row[i] for row in values]) == 1, "first moment")
        require(mean([row[i] ** 2 for row in values]) == second,
                "second moment from independent Bernoulli law")
    subsets = all_subsets(n)
    terms = {s: [subproduct(row, s) for row in values] for s in subsets}
    report = []
    for k in range(1, n + 1):
        admitted = [s for s in subsets if len(s) >= k]
        coefficients = {
            s: (-1)**(len(s) - k) * comb(len(s) - 1, k - 1)
               * subproduct(qs, s)
            for s in admitted
        }
        residual = [
            1 - sum((coefficients[s] * terms[s][j] for s in admitted), F(0))
            for j in range(len(residues))
        ]
        expected = sum(
            (prod((qs[i] if i in s else 1 - qs[i] for i in range(n)),
                  start=F(1)) for s in subsets if len(s) < k), F(0)
        )
        actual = mean([v*v for v in residual])
        require(actual == expected, "Poisson-binomial residual identity")
        for s in admitted:
            require(mean([v * t for v, t in zip(residual, terms[s])]) == 0,
                    "residual orthogonal to every admitted product")
        perturbation = [
            sum((F((-1)**j, j + 2) * terms[s][i]
                 for j, s in enumerate(admitted)), F(0))
            for i in range(len(residues))
        ]
        perturbed = mean([(r - h)**2 for r, h in zip(residual, perturbation)])
        require(perturbed == actual + mean([h*h for h in perturbation]),
                "Pythagorean optimality under an arbitrary admitted perturbation")
        changed = admitted[0]
        mutant = [r + coefficients[changed] * t
                  for r, t in zip(residual, terms[changed])]
        require(mean([r*r for r in mutant]) > actual,
                "negative control: deleting a nonzero coefficient worsens error")
        report.append({"minimum_degree": k, "residual_squared": str(actual),
                       "orthogonality_conditions": len(admitted)})
    return {"bands": bands, "rho": str(rho), "modulus": modulus,
            "reduced_residues": len(residues), "cases": report}


def check_symmetric_formula():
    cases = []
    for n, k, r in [(8, 1, F(2)), (8, 3, F(2)),
                    (8, 5, F(3, 2)), (10, 4, F(5, 2))]:
        q = 1 / r
        result = F(0)
        # U_i is r with probability q, and zero otherwise.
        for active in range(n + 1):
            probability = comb(n, active) * q**active * (1-q)**(n-active)
            projection = sum(
                ((-1)**(j-k) * comb(j-1, k-1) * comb(active, j)
                 for j in range(k, active + 1)), 0
            )
            result += probability * (1-projection)**2
        expected = sum((comb(n, j)*q**j*(1-q)**(n-j)
                        for j in range(k)), F(0))
        require(result == expected, "homogeneous binomial-tail formula")
        cases.append({"N": n, "minimum_degree": k, "R": str(r),
                      "residual_squared": str(result)})
    return cases


if __name__ == "__main__":
    records = [run_case([[3], [5], [7]], F(1, 2)),
               run_case([[3, 5], [7], [11], [13]], F(1, 2)),
               run_case([[3], [5, 7], [11]], F(2, 3))]
    print(json.dumps({"status": "PASS", "arithmetic": "exact rational",
                      "finite_CRT": records,
                      "symmetric_controls": check_symmetric_formula()}, indent=2))
