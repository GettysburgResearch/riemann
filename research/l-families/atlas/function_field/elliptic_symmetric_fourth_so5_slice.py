"""Exact Sym^4 elliptic local factors as a thin rank-one SO(5) slice.

The only finite input is the locked trace histogram in
``genus1_cubic_family_laws.json`` for q=3,5,7,11,13.  No field or curve is
enumerated here.  The symbolic all-q statements are deductions from the
locked elliptic-stack character theorem in ``genus1_cubic_family_laws.py``.
The bundled automatic Theta_12 evaluator is intentionally bounded by that
source's characteristic cap; callers beyond it must supply Theta_12(q).

For an elliptic Frobenius pair alpha+beta=a and alpha*beta=q, the five
Sym^4 eigenvalues are

    alpha^4, q*alpha^2, q^2, q*beta^2, beta^4.

The middle eigenvalue gives a genuine pointwise factor (1-q^2*T), but the
ambient irreducible Sym^4 representation has no forced common line.  The
packet keeps that family/fiber distinction explicit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import genus1_cubic_family_laws as genus1


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "elliptic_symmetric_fourth_so5_slice.json"
NOTE_PATH = HERE / "ELLIPTIC_SYMMETRIC_FOURTH_SO5_SLICE.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_symmetric_fourth_so5_slice.py"

GENUS1_FIXTURE_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_SOURCE_PATH = HERE / "genus1_cubic_family_laws.py"
PRIMITIVE_FIXTURE_PATH = HERE / "genus2_primitive_exterior_square.json"
PRIMITIVE_SOURCE_PATH = HERE / "genus2_primitive_exterior_square.py"
PRIMITIVE_NOTE_PATH = HERE / "GENUS2_PRIMITIVE_EXTERIOR_SQUARE.md"
PRIMITIVE_TEST_PATH = ROOT / "tests" / "test_genus2_primitive_exterior_square.py"

FROZEN_Q_VALUES = (3, 5, 7, 11, 13)
EXPECTED_GENUS1_PAYLOAD_SHA256 = (
    "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df"
)
EXPECTED_GENUS1_FIXTURE_SHA256 = (
    "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227"
)
EXPECTED_GENUS1_SOURCE_SHA256 = (
    "3d5baace952240c162c83bd5c66eb81db1704aee35e770de3d8df43fff669b79"
)
EXPECTED_PRIMITIVE_PAYLOAD_SHA256 = (
    "235991e9e36a55ec8352a7c18fc2e0722546267daf51a17642ff767c3387ab1c"
)
EXPECTED_PRIMITIVE_FIXTURE_SHA256 = (
    "2e39dd0f24dc38b1c03165d047f10858ac205edc780fbc8bff225717c507a976"
)
EXPECTED_PRIMITIVE_SOURCE_SHA256 = (
    "d86c58fc8a1752f43402009f1abc467a58064418a723d2fd5cf6bf8fae32e5f4"
)
EXPECTED_PRIMITIVE_NOTE_SHA256 = (
    "033cf1e6342248e037e7c375e17f47071fb5ffdfd40c649be124271055f77f32"
)
EXPECTED_PRIMITIVE_TEST_SHA256 = (
    "0190f49dd1f1f6b78ab9d73b9d11bb44861a50068e451e4719c2337c08789293"
)

MAX_COMPACT_MOMENT_ORDER = 8
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 5_000


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _fraction(value: Fraction | int) -> list[int]:
    value = Fraction(value)
    return [value.numerator, value.denominator]


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


class ResourceGuard:
    """Small auditable ledger; units are declared high-level exact work."""

    def __init__(self, cap: int = ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE) -> None:
        self.cap = cap
        self.ledger: Counter[str] = Counter()

    @property
    def total(self) -> int:
        return sum(self.ledger.values())

    def charge(self, name: str, units: int = 1) -> None:
        if units < 0:
            raise ValueError("resource charge must be nonnegative")
        if self.total + units >= self.cap:
            raise RuntimeError(
                f"accounted work would meet or exceed exclusive cap {self.cap}"
            )
        self.ledger[name] += units


def _validate_q(q: int) -> None:
    genus1.prime_power_data(q)


def multiply_polynomials(
    left: Sequence[int], right: Sequence[int]
) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def evaluate_polynomial(coefficients: Sequence[int], value: Fraction) -> Fraction:
    total = Fraction(0)
    for coefficient in reversed(coefficients):
        total = total * value + coefficient
    return total


def elliptic_power_sum(a: int, q: int, order: int) -> int:
    """Return alpha^order+beta^order from alpha+beta=a, alpha*beta=q."""

    _validate_q(q)
    if order < 0:
        raise ValueError("power-sum order must be nonnegative")
    if order == 0:
        return 2
    previous_previous, previous = 2, a
    for _ in range(2, order + 1):
        previous_previous, previous = previous, a * previous - q * previous_previous
    return previous


def sym4_power_sum(a: int, q: int, order: int) -> int:
    """Power sum of the five Sym^4 Frobenius eigenvalues."""

    _validate_q(q)
    if order < 1:
        raise ValueError("Sym^4 Newton power-sum order must be positive")
    return (
        elliptic_power_sum(a, q, 4 * order)
        + q**order * elliptic_power_sum(a, q, 2 * order)
        + q ** (2 * order)
    )


def sym4_local_coefficients_via_newton(a: int, q: int) -> tuple[int, ...]:
    """Derive det(1-Sym^4(Frob)*T) solely from Newton power sums."""

    _validate_q(q)
    coefficients = [1]
    power_sums = [0] + [sym4_power_sum(a, q, order) for order in range(1, 6)]
    for degree in range(1, 6):
        numerator = -sum(
            coefficients[degree - order] * power_sums[order]
            for order in range(1, degree + 1)
        )
        if numerator % degree:
            raise ArithmeticError("Sym^4 Newton recurrence lost integrality")
        coefficients.append(numerator // degree)
    return tuple(coefficients)


def sym4_local_coefficients_via_paired_roots(a: int, q: int) -> tuple[int, ...]:
    """Derive the same factor from its two reciprocal pairs and middle root."""

    _validate_q(q)
    u = a * a - 2 * q
    alpha4_plus_beta4 = u * u - 2 * q * q
    outer_pair = (1, -alpha4_plus_beta4, q**4)
    inner_pair = (1, -q * u, q**4)
    return multiply_polynomials(
        (1, -(q**2)), multiply_polynomials(outer_pair, inner_pair)
    )


def sym4_local_coefficients_closed(a: int, q: int) -> tuple[int, ...]:
    """Expanded degree-five weight-four local polynomial."""

    _validate_q(q)
    trace_numerator = a**4 - 3 * q * a * a + q * q
    u = a * a - 2 * q
    second_numerator = q * u * (u * u + q * u - q * q)
    return (
        1,
        -trace_numerator,
        second_numerator,
        -(q**2) * second_numerator,
        q**6 * trace_numerator,
        -(q**10),
    )


def pointwise_central_quotient(a: int, q: int) -> tuple[int, ...]:
    """The degree-four quotient after the genuine fiberwise q^2 eigenline."""

    _validate_q(q)
    u = a * a - 2 * q
    x = u * u - 2 * q * q
    y = q * u
    return (1, -(x + y), x * y + 2 * q**4, -(q**4) * (x + y), q**8)


def normalized_so5_coordinates(a: int, q: int) -> tuple[Fraction, Fraction]:
    """Return (y,d) in 1-y*z+d*z^2-d*z^3+y*z^4-z^5."""

    coefficients = sym4_local_coefficients_closed(a, q)
    return Fraction(-coefficients[1], q**2), Fraction(coefficients[2], q**4)


def rank_one_curve_residual(y: Fraction, d: Fraction) -> Fraction:
    """Residual of d^2+y*d-y^2-y^3=0."""

    return d * d + y * d - y * y - y**3


def normalized_parameterization(a: int, q: int) -> tuple[Fraction, Fraction, Fraction]:
    """Return w=a^2/q-2, y=w^2+w-1, d=w*y."""

    _validate_q(q)
    w = Fraction(a * a, q) - 2
    y = w * w + w - 1
    d = w * y
    return w, y, d


Character = dict[int, int]


def su2_tensor(left: Mapping[int, int], right: Mapping[int, int]) -> Character:
    """Multiply SU(2) characters using Clebsch--Gordan."""

    output: Counter[int] = Counter()
    for left_weight, left_multiplicity in left.items():
        for right_weight, right_multiplicity in right.items():
            for weight in range(
                abs(left_weight - right_weight), left_weight + right_weight + 1, 2
            ):
                output[weight] += left_multiplicity * right_multiplicity
    return dict(sorted(output.items()))


def su2_character_power(character: Mapping[int, int], order: int) -> Character:
    if order < 0:
        raise ValueError("character power must be nonnegative")
    output: Character = {0: 1}
    for _ in range(order):
        output = su2_tensor(output, character)
    return output


def su2_sym4_haar_trace_moments(
    maximum_order: int = MAX_COMPACT_MOMENT_ORDER,
) -> list[int]:
    """Multiplicity of the trivial representation in Sym^4(Std)^tensor n."""

    if not 0 <= maximum_order <= MAX_COMPACT_MOMENT_ORDER:
        raise ValueError(f"compact moment order is restricted to 0..{MAX_COMPACT_MOMENT_ORDER}")
    return [
        su2_character_power({4: 1}, order).get(0, 0)
        for order in range(maximum_order + 1)
    ]


Laurent = dict[tuple[int, int], int]


def _laurent_product(
    left: Mapping[tuple[int, int], int],
    right: Mapping[tuple[int, int], int],
    *,
    guard: ResourceGuard | None = None,
) -> Laurent:
    if guard is not None:
        guard.charge("weyl_laurent_term_products", len(left) * len(right))
    output: Counter[tuple[int, int]] = Counter()
    for (left_x, left_y), left_value in left.items():
        for (right_x, right_y), right_value in right.items():
            output[(left_x + right_x, left_y + right_y)] += left_value * right_value
    return {key: value for key, value in output.items() if value}


def so5_standard_haar_trace_moments(
    maximum_order: int = MAX_COMPACT_MOMENT_ORDER,
    *,
    guard: ResourceGuard | None = None,
) -> list[int]:
    """B2 Weyl constant terms for the SO(5) standard character."""

    if not 0 <= maximum_order <= MAX_COMPACT_MOMENT_ORDER:
        raise ValueError(f"compact moment order is restricted to 0..{MAX_COMPACT_MOMENT_ORDER}")
    denominator: Laurent = {(0, 0): 1}
    for root in ((1, -1), (0, 1), (1, 0), (1, 1)):
        denominator = _laurent_product(
            denominator,
            {(0, 0): 2, root: -1, (-root[0], -root[1]): -1},
            guard=guard,
        )
    character: Laurent = {
        (0, 0): 1,
        (1, 0): 1,
        (-1, 0): 1,
        (0, 1): 1,
        (0, -1): 1,
    }
    power: Laurent = {(0, 0): 1}
    moments: list[int] = []
    for order in range(maximum_order + 1):
        if guard is not None:
            guard.charge("weyl_constant_term_pairs", len(power))
        numerator = sum(
            coefficient * denominator.get((-exponent[0], -exponent[1]), 0)
            for exponent, coefficient in power.items()
        )
        if numerator % 8:
            raise ArithmeticError("B2 Weyl constant term was not divisible by 8")
        moments.append(numerator // 8)
        if order != maximum_order:
            power = _laurent_product(power, character, guard=guard)
    return moments


Y_CHARACTER: Character = {4: 1}
D_CHARACTER: Character = {2: 1, 6: 1}
SYMBOLIC_ALL_Q_COORDINATE_LAWS = {
    "mean_y": "-q^-3",
    "mean_d": "-q^-2-q^-4",
    "mean_y_squared": "1-q^-2-q^-3-q^-4-q^-5",
    "mean_y_times_d": (
        "-2*q^-2-2*q^-3-2*q^-4-q^-5-(1+Theta_12(q))*q^-6"
    ),
    "mean_d_squared": (
        "2-2*q^-2-4*q^-3-3*q^-4-3*q^-5-(1+Theta_12(q))*q^-6-q^-7"
    ),
    "mean_y_cubed": (
        "1-3*q^-2-5*q^-3-4*q^-4-3*q^-5-"
        "2*(1+Theta_12(q))*q^-6-q^-7"
    ),
}


def normalized_stack_character_mean(
    symmetric_power: int,
    q: int,
    *,
    cusp_traces: Mapping[int, int] | None = None,
) -> Fraction:
    """Uniform-model/normalized-stack mean of the SU(2) character chi_m.

    When a nonzero cusp space occurs, ``cusp_traces`` may supply its exact
    prime-power Frobenius trace.  Without that argument this inherits the
    deliberately bounded automatic evaluator in the locked genus-one source.
    """

    _validate_q(q)
    if symmetric_power < 0 or symmetric_power % 2:
        raise ValueError("this packet requests nonnegative even SU(2) characters")
    stack_sum = genus1.symmetric_character_stack_sum(
        symmetric_power, q, cusp_traces=cusp_traces
    )
    return Fraction(stack_sum, q ** (symmetric_power // 2 + 1))


def _character_mean(
    character: Mapping[int, int],
    q: int,
    *,
    cusp_traces: Mapping[int, int] | None = None,
) -> Fraction:
    return sum(
        multiplicity
        * normalized_stack_character_mean(weight, q, cusp_traces=cusp_traces)
        for weight, multiplicity in character.items()
    )


def symbolic_all_q_coordinate_laws() -> dict[str, str]:
    """Return formulas valid symbolically for every odd prime power."""

    return dict(SYMBOLIC_ALL_Q_COORDINATE_LAWS)


def _coordinate_laws_from_character_theorem(
    q: int,
    *,
    cusp_traces: Mapping[int, int] | None = None,
) -> dict[str, Fraction]:
    """Instantiate the character theorem with the supplied cusp traces."""

    _validate_q(q)
    y_squared = su2_tensor(Y_CHARACTER, Y_CHARACTER)
    y_cubed = su2_tensor(y_squared, Y_CHARACTER)
    y_times_d = su2_tensor(Y_CHARACTER, D_CHARACTER)
    d_squared = su2_tensor(D_CHARACTER, D_CHARACTER)
    return {
        "mean_y": _character_mean(Y_CHARACTER, q, cusp_traces=cusp_traces),
        "mean_d": _character_mean(D_CHARACTER, q, cusp_traces=cusp_traces),
        "mean_y_squared": _character_mean(
            y_squared, q, cusp_traces=cusp_traces
        ),
        "mean_y_times_d": _character_mean(
            y_times_d, q, cusp_traces=cusp_traces
        ),
        "mean_d_squared": _character_mean(
            d_squared, q, cusp_traces=cusp_traces
        ),
        "mean_y_cubed": _character_mean(y_cubed, q, cusp_traces=cusp_traces),
    }


def exact_coordinate_laws_with_theta12(
    q: int, theta12: int
) -> dict[str, Fraction]:
    """Instantiate the laws for an odd prime power given exact Theta_12(q)."""

    if type(theta12) is not int:
        raise TypeError("theta12 must be an integer exact Frobenius trace")
    return _coordinate_laws_from_character_theorem(
        q, cusp_traces={12: theta12}
    )


def bounded_exact_coordinate_laws(q: int) -> dict[str, Fraction]:
    """Automatically evaluate the selected laws within the locked trace cap.

    The complete bundle includes characters whose mean uses Theta_12(q).
    The locked Ramanujan-tau helper supports only characteristics at most
    ``genus1.MAX_TAU_PRIME``.  Beyond that boundary, use
    :func:`exact_coordinate_laws_with_theta12` with an externally supplied
    exact trace; the symbolic theorem itself remains all-q.
    """

    characteristic, _ = genus1.prime_power_data(q)
    if characteristic > genus1.MAX_TAU_PRIME:
        raise ValueError(
            "bounded exact coordinate-law evaluator requires "
            f"characteristic<={genus1.MAX_TAU_PRIME}; supply Theta_12(q) "
            "to exact_coordinate_laws_with_theta12"
        )
    return _coordinate_laws_from_character_theorem(q)


def _load_locked_json(
    path: Path,
    expected_file_sha256: str,
    expected_payload_sha256: str,
) -> dict[str, object]:
    actual_file_sha256 = _lf_sha256(path)
    if actual_file_sha256 != expected_file_sha256:
        raise RuntimeError(f"locked file hash drifted: {_relative(path)}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("payload_sha256") != expected_payload_sha256:
        raise RuntimeError(f"locked payload hash drifted: {_relative(path)}")
    unhashed = dict(payload)
    claimed = unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != claimed:
        raise RuntimeError(f"locked payload is internally inconsistent: {_relative(path)}")
    return payload


def _lock(path: Path, **extra: object) -> dict[str, object]:
    return {
        "path": _relative(path),
        "sha256_lf_normalized": _lf_sha256(path),
        **extra,
    }


def _source_locks() -> dict[str, object]:
    locks = {
        "genus1_fixture": _lock(
            GENUS1_FIXTURE_PATH, payload_sha256=EXPECTED_GENUS1_PAYLOAD_SHA256
        ),
        "genus1_source": _lock(GENUS1_SOURCE_PATH),
        "primitive_exterior_fixture": _lock(
            PRIMITIVE_FIXTURE_PATH,
            payload_sha256=EXPECTED_PRIMITIVE_PAYLOAD_SHA256,
        ),
        "primitive_exterior_source": _lock(PRIMITIVE_SOURCE_PATH),
        "primitive_exterior_note": _lock(PRIMITIVE_NOTE_PATH),
        "primitive_exterior_test": _lock(PRIMITIVE_TEST_PATH),
        "producer": _lock(Path(__file__).resolve()),
        "note": _lock(NOTE_PATH),
        "test": _lock(TEST_PATH),
    }
    expected = {
        "genus1_fixture": EXPECTED_GENUS1_FIXTURE_SHA256,
        "genus1_source": EXPECTED_GENUS1_SOURCE_SHA256,
        "primitive_exterior_fixture": EXPECTED_PRIMITIVE_FIXTURE_SHA256,
        "primitive_exterior_source": EXPECTED_PRIMITIVE_SOURCE_SHA256,
        "primitive_exterior_note": EXPECTED_PRIMITIVE_NOTE_SHA256,
        "primitive_exterior_test": EXPECTED_PRIMITIVE_TEST_SHA256,
    }
    for name, expected_hash in expected.items():
        if locks[name]["sha256_lf_normalized"] != expected_hash:
            raise RuntimeError(f"source lock drifted: {name}")
    return locks


def _fraction_moment(
    law: Mapping[tuple[Fraction, Fraction], int],
    member_count: int,
    y_power: int,
    d_power: int,
) -> Fraction:
    return Fraction(
        sum(
            count * y**y_power * d**d_power
            for (y, d), count in law.items()
        ),
        member_count,
    )


def _frozen_pushforward(
    genus1_fixture: Mapping[str, object], guard: ResourceGuard
) -> list[dict[str, object]]:
    rows = genus1_fixture["finite_regressions"]
    if not isinstance(rows, list) or tuple(int(row["q"]) for row in rows) != FROZEN_Q_VALUES:
        raise RuntimeError("locked genus-one fixture has the wrong q rows")

    output: list[dict[str, object]] = []
    for row in rows:
        q = int(row["q"])
        histogram = {int(a): int(count) for a, count in row["model_trace_histogram"].items()}
        member_count = sum(histogram.values())
        if member_count != q * q * (q - 1):
            raise RuntimeError("locked model histogram has the wrong mass")

        coordinate_law: Counter[tuple[Fraction, Fraction]] = Counter()
        a_squared_support: dict[int, dict[str, object]] = {}
        for a, count in sorted(histogram.items()):
            guard.charge("locked_histogram_atom_visits")
            paired = sym4_local_coefficients_via_paired_roots(a, q)
            newton = sym4_local_coefficients_via_newton(a, q)
            closed = sym4_local_coefficients_closed(a, q)
            guard.charge("newton_coefficient_checks", 5)
            if paired != newton or newton != closed:
                raise ArithmeticError("the two Sym^4 derivations disagree")
            quotient = pointwise_central_quotient(a, q)
            if closed != multiply_polynomials((1, -(q**2)), quotient):
                raise ArithmeticError("pointwise central factor division failed")
            y, d = normalized_so5_coordinates(a, q)
            w, parameter_y, parameter_d = normalized_parameterization(a, q)
            if (y, d) != (parameter_y, parameter_d):
                raise ArithmeticError("rank-one parameterization disagrees")
            if rank_one_curve_residual(y, d):
                raise ArithmeticError("normalized coefficients left the rank-one curve")
            coordinate_law[(y, d)] += count
            squared = a * a
            atom = a_squared_support.setdefault(
                squared,
                {
                    "a_squared": squared,
                    "source_traces": [],
                    "member_count": 0,
                    "w": _fraction(w),
                    "y": _fraction(y),
                    "d": _fraction(d),
                    "local_coefficients": list(closed),
                    "pointwise_central_quotient": list(quotient),
                },
            )
            atom["source_traces"].append(a)
            atom["member_count"] += count

        if sum(coordinate_law.values()) != member_count:
            raise ArithmeticError("pushforward law lost mass")
        finite_laws = {
            "mean_y": _fraction(_fraction_moment(coordinate_law, member_count, 1, 0)),
            "mean_d": _fraction(_fraction_moment(coordinate_law, member_count, 0, 1)),
            "mean_y_squared": _fraction(
                _fraction_moment(coordinate_law, member_count, 2, 0)
            ),
            "mean_y_times_d": _fraction(
                _fraction_moment(coordinate_law, member_count, 1, 1)
            ),
            "mean_d_squared": _fraction(
                _fraction_moment(coordinate_law, member_count, 0, 2)
            ),
            "mean_y_cubed": _fraction(
                _fraction_moment(coordinate_law, member_count, 3, 0)
            ),
        }
        guard.charge("finite_coordinate_moment_atom_products", 6 * len(coordinate_law))
        theorem_laws = {
            name: _fraction(value)
            for name, value in bounded_exact_coordinate_laws(q).items()
        }
        if finite_laws != theorem_laws:
            raise ArithmeticError("frozen histogram does not match the all-q stack law")

        wrong_weight_value = evaluate_polynomial(
            sym4_local_coefficients_closed(0, q), Fraction(1, q)
        )
        if not wrong_weight_value:
            raise ArithmeticError("wrong weight-one central-factor control collapsed")
        output.append(
            {
                "q": q,
                "source_histogram_sha256": _canonical_sha256(
                    {str(a): histogram[a] for a in sorted(histogram)}
                ),
                "source_trace_atom_count": len(histogram),
                "member_count": member_count,
                "complete_rank_one_pushforward": {
                    "support_size": len(coordinate_law),
                    "atoms": [a_squared_support[key] for key in sorted(a_squared_support)],
                },
                "selected_exact_coordinate_laws": finite_laws,
                "bounded_numeric_theorem_regression": theorem_laws,
                "negative_control_wrong_weight_factor": {
                    "wrong_candidate": "1-q*T",
                    "witness_trace": 0,
                    "P_at_T_equals_1_over_q": _fraction(wrong_weight_value),
                    "nonzero": True,
                },
            }
        )
    return output


def build_fixture(q_values: Iterable[int] = FROZEN_Q_VALUES) -> dict[str, object]:
    if tuple(q_values) != FROZEN_Q_VALUES:
        raise ValueError(f"frozen packet requires exactly q={FROZEN_Q_VALUES}")
    genus1_fixture = _load_locked_json(
        GENUS1_FIXTURE_PATH,
        EXPECTED_GENUS1_FIXTURE_SHA256,
        EXPECTED_GENUS1_PAYLOAD_SHA256,
    )
    primitive_fixture = _load_locked_json(
        PRIMITIVE_FIXTURE_PATH,
        EXPECTED_PRIMITIVE_FIXTURE_SHA256,
        EXPECTED_PRIMITIVE_PAYLOAD_SHA256,
    )
    guard = ResourceGuard()
    frozen = _frozen_pushforward(genus1_fixture, guard)
    su2_moments = su2_sym4_haar_trace_moments()
    so5_moments = so5_standard_haar_trace_moments(guard=guard)
    expected_su2 = [1, 0, 1, 1, 5, 16, 65, 260, 1085]
    expected_so5 = [1, 0, 1, 0, 3, 1, 15, 15, 105]
    if su2_moments != expected_su2 or so5_moments != expected_so5:
        raise ArithmeticError("compact Haar baselines drifted")
    primitive_baseline = primitive_fixture["compact_SO5_baseline"][
        "standard_trace_moments"
    ]
    if primitive_baseline != expected_so5[:7]:
        raise RuntimeError("locked primitive packet has a different SO(5) baseline")

    decompositions = {
        "y": Y_CHARACTER,
        "d": D_CHARACTER,
        "y_squared": su2_tensor(Y_CHARACTER, Y_CHARACTER),
        "y_times_d": su2_tensor(Y_CHARACTER, D_CHARACTER),
        "d_squared": su2_tensor(D_CHARACTER, D_CHARACTER),
        "y_cubed": su2_character_power(Y_CHARACTER, 3),
    }
    payload: dict[str, object] = {
        "schema": "riemann.function_field.elliptic_symmetric_fourth_so5_slice.v1",
        "raw_fixture_id": "elliptic-sym4-so5-rank-one-q3-q5-q7-q11-q13-v1",
        "status": "EXACT_ALL_Q_LOCAL_ALGEBRA_SYMBOLIC_STACK_LAWS_AND_BOUNDED_NUMERIC_PUSHFORWARD",
        "rigor_level": {
            "local_polynomial": "PROVED_POINTWISE_BY_PAIRED_ROOTS_AND_NEWTON_RECURRENCE",
            "rank_one_curve": "EXACT_ELIMINATION_IDENTITY",
            "compact_group_moments": "EXACT_CLEBSCH_GORDAN_AND_B2_WEYL_CONSTANT_TERMS",
            "symbolic_all_q_stack_laws": "PROVED_FOR_EVERY_ODD_PRIME_POWER_FROM_LOCKED_CHARACTER_THEOREM",
            "automatic_numeric_stack_laws": "EXACT_ONLY_WHEN_CHARACTERISTIC_AT_MOST_1000; LARGER_CHARACTERISTICS_REQUIRE_SUPPLIED_THETA_12",
            "finite_pushforwards": "EXACT_FOR_Q_3_5_7_11_13_FROM_COMPLETE_LOCKED_HISTOGRAMS",
            "monodromy_automorphy_and_global_analytic_claims": "NOT_INFERRED",
        },
        "input_family": {
            "marked_models": "monic squarefree cubics D over F_q, with E_D: y^2=D(x)",
            "source_measure": "uniform marked models, equivalently the normalized elliptic stack measure for trace observables",
            "source_trace": "a=q+1-#E_D(F_q), P_E(T)=1-a*T+q*T^2",
            "frozen_q_values": list(FROZEN_Q_VALUES),
            "new_field_or_curve_enumeration": False,
        },
        "local_polynomial_theorem": {
            "weight_and_degree": "Sym^4 H^1 has weight 4 and dimension 5",
            "eigenvalues": [
                "alpha^4",
                "q*alpha^2",
                "q^2",
                "q*beta^2",
                "beta^4",
            ],
            "paired_factorization": "(1-q^2*T)*(1-(a^4-4*q*a^2+2*q^2)*T+q^4*T^2)*(1-q*(a^2-2*q)*T+q^4*T^2)",
            "expanded": "1-C*T+D*T^2-q^2*D*T^3+q^6*C*T^4-q^10*T^5, C=a^4-3*q*a^2+q^2, D=q*(a^2-2*q)*((a^2-2*q)^2+q*(a^2-2*q)-q^2)",
            "independent_derivations": [
                "pair alpha^4 with beta^4 and q*alpha^2 with q*beta^2, then include q^2",
                "Newton recurrence from p_n=alpha^(4n)+q^n*(alpha^(2n)+beta^(2n))+q^(2n)+beta^(4n)",
            ],
            "functional_equation_shape": "c_3=-q^2*c_2, c_4=-q^6*c_1, c_5=-q^10",
            "pointwise_middle_factor": "1-q^2*T",
        },
        "rank_one_SO5_slice": {
            "normalized_form": "P(z/q^2)=1-y*z+d*z^2-d*z^3+y*z^4-z^5",
            "coordinates": "r=a^2/q; y=r^2-3*r+1=chi_4; d=(r-2)*y=chi_2+chi_6",
            "normalization_parameter": "w=r-2 gives y=w^2+w-1 and d=w*y",
            "eliminated_curve": "d^2+y*d-y^2-y^3=0",
            "geometry": "the reduced plane curve is rational; its normalization parameter is w, and (y,d)=(0,0) has the two Qbar preimages w^2+w-1=0",
            "arithmetic_node_exclusion": "an arithmetic input has rational r=a^2/q and w=r-2, but w^2+w-1 has discriminant 5 and no rational root; therefore no elliptic trace input hits (y,d)=(0,0)",
            "compact_subgroup": "Sym^4: SU(2)->SO(5) kills {-I,+I}, factors through an irreducible SO(3), and is the principal A1 slice inside B2 at the representation level",
            "rank_warning": "rank one refers to the one torus/conjugacy parameter, not to the rank of the five-dimensional local system",
        },
        "pointwise_q_squared_eigenline_without_forced_common_line": {
            "ambient_representation_level": "Sym^4 of the standard SL2 representation is irreducible, so ambient representation theory supplies no invariant vector or forced common Tate line",
            "actual_family_level": "the geometric and arithmetic monodromy of the marked-cubic family are not proved here; a smaller subgroup or special locus could add invariant subsystems",
            "individual_finite_field_fiber_level": "for semisimple Frobenius with eigenlines alpha,beta, the middle monomial alpha^2*beta^2=q^2 spans a genuine Frobenius-stable line in that procyclic fiber",
            "why_the_axis_varies": "the middle weight line is defined only after choosing the Frobenius torus/eigenlines and is not preserved by the full ambient SL2 action",
            "pointwise_quotient_status": "division by 1-q^2*T is exact at every fiber; assembling the quartics into a common rank-four local system, motive, or automorphic family is not asserted",
        },
        "compact_group_comparison": {
            "orders_0_through_8": list(range(9)),
            "SU2_Sym4_trace_moments": su2_moments,
            "SO5_standard_trace_moments": so5_moments,
            "first_separation": {
                "order": 3,
                "SU2_Sym4": su2_moments[3],
                "SO5_standard": so5_moments[3],
                "reason": "the principal SO(3) slice has a cubic invariant in Sym^4, whereas the SO(5) standard representation has none",
            },
            "derivations": {
                "SU2": "Clebsch--Gordan multiplicity of V_0 in V_4 tensor power n",
                "SO5": "B2 Weyl constant term for 1+x+x^-1+y+y^-1 divided by Weyl-group order 8",
            },
        },
        "all_q_stack_laws": {
            "symbolic_theorem_scope": "every odd prime power q under uniform marked models / normalized elliptic-stack measure",
            "locked_input": "E[chi_m]=-(1+Theta_(m+2)(q))/q^(m/2+1) for positive even m, E[chi_0]=1",
            "coordinate_character_decompositions": {
                name: {str(weight): multiplicity for weight, multiplicity in value.items()}
                for name, value in decompositions.items()
            },
            "symbolic_formulas": symbolic_all_q_coordinate_laws(),
            "Theta_12_convention": "the locked prime-power Frobenius trace on the one-dimensional S_12(SL(2,Z)); for q=p it is Ramanujan tau(p)",
            "numeric_evaluator_contract": {
                "automatic_function": "bounded_exact_coordinate_laws(q)",
                "automatic_characteristic_cap_inclusive": genus1.MAX_TAU_PRIME,
                "reason": "the locked automatic Ramanujan-tau helper is intentionally bounded; this is a producer limit, not a theorem limit",
                "beyond_cap_function": "exact_coordinate_laws_with_theta12(q, theta12)",
                "supplied_trace_type_contract": "theta12 must be a built-in integer; booleans and every non-integer are rejected without coercion",
                "q_1009_boundary": "bounded_exact_coordinate_laws(1009) refuses explicitly; the symbolic formulas remain valid, and exact numeric instantiation requires supplied Theta_12(1009)",
            },
            "Haar_limits_visible_in_selected_laws": {
                "mean_y_squared": 1,
                "mean_d_squared": 2,
                "mean_y_cubed": 1,
            },
        },
        "frozen_histogram_pushforwards": frozen,
        "genus2_primitive_exterior_comparator": {
            "shared_universal_shape": "both normalized factors have 1-u*z+v*z^2-v*z^3+u*z^4-z^5",
            "genus2_coordinates": "primitive exterior square uses u=s=b/q-1 and v=k=(a^2-b)/q",
            "elliptic_Sym4_coordinates": "u=y=chi_4 and v=d=chi_2+chi_6",
            "rank_contrast": "the ambient genus-two SO(5) torus has two conjugacy parameters; elliptic Sym^4 lies on d^2+y*d-y^2-y^3=0 and has one",
            "group_map_contrast": "genus two uses Sp4/{+I,-I}->SO5 through primitive exterior square; elliptic Sym^4 uses the principal SU2/{+I,-I}=SO3 subgroup representation",
            "central_eigenvalue_parallel": "the genus-two primitive factor has already removed its canonical polarization line, so its remaining pointwise unit eigenvalue does not prove another common line; Sym4 has no pre-existing common line, and its pointwise q^2 eigenvalue does not prove any common line",
            "not_an_identification": "matching reciprocal coefficient shape and ambient target do not make the two families, measures, monodromy groups, or global L-functions equal",
            "locked_comparator_payload_sha256": EXPECTED_PRIMITIVE_PAYLOAD_SHA256,
        },
        "literature_boundary": {
            "classical_context": "the degree-five symmetric-fourth transfer from GL(2) to GL(5) is classical; this packet does not claim discovery of the local factor, its functional-equation shape, or automorphy",
            "primary_reference": "Henry H. Kim, Functoriality for the exterior square of GL(4) and the symmetric fourth of GL(2), J. Amer. Math. Soc. 16 (2003), 139-183, DOI 10.1090/S0894-0347-02-00410-1, https://doi.org/10.1090/S0894-0347-02-00410-1",
            "genus2_comparator_primary_reference": primitive_fixture[
                "literature_boundary"
            ]["primary_reference"],
            "project_specific_contribution": "the exact thin-curve elimination, locked marked-cubic pushforwards, symbolic all-q character defects with bounded exact instantiations, and explicit SU2-Sym4 versus SO5 Haar separation",
        },
        "resource_contract": {
            "exclusive_accounted_work_unit_cap": guard.cap,
            "accounted_work_unit_ledger": {
                **dict(sorted(guard.ledger.items())),
                "total_accounted_work_units": guard.total,
            },
            "unit_definition": "declared histogram visits, Newton coefficient checks, finite moment atom products, and Laurent term-pair visits; not literal machine instructions or a wall-clock complexity claim",
            "field_or_curve_enumerations": 0,
            "locked_histogram_rows_read": len(FROZEN_Q_VALUES),
            "random_samples": 0,
            "floating_point_results": 0,
            "maximum_polynomial_degree": 5,
            "maximum_compact_moment_order": MAX_COMPACT_MOMENT_ORDER,
            "automatic_theta12_characteristic_cap_inclusive": genus1.MAX_TAU_PRIME,
        },
        "producer_and_source_locks": {
            "no_field_or_curve_enumeration": True,
            "locks": _source_locks(),
        },
        "scope_firewall": {
            "no_family_identification": "the elliptic Sym^4 slice is compared with, not identified with, the genus-two primitive exterior-square family",
            "no_monodromy_upgrade": "compact representation targets and Haar comparators do not prove the actual arithmetic or geometric monodromy group",
            "no_pointwise_to_global_line": "a q^2 eigenline for each Frobenius element does not provide a common rank-one sub-local-system across the family",
            "no_measure_substitution": "uniform marked cubics / normalized stack weights are not relabeled as uniform coarse elliptic classes",
            "no_finite_to_asymptotic_fit": "five exact finite pushforwards check the theorem but are not fitted to an empirical convergence rate",
            "no_symbolic_to_numeric_cap_confusion": "the character identities hold symbolically for every odd prime power, while the bundled automatic Theta_12 evaluator is explicitly limited to characteristic at most 1000",
            "no_analytic_or_RH_claim": "local identities and compact moments imply no new analytic continuation, functional equation, zero-free region, RH, or GRH theorem",
        },
        "next_targets": [
            {
                "name": "thin_slice_detector",
                "known": "the cubic moment separates SU2-Sym4 from ambient SO5 at the first possible odd order",
                "open": "quantify how fast finite family moments expose principal-A1 or other proper-subgroup slices inside larger L-function atlases",
            },
            {
                "name": "rank_one_curve_singular_point_exclusion",
                "known": "the node has two Qbar normalization preimages, but no arithmetic input hits it: rational w=a^2/q-2 cannot solve w^2+w-1=0 because its discriminant is 5",
                "open": "quantify how closely arithmetic coefficient points approach the node and whether near-node behavior correlates with special endomorphisms",
            },
            {
                "name": "quartic_quotient_globalization",
                "known": "every local Sym4 polynomial has the exact factor 1-q^2*T",
                "open": "decide in which special subfamilies the pointwise quotient globalizes to an independent compatible rank-four system",
            },
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def _write(path: Path) -> None:
    path.write_text(json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _check(path: Path) -> None:
    expected = build_fixture()
    actual = json.loads(path.read_text(encoding="utf-8"))
    if actual != expected:
        raise SystemExit(f"fixture is stale: {path}")
    print(f"fixture is current: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write", nargs="?", const=OUTPUT_PATH, type=Path)
    action.add_argument("--check", nargs="?", const=OUTPUT_PATH, type=Path)
    arguments = parser.parse_args()
    if arguments.write is not None:
        _write(arguments.write)
    elif arguments.check is not None:
        _check(arguments.check)
    else:
        print(json.dumps(build_fixture(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
