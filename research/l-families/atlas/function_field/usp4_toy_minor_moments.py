#!/usr/bin/env python3
"""Exact USp(4) Haar moments for the genus-two toy coefficient minor.

If the normalized reciprocal roots are the eigenvalues of U in USp(4), then

    F(U) = (Tr U)^2 - e_2(U)^2

is the q-to-infinity model for (q*a_1^2-a_2^2)/q^2.  This module evaluates
the first six Haar moments by the C_2 Weyl constant-term formula and compares
them with the exact q=3,5,7 histograms.  A cubic-square majorant also turns
those six moments into an exact negative-sign probability lower bound.  It
uses only small integer Laurent polynomials; there is no random-matrix
simulation or numerical integration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Iterable, Mapping, Sequence


Exponent = tuple[int, int]
Laurent = dict[Exponent, int]
HERE = Path(__file__).resolve().parent
Q_SCAN_FIXTURE = HERE / "genus2_q_scan.json"
FROZEN_MAX_MOMENT = 6
HAAR_STATUS = "RIGOROUS_CERTIFIED_WEYL_CONSTANT_TERM"
COMPARISON_STATUS = "CONJECTURAL_USP4_LIMIT_NOT_A_THEOREM"
FROZEN_PATTERN_STATUS = "EXACT_FOR_Q_3_5_7_ONLY"
HAAR_RANGE_MINIMUM = Fraction(-20, 1)
HAAR_RANGE_MAXIMUM = Fraction(4, 3)
SIGN_MAJORANT_STATUS = "PROVED_EXACT_DEGREE_SIX_MOMENT_BOUND"
SIGN_MAJORANT_COEFFICIENTS = (
    Fraction(1, 1),
    Fraction(5405, 12023),
    Fraction(264, 12023),
    Fraction(-23, 12023),
)
SUPPORT_MAJORANT_BERNSTEIN_COEFFICIENTS = (
    Fraction(1985264, 38115),
    Fraction(145906487, 2401245),
    Fraction(3063511081, 43222410),
    Fraction(198471997, 2401245),
    Fraction(1001492, 10395),
)


def _clean(poly: Mapping[Exponent, int]) -> Laurent:
    return {exponent: coefficient for exponent, coefficient in poly.items() if coefficient}


def add(*polynomials: Mapping[Exponent, int]) -> Laurent:
    result: Laurent = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return _clean(result)


def scale(polynomial: Mapping[Exponent, int], coefficient: int) -> Laurent:
    return _clean({exponent: coefficient * value for exponent, value in polynomial.items()})


def multiply(left: Mapping[Exponent, int], right: Mapping[Exponent, int]) -> Laurent:
    result: Laurent = {}
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            exponent = (left_x + right_x, left_y + right_y)
            result[exponent] = result.get(exponent, 0) + left_coefficient * right_coefficient
    return _clean(result)


def power(polynomial: Mapping[Exponent, int], exponent: int) -> Laurent:
    if exponent < 0:
        raise ValueError("Laurent-polynomial exponent must be nonnegative")
    result: Laurent = {(0, 0): 1}
    factor = dict(polynomial)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, factor)
        remaining //= 2
        if remaining:
            factor = multiply(factor, factor)
    return result


def substitute_square(polynomial: Mapping[Exponent, int]) -> Laurent:
    return {(2 * left, 2 * right): coefficient for (left, right), coefficient in polynomial.items()}


def divide_exact(polynomial: Mapping[Exponent, int], divisor: int) -> Laurent:
    if divisor == 0 or any(coefficient % divisor for coefficient in polynomial.values()):
        raise ArithmeticError("Laurent polynomial is not coefficientwise divisible")
    return _clean({exponent: coefficient // divisor for exponent, coefficient in polynomial.items()})


def constant_term(polynomial: Mapping[Exponent, int]) -> int:
    return polynomial.get((0, 0), 0)


def evaluate_at_identity(polynomial: Mapping[Exponent, int]) -> int:
    return sum(polynomial.values())


def statistic_in_trace_coordinates(left: Fraction, right: Fraction) -> Fraction:
    """Evaluate F for eigenangle traces left=2cos(theta_1), right=2cos(theta_2)."""

    if not -2 <= left <= 2 or not -2 <= right <= 2:
        raise ValueError("trace coordinates must both lie in [-2,2]")
    return (left - right) ** 2 - 4 - left * left * right * right


def trace_character() -> Laurent:
    return {(1, 0): 1, (-1, 0): 1, (0, 1): 1, (0, -1): 1}


def exterior_square_character() -> Laurent:
    return {
        (0, 0): 2,
        (1, 1): 1,
        (1, -1): 1,
        (-1, 1): 1,
        (-1, -1): 1,
    }


def statistic_character() -> Laurent:
    return add(power(trace_character(), 2), scale(power(exterior_square_character(), 2), -1))


def fundamental_five_character() -> Laurent:
    # wedge^2(Standard_4) = 1 + V_{omega_2}.
    return add(exterior_square_character(), {(0, 0): -1})


def traceless_symmetric_square_character() -> Laurent:
    # V_{2 omega_2} = Sym^2(V_{omega_2}) - 1, of dimension 14.
    five = fundamental_five_character()
    symmetric_square = divide_exact(add(power(five, 2), substitute_square(five)), 2)
    return add(symmetric_square, {(0, 0): -1})


def character_identity_residual() -> Laurent:
    # F = -(1 + chi_{omega_2} + chi_{2 omega_2}).
    return add(
        statistic_character(),
        {(0, 0): 1},
        fundamental_five_character(),
        traceless_symmetric_square_character(),
    )


def weyl_density() -> Laurent:
    density: Laurent = {(0, 0): 1}
    for root in ((2, 0), (0, 2), (1, 1), (1, -1)):
        positive = {root: 1}
        negative = {(-root[0], -root[1]): 1}
        density = multiply(density, add({(0, 0): 1}, scale(positive, -1)))
        density = multiply(density, add({(0, 0): 1}, scale(negative, -1)))
    return density


def haar_moments(max_moment: int = FROZEN_MAX_MOMENT) -> list[int]:
    if not 1 <= max_moment <= FROZEN_MAX_MOMENT:
        raise ValueError(f"max_moment must lie in [1,{FROZEN_MAX_MOMENT}]")
    density = weyl_density()
    weyl_order = constant_term(density)
    if weyl_order != 8:
        raise ArithmeticError(f"unexpected C2 Weyl normalization {weyl_order}")
    statistic = statistic_character()
    moments: list[int] = []
    current: Laurent = {(0, 0): 1}
    for _ in range(max_moment):
        current = multiply(current, statistic)
        numerator = constant_term(multiply(current, density))
        if numerator % weyl_order:
            raise ArithmeticError("Haar constant term is not divisible by the Weyl order")
        moments.append(numerator // weyl_order)
    return moments


def centered_moments(raw_moments: Sequence[int]) -> list[int]:
    """Convert exact raw moments E[F^n] to E[(F-E[F])^n]."""

    if not raw_moments:
        return []
    raw_with_zero = [1, *raw_moments]
    mean = raw_moments[0]
    return [
        sum(
            comb(order, power)
            * (-mean) ** (order - power)
            * raw_with_zero[power]
            for power in range(order + 1)
        )
        for order in range(1, len(raw_moments) + 1)
    ]


def cumulants(raw_moments: Sequence[int]) -> list[int]:
    """Convert exact raw moments to cumulants by the triangular recurrence."""

    raw_with_zero = [1, *raw_moments]
    values = [0]
    for order in range(1, len(raw_with_zero)):
        correction = sum(
            comb(order - 1, index - 1)
            * values[index]
            * raw_with_zero[order - index]
            for index in range(1, order)
        )
        values.append(raw_with_zero[order] - correction)
    return values[1:]


def convolve_rational(
    left: Sequence[Fraction], right: Sequence[Fraction]
) -> list[Fraction]:
    """Multiply two ordinary polynomials with exact rational coefficients."""

    if not left or not right:
        return []
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return result


def add_rational_polynomials(
    left: Sequence[Fraction], right: Sequence[Fraction]
) -> list[Fraction]:
    """Add ordinary exact polynomials and remove trailing zero coefficients."""

    result = [Fraction(0) for _ in range(max(len(left), len(right)))]
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    while result and result[-1] == 0:
        result.pop()
    return result


def scale_rational_polynomial(
    coefficients: Sequence[Fraction], scalar: Fraction
) -> list[Fraction]:
    return [scalar * coefficient for coefficient in coefficients]


def affine_compose_rational(
    coefficients: Sequence[Fraction], offset: Fraction, slope: Fraction
) -> list[Fraction]:
    """Return P(offset+slope*x) for an ordinary exact polynomial P."""

    result: list[Fraction] = []
    affine_power = [Fraction(1)]
    for coefficient in coefficients:
        result = add_rational_polynomials(
            result, scale_rational_polynomial(affine_power, coefficient)
        )
        affine_power = convolve_rational(affine_power, [offset, slope])
    return result


def bernstein_to_power(coefficients: Sequence[Fraction]) -> list[Fraction]:
    """Convert degree-n Bernstein coefficients on [0,1] to power coefficients."""

    if not coefficients:
        return []
    degree = len(coefficients) - 1
    result: list[Fraction] = []
    for index, coefficient in enumerate(coefficients):
        basis = convolve_rational(
            [Fraction(0)] * index + [Fraction(1)],
            [
                Fraction(comb(degree - index, power)) * (-1) ** power
                for power in range(degree - index + 1)
            ],
        )
        result = add_rational_polynomials(
            result,
            scale_rational_polynomial(basis, coefficient * comb(degree, index)),
        )
    return result


def support_adapted_sign_majorant() -> dict[str, list[Fraction]]:
    """Construct and exactly verify a support-adapted degree-six majorant."""

    polynomial_t = [Fraction(1)]
    for factor in (
        [Fraction(1), Fraction(1)],
        convolve_rational([Fraction(-13), Fraction(20)], [Fraction(-13), Fraction(20)]),
        convolve_rational([Fraction(-7), Fraction(40)], [Fraction(-7), Fraction(40)]),
        [Fraction(2927), Fraction(-2792)],
    ):
        polynomial_t = convolve_rational(polynomial_t, factor)
    polynomial_t = scale_rational_polynomial(polynomial_t, Fraction(1, 14407470))
    polynomial_x = affine_compose_rational(
        polynomial_t, Fraction(7, 8), Fraction(3, 32)
    )

    quotient_z = bernstein_to_power(SUPPORT_MAJORANT_BERNSTEIN_COEFFICIENTS)
    quotient_t = affine_compose_rational(quotient_z, Fraction(-7), Fraction(8))
    interval_factor = convolve_rational(
        [Fraction(-7, 8), Fraction(1)], [Fraction(1), Fraction(-1)]
    )
    reconstructed = add_rational_polynomials(
        [Fraction(1)], convolve_rational(interval_factor, quotient_t)
    )
    if reconstructed != polynomial_t:
        raise ArithmeticError("support-adapted sign-majorant identity failed")
    if sum(polynomial_t[index] * Fraction(7, 8) ** index for index in range(7)) != 1:
        raise ArithmeticError("support majorant does not equal one at t=7/8")
    if sum(polynomial_t) != 1:
        raise ArithmeticError("support majorant does not equal one at t=1")
    if not all(coefficient > 0 for coefficient in SUPPORT_MAJORANT_BERNSTEIN_COEFFICIENTS):
        raise ArithmeticError("support-majorant Bernstein positivity failed")
    return {
        "polynomial_t": polynomial_t,
        "polynomial_x": polynomial_x,
        "quotient_t": quotient_t,
        "quotient_bernstein": list(SUPPORT_MAJORANT_BERNSTEIN_COEFFICIENTS),
    }


def polynomial_moment(
    coefficients: Sequence[Fraction], raw_moments: Sequence[int | Fraction]
) -> Fraction:
    """Evaluate E[P(F)] exactly from P's coefficients and raw moments of F."""

    if len(raw_moments) < len(coefficients) - 1:
        raise ValueError("insufficient raw moments for polynomial expectation")
    moments = [Fraction(1), *(Fraction(value) for value in raw_moments)]
    return sum(
        (coefficient * moments[order] for order, coefficient in enumerate(coefficients)),
        Fraction(0),
    )


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def negative_sign_moment_certificate(
    haar: Sequence[int],
    comparisons: Sequence[Mapping[str, object]],
    families: Sequence[Mapping[str, object]],
) -> dict[str, object]:
    """Build a six-moment lower bound for the negative-sign probability.

    On the exact support [-20,4/3], the chosen cubic R satisfies R(x)>=1 for
    x>=0.  Hence 1_{x>=0} <= R(x)^2, and the expectation of this degree-six
    majorant is determined by the first six raw moments alone.
    """

    if len(haar) != 6:
        raise ValueError("negative-sign certificate requires exactly six Haar moments")
    comparisons_by_q = {int(item["q"]): item for item in comparisons}
    families_by_q = {int(item["q"]): item for item in families}
    if set(comparisons_by_q) != {3, 5, 7} or set(families_by_q) != {3, 5, 7}:
        raise ValueError("negative-sign certificate requires q=3,5,7")

    square = convolve_rational(SIGN_MAJORANT_COEFFICIENTS, SIGN_MAJORANT_COEFFICIENTS)
    haar_nonnegative_upper = polynomial_moment(square, haar)
    haar_negative_lower = 1 - haar_nonnegative_upper
    if haar_nonnegative_upper != Fraction(7663, 12023):
        raise ArithmeticError("unexpected Haar sign-majorant expectation")

    support_majorant = support_adapted_sign_majorant()
    support_haar_upper = polynomial_moment(support_majorant["polynomial_x"], haar)
    support_haar_lower = 1 - support_haar_upper
    if support_haar_upper != Fraction(3879608783, 6358302720):
        raise ArithmeticError("unexpected support-adapted Haar majorant expectation")

    finite_bounds: list[dict[str, object]] = []
    support_finite_bounds: list[dict[str, object]] = []
    for q in (3, 5, 7):
        comparison = comparisons_by_q[q]
        family = families_by_q[q]
        finite_raw = [
            Fraction(*moment["finite_exact"]) for moment in comparison["moments"]
        ]
        nonnegative_upper = polynomial_moment(square, finite_raw)
        negative_lower = 1 - nonnegative_upper
        sign_counts = family["sign_counts"]
        observed_negative = Fraction(
            int(sign_counts["negative"]), int(family["member_count"])
        )
        if not Fraction(0) < negative_lower <= observed_negative:
            raise ArithmeticError(f"q={q} finite negative-sign bound failed")
        finite_bounds.append(
            {
                "q": q,
                "moment_majorant_nonnegative_upper_bound": _fraction_pair(
                    nonnegative_upper
                ),
                "negative_probability_lower_bound": _fraction_pair(negative_lower),
                "observed_negative_fraction": _fraction_pair(observed_negative),
                "verified_bound_holds": True,
            }
        )
        support_nonnegative_upper = polynomial_moment(
            support_majorant["polynomial_x"], finite_raw
        )
        support_negative_lower = 1 - support_nonnegative_upper
        if not negative_lower < support_negative_lower <= observed_negative:
            raise ArithmeticError(f"q={q} support-adapted negative-sign bound failed")
        support_finite_bounds.append(
            {
                "q": q,
                "moment_majorant_nonnegative_upper_bound": _fraction_pair(
                    support_nonnegative_upper
                ),
                "negative_probability_lower_bound": _fraction_pair(
                    support_negative_lower
                ),
                "observed_negative_fraction": _fraction_pair(observed_negative),
                "verified_bound_holds": True,
            }
        )

    return {
        "status": SIGN_MAJORANT_STATUS,
        "event": "F<0",
        "support": {
            "minimum": _fraction_pair(HAAR_RANGE_MINIMUM),
            "maximum": _fraction_pair(HAAR_RANGE_MAXIMUM),
        },
        "majorant": {
            "polynomial": "R(x)=1+(5405*x+264*x^2-23*x^3)/12023",
            "coefficients_low_to_high": [
                _fraction_pair(value) for value in SIGN_MAJORANT_COEFFICIENTS
            ],
            "square_coefficients_low_to_high": [
                _fraction_pair(value) for value in square
            ],
            "pointwise_statement": "1_{x>=0} <= R(x)^2 on [-20,4/3]",
            "positive_interval_factorization": (
                "R(x)-1=x*(5405+264*x-23*x^2)/12023"
            ),
            "quadratic_endpoint_values_on_0_to_4_over_3": [
                _fraction_pair(Fraction(5405)),
                _fraction_pair(Fraction(51445, 9)),
            ],
            "proof": (
                "The quadratic 5405+264*x-23*x^2 is concave, so its minimum on "
                "[0,4/3] occurs at an endpoint; both stored endpoint values are positive. "
                "Thus R(x)>=1 for x>=0, while R(x)^2>=0 handles x<0."
            ),
            "construction": (
                "The coefficients solve the exact normal equations minimizing E[R(F)^2] "
                "among Haar cubics with R(0)=1; only the displayed pointwise inequality is "
                "used for the probability bound."
            ),
        },
        "haar": {
            "moment_majorant_nonnegative_upper_bound": _fraction_pair(
                haar_nonnegative_upper
            ),
            "negative_probability_lower_bound": _fraction_pair(haar_negative_lower),
        },
        "finite_q_bounds": finite_bounds,
        "support_adapted_majorant": {
            "coordinate": (
                "t=(3*x+28)/32 maps x in [-20,4/3] to t in [-1,1], with "
                "x>=0 equivalent to t>=7/8"
            ),
            "polynomial_factorization": (
                "p(t)=(t+1)*(20*t-13)^2*(40*t-7)^2*(2927-2792*t)/14407470"
            ),
            "coefficients_in_x_low_to_high": [
                _fraction_pair(value) for value in support_majorant["polynomial_x"]
            ],
            "pointwise_statement": (
                "1_{x>=0} <= p((3*x+28)/32) on [-20,4/3]"
            ),
            "nonnegative_support_proof": (
                "On t in [-1,1], t+1>=0, the two middle factors are squares, "
                "and 2927-2792*t>=135, so p(t)>=0."
            ),
            "positive_interval_factorization": (
                "p(t)-1=(t-7/8)*(1-t)*Q(t)"
            ),
            "positive_interval_bernstein_coordinate": "z=8*t-7 in [0,1]",
            "positive_interval_quotient_bernstein_coefficients_degree_4": [
                _fraction_pair(value)
                for value in support_majorant["quotient_bernstein"]
            ],
            "positive_interval_proof": (
                "Every stored Bernstein coefficient of Q is positive, hence Q(t)>0 "
                "on [7/8,1]; both remaining factors are nonnegative there."
            ),
            "haar": {
                "moment_majorant_nonnegative_upper_bound": _fraction_pair(
                    support_haar_upper
                ),
                "negative_probability_lower_bound": _fraction_pair(
                    support_haar_lower
                ),
            },
            "finite_q_bounds": support_finite_bounds,
            "strictly_improves_cubic_square_bound": True,
            "construction_scope": (
                "This rational support-adapted certificate is not claimed optimal among all "
                "degree-six polynomial majorants."
            ),
        },
        "conditional_consequence": {
            "status": "CONDITIONAL_ON_FIRST_SIX_MOMENT_CONVERGENCE",
            "not_an_equidistribution_proof": True,
            "assumption": (
                "The first six raw moments of the normalized finite-family statistic "
                "converge to the six stored USp(4) Haar moments."
            ),
            "statement": (
                "Under that assumption, liminf_q Pr(K_D/q^2<0) >= "
                "2478693937/6358302720."
            ),
            "reason": (
                "The expectation of the stronger support-adapted degree-six majorant then "
                "converges to 3879608783/6358302720; no boundary-mass or "
                "weak-convergence argument is needed."
            ),
        },
        "scope": (
            "These are exact lower bounds, not an evaluation of the Haar sign probability. "
            "The cubic-square construction is retained as a simple baseline; the rational "
            "support-adapted polynomial is stronger but is not claimed optimal. The q=3,5,7 "
            "rows are exact frozen checks; the liminf statement is conditional."
        ),
    }


def finite_moments(family: Mapping[str, object], max_moment: int) -> list[Fraction]:
    q = int(family["q"])
    member_count = int(family["member_count"])
    histogram = {int(key): int(value) for key, value in dict(family["K_histogram"]).items()}
    if sum(histogram.values()) != member_count:
        raise ValueError(f"q={q} histogram count mismatch")
    return [
        Fraction(
            sum(count * numerator**moment for numerator, count in histogram.items()),
            member_count * q ** (2 * moment),
        )
        for moment in range(1, max_moment + 1)
    ]


def frozen_moment_pattern(
    comparisons: Sequence[Mapping[str, object]], haar: Sequence[int]
) -> dict[str, object]:
    """Certify directional facts about the three frozen finite comparisons only."""

    q_values = [int(comparison["q"]) for comparison in comparisons]
    if q_values != [3, 5, 7]:
        raise ValueError("frozen moment pattern requires q=3,5,7 in order")
    per_order: list[dict[str, object]] = []
    for order, target in enumerate(haar, start=1):
        values = [
            Fraction(*comparison["moments"][order - 1]["finite_exact"])
            for comparison in comparisons
        ]
        gaps = [abs(value - target) for value in values]
        same_sign = all((value > 0) == (target > 0) and value != 0 for value in values)
        below = all(abs(value) < abs(target) for value in values)
        increasing = all(abs(left) < abs(right) for left, right in zip(values, values[1:]))
        decreasing_gap = all(left > right for left, right in zip(gaps, gaps[1:]))
        if not (same_sign and below and increasing and decreasing_gap):
            raise ArithmeticError(f"frozen directional moment pattern failed at order {order}")
        per_order.append(
            {
                "order": order,
                "same_nonzero_sign_as_haar": same_sign,
                "absolute_value_below_haar": below,
                "absolute_value_strictly_increases_with_q": increasing,
                "absolute_gap_strictly_decreases_with_q": decreasing_gap,
            }
        )
    return {
        "status": FROZEN_PATTERN_STATUS,
        "not_a_theorem_beyond_frozen_fields": True,
        "q_values": q_values,
        "per_order": per_order,
        "interpretation": (
            "For moment orders 1 through 6 at q=3,5,7 only, the finite moment has the "
            "Haar sign, smaller absolute value, increasing absolute magnitude, and decreasing "
            "absolute gap as q increases. No monotonicity or rate is asserted for another q."
        ),
    }


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_fixture(q_scan_fixture: Path = Q_SCAN_FIXTURE) -> dict[str, object]:
    q_scan = json.loads(q_scan_fixture.read_text(encoding="utf-8"))
    if q_scan.get("schema") != "riemann.function_field.genus2_q_scan.v1":
        raise ValueError("unexpected genus-two q-scan schema")
    if q_scan.get("resource_contract", {}).get("frozen_q_values") != [3, 5, 7]:
        raise ValueError("USp(4) comparator requires the frozen q=3,5,7 scan")
    if character_identity_residual():
        raise ArithmeticError("USp(4) character identity failed")
    haar = haar_moments()
    centered = centered_moments(haar)
    haar_cumulants = cumulants(haar)
    source_text = Path(__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
    comparisons: list[dict[str, object]] = []
    for family in q_scan["families"]:
        q = int(family["q"])
        moments = finite_moments(family, FROZEN_MAX_MOMENT)
        comparisons.append(
            {
                "q": q,
                "member_count": int(family["member_count"]),
                "moments": [
                    {
                        "order": order,
                        "finite_exact": _fraction_pair(value),
                        "usp4_haar_exact": haar[order - 1],
                        "finite_minus_haar": _fraction_pair(value - haar[order - 1]),
                    }
                    for order, value in enumerate(moments, start=1)
                ],
            }
        )
    payload: dict[str, object] = {
        "schema": "riemann.function_field.usp4_toy_minor_moments.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.USP4.TOY_MINOR.MOMENTS.V1",
        "rigor_level": HAAR_STATUS,
        "definition": (
            "For U in USp(4), F(U)=(Tr U)^2-e_2(U)^2; compare its exact Haar moments "
            "with the exact finite moments of K/q^2=(q*a_1^2-a_2^2)/q^2."
        ),
        "character_identity": {
            "status": "PROVED_EXACT_LAURENT_IDENTITY",
            "formula": "F=-(1+chi_{omega_2}+chi_{2*omega_2})",
            "dimensions_at_identity": {
                "standard": evaluate_at_identity(trace_character()),
                "omega_2": evaluate_at_identity(fundamental_five_character()),
                "2*omega_2": evaluate_at_identity(traceless_symmetric_square_character()),
                "F": evaluate_at_identity(statistic_character()),
            },
            "haar_mean_consequence": -1,
        },
        "range_certificate": {
            "status": "PROVED_EXACT_ELEMENTARY_OPTIMIZATION",
            "trace_coordinates": "X=2*cos(theta_1), Y=2*cos(theta_2), each in [-2,2]",
            "formula": "F=(X+Y)^2-(2+X*Y)^2=(X-Y)^2-4-X^2*Y^2",
            "minimum": _fraction_pair(HAAR_RANGE_MINIMUM),
            "minimum_witnesses": [
                {"X": [-2, 1], "Y": [-2, 1]},
                {"X": [2, 1], "Y": [2, 1]},
            ],
            "maximum": _fraction_pair(HAAR_RANGE_MAXIMUM),
            "maximum_witnesses": [
                {"X": [2, 1], "Y": [-2, 3]},
                {"X": [-2, 3], "Y": [2, 1]},
                {"X": [-2, 1], "Y": [2, 3]},
                {"X": [2, 3], "Y": [-2, 1]},
            ],
            "proof": (
                "The lower bound follows from (X-Y)^2>=0 and X^2Y^2<=16. For the upper "
                "bound, fix Y: the quadratic in X is convex when |Y|<=1, so an endpoint gives "
                "-3Y^2+4|Y|<=4/3; when |Y|>1, checking the feasible vertex and endpoints "
                "gives the same bound."
            ),
        },
        "weyl_certificate": {
            "root_system": "C2",
            "positive_roots_as_exponent_pairs": [[2, 0], [0, 2], [1, 1], [1, -1]],
            "formula": "integral f = CT(f*product_{alpha>0}(1-X^alpha)(1-X^-alpha))/8",
            "density_constant_term": constant_term(weyl_density()),
            "maximum_moment": FROZEN_MAX_MOMENT,
            "haar_moments_orders_1_through_6": haar,
            "haar_centered_moments_orders_1_through_6": centered,
            "haar_cumulants_orders_1_through_6": haar_cumulants,
            "arithmetic": "exact integer Laurent-polynomial convolution",
        },
        "producer": {
            "source": "research/l-families/atlas/function_field/usp4_toy_minor_moments.py",
            "source_sha256_lf_normalized": hashlib.sha256(
                source_text.encode("utf-8")
            ).hexdigest(),
            "runtime_contract": "Python 3.11+ standard library; exact integer/rational arithmetic",
            "input_provenance": "content-bound exact q-scan histogram fixture",
        },
        "finite_source": {
            "path": "research/l-families/atlas/function_field/genus2_q_scan.json",
            "canonical_sha256": _canonical_sha256(q_scan),
            "coverage": "all monic squarefree quintics over F_q for q=3,5,7",
        },
        "finite_comparisons": comparisons,
        "negative_sign_moment_certificate": negative_sign_moment_certificate(
            haar, comparisons, q_scan["families"]
        ),
        "frozen_moment_pattern": frozen_moment_pattern(comparisons, haar),
        "limit_target": {
            "status": COMPARISON_STATUS,
            "not_a_theorem": True,
            "statement": "For each fixed moment order, the finite K/q^2 moment tends to the USp(4) Haar moment as q tends to infinity.",
            "evidence_scope": "three exact fields q=3,5,7 and moment orders 1 through 6",
            "smallest_gap": "invoke a relevant hyperelliptic-family equidistribution theorem for this compact continuous class function, or evaluate the character correlations directly",
        },
        "firewall": (
            "The Weyl constant terms and the three finite histogram moments are separately exact. "
            "Their convergence is conjectural. F is a toy reciprocal-coefficient statistic, not "
            "an analytic Pick/Loewner, XD, or HCNC kernel."
        ),
        "resource_contract": {
            "maximum_moment": FROZEN_MAX_MOMENT,
            "random_sampling": False,
            "numerical_integration": False,
            "external_dependencies": False,
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare against this checked-in JSON fixture")
    parser.add_argument("--write", type=Path, help="write the exact JSON fixture")
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"USp(4) moment fixture mismatch: {args.check}")
        print(f"OK: exact USp(4) moments match {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"OK: wrote exact USp(4) moment fixture {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
