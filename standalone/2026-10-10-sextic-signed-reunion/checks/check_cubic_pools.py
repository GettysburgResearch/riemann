"""Exact controls for joint cubic pair ideals.

The checker verifies finite coefficient identities, literal residue-symbol
zeros on genuine small Eisenstein rows, and rational exponent calculations.
It proves no infinite analytic estimate. Uses only the Python standard library.
"""

import argparse
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


COUNTS = Counter()
ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
ZERO = (0, 0)
ONE = (1, 0)


def require(ok, label):
    COUNTS[label] += 1
    if not ok:
        raise RuntimeError("Exact predicate failed: " + label)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    # Z[tau], tau^2=tau-1, tau=exp(pi*i/3).
    return x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0] + x[1]*y[1]


def scale(a, z):
    return a*z[0], a*z[1]


def power(z, exponent):
    out = ONE
    for _ in range(exponent):
        out = mul(out, z)
    return out


def norm(z):
    return z[0]*z[0] + z[0]*z[1] + z[1]*z[1]


def conjugate(z):
    return z[0] + z[1], -z[1]


def phase_value(phase):
    return ZERO if phase is None else ROOTS[phase % 6]


def nonunit_power(z, exponent):
    # The exponent-zero principal factor keeps a zero at a nonunit.
    return ZERO if z == ZERO else power(z, exponent % 6)


def residue_symbol(row, prime, omega):
    # The lattice row is a+b*omega, omega^2+omega+1=0.
    x = (row[0] + row[1]*omega) % prime
    if x == 0:
        return ZERO
    value = pow(x, (prime-1)//6, prime)
    choices = [z for z in ROOTS if (z[0] + z[1]*(omega+1)) % prime == value]
    require(len(choices) == 1, "genuine_split_sextic_residue")
    return choices[0]


def all_subsets(mask):
    sub = mask
    while True:
        yield sub
        if sub == 0:
            break
        sub = (sub-1) & mask


def mixed_forward():
    # Three singleton signs (-) and three pair signs (+).
    signs = (-1, -1, -1, 1, 1, 1)
    row_powers = (1, 1, 1, 2, 2, 2)
    cases = 0
    regressions = 0
    for phase in (None, 0, 1, 2, 3, 4, 5):
        z = phase_value(phase)
        actual_prime_coeff = tuple(scale(s, nonunit_power(z, r))
                                   for s, r in zip(signs, row_powers))
        for masked in (False, True):
            for exponents in itertools.product(range(3), repeat=6):
                support = sum((1 << i) for i, e in enumerate(exponents) if e)
                result = ZERO
                for chosen in all_subsets(support):
                    residual = tuple(e - ((chosen >> i) & 1)
                                     for i, e in enumerate(exponents))
                    coefficient = 1 if masked else 1-sum(e > 0 for e in residual)
                    term = (coefficient, 0)
                    for i, e in enumerate(residual):
                        term = mul(term, power(scale(-1, actual_prime_coeff[i]), e))
                    for i in range(6):
                        if (chosen >> i) & 1:
                            term = mul(term, actual_prime_coeff[i])
                    result = add(result, term)
                expected = ONE if sum(exponents) == 0 else ZERO
                if not masked and sum(exponents) == 1:
                    expected = actual_prime_coeff[exponents.index(1)]
                require(result == expected, "six_axis_mixed_forward_coefficient")
                cases += 1
            # A positive pair coefficient is opposite to a false Mobius sign.
            if not masked and phase is not None:
                require(actual_prime_coeff[3] != scale(-1, actual_prime_coeff[3]),
                        "wrong_pair_mobius_sign_rejected")
                regressions += 1
    return {"six_axis_exponent_cap": 2, "coefficients_checked": cases,
            "nonunit_phase_included": True, "wrong_pair_sign_regressions": regressions}


def finite_triangle():
    primes = ((7, 2), (13, 3), (19, 7))
    labels = range(1 << len(primes))
    norms = [math.prod(p for i, (p, _) in enumerate(primes) if (mask >> i) & 1)
             for mask in labels]
    mobius = [(-1)**mask.bit_count() for mask in labels]
    weights = [[1 + ((i+2)*n % 11) for n in norms] for i in range(3)]
    rows = [(a, b) for a in range(-8, 9) for b in range(-8, 9)
            if 0 < a*a-a*b+b*b <= 40]
    require(sum(a*a-a*b+b*b == 1 for a, b in rows) == 6, "six_units_in_row_ball")
    row_zero_count = 0
    fully_active_count = 0
    counterexample_wrong_sign = None
    for row in rows:
        prime_symbols = [residue_symbol(row, p, omega) for p, omega in primes]
        row_zero_count += any(z == ZERO for z in prime_symbols)
        chars = []
        for mask in labels:
            z = ONE
            for i, zp in enumerate(prime_symbols):
                if (mask >> i) & 1:
                    z = mul(z, zp)
            chars.append(z)
        direct = {False: ZERO, True: ZERO}
        decomposed = {False: ZERO, True: ZERO}
        wrong = ZERO
        for tuple_n in itertools.product(labels, repeat=3):
            if tuple_n[0] & tuple_n[1] & tuple_n[2]:
                continue
            # Extract exact one-sided incidences.
            incidence = {I: 0 for I in range(1, 8)}
            for p_index in range(3):
                I = sum(1 << i for i, n in enumerate(tuple_n)
                        if (n >> p_index) & 1)
                if I:
                    incidence[I] |= 1 << p_index
            require(incidence[7] == 0, "triangle_common_gcd_one")
            singleton = (incidence[1], incidence[2], incidence[4])
            pair = (incidence[3], incidence[5], incidence[6])
            active = all(pair)
            fully_active_count += active
            integer_weight = math.prod(weights[i][n] for i, n in enumerate(tuple_n))
            original = (integer_weight*math.prod(mobius[n] for n in tuple_n), 0)
            for n in tuple_n:
                original = mul(original, chars[n])
            split = (integer_weight, 0)
            for n in singleton:
                split = mul(split, scale(mobius[n], chars[n]))
            for n in pair:
                split = mul(split, power(chars[n], 2))
            require(original == split, "literal_triangle_coefficient_identity")
            for selector in (False, True):
                if not selector or active:
                    direct[selector] = add(direct[selector], original)
                    decomposed[selector] = add(decomposed[selector], split)
            if active:
                wrong_term = split
                for n in pair:
                    wrong_term = scale(mobius[n], wrong_term)
                wrong = add(wrong, wrong_term)
        for selector in (False, True):
            require(direct[selector] == decomposed[selector],
                    "complete_triangle_portion_identity")
            require(mul(direct[selector], conjugate(direct[selector])) ==
                    (norm(direct[selector]), 0), "exact_hermitian_energy")
        if row == (1, 0):
            require(direct[True] != wrong, "native_triangle_rejects_wrong_pair_sign")
            counterexample_wrong_sign = {"row": row, "correct": direct[True], "wrong": wrong}
    require(row_zero_count > 0, "triangle_nonunit_rows_present")
    return {"prime_ideal_norms": [7, 13, 19], "row_ball_norm": 40,
            "element_rows": len(rows), "rows_with_zero_symbols": row_zero_count,
            "fully_active_tuple_row_cases": fully_active_count,
            "wrong_pair_sign_example": counterexample_wrong_sign,
            "coefficient_datum": "trivial finite-order character",
            "finite_weight_scope": "fixed integer test values, no analytic assertion"}


def pool_saving(h, r_pool, q):
    return min(F(q)*r_pool, 2*h/3, (h+F(q)*r_pool)/3)/q


def triangle_loss(h, b, r, q):
    a = 2*b-1
    x = 1-2*r
    return 3*a*x-a*x*(1-F(1, q))-pool_saving(h, 3*r, q)


def rational_certificates():
    h, b, r = F(21,20), F(7,8), F(5,24)
    require(triangle_loss(h,b,r,1) == F(181,240), "triangle_q1_loss")
    require(triangle_loss(h,b,r,2) == F(119,160), "triangle_q2_loss")
    require(F(623,720)-F(181,240) == F(1,9), "q1_improvement")
    require(F(623,720)-F(119,160) == F(35,288), "q2_improvement")
    # Endpoint certificates for every affine term throughout each h interval.
    cutoff_checks = []
    for h0 in (F(1), F(11,10)):
        r0 = F(1,2)-h0/9
        x0 = 1-2*r0
        for cost in (3*x0-3*r0, 3*x0-2*h0/3, 3*x0-r0-h0/3):
            require(cost <= 0, "classical_triangle_cutoff_affine_endpoint")
        require(r0 >= h0/3, "classical_triangle_cutoff_branch")
        require(F(1,2)-h0/12-r0 == h0/36, "classical_cutoff_gain")
        cutoff_checks.append({"h": str(h0), "r": str(r0)})
    for h0 in (F(1), F(27,26)):
        r0 = F(1,2)-4*h0/27
        require(triangle_loss(h0,F(7,8),r0,1) == 0,
                "pointwise_cutoff_long_pool_endpoint")
        require(3*r0 >= h0, "pointwise_cutoff_long_pool_branch")
    for h0 in (F(27,26), F(11,10)):
        r0 = (27-4*h0)/66
        require(triangle_loss(h0,F(7,8),r0,1) == 0,
                "pointwise_cutoff_middle_pool_endpoint")
        require(h0/2 <= 3*r0 <= h0, "pointwise_cutoff_middle_pool_branch")
    require((27-4*F(21,20))/66 == F(19,55), "pointwise_cutoff_numeric")
    require(F(1,2)-F(21,20)/9 == F(23,60), "classical_cutoff_numeric")
    require(F(33,80)-F(23,60) == F(7,240), "classical_cutoff_numeric_gain")
    for q in range(1,9):
        require(F(1,2*q)+F(q-1,2*q) == F(1,2), "one_sided_holder_budget")
        require(F(1,2)+F(q-1,2*q)+F(1,2*q) == 1, "hermitian_holder_budget")
        for beta in (F(1,2), F(7,8), F(1)):
            a = 2*beta-1
            require(F(1,2)+a/(2*q) >= F(1,2), "critical_correction_native_weight")
            require(beta*F(1,q)+F(q-1,2*q) == F(1,2)+a/(2*q),
                    "native_interpolation_exponent")
        for pair_weight in (F(1,2), F(1), F(5,6)):
            require(pair_weight >= F(1,2), "critical_correction_cubic_weight")
        for h_power in (F(1), 1-F(2,3*q), 1-F(1,3*q)):
            require(0 < h_power <= 1, "schwartz_row_growth")
    return {"triangle_prior_loss": "623/720", "triangle_q1_loss": "181/240",
            "triangle_q2_loss": "119/160", "q2_improvement": "35/288",
            "classical_diagonal_cutoff_at_h_21_20": "23/60",
            "pointwise_diagonal_cutoff_at_h_21_20": "19/55",
            "classical_affine_endpoint_certificates": cutoff_checks,
            "analytic_inputs_are_not_checked": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"scope": "finite exact algebra and exponent bookkeeping only",
              "mixed_forward": mixed_forward(),
              "triangle": finite_triangle(),
              "rational": rational_certificates()}
    result["predicate_counts"] = dict(sorted(COUNTS.items()))
    result["total_exact_predicates"] = sum(COUNTS.values())
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
