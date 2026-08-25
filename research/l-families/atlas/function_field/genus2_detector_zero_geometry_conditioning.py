#!/usr/bin/env python3
"""Exact detector/zero-geometry conditioning on frozen genus-two histograms.

The only arithmetic data read by this producer are the complete source-locked
``(a_D,b_D)`` histograms for q=3,5,7.  It never enumerates a field, polynomial,
curve, or member and never finds a root.  It pushes every histogram atom
through the locked rational coefficient adapter for the interferometry
selectors P,D,S and through two twist-invariant spectral proxies

    C = Q(1)Q(-1) = (2+b/q)^2 - 4a^2/q,
    G = Delta/q   = a^2/q - 4b/q + 8.

Every claim payload is integral or rational.  Primitive files are authenticated
before JSON parsing or dynamic module execution, and the transform refuses
more than 4,096 source atoms.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from types import ModuleType

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUT_PATH = HERE / "balanced_control_family_scan.json"
INPUT_PRODUCER_PATH = HERE / "balanced_control_family_scan.py"
COEFFICIENT_ARITHMETIC_PATH = HERE / "genus2_q_scan.py"
AFFINE_ACTION_PATH = HERE / "genus2_affine_orbits.py"
SELECTOR_PRODUCER_PATH = HERE / "frobenius_interferometry_subgroup_selectors.py"
SELECTOR_NOTE_PATH = HERE / "FROBENIUS_INTERFEROMETRY_SUBGROUP_SELECTORS.md"
OUTPUT_PATH = HERE / "genus2_detector_zero_geometry_conditioning.json"
NOTE_PATH = HERE / "GENUS2_DETECTOR_ZERO_GEOMETRY_CONDITIONING.md"
TEST_PATH = ROOT / "tests" / "test_genus2_detector_zero_geometry_conditioning.py"

FROZEN_Q_VALUES = (3, 5, 7)
SELECTOR_ORDER = ("P", "D", "S")
PROXY_ORDER = ("C", "G")
SIGN_ORDER = ("negative", "zero", "positive")
ADAPTER_KEY_BY_SELECTOR = {
    "P": "product_selector",
    "D": "doubled_selector",
    "S": "sym3_selector",
}
SOURCE_ATOM_CAP_INCLUSIVE = 4_096

EXPECTED_LF_SHA256 = {
    "histogram_fixture": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
    "histogram_producer": "7192fa26b0ea17cb68cff288620ea4dfb124e07807986d9c74fbd37e66087d3b",
    "coefficient_arithmetic": "f595dbf52d4265cfe2ea6888255f53df887fed77e204103f2b0dfd95e961f935",
    "affine_action": "32e440750b2832ec4cc84473187b4b1aa6396eda87c64f5ac845b2a96dc88f08",
    "selector_producer": "48474ebcbb99efea23227126f66f566fdb525a3c9ae9e81a77bf83d4075f55e7",
    "selector_note": "c7637d454f1fb102555e6723dd8d93a4b6a27363d80cbbb9a03061f614bd3221",
    "note": "646017184761427a214350eb356606c20a335fe0918172213caa7505362736be",
    "test": "7615baf67ad0c3326616e64bc4fda68f750d86959e5af805fe610da1506c4dfc",
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


def _pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _plain_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be a plain integer")
    return value


def _sign(value: Fraction) -> str:
    return "negative" if value < 0 else "positive" if value > 0 else "zero"


@dataclass
class SourceAtomGuard:
    cap: int = SOURCE_ATOM_CAP_INCLUSIVE
    counts: Counter[str] = field(default_factory=Counter)

    @property
    def total(self) -> int:
        return sum(self.counts.values())

    def preflight(self, amount: int) -> None:
        amount = _plain_int("source atom count", amount)
        if amount < 0:
            raise ValueError("source atom count must be nonnegative")
        if amount > self.cap:
            raise RuntimeError(
                f"source atom count {amount} exceeds inclusive cap {self.cap}"
            )

    def charge(self, name: str, amount: int = 1) -> None:
        amount = _plain_int("source atom charge", amount)
        if amount < 0:
            raise ValueError("source atom charge must be nonnegative")
        if self.total + amount > self.cap:
            raise RuntimeError(
                f"source atom transform would exceed inclusive cap {self.cap}"
            )
        self.counts[name] += amount

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
        "note": NOTE_PATH,
        "test": TEST_PATH,
    }
    for name, path in paths.items():
        if not path.is_file():
            raise FileNotFoundError(f"required source is missing: {path}")
        actual = _lf_sha256(path)
        expected = EXPECTED_LF_SHA256[name]
        if actual != expected:
            raise ValueError(
                f"source digest mismatch for {name}: {actual} != {expected}"
            )


def _load_selector_module() -> ModuleType:
    actual = _lf_sha256(SELECTOR_PRODUCER_PATH)
    if actual != EXPECTED_LF_SHA256["selector_producer"]:
        raise ValueError("selector producer digest mismatch before module load")
    spec = importlib.util.spec_from_file_location(
        "_locked_zero_geometry_selector_adapter", SELECTOR_PRODUCER_PATH
    )
    if spec is None or spec.loader is None:
        raise ImportError("could not construct locked selector module specification")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if dict(module.SELECTOR_EXPECTATIONS) != EXPECTED_SELECTOR_SIGNATURES:
        raise ValueError("selector signature sentinels drifted")
    if not callable(module.selector_values_from_squared_first_elementary):
        raise TypeError("locked rational selector adapter is missing")
    return module


def _validated_families() -> tuple[dict[str, object], list[Mapping[str, object]]]:
    _verify_primitive_hashes()
    data = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    payload = dict(data)
    claimed = payload.pop("payload_sha256", None)
    if (
        claimed != _canonical_sha256(payload)
        or claimed != EXPECTED_INPUT_PAYLOAD_SHA256
    ):
        raise ValueError("balanced-control payload/source pin mismatch")
    if data.get("schema") != "riemann.function_field.balanced_control_family_scan.v1":
        raise ValueError("unexpected balanced-control schema")
    frozen = data.get("frozen_enumeration_facts")
    if not isinstance(frozen, dict):
        raise TypeError("frozen enumeration facts must be an object")
    if frozen.get("status") != "EXHAUSTIVE_ONLY_FOR_Q_3_5_7":
        raise ValueError("frozen exhaustive-coverage status drifted")
    if tuple(frozen.get("q_values", ())) != FROZEN_Q_VALUES:
        raise ValueError("frozen q ladder drifted")
    families = sorted(frozen.get("families", []), key=lambda row: int(row["q"]))
    if tuple(int(row["q"]) for row in families) != FROZEN_Q_VALUES:
        raise ValueError("family rows drifted")

    locks = data["producer_and_source_locks"]["locks"]
    embedded = {
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
    for name, (path, digest) in embedded.items():
        lock = locks.get(name)
        if not isinstance(lock, dict):
            raise TypeError(f"embedded source lock is missing: {name}")
        if lock.get("path") != path or lock.get("sha256_lf_normalized") != digest:
            raise ValueError(f"embedded source lock drifted: {name}")

    for family in families:
        q = _plain_int("q", family.get("q"))
        if q not in EXPECTED_ATOM_COUNTS:
            raise ValueError(f"unexpected field q={q}")
        member_count = _plain_int("member count", family.get("member_count"))
        if member_count != EXPECTED_MEMBER_COUNTS[q]:
            raise ValueError(f"q={q} member-count sentinel drifted")
        if family.get("candidate_count") != q**5:
            raise ValueError(f"q={q} candidate coverage drifted")
        if family.get("expected_squarefree_count") != q**5 - q**4:
            raise ValueError(f"q={q} squarefree coverage drifted")
        if (
            family.get("member_coefficient_ledger_sha256")
            != EXPECTED_MEMBER_LEDGER_SHA256[q]
        ):
            raise ValueError(f"q={q} complete member-ledger sentinel drifted")
        joint = family.get("joint_a_D_b_D_law")
        if not isinstance(joint, dict) or not isinstance(joint.get("atoms"), list):
            raise TypeError(f"q={q} joint coefficient law is malformed")
        atoms = joint["atoms"]
        if len(atoms) != EXPECTED_ATOM_COUNTS[q] or joint.get("support_size") != len(
            atoms
        ):
            raise ValueError(f"q={q} source atom-count sentinel drifted")
        seen: set[tuple[int, int]] = set()
        mass = 0
        for atom in atoms:
            a = _plain_int("a_D", atom.get("a_D"))
            b = _plain_int("b_D", atom.get("b_D"))
            weight = _plain_int("atom member count", atom.get("member_count"))
            if weight <= 0 or (a, b) in seen:
                raise ValueError(f"q={q} malformed or duplicate histogram atom")
            seen.add((a, b))
            mass += weight
        if mass != member_count:
            raise ValueError(f"q={q} source histogram is not member-complete")
    return data, families


def selector_values(q: int, a: int, b: int, module: ModuleType) -> dict[str, Fraction]:
    raw = module.selector_values_from_squared_first_elementary(
        Fraction(a * a, q), Fraction(b, q)
    )
    if set(raw) != set(ADAPTER_KEY_BY_SELECTOR.values()):
        raise ValueError("selector adapter returned unexpected keys")
    return {name: Fraction(raw[key]) for name, key in ADAPTER_KEY_BY_SELECTOR.items()}


def spectral_proxies(q: int, a: int, b: int) -> dict[str, Fraction]:
    """Evaluate C and G from source coefficients, with no roots or floats."""

    q = _plain_int("q", q)
    a = _plain_int("a", a)
    b = _plain_int("b", b)
    if q <= 1:
        raise ValueError("q must exceed one")
    return {
        "C": (Fraction(2) + Fraction(b, q)) ** 2 - Fraction(4 * a * a, q),
        "G": Fraction(a * a - 4 * b + 8 * q, q),
    }


def spectral_proxy_cosine_identities(x: Fraction, y: Fraction) -> dict[str, Fraction]:
    """Return both sides of the two root-free cosine-coordinate identities."""

    x = Fraction(x)
    y = Fraction(y)
    e1 = 2 * (x + y)
    e2 = 2 + 4 * x * y
    return {
        "C_from_coefficients": (2 + e2) ** 2 - 4 * e1**2,
        "C_from_cosines": 16 * (1 - x**2) * (1 - y**2),
        "G_from_coefficients": e1**2 - 4 * e2 + 8,
        "G_from_cosines": 4 * (x - y) ** 2,
    }


def _matrix_pairs(matrix: Sequence[Sequence[Fraction]]) -> list[list[list[int]]]:
    return [[_pair(value) for value in row] for row in matrix]


def _proxy_statistics(
    histogram: Mapping[tuple[Fraction, Fraction], int], mass: int
) -> dict[str, object]:
    if mass <= 0 or sum(histogram.values()) != mass:
        raise ValueError("proxy statistics require positive complete mass")
    means = [
        sum(weight * point[index] for point, weight in histogram.items()) / mass
        for index in range(2)
    ]
    raw_second = [
        [
            sum(
                weight * point[left] * point[right]
                for point, weight in histogram.items()
            )
            / mass
            for right in range(2)
        ]
        for left in range(2)
    ]
    covariance = [
        [raw_second[left][right] - means[left] * means[right] for right in range(2)]
        for left in range(2)
    ]
    certificate_counts = {
        "C_zero_endpoint_certificate": sum(
            weight for (c, _), weight in histogram.items() if c == 0
        ),
        "G_zero_repeated_cosine_certificate": sum(
            weight for (_, g), weight in histogram.items() if g == 0
        ),
        "C_and_G_zero": sum(
            weight for (c, g), weight in histogram.items() if c == 0 and g == 0
        ),
    }
    positive_c = [c for c, _ in histogram if c > 0]
    positive_g = [g for _, g in histogram if g > 0]
    return {
        "member_count": mass,
        "support_size": len(histogram),
        "mean_C_G": [_pair(value) for value in means],
        "raw_second_moment_matrix_C_G": _matrix_pairs(raw_second),
        "covariance_matrix_C_G": _matrix_pairs(covariance),
        "certificate_member_counts": certificate_counts,
        "minimum_strictly_positive_C": _pair(min(positive_c)) if positive_c else None,
        "minimum_strictly_positive_G": _pair(min(positive_g)) if positive_g else None,
        "atom_columns": [
            "C_numerator",
            "C_denominator",
            "G_numerator",
            "G_denominator",
            "member_count",
        ],
        "atoms": [
            [c.numerator, c.denominator, g.numerator, g.denominator, histogram[c, g]]
            for c, g in sorted(histogram)
        ],
    }


def _state_packet(rows: Sequence[dict[str, object]]) -> dict[str, object]:
    by_state: Counter[tuple[int, int]] = Counter()
    for row in rows:
        by_state[(int(row["a"]) ** 2, int(row["b"]))] += int(row["weight"])
    return {
        "twist_quotiented_state_count": len(by_state),
        "states": [
            {"a_squared": key[0], "b": key[1], "member_count": by_state[key]}
            for key in sorted(by_state)
        ],
    }


def _witness_packet(
    value: Fraction,
    points: Sequence[tuple[Fraction, Fraction]],
    rows: Sequence[dict[str, object]],
) -> dict[str, object]:
    selected_points = (min(points), max(points))
    witnesses = []
    for point in selected_points:
        matching = [
            row for row in rows if row["proxies"] == {"C": point[0], "G": point[1]}
        ]
        witnesses.append(
            {
                "C": _pair(point[0]),
                "G": _pair(point[1]),
                "source_states": _state_packet(matching),
            }
        )
    return {
        "selector_value": _pair(value),
        "distinct_proxy_pair_count_at_value": len(points),
        "witnesses": witnesses,
    }


def _same_value_counterexamples(
    records: Sequence[dict[str, object]], selector: str
) -> dict[str, object]:
    by_value: dict[Fraction, list[dict[str, object]]] = defaultdict(list)
    for record in records:
        by_value[record["selectors"][selector]].append(record)

    multi: list[
        tuple[int, Fraction, list[tuple[Fraction, Fraction]], list[dict[str, object]]]
    ] = []
    c_certificate: list[
        tuple[Fraction, list[tuple[Fraction, Fraction]], list[dict[str, object]]]
    ] = []
    g_certificate: list[
        tuple[Fraction, list[tuple[Fraction, Fraction]], list[dict[str, object]]]
    ] = []
    for value, rows in by_value.items():
        points = sorted({(row["proxies"]["C"], row["proxies"]["G"]) for row in rows})
        if len(points) > 1:
            multi.append((len(points), value, points, rows))
        if any(c == 0 for c, _ in points) and any(c != 0 for c, _ in points):
            c_certificate.append((value, points, rows))
        if any(g == 0 for _, g in points) and any(g != 0 for _, g in points):
            g_certificate.append((value, points, rows))

    strongest = None
    if multi:
        _, value, points, rows = min(multi, key=lambda item: (-item[0], item[1]))
        strongest = _witness_packet(value, points, rows)

    def certificate_witness(
        candidates: Sequence[
            tuple[Fraction, list[tuple[Fraction, Fraction]], list[dict[str, object]]]
        ],
        coordinate: int,
    ) -> dict[str, object] | None:
        if not candidates:
            return None
        value, points, rows = min(candidates, key=lambda item: item[0])
        zero_point = min(point for point in points if point[coordinate] == 0)
        nonzero_point = min(point for point in points if point[coordinate] != 0)
        return _witness_packet(value, [zero_point, nonzero_point], rows)

    return {
        "selector_value_count": len(by_value),
        "values_with_multiple_proxy_pairs": len(multi),
        "strongest_distinct_proxy_pair_witness": strongest,
        "same_value_C_certificate_vs_noncertificate_witness": certificate_witness(
            c_certificate, 0
        ),
        "same_value_G_certificate_vs_noncertificate_witness": certificate_witness(
            g_certificate, 1
        ),
        "conclusion": (
            "the detector value does not determine endpoint proximity or cosine separation"
            if multi
            else "no same-value ambiguity was found in this frozen support"
        ),
    }


def _condition_on_sign(
    records: Sequence[dict[str, object]], selector: str, sign: str, total_mass: int
) -> dict[str, object]:
    rows = [row for row in records if _sign(row["selectors"][selector]) == sign]
    mass = sum(int(row["weight"]) for row in rows)
    if not mass:
        return {
            "status": "EMPTY_SIGN_STRATUM",
            "member_count": 0,
            "member_fraction": [0, 1],
            "proxy_law": None,
        }
    histogram: Counter[tuple[Fraction, Fraction]] = Counter()
    for row in rows:
        point = (row["proxies"]["C"], row["proxies"]["G"])
        histogram[point] += int(row["weight"])
    return {
        "status": "EXACT_NONEMPTY_SIGN_CONDITIONAL",
        "member_count": mass,
        "member_fraction": _pair(Fraction(mass, total_mass)),
        "proxy_law": _proxy_statistics(histogram, mass),
    }


def analyze_family(
    family: Mapping[str, object], module: ModuleType, guard: SourceAtomGuard
) -> dict[str, object]:
    q = int(family["q"])
    member_count = int(family["member_count"])
    records: list[dict[str, object]] = []
    full_proxy_histogram: Counter[tuple[Fraction, Fraction]] = Counter()
    all_values: dict[str, list[tuple[Fraction, Fraction, Fraction, int]]] = {
        name: [] for name in SELECTOR_ORDER
    }
    for atom in family["joint_a_D_b_D_law"]["atoms"]:
        guard.charge(f"q_{q}_source_atoms")
        a = int(atom["a_D"])
        b = int(atom["b_D"])
        weight = int(atom["member_count"])
        selectors = selector_values(q, a, b, module)
        proxies = spectral_proxies(q, a, b)
        if proxies["C"] < 0 or proxies["G"] < 0:
            raise ArithmeticError(
                f"q={q} normalized spectral proxy left its exact nonnegative cone"
            )
        record = {
            "a": a,
            "b": b,
            "weight": weight,
            "selectors": selectors,
            "proxies": proxies,
        }
        records.append(record)
        full_proxy_histogram[(proxies["C"], proxies["G"])] += weight
        for name in SELECTOR_ORDER:
            all_values[name].append(
                (selectors[name], proxies["C"], proxies["G"], weight)
            )
    if sum(full_proxy_histogram.values()) != member_count:
        raise ArithmeticError(f"q={q} proxy pushforward lost member mass")

    selector_packets = {}
    for name in SELECTOR_ORDER:
        rows = all_values[name]
        mean_selector = (
            sum(value * weight for value, _, _, weight in rows) / member_count
        )
        mean_c = sum(c * weight for _, c, _, weight in rows) / member_count
        mean_g = sum(g * weight for _, _, g, weight in rows) / member_count
        cov_c = (
            sum(value * c * weight for value, c, _, weight in rows) / member_count
            - mean_selector * mean_c
        )
        cov_g = (
            sum(value * g * weight for value, _, g, weight in rows) / member_count
            - mean_selector * mean_g
        )
        conditionals = {
            sign: _condition_on_sign(records, name, sign, member_count)
            for sign in SIGN_ORDER
        }
        positive_law = conditionals["positive"]["proxy_law"]
        negative_law = conditionals["negative"]["proxy_law"]
        contrast = None
        if positive_law is not None and negative_law is not None:
            contrast = [
                _pair(
                    Fraction(
                        positive_law["mean_C_G"][index][0],
                        positive_law["mean_C_G"][index][1],
                    )
                    - Fraction(
                        negative_law["mean_C_G"][index][0],
                        negative_law["mean_C_G"][index][1],
                    )
                )
                for index in range(2)
            ]
        selector_packets[name] = {
            "mean": _pair(mean_selector),
            "covariance_with_C_G": [_pair(cov_c), _pair(cov_g)],
            "sign_partition": "negative / zero / positive; no empirical quantile or fitted threshold",
            "sign_conditionals": conditionals,
            "positive_minus_negative_conditional_mean_C_G": contrast,
            "same_value_counterexamples": _same_value_counterexamples(records, name),
        }

    return {
        "q": q,
        "status": "EXACT_MEMBER_WEIGHT_CONDITIONING_FROM_COMPLETE_FROZEN_HISTOGRAM",
        "member_count": member_count,
        "input_signed_source_atom_count": len(records),
        "twist_quotiented_input_state_count": len(
            {(int(row["a"]) ** 2, int(row["b"])) for row in records}
        ),
        "full_proxy_law": _proxy_statistics(full_proxy_histogram, member_count),
        "selector_conditioning": selector_packets,
    }


def build_fixture() -> dict[str, object]:
    input_data, families = _validated_families()
    module = _load_selector_module()
    guard = SourceAtomGuard()
    source_atom_total = sum(len(row["joint_a_D_b_D_law"]["atoms"]) for row in families)
    guard.preflight(source_atom_total)
    analyses = [analyze_family(family, module, guard) for family in families]
    if (
        tuple(row["q"] for row in analyses) != FROZEN_Q_VALUES
        or guard.total != source_atom_total
    ):
        raise ArithmeticError("q ladder or source-atom accounting drifted")

    identity_checks = []
    for x, y in (
        (Fraction(-1), Fraction(2, 3)),
        (Fraction(-2, 5), Fraction(1, 7)),
        (Fraction(0), Fraction(1)),
    ):
        values = spectral_proxy_cosine_identities(x, y)
        if values["C_from_coefficients"] != values["C_from_cosines"]:
            raise ArithmeticError("C cosine identity failed")
        if values["G_from_coefficients"] != values["G_from_cosines"]:
            raise ArithmeticError("G cosine identity failed")
        identity_checks.append(
            {
                "x": _pair(x),
                "y": _pair(y),
                **{name: _pair(value) for name, value in values.items()},
            }
        )

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_detector_zero_geometry_conditioning.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.DETECTOR.ZERO_GEOMETRY_CONDITIONING.Q3_Q5_Q7.V1",
        "status": "EXACT_FINITE_BOUNDED_CONDITIONING_ON_SOURCE_LOCKED_COMPLETE_HISTOGRAMS",
        "scope": "member-uniform monic squarefree quintics over F_q for exactly q=3,5,7",
        "spectral_proxy_theorem": {
            "normalized_quartic": "Q(Z)=Z^4-e1*Z^3+e2*Z^2-e1*Z+1 with e1=-a_D/sqrt(q), e2=b_D/q",
            "cosine_factorization": "Q(Z)=(Z^2-2*x*Z+1)(Z^2-2*y*Z+1), x=cos(theta_1), y=cos(theta_2)",
            "coefficient_relations": "e1=2(x+y), e2=2+4xy",
            "C": {
                "source_formula": "(2+b_D/q)^2-4*a_D^2/q",
                "coefficient_identity": "Q(1)Q(-1)=(2+e2)^2-4e1^2",
                "spectral_identity": "16(1-x^2)(1-y^2)=16 sin(theta_1)^2 sin(theta_2)^2",
                "certificate": "under unit-circle factorization, C=0 iff at least one normalized root is +1 or -1",
            },
            "G": {
                "source_formula": "(a_D^2-4*b_D+8*q)/q",
                "coefficient_identity": "e1^2-4e2+8",
                "spectral_identity": "4(x-y)^2",
                "certificate": "under theta_j in [0,pi], G=0 iff the two cosine coordinates, hence the two Frobenius angles, coincide",
            },
            "twist_invariance": "under simultaneous spectral twisting U -> -U, a_D changes sign while b_D is fixed; C,G,P,D,S depend on a_D only through a_D^2",
            "exact_rational_identity_checks": identity_checks,
        },
        "partition_contract": {
            "detector_partition": "exact negative / zero / positive strata for each of P,D,S",
            "quantile_or_tail_partition": False,
            "reason": "sign conditioning is predetermined by the detector algebra and adds no fitted scale",
            "certificate_boundary": "C=0 and G=0 are exact algebraic certificates; positive values, including the smallest positive support values, are proximity/separation heuristics only and are not classified as near-zero events",
        },
        "exact_frozen_member_weight_laws": {
            "status": "EXACT_ONLY_FOR_Q_3_5_7",
            "weighting": "uniform on monic squarefree quintic members, inherited without reweighting from the complete locked coefficient histogram",
            "families": analyses,
        },
        "interpretation_firewall": {
            "exact": "all displayed q=3,5,7 joint laws, sign conditionals, means, covariances, certificate counts, and same-value witnesses",
            "not_claimed": "no asymptotic zero theorem, causal classifier, monodromy diagnosis, subgroup mixture, individual-curve certificate from P/D/S, all-q trend, RH implication, or root-level census",
            "same_value_warning": "explicit equal-detector witnesses with differing C or G show that no detector alone identifies the spectral proxy geometry on these supports",
            "small_value_warning": "C>0 or G>0 can be numerically small on a finite support but is not an endpoint or repeated-angle certificate",
        },
        "resource_contract": {
            "finite_field_enumeration": False,
            "polynomial_curve_or_member_enumeration": False,
            "root_finding": False,
            "random_sampling": False,
            "floating_point_arithmetic": False,
            "source_atom_cap_inclusive": SOURCE_ATOM_CAP_INCLUSIVE,
            "source_atom_preflight_count": source_atom_total,
            "guarded_source_atom_visits": guard.snapshot(),
            "external_dependencies": "none; Python 3.11+ standard library",
        },
        "producer_and_source_locks": {
            "validation_order": "all LF-normalized source digests are checked before JSON parsing or dynamic module execution; payload, embedded locks, coverage, member ledgers, atom counts, and member mass follow",
            "required_input_payload_sha256": EXPECTED_INPUT_PAYLOAD_SHA256,
            "required_member_ledger_sha256": {
                str(q): EXPECTED_MEMBER_LEDGER_SHA256[q] for q in FROZEN_Q_VALUES
            },
            "required_lf_sha256": dict(EXPECTED_LF_SHA256),
            "locks": {
                "histogram_fixture": {
                    "path": "research/l-families/atlas/function_field/balanced_control_family_scan.json",
                    "sha256_lf_normalized": _lf_sha256(INPUT_PATH),
                    "payload_sha256": input_data["payload_sha256"],
                },
                "histogram_producer": {
                    "path": "research/l-families/atlas/function_field/balanced_control_family_scan.py",
                    "sha256_lf_normalized": _lf_sha256(INPUT_PRODUCER_PATH),
                },
                "coefficient_arithmetic": {
                    "path": "research/l-families/atlas/function_field/genus2_q_scan.py",
                    "sha256_lf_normalized": _lf_sha256(COEFFICIENT_ARITHMETIC_PATH),
                },
                "affine_action": {
                    "path": "research/l-families/atlas/function_field/genus2_affine_orbits.py",
                    "sha256_lf_normalized": _lf_sha256(AFFINE_ACTION_PATH),
                },
                "selector_producer": {
                    "path": "research/l-families/atlas/function_field/frobenius_interferometry_subgroup_selectors.py",
                    "sha256_lf_normalized": _lf_sha256(SELECTOR_PRODUCER_PATH),
                },
                "selector_note": {
                    "path": "research/l-families/atlas/function_field/FROBENIUS_INTERFEROMETRY_SUBGROUP_SELECTORS.md",
                    "sha256_lf_normalized": _lf_sha256(SELECTOR_NOTE_PATH),
                },
                "producer": {
                    "path": "research/l-families/atlas/function_field/genus2_detector_zero_geometry_conditioning.py",
                    "sha256_lf_normalized": _lf_sha256(Path(__file__)),
                },
                "note": {
                    "path": "research/l-families/atlas/function_field/GENUS2_DETECTOR_ZERO_GEOMETRY_CONDITIONING.md",
                    "sha256_lf_normalized": _lf_sha256(NOTE_PATH),
                },
                "test": {
                    "path": "tests/test_genus2_detector_zero_geometry_conditioning.py",
                    "sha256_lf_normalized": _lf_sha256(TEST_PATH),
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
            f"genus2 detector zero geometry conditioning: q={FROZEN_Q_VALUES} atoms={fixture['resource_contract']['source_atom_preflight_count']} payload_sha256={fixture['payload_sha256']}"
        )
        return 0
    if not args.path.is_file() or args.path.read_text(encoding="utf-8") != rendered:
        print(f"stale or missing fixture: {args.path}")
        return 1
    print(
        f"genus2 detector zero geometry conditioning check: ok payload_sha256={fixture['payload_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
