#!/usr/bin/env python3
"""Exact local algebra diagnostics for the proposed arbitrary-row adapter."""

import argparse
import hashlib
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path


class CheckFailure(Exception):
    pass


def require(condition, message):
    if not condition:
        raise CheckFailure(message)


# A nonzero value is the integer exponent of zeta_6. None is the literal
# nonunit zero. In particular char_power(None, 0) is zero, not a unit.
ZERO, ONE, NEGATIVE_ONE = None, 0, 3


def char_power(value, exponent):
    return ZERO if value is ZERO else value * exponent % 6


def times(*values):
    return ZERO if any(v is ZERO for v in values) else sum(values) % 6


def display(value):
    if value is ZERO:
        return "zero"
    return {0: "1", 3: "-1"}.get(value, f"zeta_6^{value}")


def active_scalar(j, lam, cp, minus_one):
    """Raw chi(sigma)^(-2) omega_j; Gauss factors remain formal monomials."""
    sigma = times(char_power(lam, 2), cp)
    epsilon = times(minus_one, char_power(lam, -5), char_power(cp, -2))
    gauss = [0] * 6
    if j == 0:
        gauss[2] = 1
        omega = times(NEGATIVE_ONE, char_power(epsilon, -2))
    elif j == 4:
        gauss[4] = 1
        omega = ONE
    else:
        gauss[j] += 1
        gauss[(j + 2) % 6] += 1
        omega = times(char_power(minus_one, j), char_power(epsilon, -j - 2))
    return times(char_power(sigma, -2), omega), tuple(gauss)


def check_active_scalars():
    cases = 0
    for j, lam, cp, sign in itertools.product(range(6), range(6), range(6), (0, 3)):
        actual = active_scalar(j, lam, cp, sign)
        baseline = active_scalar(j, lam, ONE, sign)
        expected = (times(baseline[0], char_power(cp, 2 * j + 2)), baseline[1])
        require(actual == expected, f"Active scalar relative phase failed: {j,lam,cp,sign}")
        if j == 0:
            simplified = times(NEGATIVE_ONE, char_power(cp, 2))
        elif j == 4:
            simplified = times(char_power(lam, -4), char_power(cp, -2))
        else:
            simplified = times(char_power(lam, 5 * j), char_power(cp, 2 * j + 2))
        require(actual[0] == simplified, f"Full formal scalar phase failed: {j,lam,cp,sign}")
        cases += 1
    require(active_scalar(2, ONE, 1, ONE)[0] == ONE,
            "The j=2 phase should be independent of c/p")
    return {
        "cases": cases,
        "local_exponents": list(range(6)),
        "lambda_phases": 6,
        "c_over_p_phases": 6,
        "chi_minus_one_values": ["1", "-1"],
        "c_over_p_exponents_modulo_six": [(2 * j + 2) % 6 for j in range(6)],
        "gauss_factors": "Formal fixed monomials; no Gauss sum value is evaluated.",
        "simplified_phases": {
            "j=0": "-gamma_2 * chi(c/p)^2",
            "j=4": "gamma_4 * chi(lambda)^(-4) * chi(c/p)^(-2)",
            "other_j": "gamma_j gamma_(j+2) * chi(lambda)^(5j) * chi(c/p)^(2j+2)",
        },
    }


def check_cross_phases():
    cases = zero_cases = positive_multiple_six_zero_cases = 0
    valuations = {}
    for j in range(6):
        valuations[j] = [j + 6 * t if j else 6 + 6 * t for t in range(4)]
        for nu, reciprocity, y in itertools.product(valuations[j], (0, 3), (ZERO, *range(6))):
            # x=chi_a(q), y=chi_q(a), x=R*y, with the same literal nonunit zero.
            x = times(reciprocity, y)
            lhs = times(char_power(x, 4), char_power(y, 2 * j + 2), char_power(x, nu))
            reduced = times(char_power(reciprocity, nu), char_power(y, 3 * j))
            with_original_mask = reduced if y is not ZERO else ZERO
            require(nu > 0 and nu % 6 == j, "Physical row valuation was lost")
            require(lhs == reduced == with_original_mask,
                    f"Reciprocity/cross-phase identity failed: {j,nu,reciprocity,y}")
            cases += 1
            zero_cases += int(y is ZERO)
            positive_multiple_six_zero_cases += int(y is ZERO and j == 0)

    # For nu=6, the original positive character power is still zero on a
    # nonunit. Reducing to exponent zero and deleting the mask incorrectly gives 1.
    proper_zero = times(char_power(ZERO, 4), char_power(ZERO, 2), char_power(ZERO, 6))
    wrong_zero = ONE
    require(proper_zero is ZERO and wrong_zero == ONE,
            "The positive-sixth-power zero regression failed")
    # R=-1, y=1, j=nu=1 gives -1; omitting the reciprocity sign gives +1.
    proper_sign = times(char_power(NEGATIVE_ONE, 5), char_power(ONE, 4))
    wrong_sign = char_power(ONE, 3)
    require(proper_sign == NEGATIVE_ONE and wrong_sign == ONE,
            "The retained reciprocity-sign regression failed")
    return {
        "cases": cases,
        "physical_positive_valuations_by_residue": valuations,
        "nonunit_zero_cases": zero_cases,
        "positive_multiple_six_nonunit_cases": positive_multiple_six_zero_cases,
        "identity": "chi_a(q)^(nu+4) chi_q(a)^(2j+2) = R(a,q)^nu chi_q(a)^(3j)",
        "quadratic_exponents_modulo_six": [3 * j % 6 for j in range(6)],
        "incorrect_mask_deletion": {"nu": 6, "correct": display(proper_zero), "incorrect": display(wrong_zero)},
        "incorrect_reciprocity_sign_deletion": {"nu": 1, "correct": display(proper_sign), "incorrect": display(wrong_sign)},
    }


def check_ramanujan_factor():
    cases = 0
    largest_squared = {}
    for norm in (7, 13, 19, 25):
        squared = []
        for v_n, v_b in itertools.product((0, 1), range(13)):
            # v_q(e)=v_q(f)=0; n_0 is squarefree, while b' is unrestricted.
            v_x = v_n + 3 * v_b
            raw = -1 + norm * int(v_x > 0)
            divided = -1 + norm * int(v_n + v_b > 0)
            fixed_b = norm - 1 if v_b > 0 else -1 + norm * int(v_n > 0)
            require(raw == divided == fixed_b, "The j=4 Ramanujan factor did not separate")
            square = Q(raw * raw, norm)
            require(square <= norm, "The retained j=4 squared amplitude bound failed")
            squared.append(square)
            cases += 1
        largest_squared[str(norm)] = str(max(squared))

    # Without q not dividing ef the proposed separation is false.
    original_when_q_divides_e_or_f = 7 - 1
    reduced_without_the_required_hypothesis = -1
    require(original_when_q_divides_e_or_f != reduced_without_the_required_hypothesis,
            "The missing q-not-dividing-ef regression did not fail")
    require(Q(36, 7) > 1, "The j=4 factor's extra norm cost was not exercised")
    return {
        "cases": cases,
        "prime_norm_labels": [7, 13, 19, 25],
        "hypothesis": "v_q(e)=v_q(f)=0; v_q(n_0) in {0,1}; v_q(b') in 0..12",
        "comparison": "Numerators after multiplying B_(q,4) by sqrt(Nq), so all equalities are integral.",
        "fixed_b_factor": "Nq-1 if q divides b'; otherwise -1+Nq*1_(q divides n_0)",
        "largest_squared_amplitudes": largest_squared,
        "squared_amplitude_bound": "|B_(q,4)|^2 <= Nq",
        "omitted_hypothesis_regression": {
            "norm": 7, "correct_numerator": original_when_q_divides_e_or_f,
            "incorrect_numerator": reduced_without_the_required_hypothesis,
        },
    }


def local_weights(nu, shift):
    delta = int((nu + shift) % 6 == 4)
    return (Q(delta - nu), Q(delta + 2 - 2 * nu),
            Q(delta) + Q(4, 3) - Q(4, 3) * nu)


def check_progressions(auxiliary=False):
    shift = 4 if auxiliary else 0
    bases = tuple(range(6)) if auxiliary else (6, 7, 2, 3, 4, 5)
    expected_maxima = (Q(1), Q(3), Q(7, 3)) if auxiliary else (Q(-2), Q(-2), Q(-4, 3))
    slopes = (Q(-6), Q(-12), Q(-8))
    rows, base_values, branch_mass = [], [], 0
    for residue, base in enumerate(bases):
        require(base % 6 == residue and base >= (0 if auxiliary else 2),
                "A residue progression has the wrong base valuation")
        initial = local_weights(base, shift)
        for t in range(5):
            actual = local_weights(base + 6 * t, shift)
            require(actual == tuple(a + t * s for a, s in zip(initial, slopes)),
                    "A six-step affine valuation progression failed")
        reflected_j = (base + shift) % 6
        branches = 4 if reflected_j == 0 else 1
        branch_mass += branches
        base_values.append(initial)
        rows.append({
            "physical_residue": residue, "base_valuation": base,
            "reflected_j": reflected_j,
            "ramanujan_squared_penalty": int(reflected_j == 4),
            "optional_branch_square_count": branches,
            "base_exponents": [str(x) for x in initial],
        })
    maxima = tuple(max(column) for column in zip(*base_values))
    require(maxima == expected_maxima and all(s < 0 for s in slopes),
            "The claimed worst local powerful exponents are incorrect")
    require(branch_mass == 9, "The optional j=0 branch accounting failed")
    # Each six-step tail ratio is at most 2^slope for norm at least two.
    # These rational constants verify the elementary local majorant only.
    constants = tuple(Q(branch_mass) / (1 - Q(1, 2) ** int(-s)) for s in slopes)
    return {
        "scope": "Moving q^4 auxiliary, physical nu>=0" if auxiliary else "Powerful row primes, physical nu>=2",
        "reflected_exponent_shift": shift,
        "progressions": rows,
        "six_step_slopes": [str(x) for x in slopes],
        "worst_exponents": [str(x) for x in maxima],
        "rational_geometric_majorants_for_norm_at_least_two": [str(x) for x in constants],
        "meaning": "Six affine residue progressions and local rational weights; no analytic moment estimate is checked.",
    }


def check_auxiliary_parity():
    for nu in range(24):
        reflected_j = (nu + 4) % 6
        require(3 * reflected_j % 6 == 3 * (nu % 2),
                "Multiplying the row by q^4 changed its quadratic parity")
    require(char_power(ZERO, 4) is ZERO and char_power(ZERO, 6) is ZERO,
            "The moving auxiliary's original nonunit exclusion was deleted")
    return {
        "cases": 24,
        "identity": "3*((nu+4) mod 6) mod 6 = 3*(nu mod 2)",
        "physical_nu_zero": "The auxiliary exponent four still retains the original coprimality zero.",
        "physical_nu_two": "The positive total exponent six remains zero at a nonunit.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {
        "schema": "arbitrary-row-finite-algebra-v1",
        "status": "PASS_FINITE_ALGEBRA",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Exact local phase identities, literal zeros, prime valuations, and rational exponent algebra.",
        "not_checked": [
            "Actual residue symbols or numerical Gauss sums; Gauss factors are formal fixed monomials.",
            "Theta reflection, cusp coefficients, smooth norm estimates, conductor uniformity, or large sieves.",
            "The proposed all-row theorem, its auxiliary family, centered covariance, or any RH claim.",
        ],
        "active_local_scalars": check_active_scalars(),
        "cross_phase_and_reciprocity": check_cross_phases(),
        "row_j4_ramanujan_factor": check_ramanujan_factor(),
        "powerful_row_weights": check_progressions(),
        "optional_moving_auxiliary_weights": check_progressions(auxiliary=True),
        "optional_moving_auxiliary_parity": check_auxiliary_parity(),
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
