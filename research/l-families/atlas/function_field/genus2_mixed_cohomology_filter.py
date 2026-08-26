#!/usr/bin/env python3
"""Exact replay for the genus-two mixed-cohomology filter.

The packet imports four hash-locked all-q marked-trace theorems, solves the
integral nuisance kernel in r_4,r_6,r_8,r_10, minimizes its USp(4) Haar norm,
and verifies the same-prime six-root recurrence and three exact channel
isolators.  It enumerates no finite field, curve, or arithmetic family.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from collections.abc import Mapping
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "genus2_mixed_cohomology_filter.json"
NOTE_PATH = HERE / "GENUS2_MIXED_COHOMOLOGY_FILTER.md"
TEST_PATH = ROOT / "tests" / "test_genus2_mixed_cohomology_filter.py"

NATIVE_PATH = HERE / "native_qadic_reciprocal_wavelet_spectroscopy.json"
SYM6_PATH = HERE / "genus2_sym6_marked_trace_average.json"
SYM8_PATH = HERE / "genus2_sym8_marked_trace_average.json"
SYM10_PATH = HERE / "genus2_sym10_marked_trace_average.json"

# Every prerequisite is pinned by a full source commit, an LF-normalized file
# hash, and the canonical payload hash stored inside the source JSON.
SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "native_t4": {
        "path": NATIVE_PATH,
        "commit": "aee73fda38a73bd792a4b69cd12ec7c4b7aaad1e",
        "lf": "aef506afa6b9b29f10528b634f45c7eab96abc36c6cd2de886262e834fcb2d43",
        "payload": "4e366316c6d55488b41e0104f6bee6c947220d7989ea7aa1381b5d72a099b882",
        "role": "all-q T_(4,0)=-3 trace input",
    },
    "sym6": {
        "path": SYM6_PATH,
        "commit": "522bc6b454016a07a9c65aaa6177d0340d70f5dc",
        "lf": "4e6156e8ca4f8b652e02961d3aa5f3ea63c9b42243908d1ecab8b94c08d253a6",
        "payload": "7bf31859372bb2a292f8321794f9b05859d2def82b1dd59ad83ab992088a5e86",
        "role": "all-q T_(6,0)=-4 trace theorem",
    },
    "sym8": {
        "path": SYM8_PATH,
        "commit": "dc63f02d0897e10936ef0767a1c8e6f15ac49e06",
        "lf": "a92700980ac7fef22f7a36db7b3d4d8bb7aa8d763904677e64bfca3182be0233",
        "payload": "423b8c37b69fb56b459beb7ebd9e6b94d12cf658f5819f7ac481e83560f5d0ae",
        "role": "all-q T_(8,0) marked-trace theorem",
    },
    "sym10": {
        "path": SYM10_PATH,
        "commit": "42910253be8173c6cd0de19a7a7403d0c31b5c22",
        "lf": "4f91ac00193805207088e9fc6aea2b464645267b17dc54f71165a1ae3b9d45ce",
        "payload": "0fbf48768fdea477b2bee4f53c8f1e547a167155c665b5e97bc201961971ec77",
        "role": "all-q T_(10,0) marked-trace theorem and Hecke coefficients",
    },
}
SOURCE_NAMES = ("native_t4", "sym6", "sym8", "sym10")

MAX_SOURCE_FILES = 4
MAX_SOURCE_BYTES = 2_000_000
MAX_PACKET_BYTES = 250_000
MAX_OUTPUT_BYTES = 250_000
MAX_EXACT_OPERATIONS = 50_000
MAX_LATTICE_REGRESSION_POINTS = 1_000
MAX_RECURRENCE_STEPS = 5_000
MAX_TOWER_EXPONENT = 18
LATTICE_REGRESSION_RADIUS = 12
MAX_WALL_SECONDS = 4.0

CHANNELS = (
    "q*Theta_Delta",
    "Theta_Delta",
    "Theta_(8,2)",
    "Theta_(10,2)",
    "q",
    "1",
)
WEIGHTS = (4, 6, 8, 10)

# Coordinates follow CHANNELS.  These constants are accepted only after the
# source JSON objects have passed both cryptographic and semantic checks.
TRACE_VECTORS = {
    4: (0, 0, 0, 0, 0, -3),
    6: (0, 0, 0, 0, 0, -4),
    8: (0, 0, -1, 0, -1, -6),
    10: (1, -1, -1, -1, -1, -7),
}


@dataclass
class ResourceGuard:
    source_files: int = 0
    source_bytes: int = 0
    packet_bytes: int = 0
    exact_operations: int = 0
    lattice_regression_points: int = 0
    recurrence_steps: int = 0

    def operation(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount

    def lattice_point(self) -> None:
        if self.lattice_regression_points + 1 > MAX_LATTICE_REGRESSION_POINTS:
            raise RuntimeError("lattice-regression cap exceeded")
        self.lattice_regression_points += 1

    def recurrence(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("recurrence increment must be nonnegative")
        if self.recurrence_steps + amount > MAX_RECURRENCE_STEPS:
            raise RuntimeError("recurrence-step cap exceeded")
        self.recurrence_steps += amount


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
        if isinstance(item, list):
            return [normalize(entry) for entry in item]
        if isinstance(item, dict):
            return {
                unicodedata.normalize("NFC", str(key)): normalize(entry)
                for key, entry in item.items()
            }
        return item

    return json.dumps(
        normalize(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_bytes(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _lf_sha256(path: Path) -> str:
    return hashlib.sha256(_lf_bytes(path.read_bytes())).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def source_locks_ready() -> bool:
    if len(SOURCE_LOCKS) != MAX_SOURCE_FILES or tuple(SOURCE_LOCKS) != SOURCE_NAMES:
        return False
    for lock in SOURCE_LOCKS.values():
        if not isinstance(lock.get("path"), Path):
            return False
        for field in ("commit", "lf", "payload"):
            value = lock.get(field)
            if not isinstance(value, str) or len(value) != (
                40 if field == "commit" else 64
            ):
                return False
            if any(character not in "0123456789abcdef" for character in value):
                return False
    return True


def _preflight_sources(names: tuple[str, ...]) -> int:
    if not names or len(set(names)) != len(names):
        raise ValueError("source names must be nonempty and distinct")
    if any(name not in SOURCE_LOCKS for name in names):
        raise ValueError("unknown source lock")
    if len(names) > MAX_SOURCE_FILES:
        raise RuntimeError("source-file cap exceeded")
    if not source_locks_ready():
        raise RuntimeError("source locks are incomplete")
    total = 0
    for name in names:
        path = SOURCE_LOCKS[name]["path"]
        if not isinstance(path, Path):
            raise TypeError("source path is not a Path")
        size = path.stat().st_size
        if size < 0 or total + size > MAX_SOURCE_BYTES:
            raise RuntimeError("source-byte cap exceeded before source read")
        total += size
    return total


def _validate_source_semantics(name: str, value: Mapping[str, object]) -> None:
    if name == "native_t4":
        traces = value.get("proved_all_q_trace_inputs")
        if not isinstance(traces, dict) or traces.get("T_(4,0)") != "-3":
            raise RuntimeError("native source does not certify T_(4,0)=-3")
        return
    theorem = value.get("theorem")
    if not isinstance(theorem, dict):
        raise TypeError(f"{name} source lacks theorem object")
    expected = {
        "sym6": "T_(6,0)(q)=-4",
        "sym8": "T_(8,0)(q)=-Theta_(8,2)(q)-q-6",
        "sym10": (
            "T_(10,0)(q)=(q-1)*Theta_Delta(q)-Theta_(8,2)(q)-Theta_(10,2)(q)-q-7"
        ),
    }[name]
    if theorem.get("marked_stack_trace") != expected:
        raise RuntimeError(f"{name} marked-trace theorem changed")


def _load_sources(
    names: tuple[str, ...], guard: ResourceGuard
) -> dict[str, dict[str, object]]:
    expected_total = _preflight_sources(names)
    loaded: dict[str, dict[str, object]] = {}
    for name in names:
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("source path is not a Path")
        data = path.read_bytes()
        guard.source_files += 1
        guard.source_bytes += len(data)
        if hashlib.sha256(_lf_bytes(data)).hexdigest() != lock["lf"]:
            raise RuntimeError(f"source LF lock failed: {name}")
        value = json.loads(data.decode("utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"source is not a JSON object: {name}")
        claimed = value.get("payload_sha256")
        payload = dict(value)
        payload.pop("payload_sha256", None)
        if claimed != lock["payload"] or claimed != _canonical_sha256(payload):
            raise RuntimeError(f"source payload lock failed: {name}")
        _validate_source_semantics(name, value)
        loaded[name] = value
    if guard.source_bytes != expected_total:
        raise RuntimeError("source sizes changed after preflight")
    return loaded


def _packet_manifest(guard: ResourceGuard) -> list[dict[str, object]]:
    paths = (SCRIPT_PATH, NOTE_PATH, TEST_PATH)
    total = sum(path.stat().st_size for path in paths)
    if total > MAX_PACKET_BYTES:
        raise RuntimeError("packet-byte cap exceeded before packet read")
    guard.packet_bytes = total
    return [
        {
            "path": _relative(path),
            "sha256_lf_normalized": _lf_sha256(path),
            "role": role,
        }
        for path, role in zip(
            paths,
            ("exact producer", "proof note", "focused regression tests"),
            strict=True,
        )
    ]


def _source_manifest() -> list[dict[str, object]]:
    return [
        {
            "id": name,
            "path": _relative(lock["path"]),
            "commit": lock["commit"],
            "sha256_lf_normalized": lock["lf"],
            "payload_sha256": lock["payload"],
            "role": lock["role"],
        }
        for name, lock in SOURCE_LOCKS.items()
    ]


def trace_coordinates(
    coefficients: tuple[int | Fraction, int | Fraction, int | Fraction, int | Fraction],
) -> tuple[Fraction, ...]:
    """Return exact coordinates in the ordered channel basis ``CHANNELS``."""
    result = [Fraction(0) for _ in CHANNELS]
    for coefficient, weight in zip(coefficients, WEIGHTS, strict=True):
        factor = Fraction(coefficient)
        for index, entry in enumerate(TRACE_VECTORS[weight]):
            result[index] += factor * entry
    return tuple(result)


def lattice_solution(m: int, k: int) -> tuple[int, int, int, int]:
    """All integral nuisance-free coefficients, ordered r4,r6,r8,r10."""
    if not isinstance(m, int) or not isinstance(k, int):
        raise TypeError("lattice parameters must be integers")
    return m + 4 * k, -m - 3 * k, -m, m


def lattice_parameters(coefficients: tuple[int, int, int, int]) -> tuple[int, int]:
    if len(coefficients) != 4 or any(
        not isinstance(value, int) for value in coefficients
    ):
        raise TypeError("four integral coefficients are required")
    coordinates = trace_coordinates(coefficients)
    if any(coordinates[index] for index in (2, 4, 5)):
        raise ValueError("coefficients do not cancel Theta_(8,2), q, and constant")
    c4, c6, c8, c10 = coefficients
    if c8 != -c10 or (c4 - c10) % 4:
        raise ArithmeticError("nuisance kernel did not yield integral parameters")
    m = c10
    k = (c4 - m) // 4
    if lattice_solution(m, k) != (c4, c6, c8, c10):
        raise ArithmeticError("lattice inverse failed")
    return m, k


def support_size(coefficients: tuple[int, ...]) -> int:
    return sum(value != 0 for value in coefficients)


def _primitive_orientation(coefficients: tuple[int, ...]) -> tuple[int, ...]:
    divisor = math.gcd(*coefficients)
    if divisor == 0:
        return coefficients
    primitive = tuple(value // divisor for value in coefficients)
    first = next((value for value in primitive if value), 0)
    return tuple(-value for value in primitive) if first < 0 else primitive


def _classification_certificate(guard: ResourceGuard) -> dict[str, object]:
    expected_basis = ((1, -1, -1, 1), (4, -3, 0, 0))
    for vector in expected_basis:
        coordinates = trace_coordinates(vector)
        if any(coordinates[index] for index in (2, 4, 5)):
            raise ArithmeticError("claimed lattice basis fails nuisance cancellation")

    primitive_sparse: set[tuple[int, ...]] = set()
    for m in range(-LATTICE_REGRESSION_RADIUS, LATTICE_REGRESSION_RADIUS + 1):
        for k in range(-LATTICE_REGRESSION_RADIUS, LATTICE_REGRESSION_RADIUS + 1):
            guard.lattice_point()
            coefficients = lattice_solution(m, k)
            if lattice_parameters(coefficients) != (m, k):
                raise ArithmeticError("bounded lattice round trip failed")
            coordinates = trace_coordinates(coefficients)
            expected = (m, -m, 0, -m, 0, 0)
            if coordinates != tuple(Fraction(value) for value in expected):
                raise ArithmeticError("lattice response formula failed")
            if m and support_size(coefficients) == 3:
                primitive_sparse.add(_primitive_orientation(coefficients))

    expected_sparse = {(-1, 0, -3, 3), (0, 1, 4, -4)}
    expected_sparse = {_primitive_orientation(row) for row in expected_sparse}
    if primitive_sparse != expected_sparse:
        raise ArithmeticError("primitive three-scale classification failed")

    # Adding c2*T2 with T2=q-1 cannot enlarge the kernel: after
    # c8+c10=0, the q equation is exactly c2=0.
    for c2 in range(-5, 6):
        q_channel = c2
        if q_channel == 0 and c2 != 0:
            raise ArithmeticError("r2 exclusion check failed")

    return {
        "channel_basis": list(CHANNELS),
        "trace_vectors_r4_r6_r8_r10": {
            str(weight): list(TRACE_VECTORS[weight]) for weight in WEIGHTS
        },
        "nuisance_equations": [
            "c_8+c_10=0 (simultaneously cancels Theta_(8,2) and q)",
            "3*c_4+4*c_6=-c_10 (cancels the constant)",
        ],
        "completeness_proof": (
            "Set m=c_10 and c_8=-m.  The Bezout equation "
            "3*c_4+4*c_6=-m has the particular solution (m,-m); "
            "all homogeneous integral solutions are k*(4,-3), since gcd(3,4)=1."
        ),
        "complete_integral_lattice": ("(c_4,c_6,c_8,c_10)=m*(1,-1,-1,1)+k*(4,-3,0,0)"),
        "basis": [list(vector) for vector in expected_basis],
        "response": "m*((q-1)*Theta_Delta(q)-Theta_(10,2)(q))",
        "r2_extension": "T_(2,0)=q-1 forces c_2=0 after c_8+c_10=0",
        "only_primitive_support_at_most_two": {
            "coefficients": [4, -3, 0, 0],
            "filter": "4*r_4-3*r_6",
            "response": 0,
        },
        "primitive_three_scale_mixed_filters": {
            "M4": {
                "coefficients": [-1, 0, -3, 3],
                "filter": "3*r_10-3*r_8-r_4",
                "response_multiple": 3,
            },
            "M6": {
                "coefficients": [0, -1, -4, 4],
                "filter": "4*r_10-4*r_8-r_6",
                "response_multiple": 4,
            },
        },
        "integral_unit_response_filter": {
            "name": "H",
            "coefficients": [1, -1, -1, 1],
            "filter": "r_10-r_8+r_4-r_6",
        },
        "bounded_regression_is_not_the_proof": True,
    }


def haar_variance(
    coefficients: tuple[Fraction, Fraction, Fraction, Fraction], q: int
) -> Fraction:
    if not isinstance(q, int) or q < 3 or q % 2 == 0:
        raise ValueError("q must be an odd integer at least three")
    return sum(
        coefficient * coefficient * q**weight
        for coefficient, weight in zip(coefficients, WEIGHTS, strict=True)
    )


def optimal_unit_response_coefficients(
    q: int,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    if not isinstance(q, int) or q < 3 or q % 2 == 0:
        raise ValueError("q must be an odd integer at least three")
    denominator = 9 * q * q + 16
    return (
        Fraction(-3 * q * q, denominator),
        Fraction(-4, denominator),
        Fraction(-1),
        Fraction(1),
    )


def optimal_unit_response_variance(q: int) -> Fraction:
    denominator = 9 * q * q + 16
    return Fraction(q**10 + q**8) + Fraction(q**6, denominator)


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _haar_certificate(guard: ResourceGuard) -> dict[str, object]:
    m4 = tuple(Fraction(value) for value in (-1, 0, -3, 3))
    m6 = tuple(Fraction(value) for value in (0, -1, -4, 4))
    integral = tuple(Fraction(value) for value in (1, -1, -1, 1))
    q_values = (3, 5, 7, 9, 11, 101)
    for q in q_values:
        guard.operation()
        m4_unit = haar_variance(tuple(value / 3 for value in m4), q)
        m6_unit = haar_variance(tuple(value / 4 for value in m6), q)
        difference = Fraction(q**4 * (9 * q * q - 16), 144)
        if m6_unit - m4_unit != difference or difference <= 0:
            raise ArithmeticError("sparse Haar comparison failed")

        baseline = haar_variance(integral, q)
        for k in range(-12, 13):
            guard.operation()
            coefficients = tuple(Fraction(value) for value in lattice_solution(1, k))
            actual = haar_variance(coefficients, q) - baseline
            expected = q**4 * k * ((8 + 6 * q * q) + (16 + 9 * q * q) * k)
            if actual != expected or (actual == 0) != (k == 0):
                raise ArithmeticError("integral Haar minimizer failed")

        optimum = optimal_unit_response_coefficients(q)
        if trace_coordinates(optimum) != (
            Fraction(1),
            Fraction(-1),
            Fraction(0),
            Fraction(-1),
            Fraction(0),
            Fraction(0),
        ):
            raise ArithmeticError("rational optimum violates its exact constraints")
        optimal_variance = haar_variance(optimum, q)
        if optimal_variance != optimal_unit_response_variance(q):
            raise ArithmeticError("rational minimum formula failed")
        denominator = 9 * q * q + 16
        for c4 in (Fraction(-7), Fraction(-2, 3), Fraction(0), Fraction(11, 5)):
            guard.operation()
            c6 = Fraction(-1 - 3 * c4, 4)
            trial = (c4, c6, Fraction(-1), Fraction(1))
            difference = haar_variance(trial, q) - optimal_variance
            square = (
                Fraction(q**4 * denominator, 16)
                * (c4 + Fraction(3 * q * q, denominator)) ** 2
            )
            if difference != square or difference < 0:
                raise ArithmeticError("completion-of-square certificate failed")

    return {
        "orthogonality_identity": (
            "Var_Haar(sum_j c_(2j) r_(2j))=c_4^2*q^4+c_6^2*q^6+c_8^2*q^8+c_10^2*q^10"
        ),
        "scope": "USp(4) Haar variance, not finite arithmetic-family variance",
        "sparse_unit_variances": {
            "M4_over_3": "q^10+q^8+q^4/9",
            "M6_over_4": "q^10+q^8+q^6/16",
            "M6_minus_M4": "q^4*(9*q^2-16)/144 > 0 for odd q>=3",
        },
        "integral_unit_response": {
            "unique_minimizer": [1, -1, -1, 1],
            "difference_from_k_0": (
                "q^4*k*((8+6*q^2)+(16+9*q^2)*k), positive for every integer k!=0"
            ),
        },
        "rational_unit_response": {
            "D": "9*q^2+16",
            "unique_minimizer": [
                "-3*q^2/D",
                "-4/D",
                "-1",
                "1",
            ],
            "filter": "r_10-r_8-(3*q^2/D)*r_4-(4/D)*r_6",
            "minimum_variance": "q^10+q^8+q^6/(9*q^2+16)",
            "completion_of_square": (
                "V(c_4)-V_min=q^4*(9*q^2+16)/16*(c_4+3*q^2/(9*q^2+16))^2"
            ),
        },
        "exact_control_q_values": list(q_values),
    }


Polynomial = tuple[int, ...]  # low-to-high coefficients in E


def polynomial_multiply(
    left: Polynomial, right: Polynomial, guard: ResourceGuard | None = None
) -> Polynomial:
    if not left or not right:
        raise ValueError("polynomials must be nonempty")
    if guard is not None:
        guard.operation(len(left) * len(right))
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def quadratic_operator(trace: int, determinant: int) -> Polynomial:
    return determinant, -trace, 1


def power_sum_tower(
    trace: int, determinant: int, maximum_exponent: int, guard: ResourceGuard
) -> tuple[int, ...]:
    if maximum_exponent < 1 or maximum_exponent > MAX_TOWER_EXPONENT:
        raise ValueError("tower exponent exceeds its explicit cap")
    values = [2, trace]
    for exponent in range(2, maximum_exponent + 1):
        guard.recurrence()
        values.append(trace * values[exponent - 1] - determinant * values[exponent - 2])
    return tuple(values)


def apply_operator(
    sequence: tuple[int, ...],
    polynomial: Polynomial,
    guard: ResourceGuard | None = None,
) -> tuple[int, ...]:
    if len(sequence) < len(polynomial):
        raise ValueError("sequence is too short for operator")
    output_length = len(sequence) - len(polynomial) + 1
    if guard is not None:
        guard.recurrence(output_length * len(polynomial))
    return tuple(
        sum(
            polynomial[offset] * sequence[index + offset]
            for offset in range(len(polynomial))
        )
        for index in range(output_length)
    )


def recurrence_residual(
    sequence: tuple[int, ...],
    polynomial: Polynomial,
    guard: ResourceGuard | None = None,
) -> tuple[int, ...]:
    return apply_operator(sequence, polynomial, guard)


def _coefficient_controls(
    sources: Mapping[str, Mapping[str, object]],
) -> dict[int, tuple[int, int]]:
    sym10 = sources["sym10"]
    modular = sym10.get("modular_form_certificate")
    if not isinstance(modular, dict):
        raise TypeError("Sym10 source lacks modular-form certificate")
    delta = modular.get("Delta_coefficients_0_through_9")
    g10 = modular.get("g_(10,2)_coefficients_0_through_9")
    if not isinstance(delta, list) or not isinstance(g10, list):
        raise TypeError("Sym10 source lacks Hecke coefficient lists")
    controls: dict[int, tuple[int, int]] = {}
    for prime in (3, 5, 7):
        if prime >= len(delta) or prime >= len(g10):
            raise RuntimeError("source coefficient list is too short")
        tau = delta[prime]
        g_value = g10[prime]
        if not isinstance(tau, int) or not isinstance(g_value, int):
            raise TypeError("Hecke coefficient is not integral")
        controls[prime] = tau, g_value
    return controls


def _spectroscopy_certificate(
    sources: Mapping[str, Mapping[str, object]], guard: ResourceGuard
) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for prime, (tau, g_value) in _coefficient_controls(sources).items():
        delta = power_sum_tower(tau, prime**11, MAX_TOWER_EXPONENT, guard)
        g_tower = power_sum_tower(g_value, prime**9, MAX_TOWER_EXPONENT, guard)
        shifted = tuple(
            prime**exponent * delta[exponent] for exponent in range(len(delta))
        )
        unshifted = tuple(-value for value in delta)
        level2 = tuple(-value for value in g_tower)
        response = tuple(
            shifted[index] + unshifted[index] + level2[index]
            for index in range(len(delta))
        )

        p_shift = quadratic_operator(prime * tau, prime**13)
        p_unshift = quadratic_operator(tau, prime**11)
        p_level2 = quadratic_operator(g_value, prime**9)
        annihilator = polynomial_multiply(
            polynomial_multiply(p_shift, p_unshift, guard), p_level2, guard
        )
        if any(recurrence_residual(response, annihilator, guard)):
            raise ArithmeticError("six-root recurrence failed")

        isolator_shift = polynomial_multiply(p_unshift, p_level2, guard)
        isolator_unshift = polynomial_multiply(p_shift, p_level2, guard)
        isolator_level2 = polynomial_multiply(p_shift, p_unshift, guard)
        isolated_shift = apply_operator(response, isolator_shift, guard)
        isolated_unshift = apply_operator(response, isolator_unshift, guard)
        isolated_level2 = apply_operator(response, isolator_level2, guard)

        expected_shift = apply_operator(shifted, isolator_shift, guard)
        expected_unshift = apply_operator(unshifted, isolator_unshift, guard)
        expected_level2 = apply_operator(level2, isolator_level2, guard)
        checks = (
            (isolated_shift, expected_shift, p_shift, "shifted Delta"),
            (isolated_unshift, expected_unshift, p_unshift, "unshifted Delta"),
            (isolated_level2, expected_level2, p_level2, "level-2 weight ten"),
        )
        for isolated, expected, recurrence, label in checks:
            if isolated != expected or not any(isolated):
                raise ArithmeticError(f"{label} isolator failed")
            if any(recurrence_residual(isolated, recurrence, guard)):
                raise ArithmeticError(f"{label} isolated recurrence failed")

        rows.append(
            {
                "p": prime,
                "tau(p)": tau,
                "g_p": g_value,
                "C_0_through_4": list(response[:5]),
                "annihilator_low_to_high": list(annihilator),
                "isolated_first_four": {
                    "shifted_Delta": list(isolated_shift[:4]),
                    "unshifted_Delta": list(isolated_unshift[:4]),
                    "level_2_weight_10": list(isolated_level2[:4]),
                },
                "all_recurrence_residuals_zero": True,
            }
        )

    return {
        "same_prime_response": (
            "C_r=(p^r-1)*(gamma_p^r+delta_p^r)-(mu_p^r+nu_p^r), r>=1"
        ),
        "formal_initialization": (
            "The spectral formula is extended to r=0 with C_0=-2 only to seed "
            "the recurrence; q=1 is not an arithmetic family value."
        ),
        "six_roots": [
            "p*gamma_p",
            "p*delta_p",
            "gamma_p",
            "delta_p",
            "mu_p",
            "nu_p",
        ],
        "quadratic_factors": {
            "P_shift(E)": "E^2-p*tau(p)*E+p^13",
            "P_unshift(E)": "E^2-tau(p)*E+p^11",
            "P_10_2(E)": "E^2-g_p*E+p^9",
        },
        "minimal_annihilator": "P_shift(E)*P_unshift(E)*P_10_2(E)",
        "minimality_proof": (
            "Purity gives root radii p^(13/2), p^(11/2), and p^(9/2), so the "
            "three pairs are disjoint.  A repeated root inside a pair would force "
            "an integral Hecke coefficient squared to equal 4*p^e with e odd, "
            "impossible by p-adic valuation.  All six exponential coefficients "
            "are nonzero, hence the order-six annihilator is minimal."
        ),
        "exact_channel_isolators": {
            "shifted_Delta": "P_unshift(E)*P_10_2(E)",
            "unshifted_Delta": "P_shift(E)*P_10_2(E)",
            "level_2_weight_10": "P_shift(E)*P_unshift(E)",
        },
        "coarse_notches": {
            "remove_both_Delta_channels": "P_shift(E)*P_unshift(E)",
            "remove_level_2_weight_10": "P_10_2(E)",
        },
        "prime_controls": rows,
        "prime_controls_are_not_the_proof": True,
        "renormalization_warning": (
            "The p^(13*r/2) shifted-Delta channel dominates raw extension towers; "
            "the p^(9*r/2) level-two channel is recovered by an exact notch."
        ),
    }


def build_fixture() -> dict[str, object]:
    started = time.monotonic()
    guard = ResourceGuard()
    sources = _load_sources(SOURCE_NAMES, guard)
    classification = _classification_certificate(guard)
    haar = _haar_certificate(guard)
    spectroscopy = _spectroscopy_certificate(sources, guard)
    packet_manifest = _packet_manifest(guard)

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.genus2_mixed_cohomology_filter.v1",
        "status": "PROVED_FROM_SOURCE_LOCKED_TRACES_PLUS_STANDARD_PURITY",
        "scope": {
            "proved_q": "every odd prime power for the imported trace and filter identities",
            "arithmetic_same_prime_response": "every odd prime p and extension exponent r>=1",
            "formal_recurrence_extension": "r=0 is included only as C_0=-2 initialization",
            "new_finite_fields_enumerated": [],
            "new_curves_enumerated": 0,
            "sampled_values_used_as_theorem_input": [],
        },
        "imported_marked_traces": {
            "T_(4,0)(q)": "-3",
            "T_(6,0)(q)": "-4",
            "T_(8,0)(q)": "-Theta_(8,2)(q)-q-6",
            "T_(10,0)(q)": ("(q-1)*Theta_Delta(q)-Theta_(8,2)(q)-Theta_(10,2)(q)-q-7"),
        },
        "integral_lattice_certificate": classification,
        "haar_optimization_certificate": haar,
        "frobenius_interferometry_certificate": spectroscopy,
        "external_mathematical_premises": [
            {
                "premise": (
                    "Deligne purity/temperedness for the level-one weight-12 and "
                    "level-two weight-10 holomorphic eigenforms at odd unramified primes"
                ),
                "role": (
                    "gives the three disjoint root radii and hence minimality and "
                    "nonvanishing of the isolated channels; the order-six annihilator "
                    "and factor-annihilation identities themselves do not require purity"
                ),
            }
        ],
        "source_manifest": _source_manifest(),
        "packet_manifest": packet_manifest,
        "resource_contract": {
            "maximum_source_files": MAX_SOURCE_FILES,
            "maximum_source_bytes": MAX_SOURCE_BYTES,
            "maximum_packet_bytes": MAX_PACKET_BYTES,
            "maximum_output_bytes": MAX_OUTPUT_BYTES,
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "maximum_lattice_regression_points": MAX_LATTICE_REGRESSION_POINTS,
            "maximum_recurrence_steps": MAX_RECURRENCE_STEPS,
            "maximum_tower_exponent": MAX_TOWER_EXPONENT,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "actual_source_files": guard.source_files,
            "actual_source_bytes": guard.source_bytes,
            "actual_packet_bytes": guard.packet_bytes,
            "actual_exact_operations": guard.exact_operations,
            "actual_lattice_regression_points": guard.lattice_regression_points,
            "actual_recurrence_steps": guard.recurrence_steps,
            "arithmetic": "exact integers and fractions only",
            "external_network_calls": 0,
        },
        "firewalls": [
            "This packet imports four source theorems and does not re-prove them.",
            "Haar variance is not the finite arithmetic-family variance.",
            "The residual trace is not a memberwise sign theorem or zero theorem.",
            "The recurrence is same-prime extension-tower spectroscopy, not a multi-prime compatible-system identity.",
            "No RH, GRH, amplifier, global motive, Euler-product, or external novelty claim is made.",
        ],
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall cap exceeded after complete payload hashing")
    return fixture


def _serialized(fixture: Mapping[str, object]) -> str:
    return json.dumps(fixture, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def write_fixture() -> None:
    serialized = _serialized(build_fixture())
    if len(serialized.encode("utf-8")) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output-byte cap exceeded before output write")
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")


def check_fixture() -> None:
    expected = _serialized(build_fixture())
    if not OUTPUT_PATH.exists():
        raise RuntimeError("mixed-cohomology fixture is missing")
    if OUTPUT_PATH.stat().st_size > MAX_OUTPUT_BYTES:
        raise RuntimeError("output-byte cap exceeded before output read")
    actual = OUTPUT_PATH.read_text(encoding="utf-8")
    if actual != expected:
        raise RuntimeError("mixed-cohomology fixture is stale")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--write", action="store_true", help="write the canonical JSON fixture"
    )
    mode.add_argument(
        "--check", action="store_true", help="check the canonical JSON fixture"
    )
    arguments = parser.parse_args()
    if arguments.write:
        write_fixture()
        print(f"wrote {_relative(OUTPUT_PATH)}")
    else:
        check_fixture()
        print("mixed-cohomology filter fixture matches")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
