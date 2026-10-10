#!/usr/bin/env python3
"""Exact finite diagnostics for the joint-divisor research packet.

This does not evaluate an infinite theta series, authenticate a Hecke
subconvexity proof, or certify a generalized moment.  It reconstructs
the stated finite algebra from primitive rational/cyclotomic operations.
No stored report is read.  All checks survive Python optimization.
"""

from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import argparse
import hashlib
import json


COUNTS = {}


def require(ok, group, detail):
    if not ok:
        raise RuntimeError(f"{group}: {detail}")
    COUNTS[group] = COUNTS.get(group, 0) + 1


ZERO, ONE = (0, 0), (1, 0)


def mul(x, y):
    # Exact Z[omega], omega^2 + omega + 1 = 0.
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def power(x, n):
    # n=0 means an absent physical prime factor, not an exponent-zero
    # residue character with a retained nonunit mask.
    if n < 0:
        raise ValueError("nonnegative physical exponent required")
    ans = ONE
    for _ in range(n):
        ans = mul(ans, x)
    return ans


def mask(x):
    return ONE if x != ZERO else ZERO


def many(*args):
    ans = ONE
    for x in args:
        ans = mul(ans, x)
    return ans


def check_zero_extensions():
    roots = tuple(power((1, 1), j) for j in range(6))
    require(len(set(roots)) == 6, "cyclotomic_setup", "six distinct units")
    require(power((1, 1), 6) == ONE, "cyclotomic_setup", "sixth root")
    values = (ZERO,) + roots
    for j in range(6):
        total = ZERO
        for x in roots:
            total = add(total, power(x, j))
        require(total == ((6, 0) if j == 0 else ZERO),
                "unit_projection", j)
    for nu, qflag, fflag in product(range(12), (0, 1), (0, 1)):
        exponent = nu + 6 * qflag + 4 * fflag
        for a, n, b in product(values, repeat=3):
            lhs = many(power(a, exponent), power(n, exponent),
                       power(b, 3 * exponent))
            rhs = many(power(a, nu), power(n, nu), power(b, 3 * nu),
                       power(a, 4 * fflag), power(n, 4 * fflag),
                       mask(b) if fflag else ONE,
                       many(mask(a), mask(n), mask(b)) if qflag else ONE)
            require(lhs == rhs, "mixed_row_zero_identities",
                    (nu, qflag, fflag, a, n, b))
    require(power(ZERO, 6) != ONE, "negative_controls", "drop q mask")
    require(power(ZERO, 12) != ONE, "negative_controls", "drop cube f mask")
    require(power(ZERO, 6) == mask(ZERO),
            "zero_residue_class", "positive physical multiple of six")


def poly_add(p, q, sign=1):
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, F(0)) + sign * c
        if out[m] == 0:
            del out[m]
    return out


def poly_mul(p, q):
    # Variables A,z,e; quotient by e^2=1, no numerical substitution.
    out = {}
    for (a, z, e), c in p.items():
        for (aa, zz, ee), cc in q.items():
            m = (a + aa, z + zz, (e + ee) % 2)
            out[m] = out.get(m, F(0)) + c * cc
    return {m: c for m, c in out.items() if c}


def check_theta_algebra():
    one = {(0, 0, 0): F(1)}
    av = {(1, 0, 0): F(1)}
    zv = {(0, 1, 0): F(1)}
    ev = {(0, 0, 1): F(1)}
    den = poly_add(one, poly_mul(zv, zv), -1)
    lhs = poly_mul(poly_add(one, poly_mul(av, ev), -1), den)
    rhs = poly_mul(poly_add(one, poly_mul(zv, ev), -1),
                   poly_add(den, poly_mul(poly_add(zv, av, -1),
                                         poly_add(zv, ev))))
    require(lhs == rhs, "formal_theta_identity",
            "(1-Ae)/(1-ze)=1+(z-A)(z+e)/(1-z^2)")
    wrong = poly_mul(poly_add(one, poly_mul(zv, ev), -1),
                     poly_add(den, poly_mul(poly_add(zv, av),
                                           poly_add(zv, ev))))
    require(lhs != wrong, "negative_controls", "wrong numerator sign")
    for a0, z0, e in product((F(1, 7), F(-1, 11), F(2, 13)),
                             (F(1, 9), F(-1, 5), F(1, 17)), (-1, 1)):
        e1 = (z0 - a0) / (1 - z0 * z0)
        e0 = z0 * e1
        require((1 - a0 * e) / (1 - z0 * e) == 1 + e0 + e1 * e,
                "theta_rational_fixtures", (str(a0), str(z0), e))


def correction_powers(eta):
    # Child multipliers of X, ell, m, U in C,J,E.
    scales = {
        "X": (F(-3, 2), F(-3, 2), F(-2)),
        "ell": (F(1), F(1), F(1)),
        "m": (F(1, 3), F(1, 3), F(2, 3)),
        "U": (-eta, -eta, F(0)),
    }
    # Five parent energy monomials: X, ell, m, U exponents.
    monomials = (
        (F(1), F(0), F(0), F(0)),
        (F(5, 12), F(1), F(0), F(7, 4)),
        (F(2, 3), F(0), F(1), F(2)),
        (F(2), F(0), F(0), F(-3)),
        (F(4, 3), F(0), F(0), F(-2)),
    )
    outer = (F(-1), F(-1), F(-3, 2))
    result = []
    for row in monomials:
        exps = tuple(-(outer[j] + sum(row[i] * scales[name][j]
                                      for i, name in enumerate(scales)) / 2)
                     for j in range(3))
        result.append(exps)
    return result


def check_a2_exponents():
    expected = [
        (F(7, 4), F(7, 4), F(5, 2)),
        (F(5, 4), F(5, 4), F(17, 12)),
        (F(11, 6), F(11, 6), F(11, 6)),
        (F(7, 4), F(7, 4), F(7, 2)),
        (F(3, 2), F(3, 2), F(17, 6)),
    ]
    actual = correction_powers(F(1, 2))
    for i, (row, wanted) in enumerate(zip(actual, expected)):
        require(row == wanted, "a2_norm_weights", i)
        for exponent in row:
            require(exponent > 1, "a2_absolute_summability", str(exponent))
    for eta in (F(1, 4), F(1, 2), F(3, 4), F(99, 100)):
        require(all(x > 1 for row in correction_powers(eta) for x in row),
                "a2_cutoff_domain", str(eta))
    for eta in (F(0), F(3, 14), F(1)):
        require(not all(x > 1 for row in correction_powers(eta) for x in row),
                "negative_controls", f"nonstrict eta={eta}")
    require(correction_powers(F(0))[1][0] == F(13, 16),
            "common_cutoff_obstruction", "C exponent")
    cartan = ((2, -1), (-1, 2))
    for vector, wanted in (((1, 2), (0, 0)), ((2, 1), (0, 0)),
                           ((2, 2), (2, 2))):
        paired = tuple(sum(r[i] * vector[i] for i in range(2)) % 3
                       for r in cartan)
        require(paired == wanted, "a2_cartan_insertions", vector)
    return [[str(x) for x in row] for row in actual]


TERMS = (
    (F(1), F(1), F(0)),
    (F(5, 12), F(2), F(7, 4)),
    (F(2, 3), F(4, 3), F(2)),
    (F(2), F(1, 6), F(-3)),
    (F(4, 3), F(2, 3), F(-2)),
)


def check_optimization():
    regimes = (
        (F(0), F(38, 87), (F(4, 15), F(-7, 30)),
         (F(6, 5), F(13, 15)), (2, 3)),
        (F(38, 87), F(19, 22), (F(1, 3), F(-22, 57)),
         (F(1), F(151, 114)), (1, 3)),
    )
    for lo, hi, (r0, rh), (v0, vh), equal_terms in regimes:
        for h in (lo, hi):
            r = r0 + rh * h
            target = v0 + vh * h
            require(F(0) <= r <= F(1, 3),
                    "optimized_cutoff_endpoints", (str(h), str(r)))
            for i, (c, z, b) in enumerate(TERMS):
                value = c + z * h + b * r
                require(value <= target, "affine_interval_dominance",
                        (str(lo), str(hi), i, str(h)))
                if i in equal_terms:
                    require(value == target, "balanced_optimization_terms",
                            (i, str(h)))
    require(F(6, 5) + F(13, 15) * F(38, 87)
            == F(1) + F(151, 114) * F(38, 87),
            "optimized_junction", "two regimes")
    require(F(1) + F(151, 114) * F(114, 151) == 2,
            "diagonal_range", "114/151")
    h = F(1, 2)
    r = F(1, 3) - F(22, 57) * h
    value = max(c + z * h + b * r for c, z, b in TERMS)
    require(r == F(8, 57) and value == F(379, 228),
            "half_height_gain", (str(r), str(value)))
    require(F(25, 12) - value == F(8, 19),
            "half_height_gain", "8/19 saving")


def check_tail_exponents():
    eta = F(1, 20)
    for a in (F(51, 100), F(3, 5), F(5, 8), F(2, 3),
              F(3, 4), F(4, 5), F(83, 100)):
        b = (3 - a) / 2 + eta
        actual = (
            (F(1, 2), F(1, 2) - b),
            (1 - a, F(3, 2) - b - a / 2),
            (F(3, 4) - a / 2, F(5, 4) - b - a / 2),
            (1 - 4 * a / 5, F(3, 2) - b - 4 * a / 5),
        )
        expected_f = (a / 2 - 1 - eta, -eta,
                      -F(1, 4) - eta, -3 * a / 10 - eta)
        for (qexp, fexp), wanted in zip(actual, expected_f):
            require(fexp == wanted, "joint_tail_substitution", str(a))
            f_ratio = fexp + eta
            q_ratio = qexp - (1 - a)
            require(f_ratio <= 0 and q_ratio + F(2, 3) * f_ratio <= 0,
                    "joint_tail_threshold", str(a))
        require(a > F(1, 2) and F(5, 6) - a > 0,
                "joint_geometric_margins", str(a))
    require(not (F(1, 2) < F(5, 6) < F(5, 6)),
            "negative_controls", "exclude 5/6 endpoint")


def check_incidence_and_divisors():
    beta = F(1, 4) - (1 - 2 * F(7, 64)) / 16
    require(beta == F(103, 512), "subconvex_exponent", str(beta))
    for k in range(1, 7):
        for bits in product((0, 1), repeat=2 * k):
            multiplicity = sum(bits)
            if not multiplicity:
                continue
            residual = (sum(bits[:k]) - sum(bits[k:])) % 6
            if multiplicity == 1:
                require(residual != 0, "incidence_singletons", (k, bits))
            elif multiplicity == 2:
                same_side = sum(bits[:k]) in (0, 2)
                require((residual != 0) == same_side,
                        "incidence_double_conductor", (k, bits))
            else:
                require(F(multiplicity, 2) - beta > 1,
                        "higher_incidence_convergence", (k, multiplicity))
    norms = (7, 13, 19, 31, 37)
    for length in range(1, len(norms) + 1):
        for seq in permutations(norms, length):
            total = 1
            for p in seq:
                total *= p
            largest = max(seq)
            divisor = 1
            for p in seq:
                if divisor ** 3 * largest ** 2 >= total:
                    break
                divisor *= p
            require(total % divisor == 0,
                    "actual_conductor_divisors", seq)
            require(divisor ** 3 * largest ** 2 >= total
                    and divisor ** 3 <= total * largest,
                    "greedy_divisor_bounds", seq)
    fixtures = (
        ("general", F(101, 100), F(7, 10), F(71, 320), F(5, 64),
         None, F(1, 400), -F(869, 204800)),
        ("prime_bound", F(21, 20), F(7, 10), F(1, 5), F(1, 10),
         F(1, 10), F(1, 20), -F(1, 120)),
    )
    report = []
    for name, h, side, cross, singleton, y, old, new in fixtures:
        require(side + cross + singleton == 1,
                "factor_support_fixtures", name)
        l, g = 4 * singleton, 2 * side
        full_conductor, complexity = l + g, l + g / 2
        require(complexity - h == old,
                "old_remainder_excess", name)
        require(side < (6 - h) / 7,
                "small_gcd_support", name)
        wu = -h / 2 + (F(1, 2) + beta) * l + beta * g
        computed = wu if y is None else (
            -h / 2 + y / 6 + 2 * l / 3 + g / 6)
        require(computed == new and new < 0,
                "new_sector_gain", name)
        require(full_conductor != complexity,
                "negative_controls", f"{name}: conductor != complexity")
        if y is not None:
            require(wu == F(19, 512), "separate_divisor_gain", name)
            require(-h / 2 + 2 * l / 3 + g / 6 == -F(1, 40),
                    "balanced_divisor_gain", name)
        report.append({
            "name": name, "h": str(h), "singleton_product": str(l),
            "double_product": str(g), "conductor": str(full_conductor),
            "complexity": str(complexity), "old_excess": str(old),
            "new_excess": str(new), "gcd_margin": str((6-h)/7-side),
            "matched_cross_separation": str(1-cross),
        })
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    check_zero_extensions()
    check_theta_algebra()
    norm_table = check_a2_exponents()
    check_optimization()
    check_tail_exponents()
    fixtures = check_incidence_and_divisors()
    report = {
        "status": "passed",
        "arithmetic": "integers, rational numbers, and exact Z[omega]",
        "scope": "finite identities and exponent diagnostics only",
        "not_verified": [
            "theta automorphy and all-scale completed mean square",
            "uniform angular reciprocal estimate",
            "classical large sieves and Hecke subconvexity proofs",
            "full arithmetic moment or Riemann Hypothesis",
        ],
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "counts": dict(sorted(COUNTS.items())),
        "total_successful_checks_including_negative_controls": sum(COUNTS.values()),
        "a2_norm_denominator_table": norm_table,
        "signed_sector_fixtures": fixtures,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
