#!/usr/bin/env python3
"""Exact arithmetic pushforward of the Frobenius-interferometry selectors.

The sole finite-family input is the complete source-locked joint ``(a_D,b_D)``
histogram in ``balanced_control_family_scan.json``.  For the normalized
reciprocal quartic attached to

    T^4 + a_D*T^3 + b_D*T^2 + q*a_D*T + q^2,

the selector packet's even coefficient adapter is evaluated at

    A = a_D^2/q,  e2 = b_D/q.

No field, polynomial, curve, root, or family member is enumerated.  Every
reported number is an integer or ``Fraction``.  All primitive inputs are
checked against frozen digests before JSON parsing or dynamic module loading,
and the complete 251-atom transform refuses above 4,096 source atoms.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from math import ceil, isqrt
from pathlib import Path
from types import ModuleType
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUT_PATH = HERE / "balanced_control_family_scan.json"
INPUT_PRODUCER_PATH = HERE / "balanced_control_family_scan.py"
COEFFICIENT_ARITHMETIC_PATH = HERE / "genus2_q_scan.py"
AFFINE_ACTION_PATH = HERE / "genus2_affine_orbits.py"
SELECTOR_PRODUCER_PATH = HERE / "frobenius_interferometry_subgroup_selectors.py"
SELECTOR_NOTE_PATH = HERE / "FROBENIUS_INTERFEROMETRY_SUBGROUP_SELECTORS.md"
OUTPUT_PATH = HERE / "genus2_interferometry_arithmetic_pushforward.json"
NOTE_PATH = HERE / "GENUS2_INTERFEROMETRY_ARITHMETIC_PUSHFORWARD.md"
TEST_PATH = ROOT / "tests" / "test_genus2_interferometry_arithmetic_pushforward.py"

FROZEN_Q_VALUES = (3, 5, 7)
SELECTOR_ORDER = ("P", "D", "S")
ADAPTER_KEY_BY_SELECTOR = {
    "P": "product_selector",
    "D": "doubled_selector",
    "S": "sym3_selector",
}
SOURCE_ATOM_CAP_INCLUSIVE = 4_096
ABSOLUTE_TAIL_TARGET = Fraction(1, 100)

# These constants intentionally reject a self-consistent but substituted
# source.  LF-normalized hashes are stable across platform line endings.
EXPECTED_LF_SHA256 = {
    "histogram_fixture": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
    "histogram_producer": "7192fa26b0ea17cb68cff288620ea4dfb124e07807986d9c74fbd37e66087d3b",
    "coefficient_arithmetic": "f595dbf52d4265cfe2ea6888255f53df887fed77e204103f2b0dfd95e961f935",
    "affine_action": "32e440750b2832ec4cc84473187b4b1aa6396eda87c64f5ac845b2a96dc88f08",
    "selector_producer": "48474ebcbb99efea23227126f66f566fdb525a3c9ae9e81a77bf83d4075f55e7",
    "selector_note": "c7637d454f1fb102555e6723dd8d93a4b6a27363d80cbbb9a03061f614bd3221",
}
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
EXPECTED_SELECTOR_SIGNATURES = {
    "product_selector": (0, 2, 0, 0, 0, 0, 0),
    "doubled_selector": (0, 0, 2, 0, 0, 0, 0),
    "sym3_selector": (0, 0, 0, 2, 0, 0, 0),
}
AMBIENT_GRAM = (
    (24, -20, 4),
    (-20, 48, 0),
    (4, 0, 40),
)


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


def _plain_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be a plain integer")
    return value


def _sign(value: Fraction) -> str:
    if value < 0:
        return "negative"
    if value > 0:
        return "positive"
    return "zero"


@dataclass
class SourceAtomGuard:
    """Inclusive 4,096-source-atom refusal guard."""

    cap: int = SOURCE_ATOM_CAP_INCLUSIVE
    counts: Counter[str] = field(default_factory=Counter)

    @property
    def total(self) -> int:
        return sum(self.counts.values())

    def preflight(self, amount: int) -> None:
        number = _plain_int("source atom count", amount)
        if number < 0:
            raise ValueError("source atom count must be nonnegative")
        if number > self.cap:
            raise RuntimeError(
                f"source atom count {number} exceeds inclusive cap {self.cap}"
            )

    def charge(self, name: str, amount: int = 1) -> None:
        number = _plain_int("source atom charge", amount)
        if number < 0:
            raise ValueError("source atom charge must be nonnegative")
        if self.total + number > self.cap:
            raise RuntimeError(
                f"source atom transform would exceed inclusive cap {self.cap}"
            )
        self.counts[name] += number

    def snapshot(self) -> dict[str, int]:
        result = {name: self.counts[name] for name in sorted(self.counts)}
        result["total"] = self.total
        return result


def _verify_primitive_hashes() -> None:
    paths = {
        "histogram_fixture": INPUT_PATH,
        "histogram_producer": INPUT_PRODUCER_PATH,
        "coefficient_arithmetic": COEFFICIENT_ARITHMETIC_PATH,
        "affine_action": AFFINE_ACTION_PATH,
        "selector_producer": SELECTOR_PRODUCER_PATH,
        "selector_note": SELECTOR_NOTE_PATH,
    }
    for name, path in paths.items():
        if not path.is_file():
            raise FileNotFoundError(f"required primitive source is missing: {path}")
        actual = _lf_normalized_sha256(path)
        expected = EXPECTED_LF_SHA256[name]
        if actual != expected:
            raise ValueError(
                f"primitive source digest mismatch for {name}: {actual} != {expected}"
            )


def _load_selector_module() -> ModuleType:
    """Load the selector producer only after its digest has been authenticated."""

    actual = _lf_normalized_sha256(SELECTOR_PRODUCER_PATH)
    if actual != EXPECTED_LF_SHA256["selector_producer"]:
        raise ValueError("selector producer digest mismatch before module load")
    specification = importlib.util.spec_from_file_location(
        "_locked_frobenius_interferometry_subgroup_selectors",
        SELECTOR_PRODUCER_PATH,
    )
    if specification is None or specification.loader is None:
        raise ImportError("could not construct locked selector module specification")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    if dict(module.SELECTOR_EXPECTATIONS) != EXPECTED_SELECTOR_SIGNATURES:
        raise ValueError("selector signature sentinels drifted")
    if not callable(module.selector_values_from_squared_first_elementary):
        raise TypeError("locked selector coefficient adapter is missing")
    return module


def _validated_input() -> tuple[dict[str, object], list[Mapping[str, object]]]:
    """Authenticate every primitive and validate complete histogram semantics."""

    _verify_primitive_hashes()
    input_data = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    payload = dict(input_data)
    claimed = payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload) or claimed != EXPECTED_INPUT_PAYLOAD_SHA256:
        raise ValueError("balanced-control input payload/source pin mismatch")
    if input_data.get("schema") != "riemann.function_field.balanced_control_family_scan.v1":
        raise ValueError("unexpected balanced-control input schema")
    frozen = input_data.get("frozen_enumeration_facts")
    if not isinstance(frozen, dict):
        raise TypeError("balanced-control frozen facts must be an object")
    if frozen.get("status") != "EXHAUSTIVE_ONLY_FOR_Q_3_5_7":
        raise ValueError("balanced-control exhaustive coverage status drifted")
    if tuple(frozen.get("q_values", ())) != FROZEN_Q_VALUES:
        raise ValueError("balanced-control q ladder drifted")
    raw_families = frozen.get("families")
    if not isinstance(raw_families, list):
        raise TypeError("balanced-control families must be a list")
    families = sorted(raw_families, key=lambda row: int(row["q"]))
    if tuple(int(family["q"]) for family in families) != FROZEN_Q_VALUES:
        raise ValueError("balanced-control family rows drifted")

    locks = input_data["producer_and_source_locks"]["locks"]
    required_upstream_locks = {
        "producer": (
            "research/l-families/atlas/function_field/balanced_control_family_scan.py",
            EXPECTED_LF_SHA256["histogram_producer"],
        ),
        "coefficient_arithmetic": (
            "research/l-families/atlas/function_field/genus2_q_scan.py",
            EXPECTED_LF_SHA256["coefficient_arithmetic"],
        ),
        "affine_action": (
            "research/l-families/atlas/function_field/genus2_affine_orbits.py",
            EXPECTED_LF_SHA256["affine_action"],
        ),
    }
    for name, (expected_path, expected_digest) in required_upstream_locks.items():
        lock = locks.get(name)
        if not isinstance(lock, dict):
            raise ValueError(f"balanced-control source lock {name} is missing")
        if lock.get("path") != expected_path:
            raise ValueError(f"balanced-control source path drifted for {name}")
        if lock.get("sha256_lf_normalized") != expected_digest:
            raise ValueError(f"balanced-control embedded digest drifted for {name}")

    for family in families:
        q = _plain_int("q", family.get("q"))
        joint = family.get("joint_a_D_b_D_law")
        if not isinstance(joint, dict) or not isinstance(joint.get("atoms"), list):
            raise TypeError(f"q={q} joint coefficient law is malformed")
        atoms = joint["atoms"]
        if len(atoms) != EXPECTED_ATOM_COUNTS[q]:
            raise ValueError(f"q={q} joint atom-count sentinel drifted")
        if joint.get("support_size") != len(atoms):
            raise ValueError(f"q={q} joint support size drifted")
        member_count = _plain_int("member count", family.get("member_count"))
        if member_count != EXPECTED_MEMBER_COUNTS[q]:
            raise ValueError(f"q={q} member-count sentinel drifted")
        seen: set[tuple[int, int]] = set()
        mass = 0
        for atom in atoms:
            a = _plain_int("a_D", atom.get("a_D"))
            b = _plain_int("b_D", atom.get("b_D"))
            weight = _plain_int("atom member count", atom.get("member_count"))
            if weight <= 0:
                raise ValueError(f"q={q} joint histogram contains nonpositive mass")
            if (a, b) in seen:
                raise ValueError(f"q={q} joint histogram contains duplicate atoms")
            seen.add((a, b))
            mass += weight
        if mass != member_count:
            raise ValueError(f"q={q} joint histogram is not member-complete")
        if family.get("member_coefficient_ledger_sha256") != EXPECTED_MEMBER_LEDGER_SHA256[q]:
            raise ValueError(f"q={q} complete member-ledger sentinel drifted")
        if family.get("candidate_count") != q**5:
            raise ValueError(f"q={q} candidate coverage drifted")
        if family.get("expected_squarefree_count") != q**5 - q**4:
            raise ValueError(f"q={q} squarefree coverage drifted")
        orbit = family.get("affine_orbit_analysis")
        if not isinstance(orbit, dict) or orbit.get("B_D_invariant_on_every_orbit") is not True:
            raise ValueError(f"q={q} affine-orbit invariance source drifted")
    return input_data, families


def selector_values_from_arithmetic_coefficients(
    q: int,
    a: int,
    b: int,
    selector_module: ModuleType,
) -> dict[str, Fraction]:
    """Apply the locked adapter at ``A=a^2/q`` and ``e2=b/q``."""

    q = _plain_int("q", q)
    a = _plain_int("a", a)
    b = _plain_int("b", b)
    if q <= 1:
        raise ValueError("q must exceed one")
    raw = selector_module.selector_values_from_squared_first_elementary(
        Fraction(a * a, q), Fraction(b, q)
    )
    if set(raw) != set(ADAPTER_KEY_BY_SELECTOR.values()):
        raise ValueError("selector adapter returned unexpected keys")
    return {
        name: Fraction(raw[adapter_key])
        for name, adapter_key in ADAPTER_KEY_BY_SELECTOR.items()
    }


def integral_split_kind(q: int, a: int, b: int) -> str:
    """Formal integral factorization into two ``+q`` reciprocal quadratics."""

    delta = a * a - 4 * b + 8 * q
    if delta < 0:
        return "not_integral_plus_q_split"
    root = isqrt(delta)
    if root * root != delta or (root - a) % 2:
        return "not_integral_plus_q_split"
    return "repeated_plus_q_split" if delta == 0 else "distinct_plus_q_split"


def sym3_curve_residual(q: int, a: int, b: int) -> int:
    """Cleared normalized ``Sym^3(SU(2))`` coefficient-curve equation."""

    return -q * a**4 + q * a * a * b + q * q * a * a + b**3 - 2 * q * b * b


def sym3_generic_integer_trace_candidate(q: int, a: int, b: int) -> bool:
    """Algebraic integral-trace candidate, without a realization claim."""

    if sym3_curve_residual(q, a, b) != 0 or a * a == b:
        return False
    trace = Fraction(a * (q - b), a * a - b)
    return trace.denominator == 1 and trace * trace <= 4 * q


def _strata_for(q: int, a: int, b: int) -> frozenset[str]:
    split_kind = integral_split_kind(q, a, b)
    strata = set()
    if split_kind != "not_integral_plus_q_split":
        strata.add("integral_plus_q_split")
    if split_kind == "repeated_plus_q_split":
        strata.add("repeated_plus_q_split")
    if sym3_curve_residual(q, a, b) == 0:
        strata.add("sym3_coefficient_curve")
    if a == 0 and b == 0:
        strata.add("sym3_nodal_ghost")
    if sym3_generic_integer_trace_candidate(q, a, b):
        strata.add("sym3_generic_integer_trace_candidate")
    return frozenset(strata)


def _matrix_pairs(matrix: Sequence[Sequence[Fraction | int]]) -> list[list[list[int]]]:
    return [[_fraction_pair(value) for value in row] for row in matrix]


def _tail_packet(
    histogram: Mapping[Fraction, int], member_count: int
) -> tuple[dict[str, object], set[Fraction]]:
    """Return the outer absolute tail containing at least one percent, with ties."""

    target_count = ceil(member_count * ABSOLUTE_TAIL_TARGET)
    by_absolute: Counter[Fraction] = Counter()
    for value, weight in histogram.items():
        by_absolute[abs(value)] += weight
    accumulated = 0
    threshold: Fraction | None = None
    for absolute_value in sorted(by_absolute, reverse=True):
        accumulated += by_absolute[absolute_value]
        threshold = absolute_value
        if accumulated >= target_count:
            break
    if threshold is None:
        raise ArithmeticError("cannot form a tail from an empty histogram")
    values = {value for value in histogram if abs(value) >= threshold}
    sign_counts = Counter({"negative": 0, "zero": 0, "positive": 0})
    tail_count = 0
    for value in values:
        weight = histogram[value]
        tail_count += weight
        sign_counts[_sign(value)] += weight
    return (
        {
            "definition": "all members with |selector| at least the largest threshold whose tied tail has mass >= 1%",
            "target_fraction": _fraction_pair(ABSOLUTE_TAIL_TARGET),
            "target_member_count_ceiling": target_count,
            "absolute_threshold": _fraction_pair(threshold),
            "member_count_including_ties": tail_count,
            "member_fraction_including_ties": _fraction_pair(Fraction(tail_count, member_count)),
            "sign_member_counts": dict(sign_counts),
        },
        values,
    )


def _conditional_summary(
    records: Sequence[dict[str, object]],
    stratum: str,
    member_count: int,
    tail_values: Mapping[str, set[Fraction]],
) -> dict[str, object]:
    inside = [record for record in records if stratum in record["strata"]]
    outside = [record for record in records if stratum not in record["strata"]]
    inside_mass = sum(int(record["weight"]) for record in inside)
    outside_mass = member_count - inside_mass

    def means(rows: Sequence[dict[str, object]], mass: int) -> dict[str, Fraction]:
        if not mass:
            raise ZeroDivisionError("conditional mean needs positive mass")
        return {
            name: sum(
                int(record["weight"]) * record["values"][name] for record in rows
            )
            / mass
            for name in SELECTOR_ORDER
        }

    inside_means = means(inside, inside_mass) if inside_mass else None
    outside_means = means(outside, outside_mass) if outside_mass else None
    sign_counts = {
        name: Counter({"negative": 0, "zero": 0, "positive": 0})
        for name in SELECTOR_ORDER
    }
    tail_overlap = {name: 0 for name in SELECTOR_ORDER}
    for record in inside:
        weight = int(record["weight"])
        values = record["values"]
        for name in SELECTOR_ORDER:
            sign_counts[name][_sign(values[name])] += weight
            if values[name] in tail_values[name]:
                tail_overlap[name] += weight
    twist_states = {(int(row["a"]) ** 2, int(row["b"])) for row in inside}
    return {
        "status": (
            "NONEMPTY_EXACT_CONDITIONAL"
            if inside_mass and outside_mass
            else "EMPTY_IN_FROZEN_FAMILY"
            if not inside_mass
            else "FULL_FROZEN_FAMILY"
        ),
        "signed_source_atom_count": len(inside),
        "twist_quotiented_coefficient_state_count": len(twist_states),
        "member_count": inside_mass,
        "member_fraction": _fraction_pair(Fraction(inside_mass, member_count)),
        "conditional_mean": (
            {name: _fraction_pair(inside_means[name]) for name in SELECTOR_ORDER}
            if inside_means is not None
            else None
        ),
        "complement_mean": (
            {name: _fraction_pair(outside_means[name]) for name in SELECTOR_ORDER}
            if outside_means is not None
            else None
        ),
        "conditional_minus_complement": (
            {
                name: _fraction_pair(inside_means[name] - outside_means[name])
                for name in SELECTOR_ORDER
            }
            if inside_means is not None and outside_means is not None
            else None
        ),
        "conditional_sign_member_counts": {
            name: dict(sign_counts[name]) for name in SELECTOR_ORDER
        },
        "member_count_in_each_selector_outer_one_percent_tail": tail_overlap,
    }


def _orbit_identifiability(
    family: Mapping[str, object], records: Sequence[dict[str, object]]
) -> dict[str, object]:
    """Detect whether B-aggregated orbit counts determine selector orbit laws."""

    by_b: dict[int, list[dict[str, object]]] = defaultdict(list)
    for record in records:
        by_b[int(record["B_numerator_J"])].append(record)
    ambiguous = []
    for b_numerator in sorted(by_b):
        rows = by_b[b_numerator]
        triples = {
            tuple(record["values"][name] for name in SELECTOR_ORDER)
            for record in rows
        }
        if len(triples) > 1:
            ambiguous.append(
                {
                    "B_numerator_J": b_numerator,
                    "distinct_selector_triple_count": len(triples),
                    "member_count": sum(int(record["weight"]) for record in rows),
                }
            )
    ambiguous_mass = sum(row["member_count"] for row in ambiguous)
    orbit = family["affine_orbit_analysis"]
    if ambiguous:
        status = "NOT_IDENTIFIABLE_FROM_B_AGGREGATED_ORBIT_SOURCE"
        exact_law = None
    else:
        status = "IDENTIFIABLE_FROM_B_AGGREGATED_ORBIT_SOURCE"
        exact_law = "not constructed because no frozen field reaches this branch"
    return {
        "status": status,
        "selector_invariance": (
            "the locked affine action changes a_D only by sign and fixes b_D; "
            "P,D,S depend only on (a_D^2,b_D), so each selector is orbit-invariant"
        ),
        "source_total_affine_orbit_count": orbit["orbit_count"],
        "source_orbit_size_histogram": orbit["orbit_size_histogram"],
        "source_aggregation": "exact orbit counts are retained only by B_numerator_J",
        "B_bucket_count": len(by_b),
        "ambiguous_B_bucket_count": len(ambiguous),
        "member_count_in_ambiguous_B_buckets": ambiguous_mass,
        "ambiguous_B_buckets": ambiguous,
        "exact_uniform_orbit_selector_law": exact_law,
        "refusal_reason": (
            "an ambiguous B bucket contains multiple selector triples but only one "
            "aggregate orbit count, so allocating its orbits would add information "
            "not present in the source"
            if ambiguous
            else None
        ),
    }


def analyze_family(
    family: Mapping[str, object],
    selector_module: ModuleType,
    guard: SourceAtomGuard,
) -> dict[str, object]:
    q = int(family["q"])
    member_count = int(family["member_count"])
    atoms = family["joint_a_D_b_D_law"]["atoms"]
    records: list[dict[str, object]] = []
    joint_histogram: Counter[tuple[Fraction, Fraction, Fraction]] = Counter()
    marginals: dict[str, Counter[Fraction]] = {
        name: Counter() for name in SELECTOR_ORDER
    }
    sums = {name: Fraction(0) for name in SELECTOR_ORDER}
    second_sums = {
        (left, right): Fraction(0)
        for left in SELECTOR_ORDER
        for right in SELECTOR_ORDER
    }
    for atom in atoms:
        guard.charge(f"q_{q}_source_atoms")
        a = int(atom["a_D"])
        b = int(atom["b_D"])
        weight = int(atom["member_count"])
        values = selector_values_from_arithmetic_coefficients(
            q, a, b, selector_module
        )
        triple = tuple(values[name] for name in SELECTOR_ORDER)
        joint_histogram[triple] += weight
        for name in SELECTOR_ORDER:
            marginals[name][values[name]] += weight
            sums[name] += weight * values[name]
        for left in SELECTOR_ORDER:
            for right in SELECTOR_ORDER:
                second_sums[left, right] += weight * values[left] * values[right]
        records.append(
            {
                "a": a,
                "b": b,
                "weight": weight,
                "B_numerator_J": int(atom["B_numerator_J"]),
                "values": values,
                "strata": _strata_for(q, a, b),
            }
        )
    if sum(joint_histogram.values()) != member_count:
        raise ArithmeticError(f"q={q} selector pushforward lost member mass")

    means = {name: sums[name] / member_count for name in SELECTOR_ORDER}
    raw_second = [
        [second_sums[left, right] / member_count for right in SELECTOR_ORDER]
        for left in SELECTOR_ORDER
    ]
    covariance = [
        [
            raw_second[left_index][right_index]
            - means[left] * means[right]
            for right_index, right in enumerate(SELECTOR_ORDER)
        ]
        for left_index, left in enumerate(SELECTOR_ORDER)
    ]

    tail_packets: dict[str, dict[str, object]] = {}
    tail_values: dict[str, set[Fraction]] = {}
    marginal_packets = {}
    for name in SELECTOR_ORDER:
        histogram = marginals[name]
        tail_packet, values_in_tail = _tail_packet(histogram, member_count)
        tail_packets[name] = tail_packet
        tail_values[name] = values_in_tail
        sign_counts = Counter({"negative": 0, "zero": 0, "positive": 0})
        for value, weight in histogram.items():
            sign_counts[_sign(value)] += weight
        maximum_absolute = max(abs(value) for value in histogram)
        marginal_packets[name] = {
            "support_size": len(histogram),
            "support_minimum": _fraction_pair(min(histogram)),
            "support_maximum": _fraction_pair(max(histogram)),
            "maximum_absolute_value": _fraction_pair(maximum_absolute),
            "mean": _fraction_pair(means[name]),
            "mean_absolute_value": _fraction_pair(
                sum(weight * abs(value) for value, weight in histogram.items())
                / member_count
            ),
            "sign_member_counts": dict(sign_counts),
            "outer_one_percent_absolute_tail": tail_packet,
            "atom_columns": ["value_numerator", "value_denominator", "member_count"],
            "atoms": [
                [value.numerator, value.denominator, histogram[value]]
                for value in sorted(histogram)
            ],
        }

    stratum_names = (
        "integral_plus_q_split",
        "repeated_plus_q_split",
        "sym3_coefficient_curve",
        "sym3_nodal_ghost",
        "sym3_generic_integer_trace_candidate",
    )
    strata = {
        name: _conditional_summary(records, name, member_count, tail_values)
        for name in stratum_names
    }

    return {
        "q": q,
        "status": "EXACT_MEMBER_WEIGHT_LAW_FROM_FROZEN_COMPLETE_HISTOGRAM",
        "member_count": member_count,
        "input_signed_source_atom_count": len(atoms),
        "twist_quotiented_input_state_count": len(
            {(int(atom["a_D"]) ** 2, int(atom["b_D"])) for atom in atoms}
        ),
        "joint_selector_law": {
            "support_size": len(joint_histogram),
            "atom_columns": [
                "P_numerator",
                "P_denominator",
                "D_numerator",
                "D_denominator",
                "S_numerator",
                "S_denominator",
                "member_count",
            ],
            "atoms": [
                [
                    triple[0].numerator,
                    triple[0].denominator,
                    triple[1].numerator,
                    triple[1].denominator,
                    triple[2].numerator,
                    triple[2].denominator,
                    joint_histogram[triple],
                ]
                for triple in sorted(joint_histogram)
            ],
        },
        "marginal_selector_laws": marginal_packets,
        "mean_vector_P_D_S": [_fraction_pair(means[name]) for name in SELECTOR_ORDER],
        "raw_second_moment_matrix_P_D_S": _matrix_pairs(raw_second),
        "covariance_matrix_P_D_S": _matrix_pairs(covariance),
        "ambient_haar_comparison": {
            "ambient_mean_vector": [[0, 1], [0, 1], [0, 1]],
            "ambient_gram_matrix": [list(row) for row in AMBIENT_GRAM],
            "finite_minus_ambient_mean": [
                _fraction_pair(means[name]) for name in SELECTOR_ORDER
            ],
            "warning": (
                "finite-family means and covariance are exact census outputs, not "
                "equidistribution errors or subgroup-mixture estimates"
            ),
        },
        "exceptional_coefficient_strata": strata,
        "uniform_affine_orbit_weighting": _orbit_identifiability(family, records),
    }


def build_fixture() -> dict[str, object]:
    input_data, families = _validated_input()
    selector_module = _load_selector_module()
    guard = SourceAtomGuard()
    source_atom_total = sum(
        len(family["joint_a_D_b_D_law"]["atoms"]) for family in families
    )
    guard.preflight(source_atom_total)
    analyses = [
        analyze_family(family, selector_module, guard) for family in families
    ]
    if tuple(row["q"] for row in analyses) != FROZEN_Q_VALUES:
        raise ArithmeticError("output q ladder drifted")
    if guard.total != source_atom_total:
        raise ArithmeticError("source-atom accounting drifted")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_interferometry_arithmetic_pushforward.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.INTERFEROMETRY.ARITHMETIC_PUSHFORWARD.Q3_Q5_Q7.V1",
        "status": "EXACT_BOUNDED_TRANSFORM_OF_SOURCE_LOCKED_COMPLETE_HISTOGRAMS",
        "scope": (
            "member-uniform monic squarefree quintics over F_q for exactly q=3,5,7, "
            "using only the frozen complete coefficient histograms"
        ),
        "normalization_and_adapter": {
            "source_reciprocal_quartic": "T^4+a_D*T^3+b_D*T^2+q*a_D*T+q^2",
            "normalized_selector_quartic": "Z^4-e1*Z^3+e2*Z^2-e1*Z+1",
            "sign_relation": "e1=-a_D/sqrt(q), irrelevant because P,D,S are even in e1",
            "rational_coordinates": "A=e1^2=a_D^2/q and e2=b_D/q",
            "adapter": "selector_values_from_squared_first_elementary(A,e2)",
            "selector_definitions": {
                "P": "I_(2,2)-I_(4,4)",
                "D": "-I_(1,1)+2*I_(1,5)+I_(4,4)",
                "S": "-2*I_(2,8)",
                "I_(r,s)": "p_r*p_s-p_(r+s)",
            },
            "selector_order": list(SELECTOR_ORDER),
        },
        "exact_frozen_member_weight_laws": {
            "status": "EXACT_ONLY_FOR_Q_3_5_7",
            "weighting": (
                "uniform weight on every monic squarefree quintic member, inherited "
                "without reweighting from the locked joint coefficient histogram"
            ),
            "families": analyses,
        },
        "exceptional_stratum_contract": {
            "integral_plus_q_split": (
                "formal factorization into two integral reciprocal quadratics with "
                "constant q; this is a coefficient predicate, not a polarization theorem"
            ),
            "repeated_plus_q_split": (
                "the repeated-factor sublocus a_D^2-4*b_D+8*q=0"
            ),
            "sym3_coefficient_curve": (
                "the cleared compact Sym^3 coefficient equation "
                "-q*a^4+q*a^2*b+q^2*a^2+b^3-2*q*b^2=0"
            ),
            "sym3_nodal_ghost": (
                "the point (a,b)=(0,0), on the coefficient curve but not an odd-q "
                "integral elliptic Sym^3 trace image"
            ),
            "sym3_generic_integer_trace_candidate": (
                "off the nodal divisor, the recovered t=a(q-b)/(a^2-b) is integral "
                "and Hasse-admissible; no origin or monodromy claim is made"
            ),
        },
        "conjecture_boundary": {
            "status": "NO_ALL_Q_CONJECTURE_PROPOSED",
            "exact": (
                "every displayed q=3,5,7 law, mean, covariance, sign count, tied "
                "one-percent tail, and exceptional-stratum conditional"
            ),
            "not_inferred": (
                "no rational function of q, limiting mean, equidistribution rate, "
                "subgroup mixture, monodromy classification, or memberwise diagnosis"
            ),
            "smallest_natural_next_theorem": (
                "evaluate the exact all-q joint coefficient moments required by the "
                "three adapter polynomials, then prove an error term before comparing "
                "finite means with compact-subgroup Haar signatures"
            ),
        },
        "interpretation_firewall": {
            "compact_theorem": (
                "the locked packet proves ambient Haar means zero and the named subgroup "
                "Haar signatures (2,0,0), (0,2,0), and (0,0,2)"
            ),
            "finite_arithmetic_fact": (
                "this packet computes exact selector laws on three frozen member-uniform families"
            ),
            "forbidden_reading": (
                "a finite mean, sign, tail, or coefficient-locus conditional does not "
                "identify monodromy, an endomorphism, a correspondence, a motive, or an "
                "equidistribution law and has no RH/GRH implication"
            ),
            "orbit_measure_warning": (
                "member-uniform and uniform affine-orbit laws differ; the latter is "
                "refused where the B-aggregated source does not identify it"
            ),
        },
        "resource_contract": {
            "finite_field_enumeration": False,
            "polynomial_or_curve_enumeration": False,
            "root_finding": False,
            "random_sampling": False,
            "floating_point_arithmetic": False,
            "source_atom_cap_inclusive": SOURCE_ATOM_CAP_INCLUSIVE,
            "source_atom_preflight_count": source_atom_total,
            "guarded_source_atom_visits": guard.snapshot(),
            "external_dependencies": "none; Python 3.11+ standard library",
        },
        "producer_and_source_locks": {
            "validation_order": (
                "LF-normalized primitive digests are checked before JSON parsing or "
                "selector-module execution; payload, embedded producer locks, coverage, "
                "member ledgers, atom counts, and member mass are then checked"
            ),
            "required_input_payload_sha256": EXPECTED_INPUT_PAYLOAD_SHA256,
            "required_member_ledger_sha256": {
                str(q): EXPECTED_MEMBER_LEDGER_SHA256[q] for q in FROZEN_Q_VALUES
            },
            "required_lf_sha256": dict(EXPECTED_LF_SHA256),
            "locks": {
                "histogram_fixture": {
                    "path": "research/l-families/atlas/function_field/balanced_control_family_scan.json",
                    "sha256_lf_normalized": _lf_normalized_sha256(INPUT_PATH),
                    "payload_sha256": input_data["payload_sha256"],
                },
                "histogram_producer": {
                    "path": "research/l-families/atlas/function_field/balanced_control_family_scan.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(INPUT_PRODUCER_PATH),
                },
                "coefficient_arithmetic": {
                    "path": "research/l-families/atlas/function_field/genus2_q_scan.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(COEFFICIENT_ARITHMETIC_PATH),
                },
                "affine_action": {
                    "path": "research/l-families/atlas/function_field/genus2_affine_orbits.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(AFFINE_ACTION_PATH),
                },
                "selector_producer": {
                    "path": "research/l-families/atlas/function_field/frobenius_interferometry_subgroup_selectors.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(SELECTOR_PRODUCER_PATH),
                },
                "selector_note": {
                    "path": "research/l-families/atlas/function_field/FROBENIUS_INTERFEROMETRY_SUBGROUP_SELECTORS.md",
                    "sha256_lf_normalized": _lf_normalized_sha256(SELECTOR_NOTE_PATH),
                },
                "producer": {
                    "path": "research/l-families/atlas/function_field/genus2_interferometry_arithmetic_pushforward.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(Path(__file__)),
                },
                "note": {
                    "path": "research/l-families/atlas/function_field/GENUS2_INTERFEROMETRY_ARITHMETIC_PUSHFORWARD.md",
                    "sha256_lf_normalized": _lf_normalized_sha256(NOTE_PATH),
                },
                "test": {
                    "path": "tests/test_genus2_interferometry_arithmetic_pushforward.py",
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
            "genus2 interferometry arithmetic pushforward: "
            f"q={FROZEN_Q_VALUES} atoms={fixture['resource_contract']['source_atom_preflight_count']} "
            f"payload_sha256={fixture['payload_sha256']}"
        )
        return 0
    if not args.path.is_file() or args.path.read_text(encoding="utf-8") != rendered:
        print(f"stale or missing fixture: {args.path}")
        return 1
    print(
        "genus2 interferometry arithmetic pushforward check: ok "
        f"payload_sha256={fixture['payload_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
