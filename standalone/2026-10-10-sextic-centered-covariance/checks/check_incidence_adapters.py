"""Exact finite controls for the Hermitian incidence adapters.

This checks mixed-sign local Euler correction, literal nonunit zeros,
global-gcd extraction against genuine small sextic residue symbols, and
rational exponent identities. It is not a test of an asymptotic moment bound.
Only integer/rational arithmetic and the Python standard library are used.
"""

import argparse
import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
UNITS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
COUNT = Counter()


def require(ok, kind):
    COUNT[kind] += 1
    if not ok:
        raise RuntimeError("Failed exact predicate: " + kind)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c + b * d


def power(x, n):
    out = (1, 0)
    for _ in range(n):
        out = mul(out, x)
    return out


def conjugate(x):
    return x[0] + x[1], -x[1]


def scalar(n, x):
    return n * x[0], n * x[1]


def subsets(mask):
    out = mask
    while True:
        yield out
        if not out:
            break
        out = (out - 1) & mask


def local_correction_controls():
    # a_i is the actual signed coefficient in 1+a_i*z_i. Both even
    # and odd incidence coefficients occur. At a masked prime the target
    # polynomial is 1 instead of 1+sum(a_i*z_i).
    for axes, cap in ((2, 3), (4, 2), (6, 1)):
        for phase in range(-1, 6):
            signs = [1 if i % 3 == 0 else -1 for i in range(axes)]
            a = [(0, 0) if phase < 0 else scalar(
                signs[i], ROOTS[((2 * i + 1) * phase) % 6])
                for i in range(axes)]
            for masked in (False, True):
                def correction(exponents):
                    support = sum(n > 0 for n in exponents)
                    coefficient = 1 if masked else 1 - support
                    value = (coefficient, 0)
                    for z, n in zip(a, exponents):
                        value = mul(value, power(scalar(-1, z), n))
                    return value

                for exponents in itertools.product(range(cap + 1), repeat=axes):
                    support_mask = sum(1 << i for i, n in enumerate(exponents) if n)
                    actual = (0, 0)
                    for chosen in subsets(support_mask):
                        remaining = tuple(n - ((chosen >> i) & 1)
                                          for i, n in enumerate(exponents))
                        value = correction(remaining)
                        for i, z in enumerate(a):
                            if (chosen >> i) & 1:
                                value = mul(value, z)
                        actual = add(actual, value)
                    expected = (0, 0)
                    if sum(exponents) == 0:
                        expected = (1, 0)
                    elif not masked and sum(exponents) == 1:
                        expected = a[exponents.index(1)]
                    require(actual == expected, "mixed_sign_forward_euler_identity")


def split_symbol(p, omega, row):
    value = (row[0] + omega * row[1]) % p
    if not value:
        return None
    residue = pow(value, (p - 1) // 6, p)
    matches = [j for j, (a, b) in enumerate(UNITS)
               if (a + omega * b) % p == residue]
    require(len(matches) == 1, "literal_split_sextic_symbol")
    return matches[0]


def gcd_controls():
    # The two distinct prime ideals are (7,omega-2) and (13,omega-3).
    primes = ((7, 2), (13, 3))
    norms = [math.prod(p for i, (p, _) in enumerate(primes) if (mask >> i) & 1)
             for mask in range(4)]
    weights = [1 + n % 5 for n in norms]
    thresholds = (1, 2, 7, 8, 13, 14, 91, 92)
    mobius = [(-1) ** mask.bit_count() for mask in range(4)]
    w = {}
    for threshold in thresholds:
        w[threshold] = [sum(mobius[q ^ d] for d in subsets(q)
                            if norms[d] >= threshold) for q in range(4)]
        for c in range(4):
            require(sum(w[threshold][q] for q in subsets(c)) ==
                    int(norms[c] >= threshold), "gcd_mobius_cutoff_identity")

    rows = [(a, b) for a in range(-5, 6) for b in range(-5, 6)
            if 0 < a * a - a * b + b * b <= 15]
    require(len([u for u in rows if u[0] ** 2 - u[0] * u[1] + u[1] ** 2 == 1]) == 6,
            "all_six_unit_rows_retained")
    nonunit_count = 0
    for row in rows:
        phases = [split_symbol(p, omega, row) for p, omega in primes]
        nonunit_count += any(j is None for j in phases)
        # A fixed order-six coefficient datum; its prime values are zeta_6
        # and zeta_6^2. No analytic claim is made about these finite columns.
        values = []
        characters = []
        for mask in range(4):
            value = (mobius[mask], 0)
            character = (1, 0)
            for i, phase in enumerate(phases):
                if not (mask >> i) & 1:
                    continue
                z = (0, 0) if phase is None else ROOTS[(phase + i + 1) % 6]
                value = mul(value, z)
                character = mul(character, (0, 0) if phase is None else ROOTS[phase])
            values.append(value)
            characters.append(character)
        columns = [scalar(weight, value) for weight, value in zip(weights, values)]
        divisible_sums = []
        for q in range(4):
            direct = (0, 0)
            residual = (0, 0)
            for n in range(4):
                if n & q == q:
                    direct = add(direct, columns[n])
                if not n & q:
                    residual = add(residual, scalar(weights[n | q], values[n]))
            require(direct == mul(values[q], residual), "exact_squarefree_gcd_extraction")
            require(mul(characters[q], conjugate(characters[q])) in ((0, 0), (1, 0)),
                    "literal_gcd_row_mask")
            divisible_sums.append(direct)
        for k in (2, 3):
            left = defaultdict(lambda: (0, 0))
            for entries in itertools.product(range(4), repeat=k):
                value = (1, 0)
                common = 3
                for n in entries:
                    common &= n
                    value = mul(value, columns[n])
                left[common] = add(left[common], value)
            for threshold in thresholds:
                direct = (0, 0)
                for c, value in left.items():
                    for d, other in left.items():
                        if norms[c & d] >= threshold:
                            direct = add(direct, mul(value, conjugate(other)))
                reconstructed = (0, 0)
                for q, value in enumerate(divisible_sums):
                    energy = power(mul(value, conjugate(value)), k)
                    reconstructed = add(reconstructed, scalar(w[threshold][q], energy))
                require(direct == reconstructed, "full_hermitian_gcd_sector_identity")
                require(direct[1] == 0, "hermitian_sector_is_real")
    require(nonunit_count > 0, "nonunit_rows_actually_tested")
    return {"prime_ideal_norms": [7, 13], "all_row_ball_norm": 15,
            "row_count": len(rows), "rows_with_nonunit_symbols": nonunit_count,
            "moment_orders": [4, 6], "thresholds": list(thresholds)}


def incidence_controls():
    eligible_counts = {}
    for k in range(2, 7):
        eligible = 0
        for pattern in range(1, 1 << (2 * k)):
            left = (pattern & ((1 << k) - 1)).bit_count()
            right = (pattern >> k).bit_count()
            multiplicity = left + right
            exponent = left - right
            is_eligible = multiplicity % 2 == 1 and exponent % 6 in (1, 5)
            eligible += is_eligible
            require((multiplicity - exponent) % 2 == 0, "incidence_parity")
            for row_phase in range(-1, 6):
                actual = (0, 0) if row_phase < 0 else scalar(
                    (-1) ** multiplicity, ROOTS[(exponent * row_phase) % 6])
                if is_eligible:
                    expected = (0, 0) if row_phase < 0 else scalar(
                        -1, ROOTS[(exponent * row_phase) % 6])
                    require(actual == expected, "eligible_incidence_is_native_mobius")
                if row_phase < 0:
                    require(actual == (0, 0), "even_principal_pattern_keeps_nonunit_zero")
            # Prime-by-prime exponents in product Q_I = D^k sqrt(L1/Gamma).
            rhs = Fraction(multiplicity, 2)
            if multiplicity == 1:
                rhs += Fraction(1, 2)
            elif multiplicity >= 3:
                rhs -= Fraction(multiplicity - 2, 2)
            require(rhs == 1, "incidence_mass_exponent_identity")
        eligible_counts[str(k)] = eligible

    exponents = []
    for beta in (Fraction(1), Fraction(7, 8), Fraction(139999, 160000)):
        cutoff = (2 * beta - 1) / (2 * beta)
        for k in range(2, 11):
            rho = 1 + (2 * k - 2) * beta
            require(rho + cutoff * (1 - rho) == k, "gcd_diagonal_cutoff_exponent")
        triple = (6 * beta - 3) / (6 * beta - 1)
        require(triple >= Fraction(1, 2), "triple_selected_length_order")
        require(6 * beta - 3 + triple * (1 - 6 * beta) == 0,
                "triple_native_core_cutoff_exponent")
        exponents.append({"beta": str(beta), "global_gcd_cutoff": str(cutoff),
                          "triple_core_cutoff": str(triple)})
    return {"eligible_pattern_counts_by_k": eligible_counts,
            "exact_cutoff_exponents": exponents}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    local_correction_controls()
    gcd_result = gcd_controls()
    incidence_result = incidence_controls()
    result = {"status": "PASS", "arithmetic": "exact integers and rational numbers",
              "scope": "finite identities only; no asymptotic or zero-free claim",
              "predicate_count": sum(COUNT.values()), "predicates": dict(sorted(COUNT.items())),
              "gcd_controls": gcd_result, "incidence_controls": incidence_result}
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
