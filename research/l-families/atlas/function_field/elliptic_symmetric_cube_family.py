"""Exact packet for the symmetric-cube family of genus-one local factors.

No curves are enumerated here.  The only finite data are deterministic
transforms of the source-locked trace histograms in
``genus1_cubic_family_laws.json``.  The local-factor algebra, coefficient
curve, compact moment comparisons, and finite-family laws use exact integer
or rational arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DEFAULT_OUTPUT = HERE / "elliptic_symmetric_cube_family.json"
SOURCE_FIXTURE = HERE / "genus1_cubic_family_laws.json"
NOTE = HERE / "ELLIPTIC_SYMMETRIC_CUBE_FAMILY.md"
TEST = ROOT / "tests" / "test_elliptic_symmetric_cube_family.py"

DEFAULT_Q_VALUES = (3, 5, 7, 11, 13)
EXPECTED_SOURCE_SCHEMA = "riemann.function_field.genus1_cubic_family_laws.v1"
EXPECTED_SOURCE_PAYLOAD_SHA256 = (
    "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df"
)
EXPECTED_SOURCE_FILE_SHA256_LF = (
    "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227"
)

MAX_SOURCE_HISTOGRAM_ATOMS = 100
MAX_LAURENT_PRODUCT_PAIRS = 2_000_000
MAX_TRACE_MOMENT_DEGREE = 12
MAX_SECOND_COEFFICIENT_MOMENT_DEGREE = 6
MAX_MIXED_TRACE_DEGREE = 4
MAX_MIXED_SECOND_COEFFICIENT_DEGREE = 4


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode()).hexdigest()


def _fraction(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _load_source_fixture() -> dict[str, object]:
    if _lf_sha256(SOURCE_FIXTURE) != EXPECTED_SOURCE_FILE_SHA256_LF:
        raise RuntimeError("source genus-one fixture file hash changed")
    source = json.loads(SOURCE_FIXTURE.read_text(encoding="utf-8"))
    if source.get("schema") != EXPECTED_SOURCE_SCHEMA:
        raise RuntimeError("source genus-one fixture schema changed")
    if source.get("payload_sha256") != EXPECTED_SOURCE_PAYLOAD_SHA256:
        raise RuntimeError("source genus-one payload lock changed")
    unhashed = dict(source)
    payload_hash = unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != payload_hash:
        raise RuntimeError("source genus-one payload is not internally authentic")
    normalization = source.get("normalization", {})
    if normalization.get("l_polynomial") != "L_D(T)=1-a_D*T+q*T^2":
        raise RuntimeError("source genus-one L-polynomial convention changed")
    if not str(normalization.get("trace", "")).startswith("a_D=q+1-#E_D"):
        raise RuntimeError("source genus-one trace convention changed")
    return source


def base_power_sums(A: int, q: int, maximum: int) -> list[int]:
    """Power sums alpha^n+beta^n for alpha+beta=-A, alpha*beta=q."""

    if q <= 0 or maximum < 0:
        raise ValueError("q must be positive and maximum nonnegative")
    output = [2]
    if maximum == 0:
        return output
    output.append(-A)
    for _ in range(2, maximum + 1):
        output.append((-A) * output[-1] - q * output[-2])
    return output


def sym3_coefficients_via_newton(A: int, q: int) -> tuple[int, ...]:
    """Return det(1-Sym^3(Frob)T) from power sums and Newton identities."""

    base = base_power_sums(A, q, 12)
    sym3_power_sums = [0] + [base[3 * k] + q**k * base[k] for k in range(1, 5)]
    elementary = [1]
    for degree in range(1, 5):
        numerator = sum(
            (-1) ** (index - 1)
            * elementary[degree - index]
            * sym3_power_sums[index]
            for index in range(1, degree + 1)
        )
        if numerator % degree:
            raise ArithmeticError("Newton identity lost integrality")
        elementary.append(numerator // degree)
    return tuple((-1) ** degree * elementary[degree] for degree in range(5))


def sym3_coefficients_closed(A: int, q: int) -> tuple[int, ...]:
    """Closed coefficients for roots alpha^3,q*alpha,q*beta,beta^3."""

    first = A**3 - 2 * q * A
    second = q * (A**4 - 3 * q * A * A + 2 * q * q)
    return (1, first, second, q**3 * first, q**6)


def coefficient_curve_value(x: Fraction, y: Fraction) -> Fraction:
    """Implicit equation of the normalized Sym^3 coefficient image."""

    return -(x**4) + x * x * y + x * x + y**3 - 2 * y * y


def scaled_coefficient_curve_value(sym3_trace: int, reduced_e2: int, q: int) -> int:
    """Clear denominators in F(S/q^(3/2),D/q^2).

    Here S is the Sym^3 trace and the raw T^2 coefficient is q*D.
    """

    S = sym3_trace
    D = reduced_e2
    return -S**4 + q * S * S * D + q**3 * S * S + D**3 - 2 * q * q * D * D


def sym3_trace_difference_factor(t1: int, t2: int, q: int) -> int:
    """Factored difference S(t1)-S(t2), S(t)=t^3-2qt."""

    return (t1 - t2) * (t1 * t1 + t1 * t2 + t2 * t2 - 2 * q)


IntPolynomial = dict[int, int]


def polynomial_multiply(first: Mapping[int, int], second: Mapping[int, int]) -> IntPolynomial:
    output: Counter[int] = Counter()
    for left_degree, left_coefficient in first.items():
        for right_degree, right_coefficient in second.items():
            output[left_degree + right_degree] += left_coefficient * right_coefficient
    return {degree: coefficient for degree, coefficient in output.items() if coefficient}


def polynomial_power(base: Mapping[int, int], exponent: int) -> IntPolynomial:
    if exponent < 0:
        raise ValueError("polynomial exponent must be nonnegative")
    output: IntPolynomial = {0: 1}
    residual = exponent
    factor = dict(base)
    while residual:
        if residual & 1:
            output = polynomial_multiply(output, factor)
        residual //= 2
        if residual:
            factor = polynomial_multiply(factor, factor)
    return output


def polynomial_add(first: Mapping[int, int], second: Mapping[int, int]) -> IntPolynomial:
    output = Counter(first)
    output.update(second)
    return {degree: coefficient for degree, coefficient in output.items() if coefficient}


def su2_character(index: int) -> IntPolynomial:
    """U_index(t/2), with t the standard SU(2) trace."""

    if index < 0:
        raise ValueError("character index must be nonnegative")
    if index == 0:
        return {0: 1}
    previous: IntPolynomial = {0: 1}
    current: IntPolynomial = {1: 1}
    for _ in range(2, index + 1):
        shifted = {degree + 1: coefficient for degree, coefficient in current.items()}
        following = polynomial_add(
            shifted, {degree: -coefficient for degree, coefficient in previous.items()}
        )
        previous, current = current, following
    return current


def decompose_into_su2_characters(polynomial: Mapping[int, int]) -> dict[int, int]:
    """Triangular exact decomposition in U_n(t/2)."""

    residual = dict(polynomial)
    output: dict[int, int] = {}
    while residual:
        degree = max(residual)
        coefficient = residual[degree]
        output[degree] = coefficient
        subtraction = {
            character_degree: -coefficient * character_coefficient
            for character_degree, character_coefficient in su2_character(degree).items()
        }
        residual = polynomial_add(residual, subtraction)
    return {index: output[index] for index in sorted(output)}


BASE_TRACE_POLYNOMIAL: IntPolynomial = {1: 1}
SYM3_TRACE_POLYNOMIAL: IntPolynomial = {3: 1, 1: -2}
SYM3_E2_POLYNOMIAL: IntPolynomial = {4: 1, 2: -3, 0: 2}


def observable_polynomial(trace_power: int, e2_power: int) -> IntPolynomial:
    return polynomial_multiply(
        polynomial_power(SYM3_TRACE_POLYNOMIAL, trace_power),
        polynomial_power(SYM3_E2_POLYNOMIAL, e2_power),
    )


def normalized_base_even_moments(q: int, theta12: int) -> dict[int, Fraction]:
    """Source-locked model/stack moments E[(a_E/sqrt(q))^k], k<=12."""

    if q <= 0:
        raise ValueError("q must be positive")
    Q = Fraction(q)
    return {
        0: Fraction(1),
        2: 1 - Q**-2,
        4: 2 - 3 * Q**-2 - Q**-3,
        6: 5 - 9 * Q**-2 - 5 * Q**-3 - Q**-4,
        8: 14 - 28 * Q**-2 - 20 * Q**-3 - 7 * Q**-4 - Q**-5,
        10: (
            42
            - 90 * Q**-2
            - 75 * Q**-3
            - 35 * Q**-4
            - 9 * Q**-5
            - (1 + theta12) * Q**-6
        ),
        12: (
            132
            - 297 * Q**-2
            - 275 * Q**-3
            - 154 * Q**-4
            - 54 * Q**-5
            - 11 * (1 + theta12) * Q**-6
            - Q**-7
        ),
    }


def observable_expectation_via_base_moments(
    polynomial: Mapping[int, int], q: int, theta12: int
) -> Fraction:
    moments = normalized_base_even_moments(q, theta12)
    total = Fraction(0)
    for degree, coefficient in polynomial.items():
        if degree % 2:
            continue
        if degree not in moments:
            raise ValueError("observable requires a source moment above degree 12")
        total += coefficient * moments[degree]
    return total


def normalized_character_mean(index: int, q: int, theta12: int) -> Fraction:
    """Mean of U_index(a_E/(2sqrt(q))) in the source model measure."""

    if index == 0:
        return Fraction(1)
    if index < 0:
        raise ValueError("character index must be nonnegative")
    if index % 2:
        return Fraction(0)
    if index > 12:
        raise ValueError("this packet only imports characters through index 12")
    theta = theta12 if index == 10 else 0
    return -Fraction(1 + theta, q ** (index // 2 + 1))


def observable_expectation_via_characters(
    polynomial: Mapping[int, int], q: int, theta12: int
) -> Fraction:
    decomposition = decompose_into_su2_characters(polynomial)
    return sum(
        (
            coefficient * normalized_character_mean(index, q, theta12)
            for index, coefficient in decomposition.items()
        ),
        Fraction(0),
    )


ALL_Q_OBSERVABLES = {
    "trace_x": (1, 0),
    "second_coefficient_y": (0, 1),
    "trace_square_x2": (2, 0),
    "second_coefficient_square_y2": (0, 2),
    "trace_square_times_second_x2y": (2, 1),
    "trace_fourth_x4": (4, 0),
    "second_coefficient_cube_y3": (0, 3),
}


ALL_Q_FORMULAS = {
    "trace_x": "0",
    "second_coefficient_y": "1-q^-3",
    "trace_square_x2": "1-q^-2-q^-3-q^-4",
    "second_coefficient_square_y2": "2-q^-2-3q^-3-q^-4-q^-5",
    "trace_square_times_second_x2y": (
        "2-4q^-2-5q^-3-4q^-4-2q^-5-q^-6-Theta_12(q)q^-6"
    ),
    "trace_fourth_x4": (
        "4-9q^-2-11q^-3-10q^-4-6q^-5-3q^-6-q^-7"
        "-3Theta_12(q)q^-6"
    ),
    "second_coefficient_cube_y3": (
        "5-6q^-2-11q^-3-7q^-4-6q^-5-2q^-6-q^-7"
        "-2Theta_12(q)q^-6"
    ),
}


LaurentExponent = tuple[int, ...]
LaurentPolynomial = dict[LaurentExponent, int]


@dataclass
class LaurentAudit:
    product_pairs: int = 0
    peak_terms: int = 0

    def multiply(
        self, first: Mapping[LaurentExponent, int], second: Mapping[LaurentExponent, int]
    ) -> LaurentPolynomial:
        if not first or not second:
            return {}
        dimensions = len(next(iter(first)))
        if any(len(exponent) != dimensions for exponent in second):
            raise ValueError("Laurent dimensions disagree")
        self.product_pairs += len(first) * len(second)
        if self.product_pairs > MAX_LAURENT_PRODUCT_PAIRS:
            raise RuntimeError("Laurent product-pair cap exceeded")
        output: Counter[LaurentExponent] = Counter()
        for left, left_coefficient in first.items():
            for right, right_coefficient in second.items():
                output[tuple(a + b for a, b in zip(left, right))] += (
                    left_coefficient * right_coefficient
                )
        result = {
            exponent: coefficient for exponent, coefficient in output.items() if coefficient
        }
        self.peak_terms = max(self.peak_terms, len(result))
        return result


def _laurent_factor(exponent: LaurentExponent) -> LaurentPolynomial:
    return {(0,) * len(exponent): 1, exponent: -1}


def _weyl_density(
    positive_roots: Iterable[LaurentExponent], audit: LaurentAudit
) -> LaurentPolynomial:
    roots = tuple(positive_roots)
    if not roots:
        raise ValueError("at least one positive root is required")
    density: LaurentPolynomial = {(0,) * len(roots[0]): 1}
    for root in roots:
        density = audit.multiply(density, _laurent_factor(root))
        density = audit.multiply(
            density, _laurent_factor(tuple(-coordinate for coordinate in root))
        )
    return density


def _haar_integral(
    polynomial: Mapping[LaurentExponent, int],
    density: Mapping[LaurentExponent, int],
    weyl_order: int,
    audit: LaurentAudit,
) -> int:
    numerator = audit.multiply(polynomial, density).get(
        (0,) * len(next(iter(polynomial))), 0
    )
    if numerator % weyl_order:
        raise ArithmeticError("Weyl constant term did not divide by |W|")
    return numerator // weyl_order


def _successive_powers(
    base: Mapping[LaurentExponent, int], maximum: int, audit: LaurentAudit
) -> list[LaurentPolynomial]:
    identity = {(0,) * len(next(iter(base))): 1}
    output = [identity]
    for _ in range(maximum):
        output.append(audit.multiply(output[-1], base))
    return output


def compact_moment_comparison() -> tuple[dict[str, object], dict[str, int]]:
    audit = LaurentAudit()

    su2_density = _weyl_density(((2,),), audit)
    sym3_trace: LaurentPolynomial = {
        (3,): 1,
        (1,): 1,
        (-1,): 1,
        (-3,): 1,
    }
    sym3_e2: LaurentPolynomial = {
        (4,): 1,
        (2,): 1,
        (0,): 2,
        (-2,): 1,
        (-4,): 1,
    }
    su2_trace_powers = _successive_powers(
        sym3_trace, MAX_TRACE_MOMENT_DEGREE, audit
    )
    su2_e2_powers = _successive_powers(
        sym3_e2, MAX_SECOND_COEFFICIENT_MOMENT_DEGREE, audit
    )
    thin_trace_moments = [
        _haar_integral(polynomial, su2_density, 2, audit)
        for polynomial in su2_trace_powers
    ]
    thin_e2_moments = [
        _haar_integral(polynomial, su2_density, 2, audit)
        for polynomial in su2_e2_powers
    ]

    usp4_density = _weyl_density(((2, 0), (0, 2), (1, -1), (1, 1)), audit)
    generic_trace: LaurentPolynomial = {
        (1, 0): 1,
        (-1, 0): 1,
        (0, 1): 1,
        (0, -1): 1,
    }
    generic_e2: LaurentPolynomial = {
        (0, 0): 2,
        (1, 1): 1,
        (1, -1): 1,
        (-1, 1): 1,
        (-1, -1): 1,
    }
    generic_trace_powers = _successive_powers(
        generic_trace, MAX_TRACE_MOMENT_DEGREE, audit
    )
    generic_e2_powers = _successive_powers(
        generic_e2, MAX_SECOND_COEFFICIENT_MOMENT_DEGREE, audit
    )
    generic_trace_moments = [
        _haar_integral(polynomial, usp4_density, 8, audit)
        for polynomial in generic_trace_powers
    ]
    generic_e2_moments = [
        _haar_integral(polynomial, usp4_density, 8, audit)
        for polynomial in generic_e2_powers
    ]

    mixed_rows: list[dict[str, object]] = []
    for trace_degree in (0, 2, 4):
        thin_row = []
        generic_row = []
        for e2_degree in range(MAX_MIXED_SECOND_COEFFICIENT_DEGREE + 1):
            thin_product = audit.multiply(
                su2_trace_powers[trace_degree],
                _successive_powers(sym3_e2, MAX_MIXED_SECOND_COEFFICIENT_DEGREE, audit)[
                    e2_degree
                ],
            )
            generic_product = audit.multiply(
                generic_trace_powers[trace_degree],
                _successive_powers(
                    generic_e2, MAX_MIXED_SECOND_COEFFICIENT_DEGREE, audit
                )[e2_degree],
            )
            thin_row.append(_haar_integral(thin_product, su2_density, 2, audit))
            generic_row.append(
                _haar_integral(generic_product, usp4_density, 8, audit)
            )
        mixed_rows.append(
            {
                "trace_power": trace_degree,
                "second_coefficient_powers_0_through_4": list(range(5)),
                "sym3_su2": thin_row,
                "generic_usp4": generic_row,
            }
        )

    # Independent triangular character audit of every thin trace and e2 moment.
    character_trace_moments = [
        decompose_into_su2_characters(
            polynomial_power(SYM3_TRACE_POLYNOMIAL, degree)
        ).get(0, 0)
        for degree in range(MAX_TRACE_MOMENT_DEGREE + 1)
    ]
    character_e2_moments = [
        decompose_into_su2_characters(
            polynomial_power(SYM3_E2_POLYNOMIAL, degree)
        ).get(0, 0)
        for degree in range(MAX_SECOND_COEFFICIENT_MOMENT_DEGREE + 1)
    ]
    if character_trace_moments != thin_trace_moments:
        raise ArithmeticError("SU(2) trace character and Weyl routes disagree")
    if character_e2_moments != thin_e2_moments:
        raise ArithmeticError("SU(2) e2 character and Weyl routes disagree")

    comparison = {
        "compact_images": {
            "thin": "Sym^3(SU(2)) inside USp(4), rank one, faithful image",
            "generic": "USp(4), rank two",
            "thin_torus_eigenvalues": "z^3,z,z^-1,z^-3",
            "generic_torus_eigenvalues": "z1,z1^-1,z2,z2^-1",
        },
        "methods": {
            "thin_route_1": "SU(2) Weyl constant term, positive root 2e",
            "thin_route_2": "triangular decomposition in U_n(t/2)",
            "generic": (
                "USp(4) Weyl constant term, positive C2 roots "
                "2e1,2e2,e1-e2,e1+e2"
            ),
        },
        "trace_moments_degrees_0_through_12": {
            "sym3_su2": thin_trace_moments,
            "generic_usp4": generic_trace_moments,
        },
        "second_coefficient_moments_degrees_0_through_6": {
            "sym3_su2": thin_e2_moments,
            "generic_usp4": generic_e2_moments,
        },
        "mixed_moments": mixed_rows,
        "first_separations": {
            "trace_fourth": {"sym3_su2": 4, "generic_usp4": 3},
            "second_coefficient_third": {"sym3_su2": 5, "generic_usp4": 4},
            "trace_square_second_square": {"sym3_su2": 7, "generic_usp4": 5},
        },
    }
    return comparison, {
        "laurent_product_pairs": audit.product_pairs,
        "peak_laurent_terms": audit.peak_terms,
        "laurent_product_pair_cap": MAX_LAURENT_PRODUCT_PAIRS,
    }


def _theta12_from_source_row(row: Mapping[str, object]) -> int:
    q = int(row["q"])
    stack_rows = {
        int(item["degree"]): int(item["elliptic_stack_weighted_sum"])
        for item in row["stack_and_coarse_even_moments"]  # type: ignore[index]
    }
    W10 = stack_rows[10]
    theta12 = (
        42 * q**6
        - 90 * q**4
        - 75 * q**3
        - 35 * q**2
        - 9 * q
        - 1
        - W10
    )
    expected_W12 = (
        132 * q**7
        - 297 * q**5
        - 275 * q**4
        - 154 * q**3
        - 54 * q**2
        - 11 * q
        - 1
        - 11 * q * theta12
    )
    if stack_rows[12] != expected_W12:
        raise ArithmeticError("source W10/W12 rows give inconsistent Theta_12")
    return theta12


def _histogram_observable_expectation(
    atoms: Iterable[tuple[int, int]], q: int, trace_power: int, e2_power: int
) -> Fraction:
    if trace_power % 2:
        raise ValueError("exact rational normalization requires an even trace power")
    numerator = Fraction(0)
    member_count = 0
    for trace, count in atoms:
        sym3_trace = trace**3 - 2 * q * trace
        reduced_e2 = trace**4 - 3 * q * trace * trace + 2 * q * q
        numerator += count * Fraction(
            sym3_trace**trace_power * reduced_e2**e2_power,
            q ** (3 * trace_power // 2 + 2 * e2_power),
        )
        member_count += count
    return numerator / member_count


def _frozen_transform(row: Mapping[str, object]) -> dict[str, object]:
    q = int(row["q"])
    source_histogram = {
        int(trace): int(count)
        for trace, count in row["model_trace_histogram"].items()  # type: ignore[index]
    }
    member_count = sum(source_histogram.values())
    if member_count != q * q * (q - 1):
        raise ArithmeticError("source model histogram has wrong cardinality")
    trace_histogram: Counter[int] = Counter()
    factor_histogram: Counter[tuple[int, int]] = Counter()
    atom_rows = []
    for trace in sorted(source_histogram):
        count = source_histogram[trace]
        A = -trace
        closed = sym3_coefficients_closed(A, q)
        newton = sym3_coefficients_via_newton(A, q)
        if closed != newton:
            raise ArithmeticError("closed and Newton Sym^3 coefficients disagree")
        sym3_trace = -closed[1]
        if closed[2] % q:
            raise ArithmeticError("Sym^3 second coefficient is not divisible by q")
        reduced_e2 = closed[2] // q
        if scaled_coefficient_curve_value(sym3_trace, reduced_e2, q):
            raise ArithmeticError("source atom missed the coefficient curve")
        trace_histogram[sym3_trace] += count
        factor_histogram[(closed[1], closed[2])] += count
        atom_rows.append(
            {
                "source_geometric_trace_t": trace,
                "converted_polynomial_coefficient_A": A,
                "member_count": count,
                "sym3_trace_S": sym3_trace,
                "polynomial_coefficients_T0_through_T4": list(closed),
                "reduced_second_coefficient_D": reduced_e2,
                "normalized_trace_square_x2": _fraction(
                    Fraction(sym3_trace * sym3_trace, q**3)
                ),
                "normalized_second_coefficient_y": _fraction(
                    Fraction(reduced_e2, q**2)
                ),
            }
        )

    theta12 = _theta12_from_source_row(row)
    source_atoms = tuple(sorted(source_histogram.items()))
    exact_observables: dict[str, object] = {}
    for name, (trace_power, e2_power) in ALL_Q_OBSERVABLES.items():
        polynomial = observable_polynomial(trace_power, e2_power)
        base_route = observable_expectation_via_base_moments(
            polynomial, q, theta12
        )
        character_route = observable_expectation_via_characters(
            polynomial, q, theta12
        )
        if base_route != character_route:
            raise ArithmeticError("base-moment and character routes disagree")
        if trace_power % 2:
            histogram_route = Fraction(0)
            if any(
                source_histogram[trace] != source_histogram.get(-trace, 0)
                for trace in source_histogram
            ):
                raise ArithmeticError("source trace histogram lost twist symmetry")
        else:
            histogram_route = _histogram_observable_expectation(
                source_atoms, q, trace_power, e2_power
            )
        if histogram_route != base_route:
            raise ArithmeticError(f"q={q} frozen observable {name} mismatch")
        exact_observables[name] = {
            "formula": ALL_Q_FORMULAS[name],
            "value": _fraction(base_route),
            "routes_agree": ["source_histogram", "base_moments", "SU2_characters"],
        }

    return {
        "q": q,
        "source_histogram_atom_count": len(source_histogram),
        "source_members_represented": member_count,
        "theta12_frobenius_trace": theta12,
        "transformed_atoms": atom_rows,
        "sym3_trace_histogram": {
            str(trace): trace_histogram[trace] for trace in sorted(trace_histogram)
        },
        "local_factor_T1_T2_histogram": [
            {"T1": key[0], "T2": key[1], "member_count": factor_histogram[key]}
            for key in sorted(factor_histogram)
        ],
        "source_to_full_factor_map_is_injective_on_frozen_support": (
            len(factor_histogram) == len(source_histogram)
        ),
        "source_to_sym3_trace_map_is_injective_on_frozen_support": (
            len(trace_histogram) == len(source_histogram)
        ),
        "exact_model_stack_observable_averages": exact_observables,
    }


def build_fixture(q_values: tuple[int, ...] = DEFAULT_Q_VALUES) -> dict[str, object]:
    if not q_values:
        raise ValueError("at least one source field is required")
    if len(q_values) != len(set(q_values)):
        raise ValueError("source fields must be distinct")
    source = _load_source_fixture()
    source_rows = {
        int(row["q"]): row for row in source["finite_regressions"]  # type: ignore[index]
    }
    if any(q not in source_rows for q in q_values):
        raise ValueError("requested field is absent from the source-locked fixture")

    frozen = [_frozen_transform(source_rows[q]) for q in q_values]
    source_atom_count = sum(row["source_histogram_atom_count"] for row in frozen)
    if source_atom_count > MAX_SOURCE_HISTOGRAM_ATOMS:
        raise RuntimeError("source histogram atom cap exceeded")
    compact, compact_resources = compact_moment_comparison()

    character_decompositions = {}
    for name, (trace_power, e2_power) in ALL_Q_OBSERVABLES.items():
        character_decompositions[name] = {
            f"chi_{index}": coefficient
            for index, coefficient in decompose_into_su2_characters(
                observable_polynomial(trace_power, e2_power)
            ).items()
        }

    payload: dict[str, object] = {
        "schema": "riemann.function_field.elliptic_symmetric_cube_family.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS1.SYMMETRIC_CUBE.V1",
        "status": "EXACT_REPRESENTATION_PACKET_WITH_SOURCE_LOCKED_FINITE_LAWS",
        "rigor_level": "PROVED_ALGEBRA_PLUS_STATED_SOURCE_EICHLER_SHIMURA_INPUT",
        "source_lock": {
            "fixture": SOURCE_FIXTURE.name,
            "schema": EXPECTED_SOURCE_SCHEMA,
            "payload_sha256": EXPECTED_SOURCE_PAYLOAD_SHA256,
            "file_sha256_lf_normalized": EXPECTED_SOURCE_FILE_SHA256_LF,
            "fields_consumed": list(q_values),
            "measure_consumed": "uniform monic squarefree cubic models = normalized elliptic stack measure",
            "trace_bridge": "source t=a_D; requested P_E=1+A*T+q*T^2 uses A=-t",
        },
        "normalization": {
            "base_factor": "P_E(T)=1+A*T+q*T^2=(1-alpha*T)(1-beta*T)",
            "base_relations": "alpha+beta=-A=t, alpha*beta=q",
            "symmetric_cube_roots": ["alpha^3", "q*alpha", "q*beta", "beta^3"],
            "symmetric_cube_factor": (
                "1+(A^3-2qA)T+q(A^4-3qA^2+2q^2)T^2"
                "+q^3(A^3-2qA)T^3+q^6T^4"
            ),
            "normalized_base_trace": "t0=t/sqrt(q)=-A/sqrt(q)",
            "normalized_sym3_trace_x": "x=t0^3-2t0",
            "normalized_second_coefficient_y": "y=t0^4-3t0^2+2",
            "normalized_factor": "1-xZ+yZ^2-xZ^3+Z^4, Z=q^(3/2)T",
        },
        "literature_boundary": {
            "classical_primary_references": [
                {
                    "authors": "Henry H. Kim and Freydoon Shahidi",
                    "title": "Symmetric cube L-functions for GL_2 are entire",
                    "url": "https://arxiv.org/abs/math/9909198",
                    "scope": (
                        "holomorphy of third symmetric-power L-functions for "
                        "nonmonomial GL_2 cusp forms over arbitrary number fields"
                    ),
                },
                {
                    "authors": (
                        "Henry H. Kim and Freydoon Shahidi, with appendix by "
                        "Colin J. Bushnell and Guy Henniart"
                    ),
                    "title": (
                        "Functorial products for GL_2 x GL_3 and the symmetric "
                        "cube for GL_2"
                    ),
                    "url": "https://arxiv.org/abs/math/0409607",
                    "scope": "the functorial symmetric-cube map for GL_2 cusp forms",
                },
            ],
            "classical_not_claimed": (
                "the Sym3 representation, local root transform, reciprocal factor, "
                "and global automorphic lift are not project novelty claims"
            ),
            "project_specific_calculations": [
                "exact pushforward of the locked genus-one model/stack family",
                "eliminated nodal coefficient curve and its normalization geometry",
                "odd-q integral-trace injectivity across the real folds",
                "finite-q coefficient and mixed-moment defects through base degree 12",
            ],
            "priority_caveat": (
                "project-specific means computed for this atlas, not proved absent "
                "from the literature; a dedicated priority search remains required"
            ),
        },
        "independent_local_factor_derivations": {
            "closed_elementary_symmetric": (
                "directly expand roots alpha^3,qalpha,qbeta,beta^3"
            ),
            "power_sum_newton": (
                "p_n=(-A)p_(n-1)-q p_(n-2); "
                "P_k(Sym3)=p_(3k)+q^k p_k; Newton through degree 4"
            ),
            "source_atom_comparisons": source_atom_count,
            "all_comparisons_agree": True,
        },
        "rank_one_coefficient_curve": {
            "parameterization": "(x,y)=(t0^3-2t0,t0^4-3t0^2+2), -2<=t0<=2",
            "implicit_equation": "F=-x^4+x^2*y+x^2+y^3-2*y^2=0",
            "generic_birational_inverse": "t0=x(y-1)/(x^2-y)",
            "compact_real_endpoints": [[-4, 6], [4, 6]],
            "singular_locus": [[-1, 1], [0, 0], [1, 1]],
            "normalization_preimages": {
                "(-1,1)": "t0^2+t0-1=0",
                "(0,0)": "t0^2-2=0",
                "(1,1)": "t0^2-t0-1=0",
            },
            "tangent_cones_in_local_X_Y": {
                "(-1,1)": "-4X^2-2XY+Y^2",
                "(0,0)": "X^2-2Y^2",
                "(1,1)": "-4X^2+2XY+Y^2",
            },
            "singularity_type": "three real ordinary nodes; no cusps",
            "no_cusp_certificate": (
                "dx/dt0=3t0^2-2 and dy/dt0=2t0(2t0^2-3) have no common zero"
            ),
            "x_projection_branch_values": "x=+-4sqrt(6)/9 (x^2=32/27)",
            "y_projection_branch_values": ["-1/4", "2"],
            "generic_usp4_counterexample": "(x,y)=(0,-2) gives F=-16",
            "interpretation": (
                "the equation detects the compact rank-one Sym3(SU2) coefficient "
                "image; generic USp4 Haar is not supported on it, but the equation "
                "alone does not certify arithmetic Sym3 origin over F_q"
            ),
            "odd_q_arithmetic_false_positive": {
                "coefficient_point": [0, 0],
                "curve_check": "F(0,0)=0",
                "normalization_preimages": "t0=+-sqrt(2)",
                "arithmetic_obstruction": (
                    "an elliptic source over F_q would need an integer trace t with "
                    "t^2=2q; for odd q, v_2(2q)=1, so 2q is not a square"
                ),
                "conclusion": (
                    "membership in the compact coefficient curve is not sufficient "
                    "even for local arithmetic symmetric-cube recognition"
                ),
            },
        },
        "odd_q_arithmetic_lattice_avoidance": {
            "theorem": (
                "for every odd integer q, t -> t^3-2qt is injective on integer t; "
                "hence the Sym3 trace alone recovers the base Frobenius trace"
            ),
            "collision_factorization": (
                "S(t1)-S(t2)=(t1-t2)(t1^2+t1*t2+t2^2-2q)"
            ),
            "mod_4_certificate": {
                "values_of_r2_rs_s2_mod_4": [0, 1, 3],
                "two_q_for_odd_q_mod_4": 2,
                "conclusion": "the second factor cannot vanish for distinct integers",
            },
            "hasse_bound_needed": False,
            "oddness_is_load_bearing": (
                "at q=2, t=0 and t=2 both have Sym3 trace 0"
            ),
            "geometric_meaning": (
                "the real coefficient parameterization folds and has nodes, but the "
                "odd-q restriction places no two integral traces in the same trace "
                "fiber; one arithmetic branch may still share a value with a "
                "nonarithmetic real branch"
            ),
        },
        "compact_haar_comparison": compact,
        "all_odd_q_model_stack_laws_through_base_degree_12": {
            "scope": "every odd prime power q, using the locked genus-one stack theorem",
            "theta_convention": "Theta_12(q) is the level-one weight-12 Frobenius trace",
            "odd_in_x": "every observable odd in x has mean zero by quadratic-twist symmetry",
            "character_bridge": (
                "E[chi_0]=1; for j>=1, "
                "E[chi_(2j)]=-(1+Theta_(2j+2)(q))/q^(j+1); "
                "only chi_10 sees a cusp term through character index 12"
            ),
            "character_decompositions": character_decompositions,
            "formulas": ALL_Q_FORMULAS,
        },
        "frozen_histogram_transforms": frozen,
        "resource_contract": {
            "arithmetic": "exact integers, fractions, and Laurent coefficients",
            "new_curve_or_field_enumerations": 0,
            "source_histogram_atoms_transformed": source_atom_count,
            "source_histogram_atom_cap": MAX_SOURCE_HISTOGRAM_ATOMS,
            "source_members_represented": sum(
                row["source_members_represented"] for row in frozen
            ),
            "coefficient_derivation_comparisons": source_atom_count,
            "trace_moment_degree_cap": MAX_TRACE_MOMENT_DEGREE,
            "second_coefficient_moment_degree_cap": (
                MAX_SECOND_COEFFICIENT_MOMENT_DEGREE
            ),
            **compact_resources,
            "floats_or_randomness": "not used",
            "external_curve_or_L_function_database": "not used",
        },
        "scope_firewall": {
            "representation_image_not_generic_usp4": True,
            "coefficient_curve_is_a_representation_identity_not_a_family_equidistribution_theorem": True,
            "local_factor_algebra_does_not_assert_a_new_variety_realizing_each_factor": True,
            "actual_elliptic_h1_symmetric_cube_is_a_genuine_l_adic_representation": True,
            "coefficient_curve_alone_does_not_prove_global_recognition_or_descent": True,
            "coefficient_curve_alone_does_not_certify_local_arithmetic_sym3_origin": True,
            "classical_global_automorphy_is_not_needed_or_reproved_here": True,
            "frozen_histograms_are_transforms_not_new_enumerations": True,
            "source_stack_measure_is_not_uniform_coarse_isomorphism_classes": True,
            "candidate_novelty_requires_literature_priority_search": True,
            "no_zero_free_region_or_rh_grh_conclusion": True,
        },
        "producer": {
            "script": Path(__file__).name,
            "source_sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
            "note": NOTE.name,
            "note_sha256_lf_normalized": _lf_sha256(NOTE),
            "test": str(TEST.relative_to(ROOT)).replace("\\", "/"),
            "test_sha256_lf_normalized": _lf_sha256(TEST),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", nargs="?", const=DEFAULT_OUTPUT, type=Path)
    parser.add_argument("--write", nargs="?", const=DEFAULT_OUTPUT, type=Path)
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"elliptic symmetric-cube fixture mismatch: {args.check}")
        print(f"OK: elliptic symmetric-cube fixture matches {args.check}")
    elif args.write:
        args.write.write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")
        print(f"WROTE: {args.write}")
    else:
        print(json.dumps(fixture, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
