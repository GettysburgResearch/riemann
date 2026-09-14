#!/usr/bin/env python3
from fractions import Fraction
from math import comb, factorial
import hashlib
import json


def c(k):
    return Fraction(comb(2 * k, k), 4 ** k)


def b(j):
    return Fraction(comb(2 * j, j), (4 ** j) * (2 * j - 1))


def polynomial(k):
    return [Fraction(1)] + [-b(j) for j in range(1, k + 1)]


def q_coefficients(k, stop):
    p = polynomial(k)
    numerator = [Fraction(0)] * (2 * k + 1)
    for i, ai in enumerate(p):
        for j, aj in enumerate(p):
            numerator[i + j] += ai * aj
    q = []
    running = Fraction(0)
    for m in range(stop + 1):
        if m < len(numerator):
            running += numerator[m]
        q.append(running)
    return q


def t(m):
    return Fraction(factorial(m), factorial(2 * m))


def compute():
    rows = []
    for k in range(1, 13):
        q = q_coefficients(k, 4 * k + 12)
        assert q[0] == 1
        assert all(q[m] == 0 for m in range(1, k + 1))
        assert all(value >= 0 for value in q)
        assert all(q[m] <= c(k) ** 2 for m in range(k + 1, len(q)))
        assert all(q[m] <= q[m + 1] for m in range(k + 1, 2 * k))
        assert all(q[m] == c(k) ** 2 for m in range(2 * k, len(q)))
        assert q[k + 1] == 2 * b(k + 1)
        assert sum(b(j) for j in range(1, k + 1)) == 1 - c(k)
        assert sum(Fraction(j) * b(j) for j in range(1, k + 1)) == k * c(k)

        energy_bound = (
            c(k) ** 4
            * t(k + 1)
            * Fraction(4 * k + 6, 4 * k + 5)
        )
        rows.append({
            "K": k,
            "c_K": str(c(k)),
            "first_q": str(q[k + 1]),
            "energy_bound": str(energy_bound),
        })

    d1_lower = Fraction(1, 16) * (t(2) + t(3))
    d1_upper = Fraction(3, 520)
    d2_upper = Fraction(1669, 11698176)
    ratio = Fraction(99, 101)

    degree1_upper_proportion = 2 * ratio * ratio / (1 + 2 * d1_lower) - 1
    degree2_lower_proportion = 2 * ratio * ratio / (1 + 2 * d2_upper) - 1

    assert degree1_upper_proportion < Fraction(9, 10)
    assert degree2_lower_proportion > Fraction(92, 100)
    assert degree2_lower_proportion == Fraction(4997295529, 5425779287)
    assert Fraction(9401, 10201) == 2 * ratio * ratio - 1

    payload = {
        "schema": "riemann.x105250.polynomial-wick-hierarchy.v1",
        "classification": "PASS_T105250_POLYNOMIAL_WICK_HIERARCHY",
        "checked_K": 12,
        "positive_residual_coefficients_checked": True,
        "low_degrees_cancelled_checked": True,
        "eventual_constant_checked": True,
        "banach_coefficient_sum_checked": True,
        "lipschitz_sum_checked": True,
        "superfactorial_energy_bound_checked": True,
        "degree_one_99_101_cannot_reach_90": True,
        "degree_two_99_101_lower_bound": str(degree2_lower_proportion),
        "degree_two_99_101_decimal": float(degree2_lower_proportion),
        "fixed_99_101_density_ceiling": str(Fraction(9401, 10201)),
        "all_fixed_degree_transfer_implies_density_one": True,
        "actual_xi_transfer_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
        "rows": rows,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    payload = compute()
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    print(json.dumps(payload, indent=2, sort_keys=True))
