#!/usr/bin/env python3
"""Exact finite algebra checks; not a proof of the analytic moment estimate."""

from fractions import Fraction as Q
import json


def demand(condition, message):
    if not condition:
        raise RuntimeError(message)


def expect(actual, expected, message):
    demand(actual == expected, f"{message}: {actual!r} != {expected!r}")


def parity_sums(x, y):
    den = (1 - x * x) * (1 - y * y)
    return (1 + x * y) / den, (x + y) / den


def raw_pair_enum(x, y, a, b):
    even, odd = parity_sums(x, y)
    value = Q(0)
    for h1 in (0, 1):
        for h2 in (0, 1):
            value += (-a) ** h1 * (-b) ** h2 * (odd if (h1 + h2) % 2 else even)
    return value


def raw_pair_formula(x, y, a, b):
    return sum((1 - sign * a) * (1 - sign * b) /
               ((1 - sign * x) * (1 - sign * y))
               for sign in (-1, 1)) / 2


def ramanujan_parity_numerators(q, x, nvaluation):
    if nvaluation:
        return (q - 1) / (1 - x*x), (q - 1) * x / (1 - x*x)
    return -1 + (q - 1) * x*x / (1 - x*x), (q - 1) * x / (1 - x*x)


def ramanujan_pair_enum(q, x, y, nweight):
    result = Q(0)
    for nvaluation in (0, 1):
        x_even, x_odd = ramanujan_parity_numerators(q, x, nvaluation)
        y_even, y_odd = ramanujan_parity_numerators(q, y, nvaluation)
        result += nweight ** nvaluation * (x_even*y_even + x_odd*y_odd) / q
    return result


def ramanujan_pair_formula(q, x, y, nweight):
    even, _ = parity_sums(x, y)
    return ((q - 1)**2 / q * (1+nweight) * even
            - (q - 1) * (1/(1-x*x) + 1/(1-y*y)) + q)


def residue_average(q, b1, b2):
    result = Q(0)
    for nvaluation in (0, 1):
        probability = Q(1, q+1) if nvaluation else Q(q, q+1)
        numerator1 = q-1 if nvaluation or b1 else -1
        numerator2 = q-1 if nvaluation or b2 else -1
        result += probability * Q(numerator1*numerator2, q)
    return result


def main():
    algebra_count = 0
    critical_count = 0
    residue_count = 0
    for q0 in (4, 7, 13, 19, 31, 43, 97):
        q = Q(q0)
        for x in (Q(1, 2*q0), Q(2, q0), Q(-1, 3*q0), Q(3, 2*q0)):
            for y in (Q(1, 3*q0), Q(-2, q0), Q(3, q0)):
                a, b = 1/(q*q*x), 1/(q*q*y)
                expect(raw_pair_enum(x, y, a, b), raw_pair_formula(x, y, a, b),
                       "inverse completion parity filter")
                for nweight in (Q(1, q0), Q(2, q0), Q(1, q0*q0)):
                    expect(ramanujan_pair_enum(q, x, y, nweight),
                           ramanujan_pair_formula(q, x, y, nweight),
                           "unsplit Ramanujan parity factor")
                    algebra_count += 1
            y = 1/(q*q*x)
            if y not in (1, -1):
                expect(raw_pair_enum(x, y, y, x), Q(1), "critical raw pair")
                expect(ramanujan_pair_enum(q, x, y, 1/q), Q(1),
                       "critical unsplit Ramanujan pair")
                expect((1+1/q)*raw_pair_enum(x, y, y, x)
                       - ramanujan_pair_enum(q, x, y, 1/q)/q,
                       Q(1), "critical complete signed local mass")
                critical_count += 1
        for b1 in (0, 1):
            for b2 in (0, 1):
                if b1+b2 == 0:
                    expected = (q*q-q+1)/(q*(q+1))
                elif b1+b2 == 1:
                    expected = -(q-1)/(q*(q+1))
                else:
                    expected = (q-1)**2/q
                expect(residue_average(q0, b1, b2), expected,
                       "squarefree n residue local table")
                residue_count += 1

    # Independent enumeration of the worst nonconstant residue parity cost.
    for eta in (Q(1, 10), Q(1, 8), Q(1, 4), Q(1, 3)):
        worst = None
        for h1 in (0, 1):
            for h2 in (0, 1):
                for b1 in range(7):
                    for b2 in range(7):
                        total = h1+h2+b1+b2
                        if total == 0 or total % 2:
                            continue
                        exponent = -total + 3*eta*h1 + eta*int(b1 > 0 and b2 > 0)
                        worst = exponent if worst is None else max(worst, exponent)
        expect(worst, -2+3*eta, "residue paired exponent")

    delta = Q(1, 7)
    expect((1-3*delta)/(1-2*delta), Q(4, 5), "regular inverse threshold")
    demand(-Q(3, 2)+Q(5, 2)*delta < -1, "moving conductor sum must converge")
    demand(-2+3*delta < -1, "paired Euler remainder must converge")
    report = {
        "status": "exact_local_algebra_checks_passed",
        "scope": "finite rational algebra and exponent bookkeeping only",
        "two_variable_local_checks": algebra_count,
        "critical_hyperplane_checks": critical_count,
        "residue_table_checks": residue_count,
        "residue_exponent": "-2+3*eta; convergence eta<1/3",
        "conductor_exponent": "-3/2+(5/2)*delta; convergence delta<1/5",
        "regular_delta": str(delta),
        "regular_threshold": "4/5",
        "does_not_verify": [
            "fixed cusp identities", "Mellin contour interchange",
            "finite support continuation", "powerful row reassembly",
            "non-square quadratic correlation", "any zero-free boundary improvement"
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
