#!/usr/bin/env python3
"""Exact finite diagnostics for the principal row kernel and joint cube inverse.

These tests authenticate finite character/divisor identities only. They do not
verify Poisson decay, an infinite norm estimate, theta foundations, or RH.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import argparse

if not __debug__:
    raise RuntimeError("This finite checker requires assertions; do not use Python -O.")

ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
ONE = (1, 0)
ZERO = (0, 0)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] + x[1] * y[1])


def conjugate(x):
    return (x[0] + x[1], -x[1])


def scale(x, a):
    return (a * x[0], a * x[1])


def primitive_root(p):
    for g in range(2, p):
        if len({pow(g, j, p) for j in range(p - 1)}) == p - 1:
            return g
    raise ValueError(p)


def residue_table(p):
    g = primitive_root(p)
    table = {0: ZERO}
    for j in range(p - 1):
        table[pow(g, j, p)] = ROOTS[j % 6]
    return table


def local_value(table, x, exponent):
    if exponent == 0:
        return ONE
    if x == 0:
        return ZERO
    z = table[x]
    index = ROOTS.index(z)
    return ROOTS[(index * exponent) % 6]


def norm(exponents, primes):
    value = 1
    for e, p in zip(exponents, primes):
        value *= p ** e
    return value


def radical(exponents):
    return tuple(int(e > 0) for e in exponents)


def sf_divisors(exponents):
    return list(product(*[(0, 1) if e else (0,) for e in exponents]))


def mobius(exponents):
    return (-1) ** sum(exponents)


def partial_mobius(exponents, cutoff, primes):
    return sum(mobius(h) for h in sf_divisors(exponents)
               if norm(h, primes) <= cutoff)


def disjoint(x, y):
    return all(not (a and b) for a, b in zip(x, y))


def rational(x):
    return f"{x.numerator}/{x.denominator}"


def run():
    counts = {}
    local = {}
    local_checks = 0
    for p in (7, 13, 61, 67):
        table = residue_table(p)
        local[p] = {}
        for a, b in product(range(14), repeat=2):
            total = ZERO
            for x in range(p):
                total = add(total, mul(local_value(table, x, a),
                                       conjugate(local_value(table, x, b))))
            observed = (Fraction(total[0], p), Fraction(total[1], p))
            if a == b == 0:
                expected = (Fraction(1), Fraction(0))
            elif (a - b) % 6 == 0:
                expected = (Fraction(p - 1, p), Fraction(0))
            else:
                expected = (Fraction(0), Fraction(0))
            assert observed == expected, (p, a, b, observed, expected)
            local[p][a, b] = expected[0]
            local_checks += 1
    counts["local_residue_correlations"] = local_checks

    primes = (7, 13)
    ms = list(product(range(2), repeat=2))
    ds = list(product(range(4), repeat=2))
    columns = [(m, d, tuple(x + 3 * y for x, y in zip(m, d)))
               for m in ms for d in ds]
    alias_checks = 0
    off_product_principal_pairs = 0
    for m, d, n in columns:
        for mp, dp, np in columns:
            principal = all((x - y) % 6 == 0 for x, y in zip(n, np))
            reduced = (m == mp and
                       all((x - y) % 2 == 0 for x, y in zip(d, dp)))
            assert principal == reduced
            density = Fraction(1)
            for p, a, b in zip(primes, n, np):
                density *= local[p][a, b]
            assert bool(density) == principal
            if principal and n != np:
                off_product_principal_pairs += 1
            alias_checks += 1
    counts["cube_principal_pair_classifications"] = alias_checks

    mask_checks = 0
    for a, n, q, f in product(ms, repeat=4):
        if not disjoint(a, n):
            continue
        for d in ds:
            excluded = tuple(int(x or y or z) for x, y, z in zip(a, q, f))
            raw_allowed = disjoint(tuple(int(x or y) for x, y in zip(a, n)),
                                   tuple(int(x or y) for x, y in zip(q, f)))
            total = 0
            for h in sf_divisors(d):
                b = tuple(x - y for x, y in zip(d, h))
                allowed = raw_allowed and disjoint(h, excluded) and disjoint(b, excluded)
                if allowed:
                    total += mobius(h)
            expected = int(raw_allowed and all(x == 0 for x in d))
            assert total == expected, (a, n, q, f, d, total, expected)
            mask_checks += 1
    counts["masked_complete_cube_inverses"] = mask_checks

    # Complete multiplicativity with zero extension, including h,b sharing primes.
    phase_checks = 0
    for p in primes:
        table = residue_table(p)
        for h, b, x in product(range(2), range(4), range(p)):
            lhs = mul(local_value(table, x, 3 * h),
                      local_value(table, x, 3 * b))
            rhs = local_value(table, x, 3 * (h + b))
            assert lhs == rhs
            phase_checks += 1
    counts["cube_phase_zero_checks"] = phase_checks

    lcm_checks = 0
    for d, dp in product(ds, repeat=2):
        union = tuple(int(bool(x or y)) for x, y in zip(d, dp))
        for cutoff in (Fraction(1, 2), 1, 7, 13, 20, 91, 200):
            lhs = 0
            for h, hp in product(sf_divisors(d), sf_divisors(dp)):
                union_h = tuple(max(x, y) for x, y in zip(h, hp))
                if norm(union_h, primes) <= cutoff:
                    lhs += mobius(h) * mobius(hp)
            rhs = partial_mobius(union, cutoff, primes)
            assert lhs == rhs, (d, dp, cutoff, lhs, rhs)
            lcm_checks += 1
    counts["joint_lcm_cutoffs"] = lcm_checks

    # An lcm cutoff need not preserve cancellations of two rectangular cutoffs.
    left, right, cutoff = (2, 0), (0, 2), 20
    rectangle = partial_mobius(left, cutoff, primes) * partial_mobius(right, cutoff, primes)
    joint_lcm = partial_mobius((1, 1), cutoff, primes)
    assert rectangle == 0 and joint_lcm == -1

    a2_vectors = list(product((0, 1, 3, 4), repeat=2))
    a2_checks = 0
    for n, np in product(a2_vectors, repeat=2):
        assert (n == np) == all((a - b) % 6 == 0 for a, b in zip(n, np))
        nn, nnp = norm(n, primes), norm(np, primes)
        rn, rnp = norm(radical(n), primes), norm(radical(np), primes)
        gcd_rad = norm(tuple(int(bool(a and b)) for a, b in zip(n, np)), primes)
        union_rad = norm(tuple(int(bool(a or b)) for a, b in zip(n, np)), primes)
        assert Fraction(nn * nnp, union_rad) == Fraction(nn, rn) * Fraction(nnp, rnp) * gcd_rad
        for exponents in (n, np):
            correction = tuple(int(e in (3, 4)) for e in exponents)
            fourth = tuple(int(e == 4) for e in exponents)
            defect = norm(exponents, primes) // norm(radical(exponents), primes)
            assert defect == norm(correction, primes) ** 2 * norm(fourth, primes)
        a2_checks += 1
    counts["a2_no_alias_and_radical_defect"] = a2_checks

    # This is an actual nonunit-zero principal alias in two physical cube columns.
    witness_primes = (7, 61, 67)
    d, dp = (1, 2, 0), (1, 0, 2)
    mr = partial_mobius(d, 100, witness_primes)
    mrp = partial_mobius(dp, 100, witness_primes)
    mlcm = partial_mobius((1, 1, 1), 100, witness_primes)
    assert mr == mrp == -1 and mlcm == -2
    assert partial_mobius(d, norm(d, witness_primes), witness_primes) == 0
    assert partial_mobius(dp, norm(dp, witness_primes), witness_primes) == 0
    density = Fraction(1)
    for p in witness_primes:
        density *= Fraction(p - 1, p)
    assert density == Fraction(23760, 28609)
    # Both physical cube norms fit into one fixed factor-of-two annulus.
    ratio = Fraction(norm(dp, witness_primes) ** 3, norm(d, witness_primes) ** 3)
    assert 1 < ratio < 2

    # Two distinct squarefree columns of norms 7 and 13 fit the U=7 annulus.
    # At the unit row, every character is one. This tests centered arithmetic only.
    M, U = 2, 7
    reflected_energy = Fraction(M * M, U)
    reflected_diagonal = Fraction(M, U)
    assert reflected_energy - reflected_diagonal == Fraction(2, 7)

    script_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "PASS",
        "producer_sha256": script_sha,
        "finite_scope": "Exact root-of-unity, divisor, zero-mask, and rational identities; no analytic theorem verification.",
        "counts": counts,
        "off_product_principal_pairs_in_cube_grid": off_product_principal_pairs,
        "truncated_alias_witness": {
            "primes": list(witness_primes),
            "cutoff": 100,
            "left_cube_exponents": list(d),
            "right_cube_exponents": list(dp),
            "left_partial_mobius": mr,
            "right_partial_mobius": mrp,
            "lcm_partial_mobius": mlcm,
            "complete_principal_density": rational(density),
            "physical_cube_norm_ratio": rational(ratio),
            "complete_inverse_coefficients": [0, 0],
        },
        "lcm_not_rectangular_witness": {"cutoff": 20, "rectangle": rectangle, "lcm": joint_lcm},
        "centered_reflected_unit_witness": {
            "U": U, "column_norms": [7, 13],
            "energy": rational(reflected_energy),
            "product_diagonal": rational(reflected_diagonal),
            "centered": rational(reflected_energy - reflected_diagonal),
        },
        "not_verified": [
            "Poisson summation or uniform Fourier decay",
            "the infinite principal-energy R^-1 bound",
            "the imported theta, Gauss, or large-sieve foundations",
            "a centered original fourth moment, a zero-free boundary, or RH",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).with_name("principal_alias_checks.json"),
        help="Write the deterministic report here.")
    parser.add_argument(
        "--manuscript", type=Path,
        default=Path(__file__).with_name("CENTERED_COVARIANCE_AND_CUBE_ALIASES.md"),
        help="Manuscript whose exact bytes are bound in the report.")
    parser.add_argument(
        "--expected-manuscript-sha256",
        help="Refuse a manuscript whose SHA-256 differs from this frozen value.")
    args = parser.parse_args()
    manuscript_sha = hashlib.sha256(args.manuscript.read_bytes()).hexdigest()
    if (args.expected_manuscript_sha256 is not None
            and manuscript_sha != args.expected_manuscript_sha256):
        raise RuntimeError("The manuscript does not match the expected SHA-256.")
    result = run()
    result["manuscript_sha256"] = manuscript_sha
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

