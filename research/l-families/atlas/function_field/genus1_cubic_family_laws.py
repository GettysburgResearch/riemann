"""Exact laws for monic squarefree cubic genus-one models over odd F_q.

The proof-bearing companion note separates three ensembles:

* raw monic squarefree cubics (marked affine equations);
* the full AGL(1,q) branch-polynomial quotient, which identifies twists; and
* the square-affine quotient, whose coarse orbits are elliptic F_q-isomorphism
  classes and whose non-effective lift is the elliptic moduli groupoid.

This producer evaluates closed formulas and performs an exhaustive regression
only for the prime fields q=3,5,7,11,13 (4,023 candidate cubics in total).
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
from typing import Mapping


HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "genus1_cubic_family_laws.json"
NOTE = HERE / "GENUS1_CUBIC_FAMILY_LAWS.md"
TEST = HERE.parents[3] / "tests" / "test_genus1_cubic_family_laws.py"
DEFAULT_Q_VALUES = (3, 5, 7, 11, 13)
MAX_MOMENT_HALF_DEGREE = 6
MAX_ENUMERATED_CANDIDATES = 20_000
MAX_TAU_PRIME = 1_000


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode()).hexdigest()


def _fraction(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def prime_power_data(q: int) -> tuple[int, int]:
    """Return (p,r) for q=p^r, refusing non-prime-powers and even q."""

    if q < 3:
        raise ValueError("q must be an odd prime power")
    for candidate in range(2, math.isqrt(q) + 1):
        if q % candidate:
            continue
        if any(
            candidate % divisor == 0
            for divisor in range(2, math.isqrt(candidate) + 1)
        ):
            continue
        residue = q
        exponent = 0
        while residue % candidate == 0:
            residue //= candidate
            exponent += 1
        if residue != 1:
            raise ValueError("q must be a prime power")
        if candidate == 2:
            raise ValueError("q must be odd")
        return candidate, exponent
    if q % 2 == 0:
        raise ValueError("q must be odd")
    return q, 1


def cusp_dimension_level_one(weight: int) -> int:
    """Dimension of S_weight(SL(2,Z)) for an even integral weight."""

    if weight < 0 or weight % 2:
        raise ValueError("weight must be a nonnegative even integer")
    if weight < 12:
        return 0
    residual_weight = weight - 12
    quotient, residue = divmod(residual_weight, 12)
    return quotient if residue == 2 else quotient + 1


@lru_cache(maxsize=None)
def ramanujan_tau(n: int) -> int:
    """Return tau(n) from Delta=x*prod_(m>=1)(1-x^m)^24.

    The logarithmic-derivative recurrence is exact and dependency-free.  It is
    intentionally capped because the frozen packet needs only tau(3), tau(5),
    tau(7), and tau(11); the mathematical theorem is not restricted by this
    producer cap.
    """

    if not 1 <= n <= MAX_TAU_PRIME:
        raise ValueError(f"tau evaluator requires 1<=n<={MAX_TAU_PRIME}")
    maximum = n - 1
    sigma_one = [0] * (maximum + 1)
    for divisor in range(1, maximum + 1):
        for multiple in range(divisor, maximum + 1, divisor):
            sigma_one[multiple] += divisor
    product_coefficients = [0] * (maximum + 1)
    product_coefficients[0] = 1
    for degree in range(1, maximum + 1):
        numerator = -24 * sum(
            sigma_one[index] * product_coefficients[degree - index]
            for index in range(1, degree + 1)
        )
        if numerator % degree:
            raise ArithmeticError("Delta product recurrence lost integrality")
        product_coefficients[degree] = numerator // degree
    return product_coefficients[maximum]


def delta_frobenius_trace(q: int) -> int:
    """Trace alpha_p^r+beta_p^r for Delta when q=p^r.

    Here alpha_p+beta_p=tau(p) and alpha_p*beta_p=p^11.  For r>1 this
    is deliberately *not* tau(q): it equals
    tau(p^r)-p^11*tau(p^(r-2)).
    """

    characteristic, exponent = prime_power_data(q)
    if characteristic > MAX_TAU_PRIME:
        raise ValueError(
            f"Delta trace evaluator requires characteristic<={MAX_TAU_PRIME}"
        )
    tau_p = ramanujan_tau(characteristic)
    if exponent == 1:
        return tau_p
    previous_previous = 2
    previous = tau_p
    for _ in range(2, exponent + 1):
        previous_previous, previous = (
            previous,
            tau_p * previous - characteristic**11 * previous_previous,
        )
    return previous


def catalan(number: int) -> int:
    if number < 0:
        raise ValueError("Catalan index must be nonnegative")
    return math.comb(2 * number, number) // (number + 1)


def ballot_coefficient(half_degree: int, character_index: int) -> int:
    """Coefficient of q^(n-j) Sym^(2j) in trace^(2n)."""

    if not 0 <= character_index <= half_degree:
        raise ValueError("character index must lie in [0,half_degree]")
    lower = half_degree - character_index
    second = math.comb(2 * half_degree, lower - 1) if lower else 0
    return math.comb(2 * half_degree, lower) - second


def symbolic_even_moment(half_degree: int) -> dict[str, object]:
    """Return the all-q moment decomposition without evaluating Hecke traces."""

    if half_degree < 0:
        raise ValueError("half degree must be nonnegative")
    return {
        "half_degree": half_degree,
        "moment_degree": 2 * half_degree,
        "usp2_catalan": catalan(half_degree),
        "character_terms": [
            {
                "character_index": index,
                "symmetric_power": 2 * index,
                "modular_weight": 2 * index + 2,
                "coefficient": ballot_coefficient(half_degree, index),
                "q_power": half_degree - index,
                "cusp_dimension": cusp_dimension_level_one(2 * index + 2),
            }
            for index in range(1, half_degree + 1)
        ],
    }


def symmetric_character_stack_sum(
    symmetric_power: int,
    q: int,
    *,
    cusp_traces: Mapping[int, int] | None = None,
) -> int:
    """Sum Tr(Sym^m Frob_E)/|Aut_q(E)| over elliptic q-isomorphism classes.

    The proof note records the imported level-one Eichler--Shimura trace
    identity: the answer is q for m=0, zero for odd m, and
    -1-Theta_(m+2)(q) for positive even m.  This evaluator knows the unique
    weight-12 cusp trace and accepts explicit traces for higher weights.
    """

    prime_power_data(q)
    if symmetric_power < 0:
        raise ValueError("symmetric power must be nonnegative")
    if symmetric_power == 0:
        return q
    if symmetric_power % 2:
        return 0
    weight = symmetric_power + 2
    dimension = cusp_dimension_level_one(weight)
    if dimension == 0:
        theta = 0
    elif cusp_traces is not None and weight in cusp_traces:
        theta = int(cusp_traces[weight])
    elif weight == 12:
        theta = delta_frobenius_trace(q)
    else:
        raise ValueError(
            f"an exact Frobenius trace on S_{weight}(SL(2,Z)) is required"
        )
    return -1 - theta


def elliptic_stack_even_trace_moment(
    half_degree: int,
    q: int,
    *,
    cusp_traces: Mapping[int, int] | None = None,
) -> int:
    """Return W_(2n)=sum_[E] a_E^(2n)/|Aut_q(E)|."""

    if not 0 <= half_degree <= MAX_MOMENT_HALF_DEGREE:
        raise ValueError(
            f"numeric evaluator supports half degree in [0,{MAX_MOMENT_HALF_DEGREE}]"
        )
    if half_degree == 0:
        return q
    total = catalan(half_degree) * q ** (half_degree + 1)
    for index in range(1, half_degree + 1):
        total += (
            ballot_coefficient(half_degree, index)
            * q ** (half_degree - index)
            * symmetric_character_stack_sum(
                2 * index, q, cusp_traces=cusp_traces
            )
        )
    return total


def model_trace_moment_sum(moment_degree: int, q: int) -> int:
    """Sum a_D^k over all monic squarefree cubics D over F_q."""

    prime_power_data(q)
    if moment_degree < 0:
        raise ValueError("moment degree must be nonnegative")
    if moment_degree % 2:
        return 0
    half_degree = moment_degree // 2
    return q * (q - 1) * elliptic_stack_even_trace_moment(half_degree, q)


def branch_affine_orbit_count(q: int) -> int:
    """Coarse H_3(q)/AGL(1,q) branch-polynomial orbit count."""

    characteristic, _ = prime_power_data(q)
    return q + 1 + 2 * int((q - 1) % 3 == 0) + int(characteristic == 3)


def elliptic_isomorphism_class_count(q: int) -> int:
    """Number of elliptic F_q-isomorphism classes (square-affine orbits)."""

    characteristic, _ = prime_power_data(q)
    return (
        2 * q
        + 2 * int((q - 1) % 4 == 0)
        + 4 * int((q - 1) % 6 == 0)
        + 2 * int(characteristic == 3)
    )


def _sum_of_two_squares_prime(prime: int) -> tuple[int, int]:
    for second in range(1, math.isqrt(prime) + 1):
        remainder = prime - second * second
        first = math.isqrt(remainder)
        if first * first == remainder:
            return first, second
    raise ArithmeticError(f"p={prime} has no nontrivial two-square representation")


def _sum_of_a_square_and_three_squares_prime(prime: int) -> tuple[int, int]:
    for second in range(1, math.isqrt(prime // 3) + 1):
        remainder = prime - 3 * second * second
        first = math.isqrt(remainder)
        if first * first == remainder:
            return first, second
    raise ArithmeticError(f"p={prime} has no nontrivial A^2+3B^2 representation")


def _quadratic_ring_power(
    first: int, second: int, exponent: int, radicand: int
) -> tuple[int, int]:
    """Power (first+second*sqrt(radicand))^exponent in an integral basis."""

    output_first, output_second = 1, 0
    base_first, base_second = first, second
    residual = exponent
    while residual:
        if residual & 1:
            output_first, output_second = (
                output_first * base_first
                + radicand * output_second * base_second,
                output_first * base_second + output_second * base_first,
            )
        base_first, base_second = (
            base_first * base_first + radicand * base_second * base_second,
            2 * base_first * base_second,
        )
        residual //= 2
    return output_first, output_second


def gaussian_frobenius_coordinates(q: int) -> tuple[int, int]:
    """Return Frobenius-compatible A,B with q=A^2+B^2.

    For a split characteristic, a representation of p is raised to the
    extension degree.  Choosing an arbitrary representation of q would be
    wrong for prime powers (25=5^2+0^2=3^2+4^2 is the first warning).
    """

    characteristic, exponent = prime_power_data(q)
    if q % 4 != 1:
        raise ValueError("Gaussian coordinates require q congruent to 1 mod 4")
    if characteristic % 4 == 1:
        first, second = _sum_of_two_squares_prime(characteristic)
        first, second = _quadratic_ring_power(first, second, exponent, -1)
    else:
        if exponent % 2:
            raise ArithmeticError("inert Gaussian characteristic has odd exponent")
        first, second = characteristic ** (exponent // 2), 0
    if first * first + second * second != q:
        raise ArithmeticError("Gaussian Frobenius coordinates have the wrong norm")
    return first, second


def eisenstein_frobenius_coordinates(q: int) -> tuple[int, int]:
    """Return Frobenius-compatible A,B with q=A^2+3B^2."""

    characteristic, exponent = prime_power_data(q)
    if q % 6 != 1:
        raise ValueError("Eisenstein coordinates require q congruent to 1 mod 6")
    if characteristic % 3 == 1:
        first, second = _sum_of_a_square_and_three_squares_prime(characteristic)
        first, second = _quadratic_ring_power(first, second, exponent, -3)
    else:
        if exponent % 2:
            raise ArithmeticError("inert Eisenstein characteristic has odd exponent")
        first, second = characteristic ** (exponent // 2), 0
    if first * first + 3 * second * second != q:
        raise ArithmeticError("Eisenstein Frobenius coordinates have the wrong norm")
    return first, second


def characteristic_three_translation_correction(
    half_degree: int, q: int
) -> int:
    """Positive even-moment Burnside correction from translations in char 3."""

    characteristic, exponent = prime_power_data(q)
    if half_degree < 1:
        raise ValueError("this positive-moment correction requires half_degree>=1")
    if characteristic != 3:
        return 0
    if exponent % 2:
        return 4 * 3 ** (half_degree - 1) * q**half_degree
    numerator = 2 * (4**half_degree + 2) * q**half_degree
    if numerator % 3:
        raise ArithmeticError("characteristic-three correction is not integral")
    return numerator // 3


def elliptic_coarse_even_trace_moment_sum(half_degree: int, q: int) -> int:
    """Sum a_E^(2n) over uniform coarse elliptic F_q-isomorphism classes."""

    if not 1 <= half_degree <= MAX_MOMENT_HALF_DEGREE:
        raise ValueError(
            f"positive half degree must lie in [1,{MAX_MOMENT_HALF_DEGREE}]"
        )
    characteristic, _ = prime_power_data(q)
    total = 2 * elliptic_stack_even_trace_moment(half_degree, q)

    if (q - 1) % 4 == 0:
        first, second = gaussian_frobenius_coordinates(q)
        total += (2 * first) ** (2 * half_degree)
        total += (2 * second) ** (2 * half_degree)

    if (q - 1) % 6 == 0:
        first, second = eisenstein_frobenius_coordinates(q)
        cm_sum = (
            (2 * first) ** (2 * half_degree)
            + (first + 3 * second) ** (2 * half_degree)
            + (first - 3 * second) ** (2 * half_degree)
        )
        if 4 * cm_sum % 3:
            raise ArithmeticError("j=0 coarse correction is not integral")
        total += 4 * cm_sum // 3

    if characteristic == 3:
        total += characteristic_three_translation_correction(half_degree, q)
    return total


def branch_coarse_even_trace_moment_sum(half_degree: int, q: int) -> int:
    """Sum the descended even trace moment over full affine branch orbits."""

    elliptic_sum = elliptic_coarse_even_trace_moment_sum(half_degree, q)
    if elliptic_sum % 2:
        raise ArithmeticError("elliptic coarse even moment did not halve")
    return elliptic_sum // 2


def quotient_measure_laws(q: int) -> dict[str, object]:
    characteristic, exponent = prime_power_data(q)
    branch_count = branch_affine_orbit_count(q)
    elliptic_count = elliptic_isomorphism_class_count(q)
    branch_excess = branch_count - q
    elliptic_excess = elliptic_count - 2 * q
    return {
        "q": q,
        "characteristic": characteristic,
        "extension_degree": exponent,
        "model_count": q**2 * (q - 1),
        "full_affine_group_order": q * (q - 1),
        "square_affine_effective_group_order": q * (q - 1) // 2,
        "branch_affine_stack_cardinality": q,
        "branch_affine_coarse_orbit_count": branch_count,
        "branch_affine_coarse_excess": branch_excess,
        "branch_coarse_vs_stack_total_variation_upper_bound": _fraction(
            Fraction(branch_excess, q)
        ),
        "effective_elliptic_stack_cardinality": 2 * q,
        "actual_elliptic_stack_cardinality": q,
        "elliptic_isomorphism_class_count": elliptic_count,
        "elliptic_coarse_excess_over_effective_stack": elliptic_excess,
        "elliptic_coarse_vs_model_stack_total_variation_upper_bound": _fraction(
            Fraction(elliptic_excess, 2 * q)
        ),
        "exception_indicators": {
            "order_2_in_full_affine": True,
            "order_3_in_full_affine": (q - 1) % 3 == 0,
            "translation_in_characteristic_3": characteristic == 3,
            "order_2_in_square_affine": (q - 1) % 4 == 0,
            "order_3_in_square_affine": (q - 1) % 6 == 0,
        },
    }


def _quadratic_character_prime(value: int, q: int) -> int:
    residue = value % q
    if residue == 0:
        return 0
    return 1 if pow(residue, (q - 1) // 2, q) == 1 else -1


def _cubic_discriminant_prime(a: int, b: int, c: int, q: int) -> int:
    return (
        a * a * b * b
        - 4 * b**3
        - 4 * a**3 * c
        - 27 * c * c
        + 18 * a * b * c
    ) % q


def _prime_model_census(q: int) -> dict[tuple[int, ...], int]:
    characteristic, exponent = prime_power_data(q)
    if characteristic != q or exponent != 1:
        raise ValueError("the exhaustive regression enumerates prime fields only")
    models: dict[tuple[int, ...], int] = {}
    for a, b, c in itertools.product(range(q), repeat=3):
        if _cubic_discriminant_prime(a, b, c, q) == 0:
            continue
        trace = -sum(
            _quadratic_character_prime(x**3 + a * x * x + b * x + c, q)
            for x in range(q)
        )
        models[(c, b, a, 1)] = trace
    if len(models) != q**2 * (q - 1):
        raise ArithmeticError("squarefree cubic count is not q^2(q-1)")
    return models


def _affine_transform_prime(
    polynomial: tuple[int, ...], alpha: int, beta: int, q: int
) -> tuple[int, ...]:
    output = [0] * 4
    leading_scale = pow(pow(alpha, 3, q), -1, q)
    for exponent, coefficient in enumerate(polynomial):
        for power in range(exponent + 1):
            output[power] += (
                leading_scale
                * coefficient
                * math.comb(exponent, power)
                * pow(alpha, power, q)
                * pow(beta, exponent - power, q)
            )
    return tuple(value % q for value in output)


def _prime_orbit_census(
    q: int,
    models: Mapping[tuple[int, ...], int],
    *,
    square_multipliers_only: bool,
) -> dict[str, object]:
    multipliers = (
        sorted({pow(unit, 2, q) for unit in range(1, q)})
        if square_multipliers_only
        else list(range(1, q))
    )
    group_order = q * len(multipliers)
    unseen = set(models)
    trace_histogram: Counter[int] = Counter()
    stabilizer_histogram: Counter[int] = Counter()
    even_moment_sums = {degree: 0 for degree in range(2, 13, 2)}
    transform_evaluations = 0
    while unseen:
        representative = min(unseen)
        orbit = {
            _affine_transform_prime(representative, alpha, beta, q)
            for alpha in multipliers
            for beta in range(q)
        }
        transform_evaluations += group_order
        if not orbit <= models.keys():
            raise ArithmeticError("affine action left the squarefree family")
        traces = {models[polynomial] for polynomial in orbit}
        stabilizer = group_order // len(orbit)
        if stabilizer * len(orbit) != group_order:
            raise ArithmeticError("orbit-stabilizer failed")
        stabilizer_histogram[stabilizer] += 1
        if square_multipliers_only:
            if len(traces) != 1:
                raise ArithmeticError("trace failed to descend to square-affine orbit")
            trace = next(iter(traces))
            trace_histogram[trace] += 1
            for degree in even_moment_sums:
                even_moment_sums[degree] += trace**degree
        else:
            absolute_traces = {abs(trace) for trace in traces}
            if len(absolute_traces) != 1:
                raise ArithmeticError("absolute trace failed to descend to affine orbit")
            absolute_trace = next(iter(absolute_traces))
            trace_histogram[absolute_trace] += 1
            for degree in even_moment_sums:
                even_moment_sums[degree] += absolute_trace**degree
        unseen -= orbit
    return {
        "orbit_count": sum(stabilizer_histogram.values()),
        "trace_histogram": {
            str(key): trace_histogram[key] for key in sorted(trace_histogram)
        },
        "stabilizer_order_histogram": {
            str(key): stabilizer_histogram[key]
            for key in sorted(stabilizer_histogram)
        },
        "even_moment_sums": {
            str(key): value for key, value in even_moment_sums.items()
        },
        "affine_transform_evaluations": transform_evaluations,
    }


def _regression_row(q: int) -> dict[str, object]:
    models = _prime_model_census(q)
    trace_histogram = Counter(models.values())
    model_moments = {
        degree: sum(count * trace**degree for trace, count in trace_histogram.items())
        for degree in range(13)
    }
    for degree, value in model_moments.items():
        expected = model_trace_moment_sum(degree, q)
        if value != expected:
            raise ArithmeticError(f"q={q}, degree={degree} model moment mismatch")

    elliptic = _prime_orbit_census(
        q, models, square_multipliers_only=True
    )
    branch = _prime_orbit_census(
        q, models, square_multipliers_only=False
    )
    if elliptic["orbit_count"] != elliptic_isomorphism_class_count(q):
        raise ArithmeticError("elliptic coarse orbit count mismatch")
    if branch["orbit_count"] != branch_affine_orbit_count(q):
        raise ArithmeticError("branch-affine coarse orbit count mismatch")
    for degree in range(2, 13, 2):
        half_degree = degree // 2
        if elliptic["even_moment_sums"][str(degree)] != (
            elliptic_coarse_even_trace_moment_sum(half_degree, q)
        ):
            raise ArithmeticError("elliptic coarse moment formula mismatch")
        if branch["even_moment_sums"][str(degree)] != (
            branch_coarse_even_trace_moment_sum(half_degree, q)
        ):
            raise ArithmeticError("branch coarse moment formula mismatch")

    stack_rows = []
    for half_degree in range(MAX_MOMENT_HALF_DEGREE + 1):
        degree = 2 * half_degree
        stack_sum = elliptic_stack_even_trace_moment(half_degree, q)
        stack_rows.append(
            {
                "degree": degree,
                "elliptic_stack_weighted_sum": stack_sum,
                "uniform_model_average": _fraction(Fraction(stack_sum, q)),
                "normalized_usp2_scale_average": _fraction(
                    Fraction(stack_sum, q ** (half_degree + 1))
                ),
                "uniform_elliptic_coarse_sum": (
                    elliptic["orbit_count"]
                    if degree == 0
                    else elliptic_coarse_even_trace_moment_sum(half_degree, q)
                ),
                "uniform_branch_coarse_sum": (
                    branch["orbit_count"]
                    if degree == 0
                    else branch_coarse_even_trace_moment_sum(half_degree, q)
                ),
            }
        )

    return {
        "q": q,
        "candidate_cubics_inspected": q**3,
        "squarefree_model_count": len(models),
        "model_trace_histogram": {
            str(key): trace_histogram[key] for key in sorted(trace_histogram)
        },
        "model_moment_sums_degrees_0_through_12": {
            str(key): value for key, value in model_moments.items()
        },
        "stack_and_coarse_even_moments": stack_rows,
        "elliptic_square_affine_orbits": elliptic,
        "full_affine_branch_orbits": branch,
    }


def build_fixture(q_values: tuple[int, ...] = DEFAULT_Q_VALUES) -> dict[str, object]:
    if not q_values:
        raise ValueError("at least one regression field is required")
    if len(set(q_values)) != len(q_values):
        raise ValueError("regression fields must be distinct")
    candidate_count = sum(q**3 for q in q_values)
    if candidate_count > MAX_ENUMERATED_CANDIDATES:
        raise ValueError(
            f"candidate count {candidate_count} exceeds cap {MAX_ENUMERATED_CANDIDATES}"
        )
    regressions = [_regression_row(q) for q in q_values]
    transform_count = sum(
        row["elliptic_square_affine_orbits"]["affine_transform_evaluations"]
        + row["full_affine_branch_orbits"]["affine_transform_evaluations"]
        for row in regressions
    )

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus1_cubic_family_laws.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS1.MONIC_CUBIC.ALL_Q_LAWS.V1",
        "status": "EXACT_ALL_ODD_Q_THEOREMS_WITH_TINY_PRIME_FIELD_REGRESSION",
        "rigor_level": "PROVED_REDUCTIONS_PLUS_STATED_EICHLER_SHIMURA_INPUT",
        "normalization": {
            "family": "H_3(q)={monic squarefree cubic D over F_q}",
            "curve": "E_D:y^2=D(x), with the rational point at infinity",
            "trace": "a_D=q+1-#E_D(F_q)=-sum_x quadratic_character(D(x))",
            "l_polynomial": "L_D(T)=1-a_D*T+q*T^2",
            "model_count": "q^2*(q-1)",
        },
        "all_q_moment_theorem": {
            "scope": "every odd prime power q and every integer n>=0",
            "odd_trace_and_character_moments": 0,
            "symmetric_character_stack_sum": {
                "m=0": "q",
                "odd_m": "0",
                "positive_even_m": "-1-Theta_(m+2)(q)",
                "Theta_definition": (
                    "for q=p^r, Tr(T_(p^r)|S_k)-p^(k-1)*"
                    "Tr(T_(p^(r-2))|S_k), with the second term zero for r<2"
                ),
            },
            "raw_even_moment": (
                "W_(2n)=C_n*q^(n+1)-sum_(j=1)^n "
                "c_(n,j)*q^(n-j)*(1+Theta_(2j+2)(q)), "
                "c_(n,j)=binom(2n,n-j)-binom(2n,n-j-1)"
            ),
            "model_sum": "sum_D a_D^(2n)=q*(q-1)*W_(2n)",
            "model_average": "E_model[a_D^(2n)]=W_(2n)/q",
            "normalized_character_mean": (
                "E_model[U_(2j)(a_D/(2*sqrt(q)))]="
                "-(1+Theta_(2j+2)(q))/q^(j+1)"
            ),
            "usp2_comparison": (
                "USp(2) Haar has even normalized trace moments C_n and all "
                "nontrivial irreducible-character means zero"
            ),
            "symbolic_rows_through_degree_12": [
                symbolic_even_moment(index)
                for index in range(MAX_MOMENT_HALF_DEGREE + 1)
            ],
            "explicit_stack_sums": {
                "W_0": "q",
                "W_2": "q^2-1",
                "W_4": "2*q^3-3*q-1",
                "W_6": "5*q^4-9*q^2-5*q-1",
                "W_8": "14*q^5-28*q^3-20*q^2-7*q-1",
                "W_10": (
                    "42*q^6-90*q^4-75*q^3-35*q^2-9*q-1-Theta_12(q)"
                ),
                "W_12": (
                    "132*q^7-297*q^5-275*q^4-154*q^3-54*q^2-11*q-1"
                    "-11*q*Theta_12(q)"
                ),
            },
        },
        "quotient_laws": {
            "full_affine_branch_action": "D(T)->alpha^(-3)D(alpha*T+beta)",
            "trace_action": "a_(g.D)=quadratic_character(alpha)*a_D",
            "branch_stack_cardinality": "q",
            "branch_coarse_orbits": (
                "q+1+2*1_(3 divides q-1)+1_(characteristic 3)"
            ),
            "square_affine_action": (
                "D(T)->u^(-6)D(u^2*T+beta); effective multipliers are squares"
            ),
            "actual_elliptic_stack_cardinality": (
                "sum_[E]1/|Aut_q(E)|=q; the ineffective kernel is {+1,-1}"
            ),
            "elliptic_coarse_isomorphism_classes": (
                "2*q+2*1_(4 divides q-1)+4*1_(6 divides q-1)"
                "+2*1_(characteristic 3)"
            ),
            "coarse_even_moment_sum": (
                "2*W_(2n) plus the stated j=1728, j=0, and characteristic-3 "
                "Burnside corrections; see proof note and producer function"
            ),
            "positive_even_branch_vs_elliptic_coarse_sum": "branch=elliptic/2",
            "rows": [quotient_measure_laws(q) for q in q_values],
        },
        "prime_power_convention_regression": {
            "Theta_12(9)": delta_frobenius_trace(9),
            "tau(9)_is_not_used": -113643,
            "W_10(9)": elliptic_stack_even_trace_moment(5, 9),
            "W_12(9)": elliptic_stack_even_trace_moment(6, 9),
        },
        "finite_regressions": regressions,
        "producer": {
            "script": Path(__file__).name,
            "source_sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
            "note": NOTE.name,
            "note_sha256_lf_normalized": _lf_sha256(NOTE),
            "test": str(TEST.relative_to(HERE.parents[3])).replace("\\", "/"),
            "test_sha256_lf_normalized": _lf_sha256(TEST),
        },
        "resource_contract": {
            "arithmetic": "exact integers and fractions",
            "enumerated_fields": list(q_values),
            "candidate_cubics_inspected": candidate_count,
            "candidate_cubic_cap": MAX_ENUMERATED_CANDIDATES,
            "affine_transform_evaluations": transform_count,
            "interpolation_or_curve_database": "not used",
        },
        "scope_firewall": {
            "full_affine_branch_orbits_are_not_elliptic_isomorphism_classes": True,
            "signed_trace_does_not_descend_to_full_affine_branch_orbits": True,
            "square_affine_coarse_orbits_are_elliptic_isomorphism_classes": True,
            "uniform_models_equal_normalized_elliptic_stack_measure": True,
            "uniform_coarse_classes_are_a_different_measure": True,
            "finite_regression_is_not_the_proof_of_the_all_q_formulas": True,
            "no_number_field_transfer_or_rh_grh_conclusion": True,
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"genus-one cubic fixture mismatch: {args.check}")
        print(f"OK: exact genus-one cubic laws match {args.check}")
    elif args.write:
        args.write.write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")
        print(f"WROTE: {args.write}")
    else:
        print(json.dumps(fixture, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
