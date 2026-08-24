"""Exact coefficient recovery for elliptic ``Sym^5`` local factors.

The producer proves, over Q and for q != 0, how much of the degree-six
``Sym^5`` local factor is needed after its scalar trace is known.  It uses an
elementary Sylvester determinant and replays the 61 already-locked collision
rows; it performs no curve, field, or trace-range enumeration.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_sym5_coefficient_recovery.json"
NOTE_PATH = HERE / "ELLIPTIC_SYM5_COEFFICIENT_RECOVERY.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_sym5_coefficient_recovery.py"
SOURCE_PATH = HERE / "elliptic_sym5_collision_diophantine_pilot.json"

SCHEMA = "riemann.function_field.elliptic_sym5_coefficient_recovery.v1"
EXPECTED_SOURCE_SCHEMA = (
    "riemann.function_field.elliptic_sym5_collision_diophantine_pilot.v1"
)
EXPECTED_SOURCE_PAYLOAD_SHA256 = (
    "13bf7f95949b0905843c6f453008359fe8b05b65157fdb8c2eaf48e7af542ca5"
)
EXPECTED_SOURCE_FILE_SHA256_LF = (
    "66635391ee4d69382eaf6d11fd78a77c90cffc8919ccbede9d0f568915cdf167"
)
EXPECTED_SOURCE_COLLISION_ROWS = 61
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 25_000

Rational = int | Fraction
Monomial = tuple[int, int]
BinaryPolynomial = dict[Monomial, int]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _as_fraction(name: str, value: Rational) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be an integer or Fraction")
    return Fraction(value)


class ResourceGuard:
    """Exclusive-cap ledger for the small exact operations in this packet."""

    def __init__(self, cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE) -> None:
        _require_integer("cap", cap)
        if cap <= 0:
            raise ValueError("cap must be positive")
        self.cap = cap
        self.ledger: Counter[str] = Counter()

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: str, units: int = 1) -> None:
        _require_integer("units", units)
        if units < 0:
            raise ValueError("resource charge must be nonnegative")
        if self.total + units >= self.cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.cap}"
            )
        self.ledger[name] += units


def e_trace(order: int, t: Rational, q: Rational) -> Fraction:
    """Trace of Sym^order on roots alpha,beta with alpha+beta=t, alpha*beta=q."""

    _require_integer("order", order)
    if order < 0:
        raise ValueError("order must be nonnegative")
    t_fraction = _as_fraction("t", t)
    q_fraction = _as_fraction("q", q)
    if order == 0:
        return Fraction(1)
    previous_previous, previous = Fraction(1), t_fraction
    for _ in range(2, order + 1):
        previous_previous, previous = (
            previous,
            t_fraction * previous - q_fraction * previous_previous,
        )
    return previous


def e5_trace(t: Rational, q: Rational) -> Fraction:
    t_fraction = _as_fraction("t", t)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    return t_fraction * (t_fraction * t_fraction - q_fraction) * (
        t_fraction * t_fraction - 3 * q_fraction
    )


def sym5_second_coefficient(t: Rational, q: Rational) -> Fraction:
    t_fraction = _as_fraction("t", t)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    square = t_fraction * t_fraction
    return (
        q_fraction
        * (q_fraction - square)
        * (3 * q_fraction - square)
        * (q_fraction * q_fraction - 3 * q_fraction * square + square * square)
    )


def sym5_third_coefficient(t: Rational, q: Rational) -> Fraction:
    t_fraction = _as_fraction("t", t)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    square = t_fraction * t_fraction
    return (
        -(q_fraction**3)
        * t_fraction
        * (2 * q_fraction - square)
        * (3 * q_fraction - square)
        * (q_fraction * q_fraction - 3 * q_fraction * square + square * square)
    )


def sym5_local_factor(t: Rational, q: Rational) -> tuple[Fraction, ...]:
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    scalar = e5_trace(t, q_fraction)
    c1 = -scalar
    c2 = sym5_second_coefficient(t, q_fraction)
    c3 = sym5_third_coefficient(t, q_fraction)
    return (
        Fraction(1),
        c1,
        c2,
        c3,
        q_fraction**5 * c2,
        q_fraction**10 * c1,
        q_fraction**15,
    )


def collision_quotient(x: Rational, y: Rational, q: Rational) -> Fraction:
    x_fraction = _as_fraction("x", x)
    y_fraction = _as_fraction("y", y)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    h_value = x_fraction**2 + x_fraction * y_fraction + y_fraction**2
    k_value = (
        x_fraction**4
        + x_fraction**3 * y_fraction
        + x_fraction**2 * y_fraction**2
        + x_fraction * y_fraction**3
        + y_fraction**4
    )
    return k_value - 4 * q_fraction * h_value + 3 * q_fraction**2


def second_coefficient_quotient(
    x: Rational, y: Rational, q: Rational
) -> Fraction:
    """R where c2(x)-c2(y)=q*(x^2-y^2)*R."""

    x_fraction = _as_fraction("x", x)
    y_fraction = _as_fraction("y", y)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    square_sum = x_fraction**2 + y_fraction**2
    fourth_sum = x_fraction**4 + x_fraction**2 * y_fraction**2 + y_fraction**4
    sixth_sum = (
        x_fraction**6
        + x_fraction**4 * y_fraction**2
        + x_fraction**2 * y_fraction**4
        + y_fraction**6
    )
    return (
        -13 * q_fraction**3
        + 16 * q_fraction**2 * square_sum
        - 7 * q_fraction * fourth_sum
        + sixth_sum
    )


def recovery_flags(x: Rational, y: Rational, q: Rational) -> dict[str, bool]:
    """Actual and theorem-predicted equality flags for a rational pair."""

    x_fraction = _as_fraction("x", x)
    y_fraction = _as_fraction("y", y)
    q_fraction = _as_fraction("q", q)
    if q_fraction == 0:
        raise ValueError("q must be nonzero")
    scalar_equal = e5_trace(x_fraction, q_fraction) == e5_trace(
        y_fraction, q_fraction
    )
    c2_equal = sym5_second_coefficient(
        x_fraction, q_fraction
    ) == sym5_second_coefficient(y_fraction, q_fraction)
    c3_equal = sym5_third_coefficient(
        x_fraction, q_fraction
    ) == sym5_third_coefficient(y_fraction, q_fraction)
    pair_equal = scalar_equal and c2_equal
    triple_equal = pair_equal and c3_equal
    full_equal = sym5_local_factor(x_fraction, q_fraction) == sym5_local_factor(
        y_fraction, q_fraction
    )
    predicted_pair_equal = x_fraction == y_fraction or (
        x_fraction == -y_fraction
        and x_fraction * x_fraction in (q_fraction, 3 * q_fraction)
    )
    predicted_full_equal = x_fraction == y_fraction or (
        x_fraction == -y_fraction
        and x_fraction * x_fraction == 3 * q_fraction
    )
    return {
        "scalar_equal": scalar_equal,
        "c2_equal": c2_equal,
        "c3_equal": c3_equal,
        "pair_equal": pair_equal,
        "triple_equal": triple_equal,
        "full_equal": full_equal,
        "predicted_pair_equal": predicted_pair_equal,
        "predicted_triple_equal": predicted_full_equal,
        "predicted_full_equal": predicted_full_equal,
    }


def _poly_clean(value: Mapping[Monomial, int]) -> BinaryPolynomial:
    return {monomial: coefficient for monomial, coefficient in value.items() if coefficient}


def _poly_add(
    left: Mapping[Monomial, int], right: Mapping[Monomial, int]
) -> BinaryPolynomial:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
    return _poly_clean(result)


def _poly_scale(value: Mapping[Monomial, int], scalar: int) -> BinaryPolynomial:
    _require_integer("scalar", scalar)
    return _poly_clean(
        {monomial: scalar * coefficient for monomial, coefficient in value.items()}
    )


def _poly_mul(
    left: Mapping[Monomial, int], right: Mapping[Monomial, int]
) -> BinaryPolynomial:
    result: BinaryPolynomial = {}
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            monomial = (left_x + right_x, left_y + right_y)
            result[monomial] = (
                result.get(monomial, 0) + left_coefficient * right_coefficient
            )
    return _poly_clean(result)


def _poly_power(value: Mapping[Monomial, int], exponent: int) -> BinaryPolynomial:
    _require_integer("exponent", exponent)
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    result: BinaryPolynomial = {(0, 0): 1}
    base = dict(value)
    remaining = exponent
    while remaining:
        if remaining % 2:
            result = _poly_mul(result, base)
        remaining //= 2
        if remaining:
            base = _poly_mul(base, base)
    return result


def _poly_sum(*values: Mapping[Monomial, int]) -> BinaryPolynomial:
    result: BinaryPolynomial = {}
    for value in values:
        result = _poly_add(result, value)
    return result


def _permutation_sign(permutation: Sequence[int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def _sylvester_resultant(guard: ResourceGuard | None = None) -> BinaryPolynomial:
    """Compute Res_q(Q,R) as a literal 5-by-5 Sylvester determinant."""

    one: BinaryPolynomial = {(0, 0): 1}
    x_poly: BinaryPolynomial = {(1, 0): 1}
    y_poly: BinaryPolynomial = {(0, 1): 1}
    x2, y2 = _poly_power(x_poly, 2), _poly_power(y_poly, 2)
    xy = _poly_mul(x_poly, y_poly)
    h_poly = _poly_sum(x2, xy, y2)
    k_poly = _poly_sum(
        _poly_power(x_poly, 4),
        _poly_mul(_poly_power(x_poly, 3), y_poly),
        _poly_mul(x2, y2),
        _poly_mul(x_poly, _poly_power(y_poly, 3)),
        _poly_power(y_poly, 4),
    )
    s_poly = _poly_add(x2, y2)
    u_poly = _poly_sum(
        _poly_power(x_poly, 4), _poly_mul(x2, y2), _poly_power(y_poly, 4)
    )
    v_poly = _poly_sum(
        _poly_power(x_poly, 6),
        _poly_mul(_poly_power(x_poly, 4), y2),
        _poly_mul(x2, _poly_power(y_poly, 4)),
        _poly_power(y_poly, 6),
    )
    q_coefficients = [_poly_scale(one, 3), _poly_scale(h_poly, -4), k_poly]
    r_coefficients = [
        _poly_scale(one, -13),
        _poly_scale(s_poly, 16),
        _poly_scale(u_poly, -7),
        v_poly,
    ]
    zero: BinaryPolynomial = {}
    matrix: list[list[BinaryPolynomial]] = []
    for shift in range(3):
        row = [zero for _ in range(5)]
        for index, coefficient in enumerate(q_coefficients):
            row[shift + index] = coefficient
        matrix.append(row)
    for shift in range(2):
        row = [zero for _ in range(5)]
        for index, coefficient in enumerate(r_coefficients):
            row[shift + index] = coefficient
        matrix.append(row)

    determinant: BinaryPolynomial = {}
    for permutation in itertools.permutations(range(5)):
        if guard is not None:
            guard.charge("sylvester_determinant_permutations")
        term: BinaryPolynomial = {(0, 0): 1}
        for row_index, column_index in enumerate(permutation):
            term = _poly_mul(term, matrix[row_index][column_index])
            if not term:
                break
        if term:
            determinant = _poly_add(
                determinant, _poly_scale(term, _permutation_sign(permutation))
            )
    return determinant


def _resultant_factor_product(guard: ResourceGuard | None = None) -> BinaryPolynomial:
    x_poly: BinaryPolynomial = {(1, 0): 1}
    y_poly: BinaryPolynomial = {(0, 1): 1}
    x2, y2 = _poly_power(x_poly, 2), _poly_power(y_poly, 2)
    xy = _poly_mul(x_poly, y_poly)
    factors = [
        _poly_add(x2, _poly_scale(y2, -3)),
        _poly_add(_poly_scale(x2, 3), _poly_scale(y2, -1)),
        _poly_sum(x2, _poly_scale(xy, 3), y2),
        _poly_sum(
            _poly_power(x_poly, 3),
            _poly_scale(_poly_mul(x2, y_poly), -3),
            _poly_scale(_poly_mul(x_poly, y2), -4),
            _poly_scale(_poly_power(y_poly, 3), -1),
        ),
        _poly_sum(
            _poly_power(x_poly, 3),
            _poly_scale(_poly_mul(x2, y_poly), 4),
            _poly_scale(_poly_mul(x_poly, y2), 3),
            _poly_scale(_poly_power(y_poly, 3), -1),
        ),
    ]
    product: BinaryPolynomial = {(0, 0): 1}
    for factor in factors:
        if guard is not None:
            guard.charge("resultant_factors_multiplied")
        product = _poly_mul(product, factor)
    return product


def _binary_coefficients(
    polynomial: Mapping[Monomial, int], total_degree: int
) -> list[int]:
    return [
        int(polynomial.get((total_degree - y_power, y_power), 0))
        for y_power in range(total_degree + 1)
    ]


def _resultant_certificate(guard: ResourceGuard) -> dict[str, object]:
    determinant = _sylvester_resultant(guard)
    factor_product = _resultant_factor_product(guard)
    if determinant != factor_product:
        raise ArithmeticError("Sylvester determinant lost its exact factorization")

    # The Euclidean reduction gives 9R=(-39q+48S-52H)Q+a*q+b.
    a_coefficients = [-40, -185, -264, -185, -40]
    b_coefficients = [13, 56, 69, 60, 69, 56, 13]
    x_poly: BinaryPolynomial = {(1, 0): 1}
    y_poly: BinaryPolynomial = {(0, 1): 1}
    h_poly = _poly_sum(
        _poly_power(x_poly, 2),
        _poly_mul(x_poly, y_poly),
        _poly_power(y_poly, 2),
    )
    k_poly = _poly_sum(
        _poly_power(x_poly, 4),
        _poly_mul(_poly_power(x_poly, 3), y_poly),
        _poly_mul(_poly_power(x_poly, 2), _poly_power(y_poly, 2)),
        _poly_mul(x_poly, _poly_power(y_poly, 3)),
        _poly_power(y_poly, 4),
    )
    a_poly = {
        (4 - index, index): coefficient
        for index, coefficient in enumerate(a_coefficients)
    }
    b_poly = {
        (6 - index, index): coefficient
        for index, coefficient in enumerate(b_coefficients)
    }
    norm_numerator = _poly_sum(
        _poly_mul(k_poly, _poly_power(a_poly, 2)),
        _poly_scale(_poly_mul(h_poly, _poly_mul(a_poly, b_poly)), 4),
        _poly_scale(_poly_power(b_poly, 2), 3),
    )
    if norm_numerator != _poly_scale(determinant, 9):
        raise ArithmeticError("Euclidean norm certificate disagrees with resultant")
    guard.charge("euclidean_norm_identity_checked")

    return {
        "sylvester_matrix_size": 5,
        "exact_resultant_coefficient_vector_x12_to_y12": _binary_coefficients(
            determinant, 12
        ),
        "factorization": [
            "x^2-3*y^2",
            "3*x^2-y^2",
            "x^2+3*x*y+y^2",
            "x^3-3*x^2*y-4*x*y^2-y^3",
            "x^3+4*x^2*y+3*x*y^2-y^3",
        ],
        "factor_multiplicities": [1, 1, 1, 1, 1],
        "dropped_scalar_or_variable_factors": [],
        "euclidean_reduction": {
            "identity": "9R=(-39q+48S-52H)Q+a*q+b",
            "S": "x^2+y^2",
            "a_coefficients_x4_to_y4": a_coefficients,
            "b_coefficients_x6_to_y6": b_coefficients,
            "norm_identity": "9*Res_q(Q,R)=K*a^2+4*H*a*b+3*b^2",
        },
        "rational_projective_obstructions": [
            {
                "factor": "x^2-3*y^2",
                "affine_obstruction": "r^2=3; 3 is not a rational square",
            },
            {
                "factor": "3*x^2-y^2",
                "affine_obstruction": "(1/r)^2=3; 3 is not a rational square",
            },
            {
                "factor": "x^2+3*x*y+y^2",
                "affine_obstruction": "r^2+3r+1 has nonsquare discriminant 5",
            },
            {
                "factor": "x^3-3*x^2*y-4*x*y^2-y^3",
                "affine_obstruction": (
                    "monic rational-root candidates +/-1 give -7 and -1"
                ),
            },
            {
                "factor": "x^3+4*x^2*y+3*x*y^2-y^3",
                "affine_obstruction": (
                    "monic rational-root candidates +/-1 give 7 and -1"
                ),
            },
        ],
        "projective_point_at_y_zero": "every factor forces x=0",
        "conclusion": "the resultant has no nonzero rational projective zero",
    }


def _weight_multisets(guard: ResourceGuard) -> dict[str, object]:
    wedge2 = Counter()
    for left in range(6):
        for right in range(left + 1, 6):
            wedge2[(10 - left - right, left + right)] += 1
            guard.charge("wedge2_weight_pairs")
    wedge2_decomposition = Counter(
        [(9 - index, index + 1) for index in range(9)]
        + [(7 - index, index + 3) for index in range(5)]
        + [(5, 5)]
    )
    if wedge2 != wedge2_decomposition:
        raise ArithmeticError("Lambda^2 Sym^5 weight decomposition failed")

    wedge3 = Counter()
    for indices in itertools.combinations(range(6), 3):
        beta_power = sum(indices)
        wedge3[(15 - beta_power, beta_power)] += 1
        guard.charge("wedge3_weight_triples")
    wedge3_decomposition = Counter(
        [(12 - index, index + 3) for index in range(10)]
        + [(10 - index, index + 5) for index in range(6)]
        + [(9 - index, index + 6) for index in range(4)]
    )
    if wedge3 != wedge3_decomposition:
        raise ArithmeticError("Lambda^3 Sym^5 weight decomposition failed")

    def records(counter: Counter[tuple[int, int]]) -> list[dict[str, int]]:
        return [
            {
                "alpha_power": alpha_power,
                "beta_power": beta_power,
                "multiplicity": multiplicity,
            }
            for (alpha_power, beta_power), multiplicity in sorted(counter.items())
        ]

    return {
        "lambda2_sym5": {
            "dimension": 15,
            "decomposition": (
                "(Sym^8 V tensor det V) + (Sym^4 V tensor (det V)^3) + "
                "(det V)^5"
            ),
            "trace_identity": "c2=q*E8+q^3*E4+q^5",
            "weight_multiset": records(wedge2),
            "expanded_terms": [
                {"coefficient": 1, "t_power": 8, "q_power": 1},
                {"coefficient": -7, "t_power": 6, "q_power": 2},
                {"coefficient": 16, "t_power": 4, "q_power": 3},
                {"coefficient": -13, "t_power": 2, "q_power": 4},
                {"coefficient": 3, "t_power": 0, "q_power": 5},
            ],
        },
        "lambda3_sym5": {
            "dimension": 20,
            "decomposition": (
                "(Sym^9 V tensor (det V)^3) + "
                "(Sym^5 V tensor (det V)^5) + "
                "(Sym^3 V tensor (det V)^6)"
            ),
            "trace_identity": "-c3=q^3*E9+q^5*E5+q^6*E3",
            "weight_multiset": records(wedge3),
            "expanded_negative_c3_terms": [
                {"coefficient": 1, "t_power": 9, "q_power": 3},
                {"coefficient": -8, "t_power": 7, "q_power": 4},
                {"coefficient": 22, "t_power": 5, "q_power": 5},
                {"coefficient": -23, "t_power": 3, "q_power": 6},
                {"coefficient": 6, "t_power": 1, "q_power": 7},
            ],
        },
    }


def _load_source() -> dict[str, object]:
    if _lf_sha256(SOURCE_PATH) != EXPECTED_SOURCE_FILE_SHA256_LF:
        raise RuntimeError("Sym^5 collision source file lock mismatch")
    source = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    if source.get("schema") != EXPECTED_SOURCE_SCHEMA:
        raise RuntimeError("Sym^5 collision source schema lock mismatch")
    if source.get("payload_sha256") != EXPECTED_SOURCE_PAYLOAD_SHA256:
        raise RuntimeError("Sym^5 collision source payload lock mismatch")
    unhashed = dict(source)
    payload_hash = unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != payload_hash:
        raise RuntimeError("Sym^5 collision source payload is internally inconsistent")
    return source


def _integer(value: Fraction) -> int:
    if value.denominator != 1:
        raise ArithmeticError("locked integer collision produced a denominator")
    return value.numerator


def _replay_source_collisions(
    source: Mapping[str, object], guard: ResourceGuard
) -> dict[str, object]:
    finite_census = source.get("finite_census")
    if not isinstance(finite_census, dict):
        raise RuntimeError("locked source lost finite_census")
    source_rows = finite_census.get("rows")
    if not isinstance(source_rows, list):
        raise RuntimeError("locked source lost collision rows")

    separation_counts: Counter[str] = Counter()
    class_by_separation: Counter[tuple[str, str]] = Counter()
    c1_c2_survivors: list[dict[str, int | str]] = []
    full_factor_aliases: list[dict[str, int]] = []
    replay_projection: list[dict[str, object]] = []
    for q_row in source_rows:
        if not isinstance(q_row, dict) or not isinstance(q_row.get("pairs"), list):
            raise RuntimeError("malformed locked collision row")
        q = int(q_row["q"])
        for pair in q_row["pairs"]:
            if not isinstance(pair, dict):
                raise RuntimeError("malformed locked collision pair")
            guard.charge("locked_collision_rows_replayed")
            x, y = int(pair["x"]), int(pair["y"])
            if x >= y:
                raise ArithmeticError("locked collision pair is not ordered")
            scalar_x, scalar_y = e5_trace(x, q), e5_trace(y, q)
            if scalar_x != scalar_y or _integer(scalar_x) != int(pair["scalar_trace"]):
                raise ArithmeticError("locked scalar collision failed replay")
            flags = recovery_flags(x, y, q)
            if flags["pair_equal"] != flags["predicted_pair_equal"]:
                raise ArithmeticError("pair recovery theorem failed on locked row")
            if flags["triple_equal"] != flags["predicted_triple_equal"]:
                raise ArithmeticError("triple recovery theorem failed on locked row")
            if flags["full_equal"] != flags["predicted_full_equal"]:
                raise ArithmeticError("full recovery theorem failed on locked row")

            if not flags["c2_equal"]:
                separation = "T2"
                stored_degree: int | None = 2
            elif not flags["c3_equal"]:
                separation = "T3"
                stored_degree = 3
                c1_c2_survivors.append(
                    {"q": q, "x": x, "y": y, "outcome": separation}
                )
            elif flags["full_equal"]:
                separation = "full_factor_alias"
                stored_degree = None
                c1_c2_survivors.append(
                    {"q": q, "x": x, "y": y, "outcome": separation}
                )
                full_factor_aliases.append({"q": q, "x": x, "y": y})
            else:
                raise ArithmeticError("self-reciprocity recovery became inconsistent")
            if pair.get("first_separating_coefficient_degree") != stored_degree:
                raise ArithmeticError("locked separating degree failed replay")
            if bool(pair.get("full_local_factors_equal")) != flags["full_equal"]:
                raise ArithmeticError("locked full-factor flag failed replay")
            collision_class = str(pair["collision_class"])
            separation_counts[separation] += 1
            class_by_separation[(collision_class, separation)] += 1
            replay_projection.append(
                {
                    "q": q,
                    "x": x,
                    "y": y,
                    "class": collision_class,
                    "outcome": separation,
                }
            )

    if len(replay_projection) != EXPECTED_SOURCE_COLLISION_ROWS:
        raise ArithmeticError("locked source collision-row count changed")
    return {
        "rows_replayed": len(replay_projection),
        "row_projection_sha256": _canonical_sha256(replay_projection),
        "separation_counts": dict(sorted(separation_counts.items())),
        "class_by_separation": [
            {"collision_class": key[0], "outcome": key[1], "count": count}
            for key, count in sorted(class_by_separation.items())
        ],
        "c1_c2_survivors": c1_c2_survivors,
        "full_factor_aliases": full_factor_aliases,
        "new_curve_field_or_trace_range_enumerations": 0,
    }


def build_fixture(
    *, resource_cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE
) -> dict[str, object]:
    """Build the deterministic exact recovery fixture."""

    _require_integer("resource_cap", resource_cap)
    guard = ResourceGuard(resource_cap)
    source = _load_source()
    guard.charge("locked_source_payloads_loaded")
    resultant = _resultant_certificate(guard)
    plethysm = _weight_multisets(guard)

    for t, q in ((-7, 31), (Fraction(3, 2), Fraction(5, 3)), (4, -3)):
        c2_plethysm = q * e_trace(8, t, q) + q**3 * e_trace(4, t, q) + q**5
        c3_plethysm = -(
            q**3 * e_trace(9, t, q)
            + q**5 * e_trace(5, t, q)
            + q**6 * e_trace(3, t, q)
        )
        if c2_plethysm != sym5_second_coefficient(t, q):
            raise ArithmeticError("Lambda^2 plethystic trace identity failed")
        if c3_plethysm != sym5_third_coefficient(t, q):
            raise ArithmeticError("Lambda^3 plethystic trace identity failed")
        guard.charge("plethystic_polynomial_specializations_checked")

    replay = _replay_source_collisions(source, guard)
    fixture: dict[str, object] = {
        "schema": SCHEMA,
        "normalization": {
            "base_factor": "1-t*T+q*T^2=(1-alpha*T)*(1-beta*T)",
            "root_relations": "alpha+beta=t; alpha*beta=q",
            "sym5_factor": "det(1-Sym^5(Frob)*T), degree 6",
            "E_m": "sum(alpha^(m-j)*beta^j,j=0..m)",
            "E5": "t^5-4*q*t^3+3*q^2*t=t*(t^2-q)*(t^2-3*q)",
            "domain": "x,y,q in Q with q nonzero",
        },
        "coefficient_formulas": {
            "c1": "-E5(t,q)",
            "c2": (
                "q*(q-t^2)*(3*q-t^2)*(q^2-3*q*t^2+t^4)"
            ),
            "c3": (
                "-q^3*t*(2*q-t^2)*(3*q-t^2)*(q^2-3*q*t^2+t^4)"
            ),
            "self_reciprocal_coefficients": (
                "[1,c1,c2,c3,q^5*c2,q^10*c1,q^15]"
            ),
        },
        "exact_recovery_theorem_over_Q": {
            "pair_E5_c2_equal_iff": (
                "x=y, or x=-y and x^2=q, or x=-y and x^2=3*q"
            ),
            "triple_E5_c2_c3_equal_iff": "x=y, or x=-y and x^2=3*q",
            "full_factor_equal_iff": "x=y, or x=-y and x^2=3*q",
            "triple_equals_full_reason": (
                "fixed-q self-reciprocity determines T^4,T^5,T^6 from c2,c1,1"
            ),
            "non_diagonal_sign_cases": {
                "x2_eq_q": "E5 and c2 agree; c3 changes sign and is nonzero",
                "x2_eq_3q": "E5=c2=c3=0 and the complete factors agree",
            },
            "zero_cases": {
                "x=y=0": "diagonal",
                "exactly_one_of_x_y_zero": (
                    "cannot have both E5 and c2 equal when q is nonzero"
                ),
            },
            "minimum_depth_witnesses": [
                {
                    "q": 31,
                    "x": -7,
                    "y": 3,
                    "meaning": "E5 alone aliases; c2 is the first separator",
                },
                {
                    "q": 9,
                    "x": -3,
                    "y": 3,
                    "meaning": "E5 and c2 alias; c3 is the first separator",
                },
                {
                    "q": 3,
                    "x": -3,
                    "y": 3,
                    "meaning": "the complete degree-six factors alias",
                },
            ],
        },
        "difference_factorization": {
            "E5_difference": "E5(x,q)-E5(y,q)=(x-y)*Q",
            "Q": "K-4*q*H+3*q^2",
            "H": "x^2+x*y+y^2",
            "K": "x^4+x^3*y+x^2*y^2+x*y^3+y^4",
            "c2_difference": "c2(x,q)-c2(y,q)=q*(x^2-y^2)*R",
            "R": (
                "-13*q^3+16*q^2*(x^2+y^2)-7*q*(x^4+x^2*y^2+y^4)"
                "+(x^6+x^4*y^2+x^2*y^4+y^6)"
            ),
        },
        "resultant_certificate": resultant,
        "plethystic_certificate": plethysm,
        "locked_collision_replay": replay,
        "source_lock": {
            "path": _relative(SOURCE_PATH),
            "schema": EXPECTED_SOURCE_SCHEMA,
            "payload_sha256": EXPECTED_SOURCE_PAYLOAD_SHA256,
            "file_sha256_lf_normalized": EXPECTED_SOURCE_FILE_SHA256_LF,
            "use": (
                "replay exactly the 61 frozen scalar-collision rows; no finite "
                "field, curve, or trace-range enumeration"
            ),
        },
        "resource_contract": {
            "accounted_work_ledger": dict(sorted(guard.ledger.items())),
            "accounted_work_units": guard.total,
            "accounted_work_unit_cap_exclusive": guard.cap,
            "source_collision_rows_replayed": replay["rows_replayed"],
            "new_curve_field_or_trace_range_enumerations": 0,
            "symbolic_engine_dependency": False,
        },
        "scope_firewall": {
            "theorem_is_local_and_algebraic_over_Q": True,
            "no_curve_or_isogeny_class_realization_claim": True,
            "no_automorphy_or_modularity_claim": True,
            "no_global_compatible_family_or_euler_product_constructed": True,
            "no_RH_or_zero_distribution_consequence_claimed": True,
            "no_external_literature_priority_claim": True,
            "finite_replay_is_not_evidence_for_the_all_Q_proof": (
                "the proof is the exact difference/resultant argument; the replay is regression evidence"
            ),
        },
        "producer": {
            "script": _relative(Path(__file__).resolve()),
            "script_sha256_lf_normalized": _lf_sha256(Path(__file__).resolve()),
            "note": _relative(NOTE_PATH),
            "note_sha256_lf_normalized": _lf_sha256(NOTE_PATH),
            "test": _relative(TEST_PATH),
            "test_sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _serialized_fixture() -> str:
    return json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail unless the stored deterministic JSON equals a fresh build",
    )
    args = parser.parse_args(argv)
    serialized = _serialized_fixture()
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != serialized:
            raise SystemExit("stored Sym^5 coefficient-recovery fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
