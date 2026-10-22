#!/usr/bin/env python3
"""Exact bounded replay of the integral split locus in frozen genus-two histograms.

The sole arithmetic data source is the complete joint ``(a_D,b_D)`` member
histogram in ``balanced_control_family_scan.json``.  No finite field, curve, or
family member is enumerated.  For

    P(T) = 1 + a*T + b*T^2 + q*a*T^3 + q^2*T^4

the script classifies the factorization over Z through

    Delta = a^2 - 4*b + 8*q.

It then performs exact, resource-guarded comparisons with the balanced B
control, the toy-minor F control, the complete two-coordinate Frobenius echo,
and bounded power-to-identity certificates for cyclotomic normalized spectra.
Every numerical result is an integer or Fraction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUT_PATH = HERE / "balanced_control_family_scan.json"
INPUT_PRODUCER_PATH = HERE / "balanced_control_family_scan.py"
OUTPUT_PATH = HERE / "genus2_endoscopic_split_locus.json"
NOTE_PATH = HERE / "GENUS2_ENDOSCOPIC_SPLIT_LOCUS.md"
TEST_PATH = ROOT / "tests" / "test_genus2_endoscopic_split_locus.py"

FROZEN_Q_VALUES = (3, 5, 7)
CLASS_ORDER = (
    "split_repeated",
    "split_distinct",
    "no_integral_q_elliptic_form_factorization",
)
SPLIT_CLASSES = frozenset({"split_repeated", "split_distinct"})
MAX_ECHO_POWER = 8
MAX_CYCLOTOMIC_CERTIFICATE_POWER = 24
ABSOLUTE_MOMENT_ORDERS = (2, 4, 6, 8, 10, 12)
TRANSFORM_WORK_UNIT_CAP_EXCLUSIVE = 20_000

# This pins the exact upstream payload rather than accepting an arbitrary
# self-consistent replacement with the same schema.
EXPECTED_INPUT_PAYLOAD_SHA256 = (
    "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c"
)
EXPECTED_MEMBER_LEDGER_SHA256 = {
    3: "e38543c4526e6b330f012274398a258f2d021ddae18442d2f0094d42ec229790",
    5: "69fe496e1cca2090ca62bf7622ff34c3ab3aef1b9268dfb41c4df94d380a9d0a",
    7: "c1d4ca30f45341de53af20ab4e4ca3f9bff79542146f1ac2230169eec9669655",
}
EXPECTED_ATOM_COUNTS = {3: 32, 5: 81, 7: 138}
EXPECTED_MEMBER_COUNTS = {3: 162, 5: 2_500, 7: 14_406}


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    return hashlib.sha256(encoded).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _sign(value: Fraction) -> str:
    if value < 0:
        return "negative"
    if value > 0:
        return "positive"
    return "zero"


def _ceil_div(numerator: int, denominator: int) -> int:
    if numerator < 0 or denominator <= 0:
        raise ValueError("ceil-div inputs must be nonnegative/positive")
    return (numerator + denominator - 1) // denominator


@dataclass
class HistogramGuard:
    counts: Counter[str] = field(default_factory=Counter)

    def charge(self, name: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("transform work-unit charge must be nonnegative")
        prospective = sum(self.counts.values()) + amount
        if prospective >= TRANSFORM_WORK_UNIT_CAP_EXCLUSIVE:
            raise RuntimeError(
                "transform work-unit exclusive cap 20000 would be reached or exceeded"
            )
        self.counts[name] += amount

    def snapshot(self) -> dict[str, int]:
        result = {name: self.counts[name] for name in sorted(self.counts)}
        result["total"] = sum(self.counts.values())
        return result


@dataclass(frozen=True)
class FactorizationClassification:
    kind: str
    delta: int
    square_root_delta: int | None
    parity_ok: bool
    elliptic_traces: tuple[int, int] | None

    @property
    def in_integral_split_locus(self) -> bool:
        return self.kind in SPLIT_CLASSES


def classify_factorization(q: int, a: int, b: int) -> FactorizationClassification:
    """Classify the reciprocal quartic's factorization into q-elliptic quadratics."""

    if not all(isinstance(value, int) for value in (q, a, b)):
        raise TypeError("q, a, and b must be integers")
    if q <= 1:
        raise ValueError("q must exceed one")
    delta = a * a - 4 * b + 8 * q
    if delta < 0:
        return FactorizationClassification(
            "no_integral_q_elliptic_form_factorization", delta, None, False, None
        )
    root = isqrt(delta)
    is_square = root * root == delta
    parity_ok = is_square and (root - a) % 2 == 0
    if not parity_ok:
        return FactorizationClassification(
            "no_integral_q_elliptic_form_factorization",
            delta,
            root if is_square else None,
            False,
            None,
        )
    traces = tuple(sorted(((-a - root) // 2, (-a + root) // 2)))
    return FactorizationClassification(
        "split_repeated" if delta == 0 else "split_distinct",
        delta,
        root,
        True,
        traces,
    )


def multiply_low(left: Sequence[int], right: Sequence[int]) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            product[left_index + right_index] += left_value * right_value
    return product


def factorization_residual(q: int, a: int, b: int) -> list[int] | None:
    classification = classify_factorization(q, a, b)
    if classification.elliptic_traces is None:
        return None
    left_trace, right_trace = classification.elliptic_traces
    product = multiply_low((1, -left_trace, q), (1, -right_trace, q))
    expected = [1, a, b, q * a, q * q]
    return [actual - target for actual, target in zip(product, expected)]


def frobenius_power_coefficients(
    a: int, b: int, q: int, power: int
) -> tuple[int, int]:
    """Newton-exact coefficients after raising every Frobenius root to ``power``."""

    if q <= 1 or power < 1:
        raise ValueError("q must exceed one and power must be positive")
    coefficients = (1, a, b, q * a, q * q)
    power_sums = [0] * (2 * power + 1)
    for degree in range(1, 2 * power + 1):
        value = sum(
            coefficients[index] * power_sums[degree - index]
            for index in range(1, min(degree - 1, 4) + 1)
        )
        if degree <= 4:
            value += degree * coefficients[degree]
        power_sums[degree] = -value
    a_power = -power_sums[power]
    b_numerator = power_sums[power] ** 2 - power_sums[2 * power]
    if b_numerator % 2:
        raise ArithmeticError("Newton recurrence produced nonintegral b_power")
    return a_power, b_numerator // 2


def balanced_echo_value(a_power: int, b_power: int, q: int, power: int) -> Fraction:
    return Fraction(
        2 * q**power * a_power * a_power - b_power * b_power,
        q ** (2 * power),
    )


def echo_recurrence_profile(
    b_one: Fraction, b_two: Fraction, maximum: int
) -> list[Fraction]:
    """Return B_0,...,B_max from the two complete echo coordinates B_1,B_2."""

    if maximum < 3:
        raise ValueError("echo recurrence needs maximum at least three")
    p_value = -b_one
    h_value = (b_one * b_one + b_two) / 2
    values = [Fraction(-4), b_one, b_two]
    values.append(b_one**3 - 3 * h_value * b_one + 3 * b_one)
    for power in range(4, maximum + 1):
        values.append(
            p_value * values[power - 1]
            - h_value * values[power - 2]
            + p_value * values[power - 3]
            - values[power - 4]
        )
    return values


def cyclotomic_power_to_identity_certificate(
    q: int, powered_coefficients: Sequence[tuple[int, int]]
) -> int | None:
    """Find an exact even n<=24 for which every normalized root has n-th power 1."""

    if len(powered_coefficients) < MAX_CYCLOTOMIC_CERTIFICATE_POWER:
        raise ValueError("powered coefficient list is too short")
    for power in range(2, MAX_CYCLOTOMIC_CERTIFICATE_POWER + 1, 2):
        a_power, b_power = powered_coefficients[power - 1]
        scalar = q ** (power // 2)
        if a_power == -4 * scalar and b_power == 6 * q**power:
            return power
    return None


def _validated_input() -> tuple[dict[str, object], list[Mapping[str, object]]]:
    input_data = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    payload = dict(input_data)
    claimed = payload.pop("payload_sha256", None)
    computed = _canonical_sha256(payload)
    if claimed != computed or claimed != EXPECTED_INPUT_PAYLOAD_SHA256:
        raise ValueError("balanced-control input payload/source pin mismatch")
    if input_data.get("schema") != "riemann.function_field.balanced_control_family_scan.v1":
        raise ValueError("unexpected balanced-control input schema")
    frozen = input_data.get("frozen_enumeration_facts")
    if not isinstance(frozen, dict) or tuple(frozen.get("q_values", ())) != FROZEN_Q_VALUES:
        raise ValueError("balanced-control frozen q ladder drifted")
    if frozen.get("status") != "EXHAUSTIVE_ONLY_FOR_Q_3_5_7":
        raise ValueError("balanced-control coverage status drifted")
    families = sorted(frozen.get("families", ()), key=lambda row: int(row["q"]))
    if tuple(int(family["q"]) for family in families) != FROZEN_Q_VALUES:
        raise ValueError("balanced-control family rows drifted")

    upstream_locks = input_data["producer_and_source_locks"]["locks"]
    producer_lock = upstream_locks["producer"]
    if producer_lock["path"] != (
        "research/l-families/atlas/function_field/balanced_control_family_scan.py"
    ):
        raise ValueError("balanced-control producer path drifted")
    if producer_lock["sha256_lf_normalized"] != _lf_normalized_sha256(
        INPUT_PRODUCER_PATH
    ):
        raise ValueError("balanced-control producer no longer matches its source lock")

    for family in families:
        q = int(family["q"])
        atoms = family["joint_a_D_b_D_law"]["atoms"]
        if len(atoms) != EXPECTED_ATOM_COUNTS[q]:
            raise ValueError(f"q={q} joint atom-count sentinel drifted")
        if int(family["member_count"]) != EXPECTED_MEMBER_COUNTS[q]:
            raise ValueError(f"q={q} member-count sentinel drifted")
        if sum(int(atom["member_count"]) for atom in atoms) != EXPECTED_MEMBER_COUNTS[q]:
            raise ValueError(f"q={q} joint histogram is not member-complete")
        if family["member_coefficient_ledger_sha256"] != EXPECTED_MEMBER_LEDGER_SHA256[q]:
            raise ValueError(f"q={q} complete member-ledger sentinel drifted")
        if int(family["candidate_count"]) != q**5:
            raise ValueError(f"q={q} candidate coverage drifted")
        if int(family["expected_squarefree_count"]) != q**5 - q**4:
            raise ValueError(f"q={q} squarefree coverage drifted")
    return input_data, families


def _new_class_counter() -> dict[str, Counter[str]]:
    return {
        kind: Counter({"signed_atom_count": 0, "member_count": 0})
        for kind in CLASS_ORDER
    }


def _fiber_summary(
    fibers: Mapping[object, dict[str, object]],
    member_count: int,
    guard: HistogramGuard,
    *,
    echo: bool = False,
) -> dict[str, object]:
    mixed_rows: list[dict[str, object]] = []
    multi_label_fiber_count = 0
    same_split_status_multi_label_fiber_count = 0
    for key in sorted(fibers):
        guard.charge("detector_fiber_visit")
        raw = fibers[key]
        classes = sorted(raw["classes"], key=CLASS_ORDER.index)  # type: ignore[arg-type]
        if len(classes) < 2:
            continue
        multi_label_fiber_count += 1
        crosses_split_boundary = (
            any(kind in SPLIT_CLASSES for kind in classes)
            and any(kind not in SPLIT_CLASSES for kind in classes)
        )
        if not crosses_split_boundary:
            same_split_status_multi_label_fiber_count += 1
            continue
        if echo:
            serialized_value: object = {
                "B_1": _fraction_pair(key[0]),
                "B_2": _fraction_pair(key[1]),
            }
        else:
            serialized_value = _fraction_pair(key)
        serialized_states = []
        for state in sorted(raw["states"]):  # type: ignore[arg-type]
            guard.charge("detector_fiber_state_visit")
            serialized_states.append(
                {
                    "a_D_squared": state[0],
                    "b_D": state[1],
                    "factorization_type": raw["state_classes"][state],  # type: ignore[index]
                    "member_count": raw["state_members"][state],  # type: ignore[index]
                }
            )
        mixed_rows.append(
            {
                "detector_value": serialized_value,
                "factorization_types": classes,
                "member_count": int(raw["member_count"]),
                "signed_atom_count": int(raw["signed_atom_count"]),
                "twist_quotiented_state_count": len(raw["states"]),  # type: ignore[arg-type]
                "states": serialized_states,
            }
        )
    mixed_members = sum(int(row["member_count"]) for row in mixed_rows)
    return {
        "fiber_count": len(fibers),
        "multi_factorization_label_fiber_count": multi_label_fiber_count,
        "same_split_status_multi_label_fiber_count": (
            same_split_status_multi_label_fiber_count
        ),
        "mixed_factorization_fiber_count": len(mixed_rows),
        "member_count_in_mixed_fibers": mixed_members,
        "member_fraction_in_mixed_fibers": _fraction_pair(
            Fraction(mixed_members, member_count)
        ),
        "mixed_factorization_fibers": mixed_rows,
        "interpretation": (
            "a mixed fiber contains both a +q elliptic-form split state and a state "
            "without such an integral factorization, so it is an exact obstruction "
            "to recovering that split locus from this detector coordinate alone; "
            "a split-repeated/split-distinct collision alone is not counted as mixed"
        ),
    }


def _tail_packet(
    values: Sequence[dict[str, object]],
    detector_name: str,
    guard: HistogramGuard,
) -> dict[str, object]:
    detector_key = "B" if detector_name == "B" else "F"
    if not values:
        raise ValueError("tail packet requires at least one histogram atom")

    member_count = 0
    minimum: Fraction | None = None
    maximum: Fraction | None = None
    for row in values:
        guard.charge("tail_extrema_atom_visit")
        detector_value = Fraction(row[detector_key])
        member_count += int(row["member_count"])
        minimum = detector_value if minimum is None else min(minimum, detector_value)
        maximum = detector_value if maximum is None else max(maximum, detector_value)
    if minimum is None or maximum is None or member_count <= 0:
        raise ArithmeticError("tail packet lost its histogram mass")

    absolute_extreme = max(abs(minimum), abs(maximum))
    extrema_values = {
        value for value in (minimum, maximum) if abs(value) == absolute_extreme
    }
    target_values: dict[str, set[Fraction]] = {
        "minimum": {minimum},
        "maximum": {maximum},
        "absolute_extreme": extrema_values,
    }
    if detector_name == "B":
        target_values["minus_four"] = {Fraction(-4)}
        target_values["plus_four"] = {Fraction(4)}

    target_class_counts = {name: Counter() for name in target_values}
    moment_denominators = {order: Fraction(0) for order in ABSOLUTE_MOMENT_ORDERS}
    moment_numerators = {
        name: {order: Fraction(0) for order in ABSOLUTE_MOMENT_ORDERS}
        for name in (
            "integral_split_locus",
            "repeated_factor_locus",
            "minimum_value_fiber",
            "absolute_extreme_fibers",
        )
    }
    far_negative_member_counts = Counter()
    far_negative_atom_counts = Counter()

    for row in values:
        guard.charge("tail_aggregate_atom_visit")
        detector_value = Fraction(row[detector_key])
        weight = int(row["member_count"])
        kind = str(row["factorization_type"])
        for name, targets in target_values.items():
            if detector_value in targets:
                target_class_counts[name][kind] += weight
        if detector_name == "F" and detector_value < -4:
            far_negative_member_counts[kind] += weight
            far_negative_atom_counts[kind] += 1

        for order in ABSOLUTE_MOMENT_ORDERS:
            contribution = weight * abs(detector_value) ** order
            moment_denominators[order] += contribution
            if kind in SPLIT_CLASSES:
                moment_numerators["integral_split_locus"][order] += contribution
            if kind == "split_repeated":
                moment_numerators["repeated_factor_locus"][order] += contribution
            if detector_value == minimum:
                moment_numerators["minimum_value_fiber"][order] += contribution
            if abs(detector_value) == absolute_extreme:
                moment_numerators["absolute_extreme_fibers"][order] += contribution

    def fiber_record(name: str) -> dict[str, object]:
        by_class = target_class_counts[name]
        selected_member_count = sum(by_class.values())
        return {
            "values": [
                _fraction_pair(value) for value in sorted(target_values[name])
            ],
            "member_count": selected_member_count,
            "member_fraction": _fraction_pair(
                Fraction(selected_member_count, member_count)
            ),
            "member_counts_by_factorization_type": {
                kind: by_class[kind] for kind in CLASS_ORDER
            },
        }

    shares: dict[str, dict[str, list[int]]] = {
        "integral_split_locus": {},
        "repeated_factor_locus": {},
        "minimum_value_fiber": {},
        "absolute_extreme_fibers": {},
    }
    for order in ABSOLUTE_MOMENT_ORDERS:
        denominator = moment_denominators[order]
        if denominator == 0:
            raise ArithmeticError("absolute moment denominator unexpectedly vanished")
        for name in shares:
            shares[name][str(order)] = _fraction_pair(
                moment_numerators[name][order] / denominator
            )

    packet: dict[str, object] = {
        "minimum": fiber_record("minimum"),
        "maximum": fiber_record("maximum"),
        "absolute_extreme": fiber_record("absolute_extreme"),
        "absolute_moment_shares": shares,
    }
    if detector_name == "B":
        packet["haar_endpoints"] = {
            "minus_four": fiber_record("minus_four"),
            "plus_four": fiber_record("plus_four"),
        }
    else:
        far_negative_members = sum(far_negative_member_counts.values())
        packet["far_negative_F_below_minus_4"] = {
            "signed_atom_count": sum(far_negative_atom_counts.values()),
            "member_count": far_negative_members,
            "member_fraction": _fraction_pair(
                Fraction(far_negative_members, member_count)
            ),
            "signed_atom_counts_by_factorization_type": {
                kind: far_negative_atom_counts[kind] for kind in CLASS_ORDER
            },
            "member_counts_by_factorization_type": {
                kind: far_negative_member_counts[kind] for kind in CLASS_ORDER
            },
        }
    return packet


def _orbit_bounds(
    q: int,
    family: Mapping[str, object],
    rows: Sequence[dict[str, object]],
    guard: HistogramGuard,
) -> dict[str, object]:
    group_order = int(family["affine_orbit_analysis"]["group_order"])  # type: ignore[index]
    total_orbits = int(family["affine_orbit_analysis"]["orbit_count"])  # type: ignore[index]
    by_j: dict[int, Counter[str]] = defaultdict(Counter)
    for row in rows:
        guard.charge("orbit_bucket_atom_visit")
        by_j[int(row["B_numerator_J"])][str(row["factorization_type"])] += int(
            row["member_count"]
        )

    support = {
        int(atom["B_numerator_J"]): atom
        for atom in family["balanced_support"]["atoms"]  # type: ignore[index]
    }
    if set(by_j) != set(support):
        raise ArithmeticError(f"q={q} orbit buckets do not match B support")

    lower_total = 0
    upper_total = 0
    exact_split_orbits = 0
    forced_mixed_split_orbits = 0
    mixed_rows: list[dict[str, object]] = []
    for j_value in sorted(support):
        guard.charge("orbit_support_bucket_visit")
        source_atom = support[j_value]
        total_members = int(source_atom["member_count"])
        orbit_count = int(source_atom["affine_orbit_count"])
        counts = by_j[j_value]
        split_members = sum(counts[kind] for kind in SPLIT_CLASSES)
        complement_members = total_members - split_members
        if sum(counts.values()) != total_members:
            raise ArithmeticError(f"q={q} J={j_value} member bucket drifted")
        if split_members == 0:
            lower = upper = 0
        elif complement_members == 0:
            lower = upper = orbit_count
            exact_split_orbits += orbit_count
        else:
            lower = max(
                _ceil_div(split_members, group_order),
                orbit_count - complement_members,
            )
            upper = min(
                split_members,
                orbit_count - _ceil_div(complement_members, group_order),
            )
            if not 0 <= lower <= upper <= orbit_count:
                raise ArithmeticError(f"q={q} J={j_value} invalid orbit interval")
            mixed_rows.append(
                {
                    "B_numerator_J": j_value,
                    "B_D": _fraction_pair(Fraction(j_value, q * q)),
                    "source_affine_orbit_count": orbit_count,
                    "split_member_count": split_members,
                    "no_q_elliptic_form_factorization_member_count": (
                        complement_members
                    ),
                    "split_orbit_count_bounds": [lower, upper],
                }
            )
            if lower == upper:
                forced_mixed_split_orbits += lower
        lower_total += lower
        upper_total += upper

    exact_total = lower_total if lower_total == upper_total else None
    return {
        "status": (
            "EXACTLY_IDENTIFIED_FROM_AGGREGATED_SOURCE_AND_ORBIT_SIZE_BOUNDS"
            if exact_total is not None
            else "BOUNDED_NOT_IDENTIFIABLE_FROM_AGGREGATED_SOURCE"
        ),
        "source_total_affine_orbit_count": total_orbits,
        "exact_split_orbits_from_homogeneous_B_buckets": exact_split_orbits,
        "split_orbits_forced_in_mixed_B_buckets": forced_mixed_split_orbits,
        "integral_split_locus_affine_orbit_count": exact_total,
        "integral_split_locus_affine_orbit_count_bounds": [lower_total, upper_total],
        "uniform_affine_orbit_fraction_bounds": [
            _fraction_pair(Fraction(lower_total, total_orbits)),
            _fraction_pair(Fraction(upper_total, total_orbits)),
        ],
        "mixed_B_buckets": mixed_rows,
        "identifiability_note": (
            "the source records orbit counts only after aggregation by B; singleton "
            "mixed-bucket bounds can nevertheless force an exact total, while a "
            "non-singleton interval records the remaining lost assignment"
        ),
        "bound_derivation": (
            "each orbit stays in one (a^2,b) state, has between 1 and q*(q-1) "
            "members, and every nonempty class in a mixed B bucket needs an orbit"
        ),
    }


def analyze_family(
    family: Mapping[str, object], guard: HistogramGuard
) -> dict[str, object]:
    q = int(family["q"])
    member_count = int(family["member_count"])
    input_atoms = family["joint_a_D_b_D_law"]["atoms"]  # type: ignore[index]
    class_counts = _new_class_counter()
    state_records: dict[tuple[int, int], dict[str, object]] = {}
    fibers: dict[str, dict[object, dict[str, object]]] = {
        "B": defaultdict(dict),
        "F": defaultdict(dict),
        "echo": defaultdict(dict),
    }
    rows: list[dict[str, object]] = []
    split_rows: list[dict[str, object]] = []

    detector_sums = {
        name: {
            "all": Fraction(0),
            "split": Fraction(0),
            **{kind: Fraction(0) for kind in CLASS_ORDER},
        }
        for name in ("B", "F")
    }
    detector_signs = {
        name: {
            kind: {
                "member": Counter({"negative": 0, "zero": 0, "positive": 0}),
                "signed_atom": Counter({"negative": 0, "zero": 0, "positive": 0}),
            }
            for kind in CLASS_ORDER
        }
        for name in ("B", "F")
    }

    for atom in input_atoms:
        guard.charge("classification_atom_visit")
        a = int(atom["a_D"])
        b = int(atom["b_D"])
        weight = int(atom["member_count"])
        classification = classify_factorization(q, a, b)
        if classification.delta < 0:
            raise ArithmeticError(f"q={q} histogram contains negative Delta")
        if classification.in_integral_split_locus:
            if classification.elliptic_traces is None:
                raise ArithmeticError("split row lost its traces")
            left_trace, right_trace = classification.elliptic_traces
            if left_trace * left_trace > 4 * q or right_trace * right_trace > 4 * q:
                raise ArithmeticError(f"q={q} integral factor left the elliptic Hasse interval")
            if factorization_residual(q, a, b) != [0, 0, 0, 0, 0]:
                raise ArithmeticError(f"q={q} split factorization residual is nonzero")

        powered: list[tuple[int, int]] = []
        echoes: list[Fraction] = []
        for power in range(1, MAX_CYCLOTOMIC_CERTIFICATE_POWER + 1):
            guard.charge("powered_histogram_atom_step")
            powered_row = frobenius_power_coefficients(a, b, q, power)
            powered.append(powered_row)
            if power <= MAX_ECHO_POWER:
                echoes.append(balanced_echo_value(*powered_row, q, power))
        if echo_recurrence_profile(echoes[0], echoes[1], MAX_ECHO_POWER)[1:] != echoes:
            raise ArithmeticError(f"q={q} direct and collapsed echo profiles disagree")
        cyclotomic_exponent = cyclotomic_power_to_identity_certificate(q, powered)

        b_value = echoes[0]
        f_value = Fraction(q * a * a - b * b, q * q)
        if b_value != Fraction(*atom["B_D"]):
            raise ArithmeticError(f"q={q} input B value drifted")
        if int(atom["B_numerator_J"]) != 2 * q * a * a - b * b:
            raise ArithmeticError(f"q={q} input B numerator drifted")

        kind = classification.kind
        class_counts[kind]["signed_atom_count"] += 1
        class_counts[kind]["member_count"] += weight
        for detector_name, detector_value in (("B", b_value), ("F", f_value)):
            detector_sums[detector_name]["all"] += weight * detector_value
            detector_sums[detector_name][kind] += weight * detector_value
            if classification.in_integral_split_locus:
                detector_sums[detector_name]["split"] += weight * detector_value
            sign = _sign(detector_value)
            detector_signs[detector_name][kind]["member"][sign] += weight
            detector_signs[detector_name][kind]["signed_atom"][sign] += 1

        state = (a * a, b)
        row: dict[str, object] = {
            "q": q,
            "a_D": a,
            "b_D": b,
            "a_D_squared": a * a,
            "member_count": weight,
            "B_numerator_J": int(atom["B_numerator_J"]),
            "B": b_value,
            "F": f_value,
            "Delta": classification.delta,
            "square_root_Delta": classification.square_root_delta,
            "factorization_type": kind,
            "elliptic_traces": classification.elliptic_traces,
            "echo_B1_B2": (echoes[0], echoes[1]),
            "cyclotomic_certificate_exponent": cyclotomic_exponent,
        }
        rows.append(row)

        state_record = state_records.setdefault(
            state,
            {
                "factorization_type": kind,
                "member_count": 0,
                "signed_atom_count": 0,
                "echo_B1_B2": (echoes[0], echoes[1]),
                "cyclotomic_certificate_exponent": cyclotomic_exponent,
            },
        )
        for key, expected in (
            ("factorization_type", kind),
            ("echo_B1_B2", (echoes[0], echoes[1])),
            ("cyclotomic_certificate_exponent", cyclotomic_exponent),
        ):
            if state_record[key] != expected:
                raise ArithmeticError(f"q={q} twist state changed {key}")
        state_record["member_count"] = int(state_record["member_count"]) + weight
        state_record["signed_atom_count"] = int(state_record["signed_atom_count"]) + 1

        for detector_name, detector_value in (
            ("B", b_value),
            ("F", f_value),
            ("echo", (echoes[0], echoes[1])),
        ):
            fiber = fibers[detector_name].setdefault(
                detector_value,
                {
                    "classes": set(),
                    "member_count": 0,
                    "signed_atom_count": 0,
                    "states": set(),
                    "state_classes": {},
                    "state_members": Counter(),
                },
            )
            fiber["classes"].add(kind)  # type: ignore[union-attr]
            fiber["member_count"] = int(fiber["member_count"]) + weight
            fiber["signed_atom_count"] = int(fiber["signed_atom_count"]) + 1
            fiber["states"].add(state)  # type: ignore[union-attr]
            fiber["state_classes"][state] = kind  # type: ignore[index]
            fiber["state_members"][state] += weight  # type: ignore[index]

        if classification.in_integral_split_locus:
            left_trace, right_trace = classification.elliptic_traces or (0, 0)
            split_rows.append(
                {
                    "a_D": a,
                    "b_D": b,
                    "member_count": weight,
                    "factorization_type": kind,
                    "Delta": classification.delta,
                    "square_root_Delta": classification.square_root_delta,
                    "elliptic_traces_sorted": [left_trace, right_trace],
                    "factorization": (
                        f"(1-({left_trace})*T+{q}*T^2)*(1-({right_trace})*T+{q}*T^2)"
                    ),
                    "B": _fraction_pair(b_value),
                    "F": _fraction_pair(f_value),
                    "echo_B1_B2": [
                        _fraction_pair(echoes[0]),
                        _fraction_pair(echoes[1]),
                    ],
                    "cyclotomic_power_to_identity_exponent": cyclotomic_exponent,
                }
            )

    if sum(counter["member_count"] for counter in class_counts.values()) != member_count:
        raise ArithmeticError(f"q={q} factorization classes lost members")
    if sum(counter["signed_atom_count"] for counter in class_counts.values()) != len(input_atoms):
        raise ArithmeticError(f"q={q} factorization classes lost atoms")

    state_counts = Counter()
    for record in state_records.values():
        guard.charge("state_classification_visit")
        state_counts[str(record["factorization_type"])] += 1
    serialized_classes: dict[str, object] = {}
    for kind in CLASS_ORDER:
        members = class_counts[kind]["member_count"]
        atoms = class_counts[kind]["signed_atom_count"]
        serialized_classes[kind] = {
            "signed_coefficient_atom_count": atoms,
            "signed_coefficient_atom_fraction": _fraction_pair(
                Fraction(atoms, len(input_atoms))
            ),
            "twist_quotiented_state_count": state_counts[kind],
            "member_count": members,
            "member_fraction": _fraction_pair(Fraction(members, member_count)),
        }

    split_members = sum(class_counts[kind]["member_count"] for kind in SPLIT_CLASSES)
    split_atoms = sum(class_counts[kind]["signed_atom_count"] for kind in SPLIT_CLASSES)
    split_states = sum(state_counts[kind] for kind in SPLIT_CLASSES)

    conditional: dict[str, object] = {}
    for detector_name in ("B", "F"):
        total_mean = detector_sums[detector_name]["all"] / member_count
        split_mean = detector_sums[detector_name]["split"] / split_members
        split_probability = Fraction(split_members, member_count)
        indicator_covariance = (
            detector_sums[detector_name]["split"] / member_count
            - split_probability * total_mean
        )
        by_class = {}
        for kind in CLASS_ORDER:
            class_member_count = class_counts[kind]["member_count"]
            mean = (
                detector_sums[detector_name][kind] / class_member_count
                if class_member_count
                else Fraction(0)
            )
            by_class[kind] = {
                "conditional_member_mean": _fraction_pair(mean),
                "member_sign_counts": {
                    sign: detector_signs[detector_name][kind]["member"][sign]
                    for sign in ("negative", "zero", "positive")
                },
                "signed_atom_sign_counts": {
                    sign: detector_signs[detector_name][kind]["signed_atom"][sign]
                    for sign in ("negative", "zero", "positive")
                },
            }
        conditional[detector_name] = {
            "family_member_mean": _fraction_pair(total_mean),
            "integral_split_locus_conditional_member_mean": _fraction_pair(split_mean),
            "covariance_with_split_indicator": _fraction_pair(indicator_covariance),
            "by_factorization_type": by_class,
            "fiber_purity": _fiber_summary(
                fibers[detector_name], member_count, guard, echo=False
            ),
        }

    cyclotomic_states = []
    cyclotomic_class_counts = {
        kind: Counter({"signed_atom_count": 0, "state_count": 0, "member_count": 0})
        for kind in CLASS_ORDER
    }
    for state, record in sorted(state_records.items()):
        guard.charge("twist_state_visit")
        exponent = record["cyclotomic_certificate_exponent"]
        if exponent is None:
            continue
        kind = str(record["factorization_type"])
        cyclotomic_class_counts[kind]["signed_atom_count"] += int(
            record["signed_atom_count"]
        )
        cyclotomic_class_counts[kind]["state_count"] += 1
        cyclotomic_class_counts[kind]["member_count"] += int(record["member_count"])
        cyclotomic_states.append(
            {
                "a_D_squared": state[0],
                "b_D": state[1],
                "factorization_type": kind,
                "signed_atom_count": int(record["signed_atom_count"]),
                "member_count": int(record["member_count"]),
                "minimum_even_power_to_identity": int(exponent),
                "echo_B1_B2": [
                    _fraction_pair(record["echo_B1_B2"][0]),  # type: ignore[index]
                    _fraction_pair(record["echo_B1_B2"][1]),  # type: ignore[index]
                ],
            }
        )

    full_ledger = []
    for row in rows:
        guard.charge("classification_ledger_row_visit")
        full_ledger.append(
            [
                q,
                int(row["a_D"]),
                int(row["b_D"]),
                int(row["member_count"]),
                int(row["Delta"]),
                str(row["factorization_type"]),
                row["square_root_Delta"],
                list(row["elliptic_traces"]) if row["elliptic_traces"] else None,
            ]
        )

    return {
        "q": q,
        "input_member_count": member_count,
        "input_signed_coefficient_atom_count": len(input_atoms),
        "twist_quotiented_coefficient_state_count": len(state_records),
        "factorization_classification": {
            "classes": serialized_classes,
            "integral_split_locus": {
                "signed_coefficient_atom_count": split_atoms,
                "signed_coefficient_atom_fraction": _fraction_pair(
                    Fraction(split_atoms, len(input_atoms))
                ),
                "twist_quotiented_state_count": split_states,
                "member_count": split_members,
                "member_fraction": _fraction_pair(Fraction(split_members, member_count)),
            },
            "complete_classification_ledger_sha256": _canonical_sha256(full_ledger),
            "split_signed_coefficient_atoms": split_rows,
        },
        "detector_correlations": {
            "B": conditional["B"],
            "F": conditional["F"],
            "complete_frobenius_echo": {
                "coordinates": "(B_1,B_2); the exact recurrence determines every B_r",
                "powers_directly_cross_checked": list(range(1, MAX_ECHO_POWER + 1)),
                "fiber_purity": _fiber_summary(
                    fibers["echo"], member_count, guard, echo=True
                ),
            },
            "cyclotomic_normalized_spectrum": {
                "status": "EXACT_POSITIVE_CERTIFICATES_WITH_BOUNDED_NONDETECTION",
                "certificate": (
                    "an even n<=24 with powered polynomial "
                    "(X-q^(n/2))^4; then every normalized Frobenius root is an n-th root of unity"
                ),
                "maximum_power_checked": MAX_CYCLOTOMIC_CERTIFICATE_POWER,
                "certified_states": cyclotomic_states,
                "by_factorization_type": {
                    kind: dict(cyclotomic_class_counts[kind]) for kind in CLASS_ORDER
                },
                "nondetection_warning": (
                    "absence of this bounded certificate is not asserted to prove a noncyclotomic spectrum"
                ),
            },
        },
        "tail_and_extreme_shares": {
            "B": _tail_packet(rows, "B", guard),
            "F": _tail_packet(rows, "F", guard),
        },
        "affine_orbit_weighting": _orbit_bounds(q, family, rows, guard),
    }


def build_fixture() -> dict[str, object]:
    input_data, families = _validated_input()
    guard = HistogramGuard()
    analyses = [analyze_family(family, guard) for family in families]
    if tuple(int(row["q"]) for row in analyses) != FROZEN_Q_VALUES:
        raise ArithmeticError("output q ladder drifted")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_endoscopic_split_locus.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.ENDOSCOPIC_SPLIT_LOCUS.Q3_Q5_Q7.V1",
        "status": "EXACT_BOUNDED_TRANSFORM_OF_SOURCE_LOCKED_COMPLETE_HISTOGRAMS",
        "scope": (
            "integral +q elliptic-form factor locus and exact detector correlations in the "
            "existing q=3,5,7 monic-squarefree-quintic coefficient histograms"
        ),
        "definition_and_exact_identities": {
            "source_polynomial": "P(T)=1+a*T+b*T^2+q*a*T^3+q^2*T^4",
            "discriminant": "Delta=a^2-4*b+8*q",
            "split_criterion": (
                "Delta is a nonnegative square d^2 and d has the parity of a; "
                "then r=(-a-d)/2, s=(-a+d)/2"
            ),
            "factorization": (
                "P(T)=(1-r*T+q*T^2)*(1-s*T+q*T^2), "
                "r+s=-a, r*s=b-2*q"
            ),
            "repeated_factor": (
                "Delta=0 iff r=s=-a/2 and P(T)=(1-r*T+q*T^2)^2"
            ),
            "balanced_B": (
                "B=(2*q*a^2-b^2)/q^2=2*Delta/q-(b-4*q)^2/q^2"
            ),
            "toy_minor_F": (
                "F=(q*a^2-b^2)/q^2=Delta/q-(b-2*q)^2/q^2-4"
            ),
            "echo_collapse": (
                "the entire balanced Frobenius-power echo is determined by (B_1,B_2) "
                "through the recorded order-four recurrence"
            ),
            "affine_invariance_used_for_orbit_bounds": (
                "under the source-locked AGL action a maps to +/-a and b is fixed, "
                "so Delta and the split classification are orbit-invariant"
            ),
        },
        "frozen_histogram_results": {
            "status": "EXACT_ONLY_FOR_Q_3_5_7",
            "families": analyses,
        },
        "structural_findings": {
            "detector_non_identifiability": (
                "B, F, and even the complete two-coordinate echo each have at least one "
                "frozen fiber containing both an integral +q elliptic-form split state and "
                "a state without such a factorization"
            ),
            "cyclotomic_versus_split": (
                "bounded power-to-identity certificates occur on both sides of the integral "
                "+q elliptic-form split criterion; normalized root-of-unity spectrum and this "
                "specific reciprocal-quadratic factorization are distinct finite predicates"
            ),
            "orbit_non_identifiability": (
                "member and coefficient-atom counts are exact, while the source's orbit counts "
                "are aggregated by B across mixed split-status fibers; orbit-size constraints "
                "force exact totals at q=3,5 but leave only a rigorous interval at q=7"
            ),
        },
        "quarantined_patterns_and_targets": {
            "status": "NO_ALL_Q_FREQUENCY_FORMULA_CLAIMED",
            "three_field_member_counts": {
                str(row["q"]): row["factorization_classification"]["integral_split_locus"][  # type: ignore[index]
                    "member_count"
                ]
                for row in analyses
            },
            "three_field_member_fractions": {
                str(row["q"]): row["factorization_classification"]["integral_split_locus"][  # type: ignore[index]
                    "member_fraction"
                ]
                for row in analyses
            },
            "useful_exact_counting_target": (
                "derive the all-q joint multiplicity of integral trace pairs (r,s) in the "
                "monic squarefree quintic family, keeping repeated and distinct factors separate"
            ),
            "geometric_target": (
                "after explicitly importing Honda-Tate/Tate and polarization results, determine "
                "which polynomial-split rows give F_q product isogeny classes, which principal "
                "polarizations are Jacobians, and which rows without a ground-field integral "
                "+q elliptic-form factorization acquire one after extension"
            ),
            "warning": (
                "the q=3,5,7 values are a three-field census, not interpolation evidence, an "
                "asymptotic law, or a density theorem"
            ),
        },
        "interpretation_firewall": {
            "native_exact_claim": (
                "the displayed integral factorization of the Frobenius polynomial and every "
                "histogram-weighted finite count"
            ),
            "imported_theorem_target_not_used": (
                "turning polynomial factorization into an abelian-surface product-isogeny "
                "statement uses Honda-Tate/Tate theory and is not proved in this packet"
            ),
            "polarization_warning": (
                "an unpolarized isogeny to a product does not identify the canonical principal "
                "polarization with a product polarization and does not make the smooth genus-two "
                "curve or its principally polarized Jacobian a product"
            ),
            "geometric_warning": (
                "failure of the integral +q elliptic-form criterion at q does not prove "
                "geometric simplicity; factors or isogeny decompositions may appear after "
                "extending the base field"
            ),
            "global_warning": (
                "nothing here proves an all-q law, an equidistribution theorem, or an RH/GRH implication"
            ),
        },
        "resource_contract": {
            "frozen_q_values": list(FROZEN_Q_VALUES),
            "input": "complete source-locked (a_D,b_D) histograms only",
            "finite_field_enumeration": False,
            "curve_or_family_member_enumeration": False,
            "random_sampling": False,
            "floating_point_arithmetic": False,
            "maximum_echo_power": MAX_ECHO_POWER,
            "maximum_cyclotomic_certificate_power": MAX_CYCLOTOMIC_CERTIFICATE_POWER,
            "transform_work_unit_cap_exclusive": TRANSFORM_WORK_UNIT_CAP_EXCLUSIVE,
            "guarded_transform_work_units": guard.snapshot(),
            "work_unit_definition": (
                "one charged source-atom classification, atom-power Newton step, detector-fiber "
                "or state visit, tail atom pass, orbit-bucket visit, or output-ledger row; "
                "source parsing and constant-size dictionary bookkeeping are excluded"
            ),
            "external_dependencies": "none; Python 3.11+ standard library",
        },
        "producer_and_source_locks": {
            "input_payload_sha256_required": EXPECTED_INPUT_PAYLOAD_SHA256,
            "input_member_ledger_sha256_required": {
                str(q): EXPECTED_MEMBER_LEDGER_SHA256[q] for q in FROZEN_Q_VALUES
            },
            "locks": {
                "input_fixture": {
                    "path": "research/l-families/atlas/function_field/balanced_control_family_scan.json",
                    "sha256_lf_normalized": _lf_normalized_sha256(INPUT_PATH),
                    "payload_sha256": input_data["payload_sha256"],
                },
                "input_producer": {
                    "path": "research/l-families/atlas/function_field/balanced_control_family_scan.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(INPUT_PRODUCER_PATH),
                },
                "producer": {
                    "path": "research/l-families/atlas/function_field/genus2_endoscopic_split_locus.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(Path(__file__)),
                },
                "note": {
                    "path": "research/l-families/atlas/function_field/GENUS2_ENDOSCOPIC_SPLIT_LOCUS.md",
                    "sha256_lf_normalized": _lf_normalized_sha256(NOTE_PATH),
                },
                "test": {
                    "path": "tests/test_genus2_endoscopic_split_locus.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(TEST_PATH),
                },
            },
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write deterministic JSON")
    mode.add_argument("--check", action="store_true", help="check committed JSON")
    parser.add_argument("path", nargs="?", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args(argv)

    fixture = build_fixture()
    rendered = json.dumps(fixture, indent=2, sort_keys=True) + "\n"
    if args.write:
        args.path.write_text(rendered, encoding="utf-8", newline="\n")
        print(
            "genus2 endoscopic/split locus: "
            f"q={FROZEN_Q_VALUES} payload_sha256={fixture['payload_sha256']}"
        )
        return 0
    if not args.path.exists() or args.path.read_text(encoding="utf-8") != rendered:
        print(f"stale or missing fixture: {args.path}")
        return 1
    print(
        "genus2 endoscopic/split locus check: ok "
        f"payload_sha256={fixture['payload_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
