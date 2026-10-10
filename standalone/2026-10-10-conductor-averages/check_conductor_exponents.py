#!/usr/bin/env python3
"""Exact finite diagnostics for displayed algebra, not analytic proof.

Run from any directory. Output is stable JSON on stdout.
The finite incidence enumeration covers k=1,...,8 only. General k is
proved in the notes by the incidence and convergence arguments.
No character values, zero census, or external theorem are certified.
"""

from fractions import Fraction as F
from itertools import product
import json


def exact(value):
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def check_equal(actual, expected):
    assert actual == expected, (actual, expected)
    return exact(actual)


def main():
    beta = F(103, 512)
    retained = {(1, 1), (2, 1), (2, 2), (3, 2)}
    counts = {}
    all_types = set()
    for k in range(1, 9):
        types = set()
        tested = 0
        for rp, sp, rq, sq in product(range(k + 1), repeat=4):
            ell = rp + sp + rq + sq
            if ell == 0:
                continue
            degree = int((rp - sp) % 6 != 0) + int((rq - sq) % 6 != 0)
            tested += 1
            if degree == 0:
                assert ell >= 2
                continue
            types.add((ell, degree))
        for rp, sp in product(range(k + 1), repeat=2):
            ell = 2 * (rp + sp)
            if ell == 0:
                continue
            degree = 2 * int((rp - sp) % 6 != 0)
            tested += 1
            if degree == 0:
                assert ell >= 2
                continue
            types.add((ell, degree))
        assert {(ell, degree) for ell, degree in types if ell <= 2} <= retained
        for ell, degree in types - retained:
            assert F(degree, 2) - F(ell, 2) <= -1
            assert degree * beta - F(ell, 2) < -1
            assert F(degree, 6) - F(ell, 2) < -1
        counts[str(k)] = {"multiplicity_assignments": tested, "types": len(types)}
        all_types.update(types)

    # Conductor R,M,N exponents after the AFE length Q=(RMN)^(1/2).
    term_two = (F(1, 2), F(2, 3) + F(1, 2) - 1,
                F(1, 3) + F(1, 2) - 1)
    term_three = (F(1, 3), F(1, 3) + F(1, 3) - 1,
                  F(2, 3) + F(1, 3) - 1)
    assert term_two == (F(1, 2), F(1, 6), F(-1, 6))
    assert term_three == (F(1, 3), F(-1, 3), F(0))

    h = F(21, 20)
    cubic = {
        "column_balance": check_equal(F(3, 5) + F(7, 30) + F(1, 6), 1),
        "average_excess": check_equal(-h / 2 + F(3, 4) * F(2, 3), F(-1, 40)),
        "old_completion_excess": check_equal(F(2, 3) + F(3, 5) - h, F(13, 60)),
        "old_wu_excess": check_equal(
            -h / 2 + (F(1, 2) + beta) * F(2, 3) + beta * F(6, 5),
            F(353, 1920)),
        "balanced_divisor_excess": check_equal(
            -h / 2 + F(2, 3) * F(2, 3) + F(1, 6) * F(6, 5), F(43, 360)),
        "small_gcd_margin": check_equal((6 - h) / 7 - F(3, 5), F(3, 28)),
    }
    rational = {
        "column_balance": check_equal(
            F(7, 10) + F(1, 5) + F(1, 50) + F(2, 25), 1),
        "rational_radical": check_equal(F(7, 5) + F(2, 5) + F(1, 25) + F(8, 25),
                                         F(54, 25)),
        "new_wu_excess": check_equal(
            -h / 2 + (F(1, 2) + beta) * F(8, 25)
            + beta * F(7, 5) + 2 * beta * F(1, 25), F(-37, 12800)),
        "new_completion_excess": check_equal(
            F(8, 25) + F(7, 10) + F(1, 25) - h, F(1, 100)),
        "old_wu_excess": check_equal(
            -h / 2 + (F(1, 2) + beta) * F(2, 5)
            + beta * F(7, 5), F(19, 512)),
    }
    composition = {
        "column_balance": check_equal(
            F(1, 2) + F(3, 10) + F(1, 20) + F(3, 20), 1),
        "ideal_singleton_exponent": check_equal(F(3, 5) + 2 * F(1, 10), F(4, 5)),
        "composed_excess": check_equal(
            -h / 2 + F(3, 4) * F(3, 5) + F(1, 2) * F(1, 10), F(-1, 40)),
        "ideal_average_excess": check_equal(
            -h / 2 + F(3, 4) * F(4, 5), F(3, 40)),
        "rational_completion_excess": check_equal(
            F(3, 5) + F(1, 2) + F(1, 10) - h, F(3, 20)),
        "rational_wu_excess": exact(
            -h / 2 + (F(1, 2) + beta) * F(3, 5)
            + beta + 2 * beta * F(1, 10)),
        "radical_exponent": check_equal(1 + F(3, 5) + F(3, 5) + F(1, 10),
                                        F(23, 10)),
    }
    assert F(composition["rational_wu_excess"]) > 0
    gaussian = {
        "derivative_log_coefficient": check_equal(F(8, 2), 4),
        "pre_row_error_exponent": check_equal(1 - F(8, 2), -3),
        "fourth_moment_limit": check_equal(F(1, 2) + F(5, 24), F(17, 24)),
        "replica_height_remainder": check_equal(1 - F(1, 6), F(5, 6)),
    }
    def cubic_axis(x):
        return max(x / 2, x - h / 3, 5 * x / 6 - h / 6)

    prior_signed_comparison = {
        "scope": "Complete structured signed blocks, not tuplewise absolute accounting.",
        "cubic_fixture_axis": check_equal(cubic_axis(F(3, 5)), F(13, 40)),
        "cubic_fixture_total_D_exponent": check_equal(
            F(2, 3) + F(7, 15) + 2 * cubic_axis(F(3, 5)), F(107, 60)),
        "composition_fixture_total_D_exponent": check_equal(
            F(4, 5) + F(3, 5) + 2 * cubic_axis(F(1, 2)), F(19, 10)),
    }
    result = {
        "status": "PASS",
        "scope": "Exact rational algebra and finite incidence diagnostics only.",
        "not_checked": [
            "The analytic proof of any imported theorem.",
            "All moment orders by enumeration.",
            "Any full arithmetic moment estimate.",
            "Any zero-free region or RH.",
        ],
        "incidence_orders": counts,
        "rational_low_types": sorted([list(t) for t in all_types if t[0] <= 3]),
        "cubic_mean_ratios_R_M_N": [[exact(x) for x in term_two],
                                    [exact(x) for x in term_three]],
        "higher_ideal_multiplicity_first_exponent":
            check_equal(F(1, 4) - F(3, 2), F(-5, 4)),
        "rational_m3_subconvex_exponent":
            check_equal(2 * beta - F(3, 2), F(-281, 256)),
        "cubic_fixture": cubic,
        "rational_fixture": rational,
        "composed_fixture": composition,
        "gaussian": gaussian,
        "prior_PR926_signed_comparison": prior_signed_comparison,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
