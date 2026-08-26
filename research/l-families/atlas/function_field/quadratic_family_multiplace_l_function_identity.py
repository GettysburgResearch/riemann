#!/usr/bin/env python3
"""Replay the exact multi-place quadratic squarefree-family identity.

The proof path is formal Euler-product and coefficient algebra.  The only
direct family control enumerates the 3,125 monic quintics over F_5 once.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial
from pathlib import Path
from typing import TypeAlias

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "quadratic_family_multiplace_l_function_identity.json"
NOTE = HERE / "QUADRATIC_FAMILY_MULTIPLACE_L_FUNCTION_IDENTITY.md"
TEST = ROOT / "tests" / "test_quadratic_family_multiplace_l_function_identity.py"
SCHEMA = "riemann.function_field.quadratic_family_multiplace_l_function_identity.v1"

MAX_SERIES_DEGREE = 5
MAX_DIRECT_Q = 5
MAX_DIRECT_PLACES = 5
MAX_CANDIDATE_POLYNOMIALS = 3_125
MAX_FAMILY_PLACE_EVALUATIONS = 15_625
MAX_AUXILIARY_AFFINE_EVALUATIONS = 25
MAX_CUMULANT_ORDER = 5
MAX_SET_PARTITIONS = 52
MAX_OUTPUT_BYTES = 32_768
WALL_SECONDS = 5.0

# Sparse polynomials in (q,t,b), keyed by their three exponents.  Here t is
# q+1-#C(F_q), and b is the middle coefficient of a genus-two numerator.
Monomial: TypeAlias = tuple[int, int, int]
Expr: TypeAlias = dict[Monomial, int]


def _clean(expression: Expr) -> Expr:
    return {
        monomial: coefficient
        for monomial, coefficient in expression.items()
        if coefficient
    }


def _add(left: Expr, right: Expr) -> Expr:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
    return _clean(result)


def _scale(expression: Expr, scalar: int) -> Expr:
    return _clean(
        {monomial: scalar * coefficient for monomial, coefficient in expression.items()}
    )


def _mul(left: Expr, right: Expr) -> Expr:
    result: Expr = {}
    for (q_left, t_left, b_left), left_coefficient in left.items():
        for (q_right, t_right, b_right), right_coefficient in right.items():
            monomial = (
                q_left + q_right,
                t_left + t_right,
                b_left + b_right,
            )
            result[monomial] = (
                result.get(monomial, 0) + left_coefficient * right_coefficient
            )
    return _clean(result)


def _coefficient_kernel(m: int, k: int) -> Expr:
    """Return [u^(2k)] (1-q*u^2)/(1-u^2)^m."""
    if m < 1 or k < 0:
        raise ValueError("m must be positive and k must be nonnegative")
    constant = comb(m + k - 1, k)
    if k == 0:
        return {(0, 0, 0): constant}
    q_coefficient = -comb(m + k - 2, k - 1)
    return _clean({(0, 0, 0): constant, (1, 0, 0): q_coefficient})


def _curve_numerator(m: int) -> list[Expr]:
    """Return P_C through the only five-place cases used for specialization."""
    one: Expr = {(0, 0, 0): 1}
    minus_t: Expr = {(0, 1, 0): -1}
    q: Expr = {(1, 0, 0): 1}
    if m in {1, 2}:
        return [one]
    if m in {3, 4}:
        return [one, minus_t, q]
    if m == 5:
        # P_C=1-t*u+b*u^2-q*t*u^3+q^2*u^4.
        return [
            one,
            minus_t,
            {(0, 0, 1): 1},
            {(1, 1, 0): -1},
            {(2, 0, 0): 1},
        ]
    raise ValueError("explicit curve numerators are restricted to 1 <= m <= 5")


def _finite_dirichlet_l_coefficients(m: int) -> list[Expr]:
    """Return L(u,psi_A), including the finite-place even-character factor."""
    numerator = _curve_numerator(m)
    if m % 2:
        return numerator
    coefficients: list[Expr] = []
    for degree in range(len(numerator) + 1):
        current = numerator[degree] if degree < len(numerator) else {}
        previous = numerator[degree - 1] if degree else {}
        coefficients.append(_add(current, _scale(previous, -1)))
    return coefficients


def formal_degree_five_coefficient(m: int) -> Expr:
    """Return the exact symbolic degree-five family sum for 1 <= m <= 5."""
    if not 1 <= m <= 5:
        raise ValueError("the degree-five specialization requires 1 <= m <= 5")
    result: Expr = {}
    for degree, l_coefficient in enumerate(_finite_dirichlet_l_coefficients(m)):
        remaining = MAX_SERIES_DEGREE - degree
        if remaining < 0 or remaining % 2:
            continue
        result = _add(
            result,
            _mul(l_coefficient, _coefficient_kernel(m, remaining // 2)),
        )
    return result


Partition = tuple[tuple[int, ...], ...]


def _set_partitions(labels: tuple[int, ...]) -> tuple[Partition, ...]:
    """Return each set partition once; the public use is capped at order five."""
    if len(labels) > MAX_CUMULANT_ORDER:
        raise ValueError("set-partition replay is capped at order five")
    if not labels:
        return ((),)
    first, rest = labels[0], labels[1:]
    result: list[Partition] = []
    for partition in _set_partitions(rest):
        result.append(((first,),) + partition)
        for index, block in enumerate(partition):
            updated = list(partition)
            updated[index] = (first,) + block
            result.append(tuple(updated))
    if len(result) > MAX_SET_PARTITIONS:
        raise RuntimeError("set-partition cap exceeded")
    return tuple(result)


def cumulant_partition_skeleton(order: int) -> dict[tuple[int, ...], int]:
    """Collect nonzero centered-moment profiles in the joint cumulant."""
    if not 2 <= order <= MAX_CUMULANT_ORDER:
        raise ValueError("cumulant order must lie between two and five")
    totals: dict[tuple[int, ...], int] = {}
    for partition in _set_partitions(tuple(range(order))):
        if any(len(block) == 1 for block in partition):
            continue
        profile = tuple(sorted(len(block) for block in partition))
        coefficient = (-1) ** (len(partition) - 1) * factorial(len(partition) - 1)
        totals[profile] = totals.get(profile, 0) + coefficient
    return totals


def five_point_pair_triple_partitions() -> tuple[
    tuple[tuple[int, ...], tuple[int, ...]], ...
]:
    """Return the ten pair/triple partitions, indexed by the triple block."""
    labels = frozenset(range(5))
    rows = []
    for triple in combinations(range(5), 3):
        pair = tuple(sorted(labels.difference(triple)))
        rows.append((pair, triple))
    if len(rows) != 10 or len({pair for pair, _ in rows}) != 10:
        raise ArithmeticError("pair/triple complement bijection failed")
    return tuple(rows)


def connected_cumulant_values(
    q: int, trace_by_subset: dict[tuple[int, ...], int]
) -> dict[str, object]:
    """Evaluate the exact order-two through order-five connected formulas.

    The supplied integer traces are formal inputs.  This helper performs no
    curve or family enumeration and does not assert that arbitrary inputs are
    geometrically realizable.
    """
    if q < 5 or q % 2 == 0:
        raise ValueError("five distinct rational places require odd q at least five")
    triples = tuple(combinations(range(5), 3))
    quadruples = tuple(combinations(range(5), 4))
    required = set(triples) | set(quadruples) | {tuple(range(5))}
    missing = sorted(required.difference(trace_by_subset))
    if missing:
        raise ValueError(f"missing formal subset traces: {missing!r}")

    family_size = q**4 * (q - 1)
    pair_sum = 2 * q - 3
    pair_cumulant = Fraction(pair_sum, family_size)
    triple_cumulants = {
        subset: Fraction(3 * (q - 2) * trace_by_subset[subset], family_size)
        for subset in triples
    }
    quadruple_cumulants = {
        subset: Fraction(
            q**2 - 10 + (4 * q - 10) * trace_by_subset[subset], family_size
        )
        - 3 * pair_cumulant**2
        for subset in quadruples
    }
    full_subset = tuple(range(5))
    triple_trace_sum = sum(trace_by_subset[subset] for subset in triples)
    fifth_cumulant = Fraction(
        (q**2 - 15) * trace_by_subset[full_subset], family_size
    ) - Fraction(3 * pair_sum * (q - 2) * triple_trace_sum, family_size**2)
    return {
        "family_size": family_size,
        "pair_sum": pair_sum,
        "kappa_2": pair_cumulant,
        "kappa_3_by_triple": triple_cumulants,
        "kappa_4_by_quadruple": quadruple_cumulants,
        "triple_trace_sum": triple_trace_sum,
        "kappa_5": fifth_cumulant,
    }


def hasse_envelope_coefficients(q: int) -> dict[str, Fraction | int]:
    """Return exact rational coefficients of the connected Hasse envelopes.

    Every key ending in ``sqrt_q_coefficient`` is to be multiplied by
    sqrt(q).  No floating-point approximation or curve enumeration occurs.
    """
    if q < 5 or q % 2 == 0:
        raise ValueError("the joint four-/five-place envelope requires odd q >= 5")
    family_size = q**4 * (q - 1)
    pair_sum = 2 * q - 3
    kappa_2 = Fraction(pair_sum, family_size)
    return {
        "family_size": family_size,
        "pair_sum": pair_sum,
        "kappa_2": kappa_2,
        "kappa_2_remainder_after_2q^-4": kappa_2 - Fraction(2, q**4),
        "kappa_3_sqrt_q_coefficient": Fraction(6 * (q - 2), family_size),
        "kappa_4_universal": Fraction(q**2 - 10, family_size),
        "kappa_4_universal_remainder_after_q^-3": Fraction(q**2 - 10, family_size)
        - Fraction(1, q**3),
        "kappa_4_trace_sqrt_q_coefficient": Fraction(2 * (4 * q - 10), family_size),
        "kappa_4_pair_correction": Fraction(3 * pair_sum**2, family_size**2),
        "kappa_5_primary_sqrt_q_coefficient": Fraction(4 * (q**2 - 15), family_size),
        "kappa_5_complement_sqrt_q_coefficient": Fraction(
            60 * pair_sum * (q - 2), family_size**2
        ),
    }


EXPECTED_FORMULAS: dict[int, Expr] = {
    1: {},
    2: {(1, 0, 0): 2, (0, 0, 0): -3},
    3: {(1, 1, 0): 3, (0, 1, 0): -6},
    4: {
        (2, 0, 0): 1,
        (0, 0, 0): -10,
        (1, 1, 0): 4,
        (0, 1, 0): -10,
    },
    5: {(2, 1, 0): 1, (0, 1, 0): -15},
}

RENDERED_FORMULAS = {
    1: "0",
    2: "2*q-3",
    3: "3*(q-2)*t",
    4: "q^2-10+(4*q-10)*t",
    5: "(q^2-15)*t",
}


def _evaluate_expression(expression: Expr, q: int, t: int, b: int = 0) -> int:
    return sum(
        coefficient * q**q_power * t**t_power * b**b_power
        for (q_power, t_power, b_power), coefficient in expression.items()
    )


def _chi_prime(value: int, q: int) -> int:
    value %= q
    if value == 0:
        return 0
    return 1 if pow(value, (q - 1) // 2, q) == 1 else -1


def _trim(polynomial: list[int], q: int) -> list[int]:
    while polynomial and polynomial[-1] % q == 0:
        polynomial.pop()
    return [coefficient % q for coefficient in polynomial]


def _remainder(dividend: list[int], divisor: list[int], q: int) -> list[int]:
    dividend = _trim(dividend[:], q)
    divisor = _trim(divisor[:], q)
    if not divisor:
        raise ZeroDivisionError("zero polynomial divisor")
    leading_inverse = pow(divisor[-1], -1, q)
    while len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        scalar = dividend[-1] * leading_inverse % q
        for index, coefficient in enumerate(divisor):
            dividend[index + shift] = (
                dividend[index + shift] - scalar * coefficient
            ) % q
        dividend = _trim(dividend, q)
    return dividend


def _is_squarefree(coefficients: list[int], q: int) -> bool:
    polynomial = _trim(coefficients[:], q)
    derivative = _trim(
        [degree * coefficients[degree] for degree in range(1, len(coefficients))],
        q,
    )
    if not derivative:
        return False
    while derivative:
        polynomial, derivative = derivative, _remainder(polynomial, derivative, q)
    return len(polynomial) == 1


def _evaluate_polynomial(coefficients: list[int], value: int, q: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % q
    return result


def _auxiliary_trace(q: int, places: tuple[int, ...]) -> tuple[int, int, int]:
    """Return (trace, affine character sum, rational infinity points)."""
    affine_character_sum = 0
    for z in range(q):
        value = 1
        for place in places:
            value = value * (place - z) % q
        affine_character_sum += _chi_prime(value, q)
    infinity_points = 1 if len(places) % 2 else 2
    trace = 1 - infinity_points - affine_character_sum
    return trace, affine_character_sum, infinity_points


def direct_control(
    q: int = MAX_DIRECT_Q,
    places: tuple[int, ...] = (0, 1, 2, 3, 4),
    *,
    candidate_cap: int = MAX_CANDIDATE_POLYNOMIALS,
) -> dict[str, object]:
    """Enumerate one declared F_5 control, sharing one pass across m=1,...,5."""
    if q != MAX_DIRECT_Q:
        raise ValueError("the direct control is restricted to q=5")
    if len(places) != MAX_DIRECT_PLACES or len({place % q for place in places}) != 5:
        raise ValueError("the direct control requires all five distinct F_5 places")
    normalized_places = tuple(place % q for place in places)
    candidate_count = q**MAX_SERIES_DEGREE
    if candidate_count > candidate_cap or candidate_count > MAX_CANDIDATE_POLYNOMIALS:
        raise RuntimeError("candidate-polynomial cap would be exceeded")
    if candidate_count * len(normalized_places) > MAX_FAMILY_PLACE_EVALUATIONS:
        raise RuntimeError("family place-evaluation cap would be exceeded")
    if q * len(normalized_places) > MAX_AUXILIARY_AFFINE_EVALUATIONS:
        raise RuntimeError("auxiliary affine-evaluation cap would be exceeded")

    squarefree_count = 0
    family_sums = {m: 0 for m in range(1, 6)}
    actual_family_place_evaluations = 0
    for low_coefficients in product(range(q), repeat=MAX_SERIES_DEGREE):
        coefficients = list(low_coefficients) + [1]
        if not _is_squarefree(coefficients, q):
            continue
        squarefree_count += 1
        prefix_product = 1
        for m, place in enumerate(normalized_places, start=1):
            value = _chi_prime(_evaluate_polynomial(coefficients, place, q), q)
            actual_family_place_evaluations += 1
            prefix_product *= value
            family_sums[m] += prefix_product

    if squarefree_count != q**4 * (q - 1):
        raise ArithmeticError("squarefree family size mismatch")

    rows: dict[str, object] = {}
    for m in range(1, 6):
        trace, affine_sum, infinity_points = _auxiliary_trace(q, normalized_places[:m])
        formal = formal_degree_five_coefficient(m)
        if any(b_power for (_, _, b_power) in formal):
            raise ArithmeticError("degree-five formula unexpectedly depends on b")
        predicted = _evaluate_expression(formal, q, trace)
        if predicted != family_sums[m]:
            raise ArithmeticError(f"direct multi-place sum mismatch at m={m}")
        rows[str(m)] = {
            "places": list(normalized_places[:m]),
            "curve_trace": trace,
            "affine_character_sum": affine_sum,
            "rational_points_at_infinity": infinity_points,
            "family_sum": family_sums[m],
            "predicted_sum": predicted,
            "formula": RENDERED_FORMULAS[m],
        }

    return {
        "q": q,
        "candidate_polynomials": candidate_count,
        "squarefree_members": squarefree_count,
        "actual_family_place_evaluations": actual_family_place_evaluations,
        "auxiliary_affine_evaluations": q * len(normalized_places),
        "rows": rows,
    }


def _sparse_rows(expression: Expr) -> list[dict[str, int]]:
    return [
        {
            "q_power": q_power,
            "trace_power": t_power,
            "middle_coefficient_power": b_power,
            "coefficient": coefficient,
        }
        for (q_power, t_power, b_power), coefficient in sorted(expression.items())
    ]


def _canonical_sha256(payload: dict[str, object]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def build_payload() -> dict[str, object]:
    started = time.monotonic()
    formal = {m: formal_degree_five_coefficient(m) for m in range(1, 6)}
    if formal != EXPECTED_FORMULAS:
        raise ArithmeticError(f"degree-five formal coefficients drifted: {formal!r}")
    skeletons = {
        order: cumulant_partition_skeleton(order)
        for order in range(2, MAX_CUMULANT_ORDER + 1)
    }
    expected_skeletons = {
        2: {(2,): 1},
        3: {(3,): 1},
        4: {(4,): 1, (2, 2): -3},
        5: {(5,): 1, (2, 3): -10},
    }
    if skeletons != expected_skeletons:
        raise ArithmeticError(f"cumulant partition skeleton drifted: {skeletons!r}")
    pair_triple_partitions = five_point_pair_triple_partitions()
    envelope_probe = hasse_envelope_coefficients(5)
    if envelope_probe["kappa_2_remainder_after_2q^-4"] != Fraction(-1, 2_500):
        raise ArithmeticError("kappa_2 asymptotic remainder drifted")
    if envelope_probe["kappa_4_universal_remainder_after_q^-3"] != Fraction(-5, 2_500):
        raise ArithmeticError("kappa_4 universal remainder drifted")
    control = direct_control()
    elapsed = time.monotonic() - started
    if elapsed > WALL_SECONDS:
        raise RuntimeError("wall-clock cap exceeded")

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "status": "PROVED_EXACT_FOR_EVERY_ODD_PRIME_POWER",
        "family": "H_n(q): monic squarefree degree-n polynomials over F_q",
        "marked_places": "distinct rational a_1,...,a_m in F_q",
        "character": "psi_A(F)=product_i chi(F(a_i)), with chi(0)=0",
        "twist_convention": {
            "polynomial": "f_A(z)=product_i(a_i-z)=(-1)^m*product_i(z-a_i)",
            "curve": "C_A: y^2=f_A(z), smooth projective completion",
            "trace": "t_A=q+1-#C_A(F_q)",
            "warning": "For odd m, the monic product is -f_A: it is the nontrivial quadratic twist when -1 is nonsquare, and F_q-isomorphic to f_A when -1 is square.",
        },
        "exact_identity": {
            "squarefree_series": "sum_{n>=0} sum_{D in H_n(q)} psi_A(D)*u^n = L(u,psi_A)*(1-q*u^2)/(1-u^2)^m",
            "odd_m": "L(u,psi_A)=P_C_A(u)",
            "even_m": "L(u,psi_A)=(1-u)*P_C_A(u)",
            "parity_reason": "infinity is ramified for odd m and split for even m because f_A has square leading coefficient when m is even",
            "kernel": "[u^(2k)](1-q*u^2)/(1-u^2)^m=binom(m+k-1,k)-q*binom(m+k-2,k-1) for k>=1",
            "general_coefficient": "If L=sum_j l_j*u^j and B_m,0=1, then S_n,m=sum_(j<=n, n-j even) l_j*B_m,(n-j)/2.",
            "degree_five_coefficient": "S_5,m=(binom(m+1,2)-q*m)*l_1+(m-q)*l_3+l_5",
        },
        "degree_five_specializations": {
            str(m): {
                "formula": RENDERED_FORMULAS[m],
                "formal_sparse_q_trace_middle": _sparse_rows(formal[m]),
            }
            for m in range(1, 6)
        },
        "degree_five_curve_numerators": {
            "m=1,2": "P_C=1",
            "m=3,4": "P_C=1-t*u+q*u^2",
            "m=5": "P_C=1-t*u+b*u^2-q*t*u^3+q^2*u^4",
            "middle_coefficient_cancellation": "The m=5 degree-five family sum is independent of b.",
        },
        "connected_joint_cumulant_corollary": {
            "probability_space": "uniform D in H_5(q), with N=q^4*(q-1)",
            "variables": "X_i=chi(D(a_i)) at distinct rational places",
            "definition": "kappa_I=sum over set partitions pi of I of (-1)^(|pi|-1)*(|pi|-1)!*product_(B in pi) E[product_(i in B) X_i]",
            "constants": {
                "N": "q^4*(q-1)",
                "C": "2*q-3",
                "trace": "t_I=q+1-#C_I(F_q), C_I:y^2=product_(i in I)(a_i-z)",
            },
            "orders": {
                "2": {
                    "scope": "any distinct pair I",
                    "formula": "kappa_I=C/N",
                },
                "3": {
                    "scope": "any distinct triple I",
                    "formula": "kappa_I=3*(q-2)*t_I/N",
                },
                "4": {
                    "scope": "any distinct four-subset I",
                    "formula": "kappa_I=[q^2-10+(4*q-10)*t_I]/N-3*C^2/N^2",
                },
                "5": {
                    "scope": "A is a five-element set of distinct places",
                    "formula": "kappa_A=(q^2-15)*t_A/N-[3*C*(q-2)/N^2]*sum_(B subset A, |B|=3) t_B",
                },
            },
            "centered_partition_skeletons": {
                str(order): {
                    "+".join(str(size) for size in profile): coefficient
                    for profile, coefficient in skeletons[order].items()
                }
                for order in skeletons
            },
            "five_point_pair_triple_partitions": [
                {
                    "pair_zero_based": list(pair),
                    "triple_zero_based": list(triple),
                }
                for pair, triple in pair_triple_partitions
            ],
            "triple_trace_warning": "The ten t_B for the three-subsets B generally differ from one another and do not collapse to the five-place genus-two trace t_A.",
            "hasse_envelopes": {
                "feasibility": "A triple requires q>=3; four distinct rational places require q>=4 (hence q>=5 for odd q); five require q>=5.",
                "trace_inputs": {
                    "three_or_four_places": "|t_I|<=2*sqrt(q) (genus one)",
                    "five_places": "|t_A|<=4*sqrt(q) (genus two)",
                    "ten_triples": "sum_(|B|=3)|t_B|<=20*sqrt(q)",
                },
                "kappa_2": "kappa_2=2*q^-4-1/[q^4*(q-1)]=2*q^-4+O(q^-5)",
                "kappa_3": "|kappa_3|<=6*(q-2)/(q-1)*q^-7/2",
                "kappa_4_exact_bound": "|kappa_4-(q^2-10)/N|<=2*(4*q-10)*sqrt(q)/N+3*C^2/N^2",
                "kappa_4_asymptotic": "kappa_4=(q^2-10)/N+O(q^-7/2)+O(q^-8)=q^-3+O(q^-7/2)",
                "kappa_5_exact_bound": "|kappa_5|<=4*(q^2-15)*sqrt(q)/N+60*C*(q-2)*sqrt(q)/N^2",
                "kappa_5_asymptotic": "kappa_5=O(q^-5/2); its pair/triple complement correction is O(q^-15/2)",
            },
        },
        "standard_identity_reference": {
            "authors": "J. P. Keating and Z. Rudnick",
            "title": "Squarefree polynomials and Mobius values in short intervals and arithmetic progressions",
            "arxiv": "https://arxiv.org/abs/1504.03444",
            "location": "equation (9.7) in the preprint; equation (10-4) in the published version",
            "scope": "The Euler quotient is standard; this packet specializes the evaluation character, curve/twist adapter, and n=5 rows.",
        },
        "direct_control": control,
        "resource_contract": {
            "maximum_series_degree": MAX_SERIES_DEGREE,
            "direct_field": MAX_DIRECT_Q,
            "maximum_direct_places": MAX_DIRECT_PLACES,
            "maximum_candidate_polynomials": MAX_CANDIDATE_POLYNOMIALS,
            "maximum_family_place_evaluations": MAX_FAMILY_PLACE_EVALUATIONS,
            "maximum_auxiliary_affine_evaluations": MAX_AUXILIARY_AFFINE_EVALUATIONS,
            "maximum_cumulant_order": MAX_CUMULANT_ORDER,
            "maximum_set_partitions": MAX_SET_PARTITIONS,
            "wall_seconds_cap": WALL_SECONDS,
            "measured_wall_seconds_is_not_canonical": True,
            "extension_field_enumeration": False,
            "sampling": False,
        },
        "claim_boundary": [
            "The theorem is an identity for a complete fixed-degree quadratic function-field family; the F_5 enumeration is only a tiny convention check.",
            "The auxiliary curve records the finite Dirichlet character and its infinity factor; it is not a claimed motive or compatible system for an individual family member.",
            "The formulas do not imply a memberwise sign, a zero theorem, principal-member amplification, RH, or GRH.",
            "No external novelty claim is made.",
        ],
        "packet_files_lf_sha256": {
            "note": _file_sha256(NOTE),
            "producer": _file_sha256(Path(__file__).resolve()),
            "test": _file_sha256(TEST),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    if len(rendered) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output-byte cap exceeded")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_bytes() != rendered:
            raise SystemExit("canonical payload drift")
        print(f"verified {OUTPUT}")
    else:
        OUTPUT.write_bytes(rendered)
        print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
