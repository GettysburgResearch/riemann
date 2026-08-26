#!/usr/bin/env python3
"""Refusal-first cohomology-conjecture inference for the L-family atlas.

This bounded packet consumes only source-locked q=3,5,7 controls and exact
representation algebra.  It deliberately separates four logically different
operations:

* exact decomposition of a detector into compact-group characters;
* conditional weight and Frobenius-recurrence schemas;
* exact identifiability/ambiguity calculations; and
* external structural identification of a cohomological or automorphic name.

The genus-one tenth moment is a positive control: its Delta identification is
accepted because an exact trace formula and dim S_12=1 are supplied, not
because three prime values resemble Ramanujan tau.  The genus-two channels are
refused names because no comparable stack/local-system comparison or
one-dimensional target-space certificate is presently bound to the packet.

No finite field is enumerated and no modular-form database is queried.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import genus1_cubic_family_laws as genus1
import genus2_high_weight_channel_probe as genus2
import usp4_toy_minor_character_decomposition as c2


HERE = Path(__file__).resolve().parent
GENUS1_FIXTURE = HERE / "genus1_cubic_family_laws.json"
GENUS2_FIXTURE = HERE / "genus2_high_weight_channel_probe.json"
EXPECTED_FIXTURE_SHA256_LF = {
    "genus1_cubic_family_laws.json": (
        "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227"
    ),
    "genus2_high_weight_channel_probe.json": (
        "bfa4aaca81a755ee9d02d2ae3741b0c511f91899a75adf85ada00007612f9541"
    ),
}
FROZEN_Q_VALUES = (3, 5, 7)
MAX_L1_VECTORS = 10_000
MAX_CHARACTER_TERMS = 128
MAX_WALL_SECONDS = 3.0

Polynomial = tuple[int, ...]  # coefficients in increasing exponent order
Observation = tuple[int, int]
Exponent = tuple[int, int]
Laurent = dict[Exponent, int]


CHANNEL_CONFIG = {
    "chi_(0,3)": {
        "highest_weight": (3, 3),
        "local_system_weight": 6,
        "minimal_ambiguity_degree_cap": 4,
        "nominated_polynomial": (-1, -2, 0, 0, 1),
        "nominated_formula": "q^4-2*q-1",
    },
    "chi_(2,2)": {
        "highest_weight": (4, 2),
        "local_system_weight": 6,
        "minimal_ambiguity_degree_cap": 3,
        "nominated_polynomial": (-2, -2, -1, 2),
        "nominated_formula": "2*q^3-q^2-2*q-2",
    },
    "chi_(0,4)": {
        "highest_weight": (4, 4),
        "local_system_weight": 8,
        "minimal_ambiguity_degree_cap": 3,
        "nominated_polynomial": (-1, 0, -2, 0),
        "nominated_formula": "-(2*q^2+1)",
    },
}


def _normalize_json(value: object) -> object:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [_normalize_json(item) for item in value]
    if isinstance(value, dict):
        return {
            unicodedata.normalize("NFC", str(key)): _normalize_json(item)
            for key, item in value.items()
        }
    return value


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        _normalize_json(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _load_locked_fixture(path: Path) -> dict[str, object]:
    expected_file_hash = EXPECTED_FIXTURE_SHA256_LF.get(path.name)
    if expected_file_hash is None:
        raise ValueError(f"no external fixture digest is pinned for {path.name}")
    actual_file_hash = _lf_normalized_sha256(path)
    if actual_file_hash != expected_file_hash:
        raise ArithmeticError(
            f"{path.name} external file hash mismatch: "
            f"{actual_file_hash!r} != {expected_file_hash!r}"
        )
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"{path.name} is not a JSON object")
    claimed = value.get("payload_sha256")
    payload = dict(value)
    payload.pop("payload_sha256", None)
    actual = _canonical_sha256(payload)
    if claimed != actual:
        raise ArithmeticError(
            f"{path.name} payload hash mismatch: {claimed!r} != {actual!r}"
        )
    return value


def _verify_upstream_generator_locks(
    genus1_fixture: Mapping[str, object], genus2_fixture: Mapping[str, object]
) -> dict[str, str]:
    genus1_producer = genus1_fixture.get("producer")
    genus2_locks = genus2_fixture.get("source_locks")
    if not isinstance(genus1_producer, dict) or not isinstance(genus2_locks, dict):
        raise TypeError("upstream fixtures lost generator source locks")
    genus2_probe = genus2_locks.get("probe_generator")
    genus2_c2 = genus2_locks.get("C2_character_generator")
    if not isinstance(genus2_probe, dict) or not isinstance(genus2_c2, dict):
        raise TypeError("genus-two fixture lost probe/C2 source locks")
    actual = {
        "genus1_generator_sha256_lf": _lf_normalized_sha256(Path(genus1.__file__)),
        "genus2_generator_sha256_lf": _lf_normalized_sha256(Path(genus2.__file__)),
        "c2_generator_sha256_lf": _lf_normalized_sha256(Path(c2.__file__)),
    }
    expected = {
        "genus1_generator_sha256_lf": genus1_producer.get(
            "source_sha256_lf_normalized"
        ),
        "genus2_generator_sha256_lf": genus2_probe.get("sha256_lf_normalized"),
        "c2_generator_sha256_lf": genus2_c2.get("sha256_lf_normalized"),
    }
    if actual != expected:
        raise ArithmeticError(
            f"upstream generator source-lock mismatch: actual={actual}, expected={expected}"
        )
    return actual


def _fraction(pair: Sequence[int]) -> Fraction:
    if len(pair) != 2:
        raise ValueError("fraction pair must have length two")
    return Fraction(int(pair[0]), int(pair[1]))


def evaluate_polynomial(coefficients: Sequence[int], q: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = value * q + int(coefficient)
    return value


def _trim_polynomial(coefficients: Sequence[int]) -> Polynomial:
    result = list(map(int, coefficients))
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def multiply_polynomials(left: Sequence[int], right: Sequence[int]) -> Polynomial:
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += int(left_value) * int(right_value)
    return _trim_polynomial(result)


def vanishing_polynomial(points: Sequence[int]) -> Polynomial:
    result: Polynomial = (1,)
    for point in points:
        result = multiply_polynomials(result, (-int(point), 1))
    return result


def _rref_solve_square(matrix: Sequence[Sequence[int]], rhs: Sequence[int]) -> list[Fraction]:
    size = len(matrix)
    if size == 0 or len(rhs) != size or any(len(row) != size for row in matrix):
        raise ValueError("expected a nonempty square system")
    augmented = [
        [Fraction(value) for value in row] + [Fraction(rhs[index])]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column]),
            None,
        )
        if pivot is None:
            raise ArithmeticError("singular interpolation system")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [value / divisor for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            multiple = augmented[row][column]
            if multiple:
                augmented[row] = [
                    augmented[row][index] - multiple * augmented[column][index]
                    for index in range(size + 1)
                ]
    return [augmented[index][-1] for index in range(size)]


def interpolate_quadratic(observations: Sequence[Observation]) -> Polynomial:
    if len(observations) != 3 or len({q for q, _ in observations}) != 3:
        raise ValueError("exactly three observations at distinct q are required")
    matrix = [[1, q, q * q] for q, _ in observations]
    solution = _rref_solve_square(matrix, [value for _, value in observations])
    if any(value.denominator != 1 for value in solution):
        raise ArithmeticError("quadratic interpolant is not integral")
    return tuple(int(value) for value in solution)


def polynomial_divmod_monic(
    numerator: Sequence[int], denominator: Sequence[int]
) -> tuple[Polynomial, Polynomial]:
    numerator_work = list(_trim_polynomial(numerator))
    denominator_clean = _trim_polynomial(denominator)
    if denominator_clean[-1] != 1:
        raise ValueError("denominator must be monic")
    if len(numerator_work) < len(denominator_clean):
        return (0,), tuple(numerator_work)
    quotient = [0] * (len(numerator_work) - len(denominator_clean) + 1)
    while len(numerator_work) >= len(denominator_clean):
        shift = len(numerator_work) - len(denominator_clean)
        leading = numerator_work[-1]
        quotient[shift] = leading
        for index, coefficient in enumerate(denominator_clean):
            numerator_work[index + shift] -= leading * coefficient
        while len(numerator_work) > 1 and numerator_work[-1] == 0:
            numerator_work.pop()
    return _trim_polynomial(quotient), _trim_polynomial(numerator_work)


def _l1_vectors(dimension: int, radius: int) -> Iterable[Polynomial]:
    if dimension <= 0 or radius < 0:
        raise ValueError("invalid lattice-ball parameters")

    def visit(prefix: tuple[int, ...], remaining_dimension: int, remaining: int):
        if remaining_dimension == 1:
            for value in range(-remaining, remaining + 1):
                yield prefix + (value,)
            return
        for value in range(-remaining, remaining + 1):
            yield from visit(
                prefix + (value,), remaining_dimension - 1, remaining - abs(value)
            )

    yield from visit((), dimension, radius)


def _minimum_support_solutions(
    observations: Sequence[Observation], degree_cap: int
) -> tuple[int, list[Polynomial]]:
    """Find every minimum-support integral continuation.

    The integral quadratic interpolant guarantees a solution with support at
    most three.  It is therefore enough to inspect all one-, two-, and
    three-column generalized Vandermonde systems exactly.
    """

    for support_size in range(1, min(3, degree_cap + 1) + 1):
        solutions: list[Polynomial] = []
        for exponents in combinations(range(degree_cap + 1), support_size):
            matrix = [
                [q**exponent for exponent in exponents]
                for q, _ in observations[:support_size]
            ]
            rhs = [value for _, value in observations[:support_size]]
            try:
                coefficients = _rref_solve_square(matrix, rhs)
            except ArithmeticError:
                continue
            if any(value.denominator != 1 or value == 0 for value in coefficients):
                continue
            full = [0] * (degree_cap + 1)
            for exponent, coefficient in zip(exponents, coefficients):
                full[exponent] = int(coefficient)
            if all(
                evaluate_polynomial(full, q) == value
                for q, value in observations
            ):
                solutions.append(tuple(full))
        if solutions:
            return support_size, sorted(set(solutions))
    raise ArithmeticError("integral quadratic interpolant failed support search")


def ambiguity_certificate(
    observations: Sequence[Observation],
    degree_cap: int,
    nominated: Sequence[int],
) -> dict[str, object]:
    """Return the complete integer-polynomial ambiguity lattice.

    For three sample points, all integral polynomials of degree at most D that
    agree with an integral quadratic interpolant P0 are

        P0 + (X-q1)(X-q2)(X-q3) Q,  Q in Z[X], deg Q <= D-3.

    Monicity of the vanishing polynomial makes this an equality over Z[X],
    not merely over Q[X].
    """

    observations = tuple((int(q), int(value)) for q, value in observations)
    if degree_cap < 3:
        raise ValueError("ambiguity certificate requires degree cap at least three")
    nominated = tuple(map(int, nominated))
    if len(nominated) > degree_cap + 1:
        raise ValueError("nominated polynomial exceeds degree cap")
    nominated = nominated + (0,) * (degree_cap + 1 - len(nominated))
    if any(evaluate_polynomial(nominated, q) != value for q, value in observations):
        raise ArithmeticError("nominated polynomial misses an observation")

    base = interpolate_quadratic(observations)
    base_padded = base + (0,) * (degree_cap + 1 - len(base))
    vanisher = vanishing_polynomial([q for q, _ in observations])
    difference = tuple(
        nominated[index] - base_padded[index] for index in range(degree_cap + 1)
    )
    quotient, remainder = polynomial_divmod_monic(difference, vanisher)
    if remainder != (0,):
        raise ArithmeticError("nominated continuation escaped ambiguity lattice")

    lattice_basis = []
    for shift in range(degree_cap - 2):
        row = (0,) * shift + vanisher
        row += (0,) * (degree_cap + 1 - len(row))
        lattice_basis.append(row)
    quotient_padded = quotient + (0,) * (len(lattice_basis) - len(quotient))

    nominated_l1 = sum(abs(value) for value in nominated)
    minimizers: list[Polynomial] = []
    examined = 0
    for candidate in _l1_vectors(degree_cap + 1, nominated_l1):
        examined += 1
        if examined > MAX_L1_VECTORS:
            raise RuntimeError("L1 lattice-ball cap exceeded")
        if all(
            evaluate_polynomial(candidate, q) == value
            for q, value in observations
        ):
            minimizers.append(candidate)
    if not minimizers:
        raise ArithmeticError("nominated L1 ball unexpectedly contains no continuation")
    minimum_l1 = min(sum(abs(value) for value in row) for row in minimizers)
    exact_minimizers = [
        row for row in minimizers if sum(abs(value) for value in row) == minimum_l1
    ]
    if tuple(nominated) not in exact_minimizers:
        raise ArithmeticError("nominated continuation is not L1-minimal")
    minimum_support, support_solutions = _minimum_support_solutions(
        observations, degree_cap
    )
    nominated_support = sum(value != 0 for value in nominated)

    return {
        "status": "EXACT_AFFINE_LATTICE_AND_BOUNDED_NORM_CERTIFICATE",
        "observations": [
            {"q": q, "normalized_trace": value} for q, value in observations
        ],
        "degree_cap": degree_cap,
        "base_quadratic_coefficients_low_to_high": list(base_padded),
        "vanishing_polynomial_coefficients_low_to_high": list(vanisher),
        "ambiguity_rank": len(lattice_basis),
        "complete_integer_ambiguity_lattice": (
            "P=P0+V*Q with Q in Z[X] and deg(Q)<=degree_cap-3"
        ),
        "lattice_basis_coefficients_low_to_high": [list(row) for row in lattice_basis],
        "nominated_coefficients_low_to_high": list(nominated),
        "nominated_lattice_coordinates_low_to_high": list(quotient_padded),
        "l1_search_vectors_examined": examined,
        "minimum_l1_norm": minimum_l1,
        "minimum_l1_minimizers": [list(row) for row in exact_minimizers],
        "nominated_is_unique_l1_minimizer": exact_minimizers == [tuple(nominated)],
        "minimum_monomial_support": minimum_support,
        "minimum_support_solutions": [list(row) for row in support_solutions],
        "nominated_monomial_support": nominated_support,
        "nominated_is_support_minimal": nominated_support == minimum_support,
        "nominated_is_unique_support_minimizer": (
            support_solutions == [tuple(nominated)]
        ),
        "logical_force": (
            "coefficient L1 norm selects a canonical candidate inside this degree "
            "envelope; monomial support is recorded separately; the three "
            "observations do not prove that candidate"
        ),
    }


def _invariant_polynomial_from_fixture(terms: Sequence[Mapping[str, object]]) -> dict[tuple[int, int], int]:
    result: dict[tuple[int, int], int] = {}
    for row in terms:
        monomial = (int(row["trace_power"]), int(row["exterior_square_power"]))
        result[monomial] = result.get(monomial, 0) + int(row["coefficient"])
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def _laurent_power(value: Mapping[Exponent, int], exponent: int, guard: c2.ResourceGuard) -> Laurent:
    if not 0 <= exponent <= 8:
        raise ValueError("character exponent must lie in [0,8]")
    result: Laurent = {(0, 0): 1}
    for _ in range(exponent):
        result = c2.multiply(result, value, guard)
    return result


def expand_invariant_polynomial(
    polynomial: Mapping[tuple[int, int], int], guard: c2.ResourceGuard
) -> Laurent:
    trace = c2.standard_trace_character()
    exterior = c2.standard_exterior_square_character()
    result: Laurent = {}
    for (trace_power, exterior_power), coefficient in sorted(polynomial.items()):
        term = c2.multiply(
            _laurent_power(trace, trace_power, guard),
            _laurent_power(exterior, exterior_power, guard),
            guard,
        )
        result = c2.add_scaled(result, term, coefficient, guard)
    return {weight: coefficient for weight, coefficient in result.items() if coefficient}


def decompose_virtual_character(
    polynomial: Mapping[Exponent, int], engine: c2.C2CharacterEngine
) -> dict[Exponent, int]:
    """Exact C2 highest-weight subtraction allowing virtual coefficients."""

    residual = dict(polynomial)
    decomposition: dict[Exponent, int] = {}
    while residual:
        dominant = [
            weight
            for weight, coefficient in residual.items()
            if coefficient and weight[0] >= weight[1] >= 0
        ]
        if not dominant:
            raise ArithmeticError("virtual-character residual has no dominant weight")
        highest = max(dominant)
        coefficient = residual[highest]
        decomposition[highest] = decomposition.get(highest, 0) + coefficient
        if len(decomposition) > MAX_CHARACTER_TERMS:
            raise RuntimeError("virtual-character decomposition cap exceeded")
        residual = c2.add_scaled(
            residual, engine.character(highest), -coefficient, engine.guard
        )
    return {weight: coefficient for weight, coefficient in decomposition.items() if coefficient}


def conditional_weight_envelope(
    highest_weight: Sequence[int], geometric_dimension: int
) -> dict[str, object]:
    highest = tuple(map(int, highest_weight))
    if len(highest) != 2 or highest[0] < highest[1] or highest[1] < 0:
        raise ValueError("invalid C2 highest weight")
    if geometric_dimension < 0:
        raise ValueError("geometric dimension must be nonnegative")
    local_system_weight = sum(highest)
    return {
        "status": "CONDITIONAL_WEIGHT_UPPER_BOUNDS_NOT_A_DECOMPOSITION",
        "highest_weight_e_basis": list(highest),
        "local_system_weight": local_system_weight,
        "condition": (
            "if the monic-quintic quotient is identified with the intended smooth "
            "marked stack and the associated local system is pure of this weight"
        ),
        "compact_support_degree_upper_weight_bounds": [
            {"cohomological_degree": degree, "weight_at_most": local_system_weight + degree}
            for degree in range(2 * geometric_dimension + 1)
        ],
        "warning": (
            "upper bounds do not determine which degrees occur, their multiplicities, "
            "Tate/endoscopic/cuspidal splitting, or a named eigenpacket"
        ),
    }


def rank_two_recurrence_audit(
    characteristic: int,
    determinant_exponent: int | None,
    traces_by_extension_degree: Mapping[int, int],
) -> dict[str, object]:
    """Audit s_r=A*s_(r-1)-p^w*s_(r-2), with s_0=2.

    Three consecutive extension degrees are required.  Prime values at three
    different characteristics are never treated as recurrence evidence.
    """

    if characteristic <= 1 or (
        determinant_exponent is not None and determinant_exponent < 0
    ):
        raise ValueError("invalid recurrence parameters")
    traces = {int(degree): int(value) for degree, value in traces_by_extension_degree.items()}
    missing = [degree for degree in (1, 2, 3) if degree not in traces]
    if missing:
        return {
            "status": "INSUFFICIENT_SAME_CHARACTERISTIC_EXTENSION_DATA",
            "characteristic": characteristic,
            "determinant_exponent": determinant_exponent,
            "determinant_status": (
                "SPECIFIED" if determinant_exponent is not None else "NOT_INFERRED"
            ),
            "available_extension_degrees": sorted(traces),
            "missing_extension_degrees": missing,
            "warning": "cross-prime samples cannot test a Frobenius-power recurrence",
        }
    if determinant_exponent is None:
        return {
            "status": "INSUFFICIENT_DETERMINANT_WEIGHT_SPECIFICATION",
            "characteristic": characteristic,
            "determinant_exponent": None,
            "determinant_status": "NOT_INFERRED",
            "available_extension_degrees": sorted(traces),
            "warning": (
                "a local-system weight upper bound does not identify the weight or "
                "determinant of a pure rank-two cohomological summand"
            ),
        }
    determinant = characteristic**determinant_exponent
    first = traces[1]
    expected_second = first * first - 2 * determinant
    expected_third = first * traces[2] - determinant * first
    matches = traces[2] == expected_second and traces[3] == expected_third
    return {
        "status": "EXACT_RECURRENCE_MATCH" if matches else "EXACT_RECURRENCE_REJECTION",
        "characteristic": characteristic,
        "determinant_exponent": determinant_exponent,
        "traces_by_extension_degree": {str(key): traces[key] for key in sorted(traces)},
        "expected_degree_2_trace": expected_second,
        "expected_degree_3_trace": expected_third,
        "matches": matches,
    }


def identification_decision(
    *,
    exact_character_isolation: bool,
    exact_family_trace_identity: bool,
    exact_geometric_adapter: bool,
    target_space_dimension: int | None,
    normalized_generator_is_unique: bool,
    proposed_name: str,
) -> dict[str, object]:
    requirements = {
        "exact_character_isolation": exact_character_isolation,
        "exact_family_trace_identity": exact_family_trace_identity,
        "exact_geometric_adapter": exact_geometric_adapter,
        "target_space_dimension_is_one": target_space_dimension == 1,
        "normalized_generator_is_unique": normalized_generator_is_unique,
    }
    missing = [name for name, satisfied in requirements.items() if not satisfied]
    if missing:
        return {
            "status": "REFUSED_UNSUPPORTED_COHOMOLOGY_IDENTIFICATION",
            "proposed_name": proposed_name,
            "requirements": requirements,
            "missing_requirements": missing,
            "reason": "finite-value resemblance is not a structural identification",
        }
    return {
        "status": "ACCEPTED_FROM_EXACT_STRUCTURE_NOT_PATTERN_MATCHING",
        "proposed_name": proposed_name,
        "requirements": requirements,
        "missing_requirements": [],
    }


def _genus1_positive_control(fixture: Mapping[str, object]) -> dict[str, object]:
    rows = fixture.get("finite_regressions")
    if not isinstance(rows, list):
        raise TypeError("genus-one fixture lost finite regressions")
    by_q = {int(row["q"]): row for row in rows}
    if not set(FROZEN_Q_VALUES).issubset(by_q):
        raise ValueError("genus-one fixture lost q=3,5,7")

    decomposition = genus1.symbolic_even_moment(5)
    terms = decomposition["character_terms"]
    if not isinstance(terms, list):
        raise TypeError("genus-one character terms are malformed")
    coefficients = {int(row["character_index"]): int(row["coefficient"]) for row in terms}
    if coefficients != {1: 90, 2: 75, 3: 35, 4: 9, 5: 1}:
        raise ArithmeticError("tenth-moment SU2 decomposition drifted")

    isolated_rows = []
    for q in FROZEN_Q_VALUES:
        moment_rows = by_q[q].get("stack_and_coarse_even_moments")
        if not isinstance(moment_rows, list):
            raise TypeError(f"q={q} genus-one moment rows are malformed")
        moment10 = next(
            int(row["elliptic_stack_weighted_sum"])
            for row in moment_rows
            if int(row["degree"]) == 10
        )
        known = genus1.catalan(5) * q**6
        for index in range(1, 5):
            known -= coefficients[index] * q ** (5 - index)
        sym10_stack_sum = moment10 - known
        theta12 = -1 - sym10_stack_sum
        if theta12 != genus1.ramanujan_tau(q):
            raise ArithmeticError(f"q={q} positive-control trace isolation failed")
        isolated_rows.append(
            {
                "q": q,
                "source_locked_tenth_stack_moment": moment10,
                "isolated_sym10_stack_sum": sym10_stack_sum,
                "boundary_removed_theta12": theta12,
            }
        )

    symbolic_traces = {
        degree: genus1.delta_frobenius_trace(3**degree) for degree in (1, 2, 3)
    }
    recurrence = rank_two_recurrence_audit(3, 11, symbolic_traces)
    if recurrence["status"] != "EXACT_RECURRENCE_MATCH":
        raise ArithmeticError("Delta symbolic recurrence positive control failed")

    return {
        "status": "POSITIVE_CONTROL_PASSED",
        "raw_detector": "a_E^10",
        "exact_su2_character_decomposition": decomposition,
        "isolated_source_locked_rows": isolated_rows,
        "weight_inference": {
            "sym10_local_system_to_modular_weight": "10+2=12",
            "target_space": "S_12(SL(2,Z))",
            "exact_dimension": genus1.cusp_dimension_level_one(12),
            "rank_two_frobenius_weight": 11,
        },
        "symbolic_recurrence_control": {
            "origin": (
                "theorem-supplied Delta recurrence evaluated symbolically; not new "
                "finite-field family data"
            ),
            "audit": recurrence,
        },
        "identification": identification_decision(
            exact_character_isolation=True,
            exact_family_trace_identity=True,
            exact_geometric_adapter=True,
            target_space_dimension=1,
            normalized_generator_is_unique=True,
            proposed_name="Ramanujan Delta / the unique normalized generator of S_12",
        ),
        "methodological_point": (
            "the name is forced by the exact trace formula and one-dimensional target "
            "space; q=3,5,7 values alone would not justify it"
        ),
    }


def _genus2_candidate_packet(fixture: Mapping[str, object]) -> dict[str, object]:
    controls = fixture.get("finite_aggregate_controls")
    character_certificate = fixture.get("character_certificate")
    if not isinstance(controls, list) or not isinstance(character_certificate, dict):
        raise TypeError("genus-two fixture lost required blocks")
    channels = character_certificate.get("channels")
    if not isinstance(channels, dict):
        raise TypeError("genus-two fixture lost character channels")
    by_q = {int(row["q"]): row for row in controls}
    if tuple(sorted(by_q)) != FROZEN_Q_VALUES:
        raise ValueError("genus-two fixture must bind exactly q=3,5,7")

    guard = c2.ResourceGuard()
    engine = c2.C2CharacterEngine(guard)
    output_channels: dict[str, object] = {}
    for name, config in CHANNEL_CONFIG.items():
        source_channel = channels.get(name)
        if not isinstance(source_channel, dict):
            raise TypeError(f"missing source channel {name}")
        terms = source_channel.get("invariant_polynomial_terms")
        if not isinstance(terms, list):
            raise TypeError(f"malformed source terms for {name}")
        invariant = _invariant_polynomial_from_fixture(terms)
        laurent = expand_invariant_polynomial(invariant, guard)
        decomposition = decompose_virtual_character(laurent, engine)
        expected_highest = tuple(config["highest_weight"])
        if decomposition != {expected_highest: 1}:
            raise ArithmeticError(f"C2 decomposition drifted for {name}: {decomposition}")

        weight = int(config["local_system_weight"])
        observations = []
        recurrence_audits = []
        for q in FROZEN_Q_VALUES:
            means = by_q[q].get("channel_means")
            if not isinstance(means, dict):
                raise TypeError(f"q={q} channel means are malformed")
            member_count = int(by_q[q]["member_count"])
            if member_count != q**4 * (q - 1):
                raise ArithmeticError(f"q={q} genus-two family size drifted")
            mean = _fraction(means[name])
            trace_sum = mean * member_count
            normalized_trace = trace_sum * Fraction(q ** (weight // 2), q * (q - 1))
            if normalized_trace.denominator != 1:
                raise ArithmeticError(f"q={q} normalized trace is nonintegral for {name}")
            observations.append((q, int(normalized_trace)))
            recurrence_audits.append(
                rank_two_recurrence_audit(q, None, {1: int(normalized_trace)})
            )

        ambiguity = ambiguity_certificate(
            observations,
            int(config["minimal_ambiguity_degree_cap"]),
            config["nominated_polynomial"],
        )
        output_channels[name] = {
            "machine_candidate_schema": {
                "status": "CONJECTURE_UNIQUE_BY_L1_NOT_IDENTIFIED_COHOMOLOGICALLY",
                "normalized_trace_formula": config["nominated_formula"],
                "allowed_claim": (
                    "unique minimum-L1 integral continuation in the declared degree "
                    "cap, matching exact q=3,5,7 controls"
                ),
                "forbidden_promotions": [
                    "all-q theorem",
                    "Tate-only decomposition",
                    "named eigenform or cohomology class",
                    "Frobenius recurrence",
                ],
                "proof_obligations": [
                    "exact marked-stack/measure adapter",
                    "all-q arithmetic or cohomological trace calculation",
                    "same-characteristic extension data for any recurrence claim",
                    "theorem-backed target-space multiplicities before naming a packet",
                ],
            },
            "exact_detector_decomposition": {
                "status": "EXACT_IRREDUCIBLE_C2_CHARACTER",
                "highest_weight_e_basis": list(expected_highest),
                "multiplicity": 1,
                "invariant_polynomial_terms": terms,
                "laurent_support_size": len(laurent),
            },
            "conditional_weight_envelope": conditional_weight_envelope(
                expected_highest, geometric_dimension=3
            ),
            "conditional_rank_two_recurrence_schema": {
                "status": "FORMAL_SCHEMA_WITH_UNDETERMINED_DETERMINANT",
                "template": "s_r=A_p*s_(r-1)-delta_p*s_(r-2), s_0=2",
                "warning": (
                    "neither rank two, purity weight, determinant exponent, nor "
                    "determinant phase follows from the C2 character identity"
                ),
            },
            "normalized_trace_definition": (
                "T_lambda(q)=q^(w/2)/(q(q-1))*sum_D chi_lambda(D)"
            ),
            "ambiguity": ambiguity,
            "recurrence_audits": recurrence_audits,
            "identification": identification_decision(
                exact_character_isolation=True,
                exact_family_trace_identity=False,
                exact_geometric_adapter=False,
                target_space_dimension=None,
                normalized_generator_is_unique=False,
                proposed_name="unspecified genus-two cohomological/eigenform packet",
            ),
        }

    return {
        "status": "CERTIFIED_CANDIDATE_SCHEMA_WITH_IDENTIFICATION_REFUSAL",
        "channels": output_channels,
        "character_resource_counts": dict(guard.counts),
        "joint_no_go": {
            "status": "EXACT_IDENTIFIABILITY_NO_GO",
            "statement": (
                "At q=3,5,7, each integer Tate-polynomial continuation remains "
                "unchanged after adding V(q)Q(q), V=(q-3)(q-5)(q-7). Hence any "
                "degree envelope allowing a cubic term has positive ambiguity rank. "
                "Moreover, three distinct primes provide no Frobenius-power recurrence "
                "test, which requires repeated extensions of one characteristic."
            ),
            "what_remains_certified": (
                "inside the stated minimal degree envelopes, each nominated "
                "small-coefficient formula is the unique minimum-L1 integral "
                "continuation; monomial-support minimality is a separate result"
            ),
        },
    }


def build_certificate() -> dict[str, object]:
    started = time.perf_counter()
    genus1_fixture = _load_locked_fixture(GENUS1_FIXTURE)
    genus2_fixture = _load_locked_fixture(GENUS2_FIXTURE)
    verified_generator_hashes = _verify_upstream_generator_locks(
        genus1_fixture, genus2_fixture
    )
    positive_control = _genus1_positive_control(genus1_fixture)
    genus2_packet = _genus2_candidate_packet(genus2_fixture)
    elapsed = time.perf_counter() - started
    if elapsed > MAX_WALL_SECONDS:
        raise RuntimeError(
            f"guarded inference exceeded {MAX_WALL_SECONDS:g} seconds ({elapsed:.3f}s)"
        )
    return {
        "schema": "riemann.function_field.guarded_cohomology_inference.v1",
        "status": "EXACT_PROTOCOL_AND_NO_GO_WITH_GUARDED_CANDIDATES",
        "scope": (
            "source-locked q=3,5,7 data, exact SU2/C2 character algebra, and "
            "symbolic recurrence constraints only; no field enumeration or database"
        ),
        "protocol": {
            "stages": [
                "exact compact-group character decomposition",
                "conditional weight envelope with hypotheses displayed",
                "complete finite-data ambiguity lattice",
                "same-characteristic recurrence audit",
                "structural identification gate",
            ],
            "hard_refusal_rule": (
                "a named cohomology/eigenform identification requires exact character "
                "isolation, an exact family trace identity, an exact geometric adapter, "
                "a one-dimensional target, and a unique normalization"
            ),
        },
        "source_locks": {
            "genus1_fixture": {
                "path": str(GENUS1_FIXTURE.relative_to(HERE.parents[3])).replace("\\", "/"),
                "file_sha256_lf": _lf_normalized_sha256(GENUS1_FIXTURE),
                "payload_sha256": genus1_fixture["payload_sha256"],
                "canonical_sha256": _canonical_sha256(genus1_fixture),
            },
            "genus2_fixture": {
                "path": str(GENUS2_FIXTURE.relative_to(HERE.parents[3])).replace("\\", "/"),
                "file_sha256_lf": _lf_normalized_sha256(GENUS2_FIXTURE),
                "payload_sha256": genus2_fixture["payload_sha256"],
                "canonical_sha256": _canonical_sha256(genus2_fixture),
            },
            **verified_generator_hashes,
        },
        "genus1_positive_control": positive_control,
        "genus2_guarded_candidates": genus2_packet,
        "resource_contract": {
            "finite_fields_enumerated": [],
            "database_queries": 0,
            "frozen_q_values": list(FROZEN_Q_VALUES),
            "max_l1_vectors_per_channel": MAX_L1_VECTORS,
            "max_character_terms": MAX_CHARACTER_TERMS,
            "max_wall_seconds": MAX_WALL_SECONDS,
        },
        "firewalls": [
            "a unique minimum-L1 continuation is not an all-q theorem",
            "conditional weight bounds are not a cohomological decomposition",
            "cross-prime samples are not Frobenius-power recurrence evidence",
            "a character identity does not identify a moduli-stack local system",
            "no Siegel or elliptic eigenform is named from finite-value resemblance",
            "no number-field, RH, or GRH conclusion is drawn",
        ],
    }


def _summary(certificate: Mapping[str, object]) -> str:
    packet = certificate["genus2_guarded_candidates"]
    channels = packet["channels"]
    rows = []
    for name in CHANNEL_CONFIG:
        ambiguity = channels[name]["ambiguity"]
        rows.append(
            f"{name}: ambiguity rank {ambiguity['ambiguity_rank']}, "
            f"unique L1 minimizer={ambiguity['nominated_is_unique_l1_minimizer']}"
        )
    return "\n".join(
        [
            str(certificate["status"]),
            "genus-one positive control: PASSED",
            *rows,
            "genus-two cohomology/eigenform naming: REFUSED",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print the full certificate")
    args = parser.parse_args()
    certificate = build_certificate()
    if args.json:
        print(json.dumps(certificate, indent=2, sort_keys=True))
    else:
        print(_summary(certificate))


if __name__ == "__main__":
    main()
