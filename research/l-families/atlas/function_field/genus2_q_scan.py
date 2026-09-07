#!/usr/bin/env python3
"""Exact lightweight genus-two family scan for q=3,5,7.

For every monic squarefree quintic D over F_q, the scanner computes the first
two L-polynomial coefficients from character sums over F_q and F_(q^2):

    a = sum_x chi(D(x)),
    b = (sum_z chi_2(D(z)) + a^2) / 2.

It then evaluates K=q*a^2-b^2, the numerator of the normalized toy
reciprocal-coefficient Hankel minor.  The family loop never enumerates Euler
coefficients and never approximates a root.  Direct Euler coefficients are
used only for two declared sample controls per field.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import time
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Sequence

import pilot
import genus2_moment_identity as moment_identity


Poly = tuple[int, ...]
Fq2 = tuple[int, int]
FROZEN_Q_VALUES = (3, 5, 7)
DEFAULT_CANDIDATE_CAP = 20_000
MAX_WALL_SECONDS = 8.0
DEFAULT_GUARD_INTERVAL = 256
FORMULA_STATUS = "PROVED_IN_DRAFT_RESEARCH_NOTE"
MEAN_LIMIT_STATUS = "PROVED_FROM_EXACT_FORMULA"
HERE = Path(__file__).resolve().parent
Q3_FIXTURE = HERE / "genus2_f3_quintics.json"
MOMENT_IDENTITY_NOTE = HERE / "GENUS2_MOMENT_IDENTITY.md"
MOMENT_IDENTITY_CERTIFICATE = HERE / "genus2_moment_identity.py"


@dataclass(frozen=True)
class FieldTables:
    q: int
    nonsquare: int
    base_powers: tuple[tuple[int, ...], ...]
    base_character: dict[int, int]
    extension_elements: tuple[Fq2, ...]
    extension_powers: tuple[tuple[Fq2, ...], ...]
    extension_character: dict[Fq2, int]


@dataclass(frozen=True)
class ScanOutput:
    payload: dict[str, object]
    sample_conductors: tuple[Poly, ...]


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _trim(coefficients: Iterable[int], q: int) -> list[int]:
    result = [coefficient % q for coefficient in coefficients]
    while result and result[-1] == 0:
        result.pop()
    return result


def _remainder(dividend: Sequence[int], divisor: Sequence[int], q: int) -> list[int]:
    remainder = _trim(dividend, q)
    normalized_divisor = _trim(divisor, q)
    if not normalized_divisor:
        raise ZeroDivisionError("polynomial remainder modulo zero")
    inverse_lead = pow(normalized_divisor[-1], -1, q)
    while len(remainder) >= len(normalized_divisor):
        coefficient = remainder[-1] * inverse_lead % q
        shift = len(remainder) - len(normalized_divisor)
        for index, value in enumerate(normalized_divisor):
            remainder[shift + index] = (remainder[shift + index] - coefficient * value) % q
        while remainder and remainder[-1] == 0:
            remainder.pop()
    return remainder


def is_squarefree_quintic(conductor: Poly, q: int) -> bool:
    if len(conductor) != 6 or conductor[-1] % q != 1:
        raise ValueError("expected a monic quintic")
    left = list(conductor)
    right = _trim((index * conductor[index] for index in range(1, 6)), q)
    while right:
        left, right = right, _remainder(left, right, q)
    return len(left) == 1


def _smallest_nonsquare(q: int) -> int:
    for candidate in range(2, q):
        if pow(candidate, (q - 1) // 2, q) == q - 1:
            return candidate
    raise ArithmeticError(f"no nonsquare found in F_{q}")


def fq2_multiply(left: Fq2, right: Fq2, q: int, nonsquare: int) -> Fq2:
    """Multiply in F_q[theta]/(theta^2-nonsquare)."""

    return (
        (left[0] * right[0] + nonsquare * left[1] * right[1]) % q,
        (left[0] * right[1] + left[1] * right[0]) % q,
    )


def build_field_tables(q: int) -> FieldTables:
    if q not in FROZEN_Q_VALUES:
        raise ValueError(f"q must be one of the frozen values {FROZEN_Q_VALUES}")
    nonsquare = _smallest_nonsquare(q)
    extension_elements = tuple(itertools.product(range(q), repeat=2))
    extension_squares = {
        fq2_multiply(value, value, q, nonsquare) for value in extension_elements
    }
    extension_character = {
        value: (
            0
            if value == (0, 0)
            else 1
            if value in extension_squares
            else -1
        )
        for value in extension_elements
    }
    base_squares = {value * value % q for value in range(q)}
    base_character = {
        value: 0 if value == 0 else 1 if value in base_squares else -1
        for value in range(q)
    }
    base_powers = tuple(
        tuple(pow(value, exponent, q) for exponent in range(6)) for value in range(q)
    )
    extension_power_rows: list[tuple[Fq2, ...]] = []
    for value in extension_elements:
        powers = [(1, 0)]
        for _ in range(5):
            powers.append(fq2_multiply(powers[-1], value, q, nonsquare))
        extension_power_rows.append(tuple(powers))
    return FieldTables(
        q=q,
        nonsquare=nonsquare,
        base_powers=base_powers,
        base_character=base_character,
        extension_elements=extension_elements,
        extension_powers=tuple(extension_power_rows),
        extension_character=extension_character,
    )


def coefficients_from_character_sums(
    conductor: Poly,
    tables: FieldTables,
) -> tuple[int, int]:
    q = tables.q
    if len(conductor) != 6 or conductor[-1] != 1:
        raise ValueError("expected a monic quintic")
    a = sum(
        tables.base_character[
            sum(coefficient * powers[index] for index, coefficient in enumerate(conductor)) % q
        ]
        for powers in tables.base_powers
    )
    second_character_sum = 0
    for powers in tables.extension_powers:
        value = (
            sum(
                coefficient * powers[index][0]
                for index, coefficient in enumerate(conductor)
            )
            % q,
            sum(
                coefficient * powers[index][1]
                for index, coefficient in enumerate(conductor)
            )
            % q,
        )
        second_character_sum += tables.extension_character[value]
    twice_b = second_character_sum + a * a
    if twice_b % 2:
        raise ArithmeticError("S_2+a^2 is not even")
    return a, twice_b // 2


def candidate_mean_a_squared(q: int) -> Fraction:
    return Fraction(q - 1, 1) + Fraction(q * q + q - 2, q**3)


def candidate_mean_a_fourth(q: int) -> Fraction:
    return (
        Fraction(3 * q * q - 7 * q + 5, 1)
        + Fraction(12, q)
        - Fraction(14, q * q)
        - Fraction(11, q**3)
    )


def candidate_mean_a_squared_b(q: int) -> Fraction:
    return Fraction(
        (q + 1) * (q * q - 2 * q + 3) * (2 * q * q - 2 * q - 1),
        q**3,
    )


def candidate_mean_b(q: int) -> Fraction:
    return Fraction(q - 1) + Fraction(q * q - 1, q**3)


def candidate_mean_b_squared(q: int) -> Fraction:
    return Fraction(2 * q * q - 3 * q + 2, 1) + Fraction(q * q - 3 * q - 1, q**3)


def candidate_mean_k(q: int) -> Fraction:
    return -Fraction((q - 1) ** 2, 1) + Fraction(q + 1, q**3)


def candidate_normalized_mean_k(q: int) -> Fraction:
    return candidate_mean_k(q) / (q * q)


def candidate_low_weight_character_means(q: int) -> dict[str, Fraction]:
    """Exact family means for five nontrivial C2 characters."""

    return {
        "chi_(0,1)": -Fraction(1, q) + Fraction(1, q**2) - Fraction(1, q**4),
        "chi_(2,0)": Fraction(q - 1, q**4),
        "chi_(0,2)": -Fraction(1, q) - Fraction(1, q**5),
        "chi_(2,1)": Fraction(2, q**3) - Fraction(1, q**4) - Fraction(2, q**5),
        "chi_(4,0)": -Fraction(3, q**5),
    }


def _guard(
    *,
    clock: Callable[[], float],
    deadline: float,
    q: int,
    candidates_seen: int,
) -> None:
    if clock() >= deadline:
        raise TimeoutError(
            f"q={q} exact scan exceeded its monotonic wall deadline after "
            f"{candidates_seen} candidates"
        )


def scan_q(
    q: int,
    *,
    candidate_cap: int = DEFAULT_CANDIDATE_CAP,
    wall_limit_seconds: float = MAX_WALL_SECONDS,
    guard_interval: int = DEFAULT_GUARD_INTERVAL,
    clock: Callable[[], float] = time.monotonic,
    deadline: float | None = None,
) -> ScanOutput:
    if q not in FROZEN_Q_VALUES:
        raise ValueError(f"refusing q={q}; frozen exact scan supports only {FROZEN_Q_VALUES}")
    if candidate_cap <= 0 or q**5 > candidate_cap:
        raise ValueError(
            f"q={q} requires {q**5} monic candidates, above candidate cap {candidate_cap}"
        )
    if not 0 < wall_limit_seconds <= MAX_WALL_SECONDS:
        raise ValueError(f"wall limit must lie in (0,{MAX_WALL_SECONDS}]")
    if guard_interval < 1:
        raise ValueError("guard interval must be positive")
    start = clock()
    local_deadline = start + wall_limit_seconds
    if deadline is not None:
        local_deadline = min(local_deadline, deadline)

    tables = build_field_tables(q)
    _guard(clock=clock, deadline=local_deadline, q=q, candidates_seen=0)
    member_count = 0
    sum_a_squared = 0
    sum_a_fourth = 0
    sum_a_squared_b = 0
    sum_b = 0
    sum_b_squared = 0
    sum_k = 0
    histogram: Counter[int] = Counter()
    sign_counts = {"negative": 0, "zero": 0, "positive": 0}
    witnesses: dict[str, dict[str, object] | None] = {
        "negative": None,
        "zero": None,
        "positive": None,
    }
    sample_conductors: list[Poly] = []

    for candidate_index, coefficients in enumerate(
        itertools.product(range(q), repeat=5), start=1
    ):
        if candidate_index % guard_interval == 0:
            _guard(
                clock=clock,
                deadline=local_deadline,
                q=q,
                candidates_seen=candidate_index,
            )
        conductor = tuple(coefficients) + (1,)
        if not is_squarefree_quintic(conductor, q):
            continue
        a, b = coefficients_from_character_sums(conductor, tables)
        k = q * a * a - b * b
        member_count += 1
        sum_a_squared += a * a
        sum_a_fourth += a**4
        sum_a_squared_b += a * a * b
        sum_b += b
        sum_b_squared += b * b
        sum_k += k
        histogram[k] += 1
        sign = "negative" if k < 0 else "positive" if k > 0 else "zero"
        sign_counts[sign] += 1
        conductor_text = pilot.poly_string(conductor)
        witness = {
            "conductor_coefficients_low_to_high": list(conductor),
            "conductor": conductor_text,
            "a": a,
            "b": b,
            "N1": q + 1 + a,
            "N2": q * q + 1 + 2 * b - a * a,
            "K": k,
            "normalized_K": _fraction_pair(Fraction(k, q * q)),
        }
        current = witnesses[sign]
        if current is None or conductor_text < str(current["conductor"]):
            witnesses[sign] = witness
        if len(sample_conductors) < 2:
            sample_conductors.append(conductor)

    _guard(
        clock=clock,
        deadline=local_deadline,
        q=q,
        candidates_seen=q**5,
    )
    expected_members = q**5 - q**4
    if member_count != expected_members:
        raise ArithmeticError(
            f"q={q} squarefree count {member_count} differs from {expected_members}"
        )
    if any(witness is None for witness in witnesses.values()):
        raise ArithmeticError(f"q={q} scan did not produce all three sign witnesses")

    mean_a_squared = Fraction(sum_a_squared, member_count)
    mean_a_fourth = Fraction(sum_a_fourth, member_count)
    mean_a_squared_b = Fraction(sum_a_squared_b, member_count)
    mean_b = Fraction(sum_b, member_count)
    mean_b_squared = Fraction(sum_b_squared, member_count)
    mean_k = Fraction(sum_k, member_count)
    normalized_sum_k = Fraction(sum_k, q * q)
    normalized_mean_k = mean_k / (q * q)
    chi_0_1 = mean_b / q - 1
    chi_2_0 = mean_a_squared / q - 1 - chi_0_1
    chi_0_2 = mean_b_squared / (q * q) - 2 - 2 * chi_0_1 - chi_2_0
    chi_2_1 = mean_a_squared_b / (q * q) - 2 - 3 * chi_0_1 - chi_0_2 - 3 * chi_2_0
    chi_4_0 = (
        mean_a_fourth / (q * q)
        - 3
        - 5 * chi_0_1
        - 6 * chi_2_0
        - 2 * chi_0_2
        - 3 * chi_2_1
    )
    low_weight_character_means = {
        "chi_(0,1)": chi_0_1,
        "chi_(2,0)": chi_2_0,
        "chi_(0,2)": chi_0_2,
        "chi_(2,1)": chi_2_1,
        "chi_(4,0)": chi_4_0,
    }
    if low_weight_character_means != candidate_low_weight_character_means(q):
        raise ArithmeticError(f"q={q} low-weight character profile drifted")
    candidate_values = {
        "mean_a_squared": candidate_mean_a_squared(q),
        "mean_a_fourth": candidate_mean_a_fourth(q),
        "mean_a_squared_b": candidate_mean_a_squared_b(q),
        "mean_b": candidate_mean_b(q),
        "mean_b_squared": candidate_mean_b_squared(q),
        "mean_K": candidate_mean_k(q),
        "normalized_mean_K": candidate_normalized_mean_k(q),
    }
    actual_values = {
        "mean_a_squared": mean_a_squared,
        "mean_a_fourth": mean_a_fourth,
        "mean_a_squared_b": mean_a_squared_b,
        "mean_b": mean_b,
        "mean_b_squared": mean_b_squared,
        "mean_K": mean_k,
        "normalized_mean_K": normalized_mean_k,
    }
    formula_comparison = {
        name: {
            "actual": _fraction_pair(actual_values[name]),
            "candidate": _fraction_pair(candidate_values[name]),
            "matches": actual_values[name] == candidate_values[name],
        }
        for name in actual_values
    }
    if not all(entry["matches"] for entry in formula_comparison.values()):
        raise ArithmeticError(f"q={q} frozen moment totals drifted from the recorded candidate")

    return ScanOutput(
        payload={
            "q": q,
            "nonsquare_for_Fq2": tables.nonsquare,
            "candidate_count": q**5,
            "member_count": member_count,
            "expected_squarefree_count": expected_members,
            "moments": {
                "a_squared": {
                    "sum": sum_a_squared,
                    "mean": _fraction_pair(mean_a_squared),
                },
                "a_fourth": {
                    "sum": sum_a_fourth,
                    "mean": _fraction_pair(mean_a_fourth),
                },
                "a_squared_b": {
                    "sum": sum_a_squared_b,
                    "mean": _fraction_pair(mean_a_squared_b),
                },
                "b": {
                    "sum": sum_b,
                    "mean": _fraction_pair(mean_b),
                },
                "b_squared": {
                    "sum": sum_b_squared,
                    "mean": _fraction_pair(mean_b_squared),
                },
                "K": {"sum": sum_k, "mean": _fraction_pair(mean_k)},
                "normalized_K": {
                    "sum": _fraction_pair(normalized_sum_k),
                    "mean": _fraction_pair(normalized_mean_k),
                },
            },
            "sign_counts": sign_counts,
            "low_weight_character_means": {
                name: _fraction_pair(value)
                for name, value in low_weight_character_means.items()
            },
            "K_histogram": {
                str(key): histogram[key] for key in sorted(histogram)
            },
            "witnesses": {key: value for key, value in witnesses.items()},
            "formula_comparison": formula_comparison,
        },
        sample_conductors=tuple(sample_conductors),
    )


def _sample_cross_checks(q: int, conductors: Sequence[Poly]) -> list[dict[str, object]]:
    tables = build_field_tables(q)
    controls: list[dict[str, object]] = []
    for conductor in conductors:
        a, b = coefficients_from_character_sums(conductor, tables)
        direct_l = pilot.l_coefficients(conductor, q)
        expected_l = (1, a, b, q * a, q * q)
        if direct_l != expected_l:
            raise ArithmeticError(
                f"q={q} point-character coefficients disagree with direct Euler sample {conductor}"
            )
        controls.append(
            {
                "conductor_coefficients_low_to_high": list(conductor),
                "character_sum_coefficients": [a, b],
                "direct_L_coefficients_low_to_high": list(direct_l),
                "matches": True,
            }
        )
    return controls


def _check_q3_fixture(q3_payload: dict[str, object], fixture: dict[str, object]) -> dict[str, object]:
    statistics = fixture["family_statistics"]
    comparisons = {
        "member_count": q3_payload["member_count"] == fixture["family"]["member_count"],
        "K_histogram": q3_payload["K_histogram"] == statistics["toy_minor_numerator_histogram"],
        "sign_counts": q3_payload["sign_counts"]
        == {
            "negative": statistics["negative_member_count"],
            "zero": statistics["zero_member_count"],
            "positive": statistics["positive_member_count"],
        },
        "mean_K": q3_payload["moments"]["K"]["mean"]
        == statistics["toy_minor_numerator_mean"],
        "normalized_mean_K": q3_payload["moments"]["normalized_K"]["mean"]
        == statistics["normalized_toy_minor_mean"],
    }
    if not all(comparisons.values()):
        raise ArithmeticError(f"q=3 scan differs from the existing genus-two fixture: {comparisons}")
    return {
        "fixture": "research/l-families/atlas/function_field/genus2_f3_quintics.json",
        "fixture_canonical_sha256": _canonical_sha256(fixture),
        "comparisons": comparisons,
    }


def build_fixture(
    *,
    q_values: Sequence[int] = FROZEN_Q_VALUES,
    candidate_cap: int = DEFAULT_CANDIDATE_CAP,
    wall_limit_seconds: float = MAX_WALL_SECONDS,
    clock: Callable[[], float] = time.monotonic,
) -> dict[str, object]:
    if tuple(q_values) != FROZEN_Q_VALUES:
        raise ValueError(f"frozen fixture requires exactly q={FROZEN_Q_VALUES}")
    if not 0 < wall_limit_seconds <= MAX_WALL_SECONDS:
        raise ValueError(f"wall limit must lie in (0,{MAX_WALL_SECONDS}]")
    start = clock()
    deadline = start + wall_limit_seconds
    scans: list[ScanOutput] = []
    for q in q_values:
        scans.append(
            scan_q(
                q,
                candidate_cap=candidate_cap,
                wall_limit_seconds=wall_limit_seconds,
                clock=clock,
                deadline=deadline,
            )
        )

    sample_controls: dict[str, object] = {}
    for scan in scans:
        q = int(scan.payload["q"])
        _guard(clock=clock, deadline=deadline, q=q, candidates_seen=q**5)
        sample_controls[str(q)] = _sample_cross_checks(q, scan.sample_conductors)
        _guard(clock=clock, deadline=deadline, q=q, candidates_seen=q**5)

    q3_fixture = json.loads(Q3_FIXTURE.read_text(encoding="utf-8"))
    q3_control = _check_q3_fixture(scans[0].payload, q3_fixture)
    moment_certificate = moment_identity.build_certificate()
    sign_density_certificate = moment_identity.build_sign_density_certificate(
        moment_certificate
    )
    proof_controls: dict[str, object] = {}
    for scan in scans:
        q = int(scan.payload["q"])
        certified = moment_certificate.totals_at(q)
        moments = scan.payload["moments"]
        checks = {
            "member_count": certified["member_count"] == scan.payload["member_count"],
            "sum_a_squared": certified["sum_a_squared"] == moments["a_squared"]["sum"],
            "sum_a_fourth": certified["sum_a_fourth"] == moments["a_fourth"]["sum"],
            "sum_a_squared_b": (
                certified["sum_a_squared_b"] == moments["a_squared_b"]["sum"]
            ),
            "sum_b": certified["sum_b"] == moments["b"]["sum"],
            "sum_b_squared": certified["sum_b_squared"] == moments["b_squared"]["sum"],
            "sum_K": certified["sum_K"] == moments["K"]["sum"],
        }
        if not all(checks.values()):
            raise ArithmeticError(f"q={q} exhaustive scan differs from the all-q proof certificate")
        proof_controls[str(q)] = checks
    source_text = Path(__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
    pilot_text = Path(pilot.__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
    proof_note_text = MOMENT_IDENTITY_NOTE.read_text(encoding="utf-8").replace("\r\n", "\n")
    proof_source_text = MOMENT_IDENTITY_CERTIFICATE.read_text(encoding="utf-8").replace(
        "\r\n", "\n"
    )
    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_q_scan.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.Q3_Q5_Q7.EXACT_SCAN.V1",
        "rigor_level": "RIGOROUS_CERTIFIED",
        "scope": "exhaustive monic squarefree quintics over F_q for exactly q=3,5,7",
        "method": {
            "coefficient_reconstruction": (
                "a=sum_Fq chi(D(x)); b=(sum_Fq2 chi_2(D(x))+a^2)/2; K=q*a^2-b^2"
            ),
            "extension_model": "F_q[theta]/(theta^2-nu) for the recorded smallest nonsquare nu",
            "family_algorithm": "squarefree gcd plus precomputed exact character and power tables",
            "excluded_algorithms": [
                "numerical root finding",
                "per-member Euler coefficient enumeration",
                "floating-point arithmetic",
            ],
        },
        "resource_contract": {
            "frozen_q_values": list(FROZEN_Q_VALUES),
            "candidate_cap": candidate_cap,
            "candidate_cap_scope": "PER_FIELD_Q_SCAN",
            "maximum_wall_seconds": wall_limit_seconds,
            "clock": "time.monotonic",
            "guard_interval_candidates": DEFAULT_GUARD_INTERVAL,
            "larger_q_policy": "refuse q>7 and any q outside the frozen set",
            "runtime_not_in_identity": True,
        },
        "producer": {
            "source": "research/l-families/atlas/function_field/genus2_q_scan.py",
            "source_sha256_lf_normalized": hashlib.sha256(source_text.encode("utf-8")).hexdigest(),
            "shared_arithmetic_source": "research/l-families/atlas/function_field/pilot.py",
            "shared_arithmetic_sha256_lf_normalized": hashlib.sha256(
                pilot_text.encode("utf-8")
            ).hexdigest(),
            "runtime_contract": "Python 3.11+ standard library; exact integer/rational arithmetic",
            "input_provenance": "complete deterministic generation, no external data",
        },
        "families": [scan.payload for scan in scans],
        "sample_euler_cross_checks": sample_controls,
        "q3_existing_fixture_control": q3_control,
        "closed_formula_target": {
            "status": FORMULA_STATUS,
            "not_a_theorem": False,
            "scope": "every odd prime power q",
            "mean_a_squared": "q-1+(q^2+q-2)/q^3",
            "mean_a_fourth": "3*q^2-7*q+5+12/q-14/q^2-11/q^3",
            "mean_a_squared_b": "(q+1)*(q^2-2*q+3)*(2*q^2-2*q-1)/q^3",
            "mean_b": "q-1+(q^2-1)/q^3",
            "mean_b_squared": "2*q^2-3*q+2+(q^2-3*q-1)/q^3",
            "mean_K": "-(q-1)^2+(q+1)/q^3",
            "normalized_mean_K": "-(1-1/q)^2+(q+1)/q^5",
            "low_weight_character_profile": {
                "normalization": (
                    "b_D/q=1+chi_(0,1); a_D^2/q=1+chi_(0,1)+chi_(2,0); "
                    "b_D^2/q^2=2+2*chi_(0,1)+chi_(2,0)+chi_(0,2); "
                    "a_D^2*b_D/q^2=2+3*chi_(0,1)+3*chi_(2,0)+chi_(0,2)+chi_(2,1); "
                    "a_D^4/q^2=3+5*chi_(0,1)+6*chi_(2,0)+2*chi_(0,2)+3*chi_(2,1)+chi_(4,0)"
                ),
                "mean_chi_(0,1)": "-1/q+1/q^2-1/q^4",
                "mean_chi_(2,0)": "1/q^3-1/q^4",
                "mean_chi_(0,2)": "-1/q-1/q^5",
                "mean_chi_(2,1)": "2/q^3-1/q^4-2/q^5",
                "mean_chi_(4,0)": "-3/q^5",
                "status": "PROVED_FROM_EXACT_COEFFICIENT_MOMENTS",
                "scope": "every odd prime power q",
            },
            "proof": {
                "note": "research/l-families/atlas/function_field/GENUS2_MOMENT_IDENTITY.md",
                "note_sha256_lf_normalized": hashlib.sha256(
                    proof_note_text.encode("utf-8")
                ).hexdigest(),
                "certificate": "research/l-families/atlas/function_field/genus2_moment_identity.py",
                "certificate_sha256_lf_normalized": hashlib.sha256(
                    proof_source_text.encode("utf-8")
                ).hexdigest(),
                "symbolic_operations": moment_certificate.operations_used,
                "operation_cap": moment_identity.HARD_OPERATION_LIMIT,
                "scan_regression_controls": proof_controls,
            },
            "evidence": (
                "complete squarefree-Moebius proof and exact Q[q] certificate; q=3,5,7 "
                "enumerations are regression controls, not proof inputs"
            ),
            "smallest_gap": (
                "formal proof-assistant translation or frozen-head review before integration; "
                "no mathematical gap is known in the stated identity"
            ),
        },
        "negative_proportion_corollary": {
            "status": "PROVED_FROM_EXACT_MEAN_AND_USP4_RANGE",
            "scope": "every odd prime power q",
            "statistic": "Z_D=(q*a_D^2-b_D^2)/q^2",
            "range_lower_bound": sign_density_certificate.range_lower_bound,
            "mean_deficit": "A(q)=(1-1/q)^2-(q+1)/q^5=P(q)/q^5",
            "mean_deficit_numerator": "P(q)=q^5-2*q^4+q^3-q-1",
            "certified_moment_bridge": "-sum_D K_D=q*(q-1)*P(q)",
            "mean_deficit_numerator_coefficients_low_to_high": [
                int(coefficient)
                for coefficient in sign_density_certificate.mean_deficit_numerator.coefficients
            ],
            "shifted_positivity_identity": (
                "P(t+3)=t^5+13*t^4+67*t^3+171*t^2+215*t+104 for t=q-3>=0"
            ),
            "shifted_positive_coefficients_low_to_high": [
                int(coefficient)
                for coefficient in sign_density_certificate.shifted_positive_polynomial.coefficients
            ],
            "negative_proportion_lower_bound": (
                "rho_-(q)>=P(q)/(20*q^5)"
            ),
            "frozen_lower_bound_regressions": {
                str(q): _fraction_pair(sign_density_certificate.lower_bound_at(q))
                for q in FROZEN_Q_VALUES
            },
            "liminf_lower_bound": [1, sign_density_certificate.proportion_denominator],
            "memberwise_consequence": (
                "for every odd prime power q, at least one family member has negative Z_D"
            ),
            "scope_boundary": (
                "This is a lower density floor only; it does not determine the sign law, prove "
                "equidistribution, or identify the toy minor with an analytic detector."
            ),
        },
        "usp4_limit_target": {
            "status": MEAN_LIMIT_STATUS,
            "not_a_theorem": False,
            "statement": "the exact normalized family mean tends to -1 as q tends to infinity through odd prime powers",
            "proof": "immediate from -(1-1/q)^2+(q+1)/q^5",
            "scope_boundary": (
                "this proves the first-moment limit only; it does not prove higher-moment "
                "equidistribution or evaluate additional fields"
            ),
        },
        "firewall": (
            "All frozen family totals are exact finite results. The all-odd-prime-power mean formula and its "
            "first-moment limit are proved by the separately source-locked research note and exact "
            "certificate, not inferred from three scans. Higher-moment USp(4) convergence remains "
            "proposed. The negative-sign density floor uses only the exact mean and exact lower "
            "range bound. The toy coefficient minor is not an analytic Pick/Loewner, XD, or HCNC kernel."
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare the exact scan with this JSON fixture")
    parser.add_argument("--write", type=Path, help="write the compact exact scan fixture")
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"genus-two q-scan fixture mismatch: {args.check}")
        print(f"OK: exact genus-two q-scan matches {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"OK: wrote exact genus-two q-scan {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
