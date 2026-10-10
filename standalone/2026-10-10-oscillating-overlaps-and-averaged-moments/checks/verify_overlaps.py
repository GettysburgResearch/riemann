#!/usr/bin/env python3
"""Exact checks for the new cubic overlap argument.

This is not a numerical test of a moment estimate. It verifies universal
monomial certificates, exact rational exponent budgets, and finite incidence
algebra with literal character zeros. It does not prove the imported sieves.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path


def require(condition, message="exact check failed"):
    if not condition:
        raise ArithmeticError(message)


def vadd(*vectors):
    return tuple(sum(xs) for xs in zip(*vectors))


def vmul(a, v):
    return tuple(a * x for x in v)


def branch_substitute(v, branch):
    """Log variables: A=B*U or B=A*U; output powers of (V, smaller, U)."""
    xv, xa, xb = v
    if branch == "A>=B":
        return (xv, xa + xb, xa)
    return (xv, xa + xb, xb)


def monomial_certificates():
    p = (3, 1, 2)  # P=V^3*A*B^2
    f = (1, 1, 1)  # F=V*A*B
    records = []
    for branch, m in (("A>=B", (0, 1, 0)), ("B>=A", (0, 0, 1))):
        certificates = {
            "P/F": vadd(p, vmul(-1, f)),
            "P*M^3/F^3": vadd(p, vmul(3, m), vmul(-3, f)),
            "P^2*M/F^3": vadd(vmul(2, p), m, vmul(-3, f)),
        }
        powers = {
            name: branch_substitute(vector, branch)
            for name, vector in certificates.items()
        }
        require(all(e >= 0 for vector in powers.values() for e in vector),
                ("negative monomial power", branch, powers))
        records.append({"branch": branch, "powers_in_V_smaller_U": powers})
    return {
        "result": "pass",
        "scope": "universal for all real V,A,B>=1; nonnegative monomial powers",
        "certificates": records,
    }


def affine_value(v, x):
    return v[0] + v[1] * x


def affine_sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def interval_check(name, expression, lo, hi, strict=False):
    values = [affine_value(expression, x) for x in (lo, hi)]
    require(all(x > 0 if strict else x >= 0 for x in values), (name, values))
    return {
        "name": name,
        "interval": [str(lo), str(hi)],
        "endpoint_values": list(map(str, values)),
        "strict_on_closed_interval": strict,
    }


def exponent_budgets():
    new = (F(6, 7), F(-1, 7))
    old = (F(1), F(-1, 4))
    checks = [
        interval_check("new >= 2/3", affine_sub(new, (F(2, 3), F(0))),
                       F(1), F(11, 10)),
        interval_check("new >= 1-h/3", affine_sub(new, (F(1), F(-1, 3))),
                       F(1), F(11, 10)),
        interval_check("old > new", affine_sub(old, new),
                       F(1), F(11, 10), strict=True),
    ]
    # Check each energy term directly against the target H*D^2.
    # Term exponent = 4 + a*h + b*gamma(h).
    terms = [(F(1), F(-3)), (F(1, 3), F(-2)), (F(2, 3), F(-7, 3))]
    for i, (a, b) in enumerate(terms, 1):
        term = (F(4) + b * new[0], a + b * new[1])
        deficit = affine_sub((F(2), F(1)), term)
        checks.append(interval_check(f"fourth energy term {i} within target",
                                     deficit, F(1), F(11, 10)))
    # Rectangular parameter t=log(H)/log(P).
    rectangular = (F(3, 7), F(-1, 7))
    checks.extend([
        interval_check("rectangular third >= first",
                       affine_sub(rectangular, (F(1, 3), F(0))),
                       F(3, 8), F(2, 3)),
        interval_check("rectangular third >= second",
                       affine_sub(rectangular, (F(1, 2), F(-1, 3))),
                       F(3, 8), F(2, 3)),
        interval_check("rectangular old >= new",
                       affine_sub((F(1, 2), F(-1, 4)), rectangular),
                       F(3, 8), F(2, 3)),
    ])
    # Kernel H^a L^b, coefficient mass L, squared tuple cost L^(-2m).
    # Store the resulting C exponent as constant + coefficient*m.
    master = {}
    for r in (1, 2, 3, 6):
        kernel = {
            1: [(F(1), F(1))],
            2: [(F(1), F(0)), (F(1, 2), F(1))],
            3: [(F(1), F(0)), (F(1, 3), F(1)), (F(2, 3), F(2, 3))],
            6: [(F(1), F(0)), (F(1, 6), F(1)), (F(2, 3), F(2, 3))],
        }[r]
        master[str(r)] = [
            {"H_power": str(a), "C_power_constant": str(1 + b),
             "C_power_coefficient_of_m": "-2"}
            for a, b in kernel
        ]
    # The outside-pair count squares to D^(2*(ell-1)); adding the
    # fourth-polynomial D^4 cost gives D^(2ell+2)=D^(k+2).
    require(vadd((2, -2), (0, 4)) == (2, 2), "localized degree budget")
    return {
        "result": "pass",
        "scope": "exact affine checks; endpoint tests certify whole intervals",
        "checks": checks,
        "master_energy_exponents_formal_in_m": master,
        "localized_pair_budget": "2*(ell-1)+4=2*ell+2=k+2",
    }


def subsets(mask):
    sub = mask
    while True:
        yield sub
        if not sub:
            return
        sub = (sub - 1) & mask


def incidence_check():
    """Exhaust every tuple and every candidate designated divisor."""
    configurations = [(3, 2), (3, 3), (3, 4), (2, 5), (2, 6)]
    records = []
    for primes, k in configurations:
        universe = (1 << primes) - 1
        index_sets = [
            tuple(i for i in range(k) if mask >> i & 1)
            for mask in range(1, 1 << k) if mask.bit_count() >= 2
        ]
        candidate_count = eligible_count = order_one_nonunit_columns = 0
        for ns in itertools.product(range(1 << primes), repeat=k):
            original_counts = tuple(sum(bool(n & (1 << p)) for n in ns)
                                    for p in range(primes))
            for inside in index_sets:
                m = len(inside)
                outside = tuple(i for i in range(k) if i not in inside)
                common = universe
                outside_union = 0
                for i in inside:
                    common &= ns[i]
                for j in outside:
                    outside_union |= ns[j]
                exact = common & (universe ^ outside_union)
                for c in subsets(common):
                    candidate_count += 1
                    residuals = tuple(ns[i] ^ c for i in inside)
                    residual_union = 0
                    residual_common = universe
                    for a in residuals:
                        residual_union |= a
                        residual_common &= a
                    eligible = not (c & (outside_union | residual_union))
                    eligible &= not (residual_common & (universe ^ outside_union))
                    require(eligible == (c == exact),
                            ("incidence eligibility", ns, inside, c, exact))
                    if not eligible:
                        continue
                    eligible_count += 1
                    reconstructed = tuple(
                        m * bool(c & (1 << p))
                        + sum(bool(a & (1 << p)) for a in residuals)
                        + sum(bool(ns[j] & (1 << p)) for j in outside)
                        for p in range(primes)
                    )
                    # Equality of multiplicity vectors proves every phase
                    # identity, every Möbius parity, and every zero support.
                    require(reconstructed == original_counts,
                            ("multiplicity identity", ns, inside, c))
                    require((c | residual_union | outside_union) == (
                        sum((1 << p) for p, e in enumerate(original_counts) if e)
                    ), ("zero support identity", ns, inside, c))
                    if m % 6 == 0 and c:
                        order_one_nonunit_columns += 1
        records.append({
            "formal_primes": primes, "polynomial_degree": k,
            "candidate_divisors_checked": candidate_count,
            "exact_eligible_decompositions": eligible_count,
            "principal_power_cases_with_nonunit_columns": order_one_nonunit_columns,
        })
    require(records[-1]["principal_power_cases_with_nonunit_columns"] > 0,
            "the model must contain nonunit principal-power columns")
    return {
        "result": "pass",
        "scope": "finite ideal model; multiplicity vectors retain all zero supports",
        "configurations": records,
    }


def multiply_phases(*phases):
    """None denotes the literal character zero; integers denote zeta_6 powers."""
    return None if any(x is None for x in phases) else sum(phases) % 6


def power_phase(phase, exponent):
    require(exponent > 0, "only positive character powers are used")
    return None if phase is None else phase * exponent % 6


def character(column, valuations, unit, unit_phases, cross):
    if any((column >> p & 1) and valuations[p] for p in range(len(valuations))):
        return None
    exponent = 0
    for p in range(len(valuations)):
        if column >> p & 1:
            exponent += unit * unit_phases[p]
            exponent += sum(e * cross[p][q] for q, e in enumerate(valuations))
    return exponent % 6


def cubic_zero_check():
    primes = 3
    cross = ((0, 1, 4), (5, 0, 2), (3, 4, 0))
    patterns = [(0, 0, 0), (1, 2, 3), (5, 4, 2)]
    zero = (0,) * primes
    count = zero_count = overlapping_v_count = 0
    for valuations in itertools.product(range(9), repeat=primes):
        ve = tuple(e // 3 for e in valuations)
        ae = tuple(int(e % 3 == 1) for e in valuations)
        be = tuple(int(e % 3 == 2) for e in valuations)
        overlapping_v = any(v and (a or b) for v, a, b in zip(ve, ae, be))
        for column, unit, phases in itertools.product(range(8), range(6), patterns):
            lhs = power_phase(character(column, valuations, unit, phases, cross), 2)
            fixed_unit = power_phase(character(column, zero, unit, phases, cross), 2)
            v_mask = None if any((column >> p & 1) and ve[p] for p in range(primes)) else 0
            rhs = multiply_phases(
                fixed_unit, v_mask,
                power_phase(character(column, ae, 0, phases, cross), 2),
                power_phase(character(column, be, 0, phases, cross), 4),
            )
            require(lhs == rhs, ("cubic row identity", valuations, column, unit, phases))
            count += 1
            zero_count += lhs is None
            overlapping_v_count += overlapping_v
    # Concrete failure if a cube or sixth-power zero mask is suppressed.
    require(power_phase(None, 6) is None, "sixth power must retain its zero")
    witness_valuations = (3, 0, 0)
    require(power_phase(character(1, witness_valuations, 0, patterns[0], cross), 2) is None,
            "cube witness must have a literal zero")
    unmasked_rhs = multiply_phases(0, 0, 0)
    require(unmasked_rhs == 0, "mask-free witness is the unit root, not zero")
    return {
        "result": "pass",
        "cases": count,
        "cases_with_literal_zero": zero_count,
        "cases_allowing_v_to_overlap_a_or_b": overlapping_v_count,
        "unmasked_cube_witness": {
            "column": "p1", "row": "p1^3",
            "exact_cubic_value": "zero", "mask_dropped_value": "one",
        },
        "six_divides_m_witness": {
            "local_character": "zero", "sixth_power": "zero",
            "principal_without_mask_would_be": "one",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path,
                        default=Path(__file__).with_suffix(".json"))
    parser.add_argument("--note", type=Path)
    args = parser.parse_args()
    report = {
        "status": "pass",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "purpose": "exact proof guards, not empirical verification of moment bounds",
        "monomial_certificates": monomial_certificates(),
        "rational_exponents": exponent_budgets(),
        "incidence_eligibility": incidence_check(),
        "cubic_and_principal_zero_masks": cubic_zero_check(),
        "limitations": [
            "The imported cubic, quadratic, and sextic large sieves are assumptions.",
            "The finite ideal model verifies algebra, not distribution of arithmetic rows.",
            "No full fourth-moment or higher-moment estimate is tested or claimed.",
        ],
    }
    if args.note is not None:
        report["note"] = {
            "name": "OSCILLATING_OVERLAPS.md",
            "sha256": hashlib.sha256(args.note.read_bytes()).hexdigest(),
        }
    args.json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "output": str(args.json.resolve()),
        "incidence_candidates": sum(
            c["candidate_divisors_checked"]
            for c in report["incidence_eligibility"]["configurations"]
        ),
        "cubic_cases": report["cubic_and_principal_zero_masks"]["cases"],
    }, indent=2))


if __name__ == "__main__":
    main()
