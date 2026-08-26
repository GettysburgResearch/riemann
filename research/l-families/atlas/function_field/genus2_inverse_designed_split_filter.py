#!/usr/bin/env python3
"""Bounded inverse design of a genus-two integral-split detector.

Only the complete, source-locked ``(a_D,b_D)`` histograms for q=3,5,7 are
read.  The q=3,5 rows are the design set and q=7 is passed only to the
post-design audit.  No field, polynomial, curve, root, or family member is
enumerated.

The search lattice is the complete set of even-parity raw interferometers
``I_(r,s)`` with ``r+s <= 10`` and zero ambient USp(4) Haar mean.  Primitive
integer combinations, modulo overall sign, are searched under ``L1 <= 8``.
The exact maximin squared point-biserial correlation is the scale-free design
objective.  All arithmetic is integral or ``Fraction`` arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import sys
from collections import Counter
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from types import ModuleType

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUT_PATH = HERE / "balanced_control_family_scan.json"
INPUT_PRODUCER_PATH = HERE / "balanced_control_family_scan.py"
INTERFEROMETER_PATH = HERE / "frobenius_interferometry_subgroup_selectors.py"
SPLIT_PREDICATE_PATH = HERE / "genus2_endoscopic_split_locus.py"
OUTPUT_PATH = HERE / "genus2_inverse_designed_split_filter.json"
NOTE_PATH = HERE / "GENUS2_INVERSE_DESIGNED_SPLIT_FILTER.md"
TEST_PATH = ROOT / "tests" / "test_genus2_inverse_designed_split_filter.py"

FROZEN_Q_VALUES = (3, 5, 7)
TRAINING_Q_VALUES = (3, 5)
HELD_OUT_Q = 7
MAX_TOTAL_FREQUENCY = 10
L1_CAP_INCLUSIVE = 8
CANDIDATE_CAP_INCLUSIVE = 4_096
SOURCE_ATOM_CAP_INCLUSIVE = 4_096
MOMENT_CONTRACTION_CAP_EXCLUSIVE = 50_000
OUTER_TAIL_TARGET = Fraction(1, 100)

# Lexicographic order is deliberate and is part of the search contract.
RAW_POOL = ((1, 7), (1, 9), (2, 4), (2, 8))
RAW_POOL_NAMES = tuple(f"I_({r},{s})" for r, s in RAW_POOL)
EXPECTED_RAW_SIGNATURES = (
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, -2, -4, -2, 0, 0, 0),
    (0, 0, 0, -1, 0, 0, 0),
)
GROUP_ORDER = (
    "USp4",
    "SU2xSU2_block",
    "SU2_doubled_standard",
    "SU2_Sym3",
    "T2_uniform",
    "T_doubled_uniform",
    "T_Sym3_uniform",
)
BENCHMARK_ORDER = ("P", "D", "S")
DETECTOR_ORDER = ("F_star", "P", "D", "S")

EXPECTED_LF_SHA256 = {
    "histogram_fixture": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
    "histogram_producer": "7192fa26b0ea17cb68cff288620ea4dfb124e07807986d9c74fbd37e66087d3b",
    "interferometer_engine": "48474ebcbb99efea23227126f66f566fdb525a3c9ae9e81a77bf83d4075f55e7",
    "split_predicate": "4489c109f25f8e0ca3051dc9983a8738b7aaee941a351959c552aa19b001e4de",
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
EXPECTED_CANDIDATE_COUNT = 1_640
EXPECTED_TRAINING_ELIGIBLE_COUNT = 849
EXPECTED_HELD_OUT_SURVIVOR_COUNT = 80
EXPECTED_WINNER_CANONICAL = (2, 4, -1, 1)
EXPECTED_WINNER_SIGNATURE = (0, 2, 4, 1, 0, 0, 0)

# F_star in the exact root-free coordinates A=e1^2 and e=e2.
EXPECTED_WINNER_POLYNOMIAL: dict[tuple[int, int], int] = {
    (4, 1): 4,
    (4, 0): -6,
    (3, 2): -31,
    (3, 1): 74,
    (3, 0): -37,
    (2, 3): 74,
    (2, 2): -208,
    (2, 1): 116,
    (2, 0): 32,
    (1, 4): -55,
    (1, 3): 134,
    (1, 2): 42,
    (1, 1): -204,
    (1, 0): 34,
    (0, 5): 6,
    (0, 4): -4,
    (0, 3): -32,
    (0, 2): 16,
    (0, 1): 40,
    (0, 0): -8,
}


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
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


def _has_float(value: object) -> bool:
    if isinstance(value, float):
        return True
    if isinstance(value, dict):
        return any(_has_float(key) or _has_float(item) for key, item in value.items())
    if isinstance(value, (list, tuple)):
        return any(_has_float(item) for item in value)
    return False


@dataclass
class ResourceGuard:
    """Fail-closed logical-work ledger for the bounded replay."""

    source_atom_cap: int = SOURCE_ATOM_CAP_INCLUSIVE
    candidate_cap: int = CANDIDATE_CAP_INCLUSIVE
    contraction_cap: int = MOMENT_CONTRACTION_CAP_EXCLUSIVE
    ledger: Counter[str] = field(default_factory=Counter)

    def charge_source_atoms(self, amount: int) -> None:
        number = _plain_int("source-atom charge", amount)
        if number < 0:
            raise ValueError("source-atom charge must be nonnegative")
        if self.ledger["source_atoms"] + number > self.source_atom_cap:
            raise RuntimeError("source-atom inclusive cap would be exceeded")
        self.ledger["source_atoms"] += number

    def charge_candidate(self) -> None:
        if self.ledger["candidates"] + 1 > self.candidate_cap:
            raise RuntimeError("candidate inclusive cap would be exceeded")
        self.ledger["candidates"] += 1

    def charge_contraction(self, name: str, amount: int = 1) -> None:
        number = _plain_int("moment-contraction charge", amount)
        if number < 0:
            raise ValueError("moment-contraction charge must be nonnegative")
        current = sum(
            value
            for key, value in self.ledger.items()
            if key.startswith("contraction_")
        )
        if current + number >= self.contraction_cap:
            raise RuntimeError("moment-contraction exclusive cap would be reached")
        self.ledger[f"contraction_{name}"] += number

    def packet(self) -> dict[str, object]:
        contractions = sum(
            value
            for key, value in self.ledger.items()
            if key.startswith("contraction_")
        )
        return {
            "source_atom_cap_inclusive": self.source_atom_cap,
            "candidate_cap_inclusive": self.candidate_cap,
            "moment_contraction_cap_exclusive": self.contraction_cap,
            "ledger": dict(sorted(self.ledger.items())),
            "moment_contraction_total": contractions,
        }


def _verify_source_hashes() -> None:
    paths = {
        "histogram_fixture": INPUT_PATH,
        "histogram_producer": INPUT_PRODUCER_PATH,
        "interferometer_engine": INTERFEROMETER_PATH,
        "split_predicate": SPLIT_PREDICATE_PATH,
    }
    for name, path in paths.items():
        if not path.is_file():
            raise FileNotFoundError(f"required locked dependency is missing: {path}")
        actual = _lf_normalized_sha256(path)
        expected = EXPECTED_LF_SHA256[name]
        if actual != expected:
            raise ValueError(f"locked dependency drifted for {name}: {actual}")


def _load_locked_module(path: Path, digest: str, module_name: str) -> ModuleType:
    if _lf_normalized_sha256(path) != digest:
        raise ValueError(f"refusing to load unauthenticated module {path.name}")
    specification = importlib.util.spec_from_file_location(module_name, path)
    if specification is None or specification.loader is None:
        raise ImportError(f"could not load locked module {path.name}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[module_name] = module
    specification.loader.exec_module(module)
    return module


def _validated_families() -> list[Mapping[str, object]]:
    _verify_source_hashes()
    data = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    payload = dict(data)
    claimed = payload.pop("payload_sha256", None)
    if claimed != EXPECTED_INPUT_PAYLOAD_SHA256:
        raise ValueError("balanced-control payload pin drifted")
    if claimed != _canonical_sha256(payload):
        raise ArithmeticError("balanced-control canonical payload hash failed")
    if data.get("schema") != "riemann.function_field.balanced_control_family_scan.v1":
        raise ValueError("unexpected balanced-control schema")
    frozen = data.get("frozen_enumeration_facts")
    if not isinstance(frozen, dict):
        raise TypeError("frozen enumeration facts must be an object")
    if frozen.get("status") != "EXHAUSTIVE_ONLY_FOR_Q_3_5_7":
        raise ValueError("source exhaustiveness status drifted")
    if tuple(frozen.get("q_values", ())) != FROZEN_Q_VALUES:
        raise ValueError("source q ladder drifted")
    raw_families = frozen.get("families")
    if not isinstance(raw_families, list):
        raise TypeError("source family rows must be a list")
    families = sorted(raw_families, key=lambda row: int(row["q"]))
    if tuple(int(row["q"]) for row in families) != FROZEN_Q_VALUES:
        raise ValueError("source family row order drifted")

    locks = data.get("producer_and_source_locks", {}).get("locks", {})
    producer_lock = locks.get("producer")
    if not isinstance(producer_lock, dict):
        raise TypeError("embedded producer lock is absent")
    if (
        producer_lock.get("sha256_lf_normalized")
        != EXPECTED_LF_SHA256["histogram_producer"]
    ):
        raise ValueError("embedded histogram-producer lock drifted")

    for family in families:
        q = _plain_int("q", family.get("q"))
        member_count = _plain_int("member count", family.get("member_count"))
        if member_count != EXPECTED_MEMBER_COUNTS[q]:
            raise ValueError(f"q={q} member-count sentinel drifted")
        if family.get("candidate_count") != q**5:
            raise ValueError(f"q={q} complete candidate coverage drifted")
        if family.get("expected_squarefree_count") != q**5 - q**4:
            raise ValueError(f"q={q} squarefree coverage drifted")
        if (
            family.get("member_coefficient_ledger_sha256")
            != EXPECTED_MEMBER_LEDGER_SHA256[q]
        ):
            raise ValueError(f"q={q} member ledger drifted")
        joint = family.get("joint_a_D_b_D_law")
        if not isinstance(joint, dict) or not isinstance(joint.get("atoms"), list):
            raise TypeError(f"q={q} joint law is malformed")
        atoms = joint["atoms"]
        if len(atoms) != EXPECTED_ATOM_COUNTS[q]:
            raise ValueError(f"q={q} joint atom-count sentinel drifted")
        if joint.get("support_size") != len(atoms):
            raise ValueError(f"q={q} joint support-size sentinel drifted")
        seen: set[tuple[int, int]] = set()
        mass = 0
        for atom in atoms:
            a = _plain_int("a_D", atom.get("a_D"))
            b = _plain_int("b_D", atom.get("b_D"))
            weight = _plain_int("member count", atom.get("member_count"))
            if weight <= 0 or (a, b) in seen:
                raise ValueError(f"q={q} joint atom support/mass is invalid")
            seen.add((a, b))
            mass += weight
        if mass != member_count:
            raise ArithmeticError(f"q={q} joint histogram lost member mass")
    return families


Poly = dict[tuple[int, int], int]


def _poly_clean(poly: Mapping[tuple[int, int], int]) -> Poly:
    return {power: coefficient for power, coefficient in poly.items() if coefficient}


def _poly_add(*terms: tuple[int, Mapping[tuple[int, int], int]]) -> Poly:
    result: Counter[tuple[int, int]] = Counter()
    for scalar, poly in terms:
        for power, coefficient in poly.items():
            result[power] += scalar * coefficient
    return _poly_clean(result)


def _poly_multiply(
    left: Mapping[tuple[int, int], int], right: Mapping[tuple[int, int], int]
) -> Poly:
    result: Counter[tuple[int, int]] = Counter()
    for (a_left, e_left), left_coefficient in left.items():
        for (a_right, e_right), right_coefficient in right.items():
            result[a_left + a_right, e_left + e_right] += (
                left_coefficient * right_coefficient
            )
    return _poly_clean(result)


def _poly_shift(poly: Mapping[tuple[int, int], int], a: int = 0, e: int = 0) -> Poly:
    return {
        (a_power + a, e_power + e): coefficient
        for (a_power, e_power), coefficient in poly.items()
    }


def trace_quotient_polynomials(maximum: int = MAX_TOTAL_FREQUENCY) -> tuple[Poly, ...]:
    """Return Q_n(A,e) where p_n=t^(n mod 2) Q_n and A=t^2."""

    maximum = _plain_int("maximum frequency", maximum)
    if maximum < 3 or maximum > MAX_TOTAL_FREQUENCY:
        raise ValueError("trace quotient maximum lies outside the locked engine cap")
    one: Poly = {(0, 0): 1}
    q_values: list[Poly] = [
        {(0, 0): 4},
        one,
        {(1, 0): 1, (0, 1): -2},
        {(1, 0): 1, (0, 1): -3, (0, 0): 3},
    ]
    for frequency in range(4, maximum + 1):
        if frequency % 2 == 0:
            first = _poly_shift(q_values[frequency - 1], a=1)
            third = _poly_shift(q_values[frequency - 3], a=1)
        else:
            first = q_values[frequency - 1]
            third = q_values[frequency - 3]
        second = _poly_shift(q_values[frequency - 2], e=1)
        q_values.append(
            _poly_add(
                (1, first),
                (-1, second),
                (1, third),
                (-1, q_values[frequency - 4]),
            )
        )
    return tuple(q_values)


def raw_interferometer_polynomial(pair: tuple[int, int]) -> Poly:
    r, s = pair
    if r < 1 or s < r or r + s > MAX_TOTAL_FREQUENCY or (r + s) % 2:
        raise ValueError("root-free raw adapter needs 1<=r<=s, even r+s<=10")
    traces = trace_quotient_polynomials()
    product = _poly_multiply(traces[r], traces[s])
    if r % 2:
        product = _poly_shift(product, a=1)
    return _poly_add((1, product), (-1, traces[r + s]))


def _evaluate_poly(
    poly: Mapping[tuple[int, int], int], a_square: Fraction, e2: Fraction
) -> Fraction:
    return sum(
        coefficient * a_square**a_power * e2**e_power
        for (a_power, e_power), coefficient in poly.items()
    )


def winner_polynomial(coefficients: Sequence[int]) -> Poly:
    if len(coefficients) != len(RAW_POOL):
        raise ValueError("winner coefficient vector has wrong dimension")
    return _poly_add(
        *tuple(
            (coefficient, raw_interferometer_polynomial(pair))
            for coefficient, pair in zip(coefficients, RAW_POOL)
        )
    )


def _compact_packet(engine: ModuleType) -> dict[str, object]:
    guard = engine.ResourceGuard()
    context = engine.HaarContext(guard)
    all_even_ambient_zero: list[tuple[int, int]] = []
    signatures: dict[tuple[int, int], tuple[int, ...]] = {}
    polynomials = {}
    for total in range(2, MAX_TOTAL_FREQUENCY + 1):
        for left in range(1, total // 2 + 1):
            right = total - left
            if total % 2:
                continue
            polynomial = engine.interferometer(left, right, guard)
            signature = context.signature(polynomial)
            if any(value.denominator != 1 for value in signature):
                raise ArithmeticError(
                    "raw compact signature is unexpectedly nonintegral"
                )
            integer_signature = tuple(value.numerator for value in signature)
            if integer_signature[0] == 0:
                all_even_ambient_zero.append((left, right))
                signatures[left, right] = integer_signature
                polynomials[left, right] = polynomial
    if tuple(sorted(all_even_ambient_zero)) != RAW_POOL:
        raise ArithmeticError("complete even ambient-zero raw pool drifted")
    if tuple(signatures[pair] for pair in RAW_POOL) != EXPECTED_RAW_SIGNATURES:
        raise ArithmeticError("raw pool compact signatures drifted")

    winner_poly = engine.laurent_linear_combination(
        tuple(
            (coefficient, polynomials[pair])
            for coefficient, pair in zip(EXPECTED_WINNER_CANONICAL, RAW_POOL)
        ),
        guard,
    )
    winner_signature_fraction = context.signature(winner_poly)
    winner_signature = tuple(value.numerator for value in winner_signature_fraction)
    if winner_signature != EXPECTED_WINNER_SIGNATURE:
        raise ArithmeticError("winner compact signature drifted")

    all_raw = engine._raw_polynomials(context)
    selector_polys = engine.selector_polynomials(all_raw, guard)
    selector_signatures = {
        name: context.signature(poly) for name, poly in selector_polys.items()
    }
    selector_order = ("product_selector", "doubled_selector", "sym3_selector")
    expected_selector_signatures = (
        (0, 2, 0, 0, 0, 0, 0),
        (0, 0, 2, 0, 0, 0, 0),
        (0, 0, 0, 2, 0, 0, 0),
    )
    observed_selector_signatures = tuple(
        tuple(value.numerator for value in selector_signatures[name])
        for name in selector_order
    )
    if observed_selector_signatures != expected_selector_signatures:
        raise ArithmeticError("P,D,S compact signatures drifted")

    # Exact equality in the raw-observable module:
    # F*=P+2D+S/2+R, and R has zero mean in all seven locked contexts.
    half_s = {
        exponent: Fraction(coefficient, 2)
        for exponent, coefficient in selector_polys["sym3_selector"].items()
    }
    residual: dict[tuple[int, int], Fraction] = {}
    for exponent in (
        set(winner_poly)
        | set(selector_polys["product_selector"])
        | set(selector_polys["doubled_selector"])
        | set(half_s)
    ):
        value = (
            Fraction(winner_poly.get(exponent, 0))
            - Fraction(selector_polys["product_selector"].get(exponent, 0))
            - 2 * Fraction(selector_polys["doubled_selector"].get(exponent, 0))
            - half_s.get(exponent, Fraction(0))
        )
        if value:
            residual[exponent] = value
    residual_signature = context.signature(residual)
    if any(residual_signature):
        raise ArithmeticError("declared compact-signature residual is not null")
    return {
        "group_order": list(GROUP_ORDER),
        "complete_pool_classification": (
            "all and only raw I_(r,s) with 1<=r<=s, even r+s<=10, and zero ambient USp(4) Haar mean"
        ),
        "raw_pool": [
            {
                "name": name,
                "frequencies": list(pair),
                "signature": list(signatures[pair]),
            }
            for name, pair in zip(RAW_POOL_NAMES, RAW_POOL)
        ],
        "winner_signature": list(winner_signature),
        "exact_signature_decomposition": {
            "identity": "F_star=P+2*D+(1/2)*S+R_null",
            "P_signature": list(expected_selector_signatures[0]),
            "D_signature": list(expected_selector_signatures[1]),
            "S_signature": list(expected_selector_signatures[2]),
            "R_null_signature": [0] * len(GROUP_ORDER),
            "raw_identity_for_R_null": (
                "2*I_(1,1)-I_(2,2)-4*I_(1,5)-I_(4,4)+2*I_(1,7)+4*I_(1,9)-I_(2,4)+2*I_(2,8)"
            ),
            "scope": "equality modulo the seven exact Haar constant-term functionals, with the displayed raw identity defining the exact residual",
        },
        "engine_accounted_work": dict(sorted(guard.ledger.items())),
        "engine_accounted_work_total": guard.total,
    }


def _candidate_vectors(guard: ResourceGuard) -> tuple[tuple[int, ...], ...]:
    candidates = []
    for coefficients in itertools.product(
        range(-L1_CAP_INCLUSIVE, L1_CAP_INCLUSIVE + 1), repeat=len(RAW_POOL)
    ):
        if not any(coefficients):
            continue
        if sum(abs(value) for value in coefficients) > L1_CAP_INCLUSIVE:
            continue
        if math.gcd(*(abs(value) for value in coefficients)) != 1:
            continue
        first = next(value for value in coefficients if value)
        if first < 0:
            continue
        guard.charge_candidate()
        candidates.append(coefficients)
    if len(candidates) != EXPECTED_CANDIDATE_COUNT:
        raise ArithmeticError("primitive candidate count drifted")
    return tuple(candidates)


@dataclass(frozen=True)
class Record:
    q: int
    a: int
    b: int
    weight: int
    split: bool
    raw_values: tuple[Fraction, ...]
    benchmark_values: tuple[Fraction, ...]


def _build_records(
    families: Sequence[Mapping[str, object]],
    engine: ModuleType,
    split_module: ModuleType,
    guard: ResourceGuard,
) -> dict[int, tuple[Record, ...]]:
    raw_polynomials = tuple(raw_interferometer_polynomial(pair) for pair in RAW_POOL)
    result: dict[int, tuple[Record, ...]] = {}
    for family in families:
        q = int(family["q"])
        rows = []
        for atom in family["joint_a_D_b_D_law"]["atoms"]:
            guard.charge_source_atoms(1)
            a = int(atom["a_D"])
            b = int(atom["b_D"])
            weight = int(atom["member_count"])
            a_square = Fraction(a * a, q)
            e2 = Fraction(b, q)
            raw_values = tuple(
                _evaluate_poly(poly, a_square, e2) for poly in raw_polynomials
            )
            benchmark_raw = engine.selector_values_from_squared_first_elementary(
                a_square, e2
            )
            benchmark_values = (
                Fraction(benchmark_raw["product_selector"]),
                Fraction(benchmark_raw["doubled_selector"]),
                Fraction(benchmark_raw["sym3_selector"]),
            )
            classification = split_module.classify_factorization(q, a, b)
            split = bool(classification.in_integral_split_locus)
            if split != (classification.kind in {"split_repeated", "split_distinct"}):
                raise ArithmeticError("split-predicate semantics drifted")
            rows.append(Record(q, a, b, weight, split, raw_values, benchmark_values))
        if sum(row.weight for row in rows) != EXPECTED_MEMBER_COUNTS[q]:
            raise ArithmeticError(f"q={q} record transform lost member mass")
        result[q] = tuple(rows)
    if sum(len(rows) for rows in result.values()) != sum(EXPECTED_ATOM_COUNTS.values()):
        raise ArithmeticError("record source-atom accounting drifted")
    return result


@dataclass(frozen=True)
class FeatureSummary:
    q: int
    member_count: int
    split_count: int
    complement_count: int
    mean: tuple[Fraction, ...]
    split_mean: tuple[Fraction, ...]
    complement_mean: tuple[Fraction, ...]
    covariance: tuple[tuple[Fraction, ...], ...]


def _feature_summary(rows: Sequence[Record]) -> FeatureSummary:
    if not rows:
        raise ValueError("cannot summarize an empty family")
    dimension = len(RAW_POOL)
    member_count = sum(row.weight for row in rows)
    split_count = sum(row.weight for row in rows if row.split)
    complement_count = member_count - split_count
    if not split_count or not complement_count:
        raise ArithmeticError("design needs nonempty split and complement classes")

    def weighted_mean(
        selected: Callable[[Record], bool], mass: int
    ) -> tuple[Fraction, ...]:
        return tuple(
            sum(row.weight * row.raw_values[index] for row in rows if selected(row))
            / mass
            for index in range(dimension)
        )

    mean = weighted_mean(lambda row: True, member_count)
    split_mean = weighted_mean(lambda row: row.split, split_count)
    complement_mean = weighted_mean(lambda row: not row.split, complement_count)
    covariance = tuple(
        tuple(
            sum(
                row.weight
                * (row.raw_values[left] - mean[left])
                * (row.raw_values[right] - mean[right])
                for row in rows
            )
            / member_count
            for right in range(dimension)
        )
        for left in range(dimension)
    )
    return FeatureSummary(
        rows[0].q,
        member_count,
        split_count,
        complement_count,
        mean,
        split_mean,
        complement_mean,
        covariance,
    )


def _dot(left: Sequence[int | Fraction], right: Sequence[int | Fraction]) -> Fraction:
    if len(left) != len(right):
        raise ValueError("dot-product dimensions differ")
    return sum((Fraction(a) * Fraction(b) for a, b in zip(left, right)), Fraction(0))


def _candidate_field_score(
    coefficients: Sequence[int], summary: FeatureSummary
) -> dict[str, Fraction]:
    contrast_vector = tuple(
        inside - outside
        for inside, outside in zip(summary.split_mean, summary.complement_mean)
    )
    contrast = _dot(coefficients, contrast_vector)
    variance = sum(
        Fraction(coefficients[left])
        * Fraction(coefficients[right])
        * summary.covariance[left][right]
        for left in range(len(coefficients))
        for right in range(len(coefficients))
    )
    if variance <= 0:
        raise ArithmeticError("candidate has nonpositive finite-family variance")
    prevalence_variance = Fraction(
        summary.split_count * summary.complement_count,
        summary.member_count**2,
    )
    correlation_squared = prevalence_variance * contrast * contrast / variance
    return {
        "contrast": contrast,
        "variance": variance,
        "correlation_squared": correlation_squared,
    }


def _candidate_complexity(coefficients: Sequence[int]) -> tuple[object, ...]:
    return (
        sum(abs(value) for value in coefficients),
        sum(value != 0 for value in coefficients),
        max(abs(value) for value in coefficients),
        tuple(abs(value) for value in coefficients),
        tuple(coefficients),
    )


def design_on_q3_q5_only(
    candidates: Sequence[tuple[int, ...]],
    training: Mapping[int, FeatureSummary],
    guard: ResourceGuard,
) -> dict[str, object]:
    """Select a direction without accepting or consulting any q=7 object."""

    if tuple(sorted(training)) != TRAINING_Q_VALUES:
        raise ValueError("design function accepts exactly q=3,5 summaries")
    best: dict[str, object] | None = None
    eligible = 0
    rejected_direction = 0
    objective_counts: Counter[tuple[Fraction, Fraction]] = Counter()
    for coefficients in candidates:
        field_scores = {}
        for q in TRAINING_Q_VALUES:
            guard.charge_contraction("candidate_training_field")
            field_scores[q] = _candidate_field_score(coefficients, training[q])
        if field_scores[3]["contrast"] * field_scores[5]["contrast"] <= 0:
            rejected_direction += 1
            continue
        eligible += 1
        objective = (
            min(
                field_scores[3]["correlation_squared"],
                field_scores[5]["correlation_squared"],
            ),
            field_scores[3]["correlation_squared"]
            + field_scores[5]["correlation_squared"],
        )
        objective_counts[objective] += 1
        complexity = _candidate_complexity(coefficients)
        if (
            best is None
            or objective > best["objective"]
            or (objective == best["objective"] and complexity < best["complexity"])
        ):
            best = {
                "canonical_coefficients": tuple(coefficients),
                "field_scores": field_scores,
                "objective": objective,
                "complexity": complexity,
            }
    if best is None:
        raise ArithmeticError("no sign-consistent training candidate exists")
    if eligible != EXPECTED_TRAINING_ELIGIBLE_COUNT:
        raise ArithmeticError("training-eligible candidate count drifted")
    if eligible + rejected_direction != len(candidates):
        raise ArithmeticError("candidate disposition ledger drifted")
    if best["canonical_coefficients"] != EXPECTED_WINNER_CANONICAL:
        raise ArithmeticError("inverse-design winner drifted")
    orientation = 1 if best["field_scores"][3]["contrast"] > 0 else -1
    best["oriented_coefficients"] = tuple(
        orientation * value for value in best["canonical_coefficients"]
    )
    best["orientation"] = orientation
    best["eligible_candidate_count"] = eligible
    best["rejected_training_direction_count"] = rejected_direction
    best["winning_objective_tie_count"] = objective_counts[best["objective"]]
    if best["winning_objective_tie_count"] != 1:
        raise ArithmeticError("winning training objective is no longer unique")
    return best


def _linear_value(coefficients: Sequence[int], values: Sequence[Fraction]) -> Fraction:
    return _dot(coefficients, values)


def _outer_tail_packet(
    values: Sequence[tuple[Fraction, bool, int]], member_count: int, split_count: int
) -> dict[str, object]:
    histogram: Counter[Fraction] = Counter()
    split_histogram: Counter[Fraction] = Counter()
    for value, split, weight in values:
        histogram[value] += weight
        if split:
            split_histogram[value] += weight
    target_count = (member_count + 99) // 100
    by_absolute: Counter[Fraction] = Counter()
    for value, weight in histogram.items():
        by_absolute[abs(value)] += weight
    accumulated = 0
    threshold = None
    for absolute in sorted(by_absolute, reverse=True):
        accumulated += by_absolute[absolute]
        threshold = absolute
        if accumulated >= target_count:
            break
    if threshold is None:
        raise ArithmeticError("cannot construct an outer tail")
    selected_values = {value for value in histogram if abs(value) >= threshold}
    tail_count = sum(histogram[value] for value in selected_values)
    split_tail_count = sum(split_histogram[value] for value in selected_values)
    tail_split_fraction = Fraction(split_tail_count, tail_count)
    baseline_split_fraction = Fraction(split_count, member_count)
    return {
        "definition": "all members with |detector| at least the largest tied threshold giving mass >=1%",
        "target_member_count_ceiling": target_count,
        "absolute_threshold": _fraction_pair(threshold),
        "member_count_including_ties": tail_count,
        "split_member_count": split_tail_count,
        "split_fraction_in_tail": _fraction_pair(tail_split_fraction),
        "baseline_split_fraction": _fraction_pair(baseline_split_fraction),
        "split_enrichment_ratio": _fraction_pair(
            tail_split_fraction / baseline_split_fraction
        ),
    }


def _detector_diagnostics(
    rows: Sequence[Record], value: Callable[[Record], Fraction]
) -> dict[str, object]:
    member_count = sum(row.weight for row in rows)
    split_count = sum(row.weight for row in rows if row.split)
    complement_count = member_count - split_count
    triples = [(value(row), row.split, row.weight) for row in rows]

    def moments(
        selected: Callable[[bool], bool], mass: int
    ) -> tuple[Fraction, Fraction]:
        mean = (
            sum(
                detector * weight
                for detector, split, weight in triples
                if selected(split)
            )
            / mass
        )
        variance = (
            sum(
                weight * (detector - mean) ** 2
                for detector, split, weight in triples
                if selected(split)
            )
            / mass
        )
        return mean, variance

    mean, variance = moments(lambda split: True, member_count)
    split_mean, split_variance = moments(lambda split: split, split_count)
    complement_mean, complement_variance = moments(
        lambda split: not split, complement_count
    )
    contrast = split_mean - complement_mean
    covariance_with_indicator = (
        Fraction(split_count * complement_count, member_count**2) * contrast
    )
    indicator_variance = Fraction(split_count * complement_count, member_count**2)
    correlation_squared = (
        covariance_with_indicator**2 / (variance * indicator_variance)
        if variance
        else Fraction(0)
    )
    sign_counts = {
        "all": Counter({"negative": 0, "zero": 0, "positive": 0}),
        "split": Counter({"negative": 0, "zero": 0, "positive": 0}),
        "complement": Counter({"negative": 0, "zero": 0, "positive": 0}),
    }
    for detector, split, weight in triples:
        label = _sign(detector)
        sign_counts["all"][label] += weight
        sign_counts["split" if split else "complement"][label] += weight
    return {
        "mean": _fraction_pair(mean),
        "variance": _fraction_pair(variance),
        "split_conditional_mean": _fraction_pair(split_mean),
        "split_conditional_variance": _fraction_pair(split_variance),
        "complement_conditional_mean": _fraction_pair(complement_mean),
        "complement_conditional_variance": _fraction_pair(complement_variance),
        "split_minus_complement": _fraction_pair(contrast),
        "covariance_with_split_indicator": _fraction_pair(covariance_with_indicator),
        "squared_point_biserial_correlation": _fraction_pair(correlation_squared),
        "sign_member_counts": {
            name: dict(counts) for name, counts in sign_counts.items()
        },
        "outer_one_percent_absolute_tail": _outer_tail_packet(
            triples, member_count, split_count
        ),
    }


def _conditional_vector_packet(
    rows: Sequence[Record],
    value_functions: Sequence[Callable[[Record], Fraction]],
    selected: Callable[[Record], bool],
) -> dict[str, object]:
    chosen = [row for row in rows if selected(row)]
    mass = sum(row.weight for row in chosen)
    if not mass:
        raise ArithmeticError("conditional covariance class is empty")
    means = tuple(
        sum(row.weight * function(row) for row in chosen) / mass
        for function in value_functions
    )
    covariance = tuple(
        tuple(
            sum(
                row.weight
                * (value_functions[left](row) - means[left])
                * (value_functions[right](row) - means[right])
                for row in chosen
            )
            / mass
            for right in range(len(value_functions))
        )
        for left in range(len(value_functions))
    )
    return {
        "member_count": mass,
        "mean_vector": [_fraction_pair(value) for value in means],
        "covariance_matrix": [
            [_fraction_pair(value) for value in row] for row in covariance
        ],
    }


def _family_packet(
    q: int, rows: Sequence[Record], winner: Sequence[int]
) -> dict[str, object]:
    value_functions = (
        lambda row: _linear_value(winner, row.raw_values),
        lambda row: row.benchmark_values[0],
        lambda row: row.benchmark_values[1],
        lambda row: row.benchmark_values[2],
    )
    member_count = sum(row.weight for row in rows)
    split_count = sum(row.weight for row in rows if row.split)
    return {
        "q": q,
        "role": "training" if q in TRAINING_Q_VALUES else "held_out",
        "member_count": member_count,
        "signed_source_atom_count": len(rows),
        "integral_plus_q_split_member_count": split_count,
        "integral_plus_q_split_member_fraction": _fraction_pair(
            Fraction(split_count, member_count)
        ),
        "detectors": {
            name: _detector_diagnostics(rows, function)
            for name, function in zip(DETECTOR_ORDER, value_functions)
        },
        "vector_order": list(DETECTOR_ORDER),
        "all_member_vector_moments": _conditional_vector_packet(
            rows, value_functions, lambda row: True
        ),
        "split_conditional_vector_moments": _conditional_vector_packet(
            rows, value_functions, lambda row: row.split
        ),
        "complement_conditional_vector_moments": _conditional_vector_packet(
            rows, value_functions, lambda row: not row.split
        ),
    }


def _post_design_audit(
    candidates: Sequence[tuple[int, ...]],
    design: Mapping[str, object],
    summaries: Mapping[int, FeatureSummary],
    guard: ResourceGuard,
) -> dict[str, object]:
    """Consult q=7 only after the q=3,5 winner has been frozen."""

    oriented = tuple(int(value) for value in design["oriented_coefficients"])
    winner_holdout = _candidate_field_score(oriented, summaries[HELD_OUT_Q])
    training_sign = _sign(design["field_scores"][3]["contrast"])
    holdout_sign = _sign(winner_holdout["contrast"])
    if training_sign != "positive":
        raise ArithmeticError(
            "winner orientation failed to make training direction positive"
        )

    eligible = []
    for coefficients in candidates:
        guard.charge_contraction("posthoc_training_score_replay", 2)
        score3 = _candidate_field_score(coefficients, summaries[3])
        score5 = _candidate_field_score(coefficients, summaries[5])
        if score3["contrast"] * score5["contrast"] <= 0:
            continue
        guard.charge_contraction("posthoc_candidate_holdout")
        score7 = _candidate_field_score(coefficients, summaries[7])
        survives = score3["contrast"] * score7["contrast"] > 0
        objective = (
            min(score3["correlation_squared"], score5["correlation_squared"]),
            score3["correlation_squared"] + score5["correlation_squared"],
        )
        eligible.append((coefficients, score3, score5, score7, survives, objective))
    survivors = [row for row in eligible if row[4]]
    if len(eligible) != EXPECTED_TRAINING_ELIGIBLE_COUNT:
        raise ArithmeticError("post-design eligible ledger drifted")
    if len(survivors) != EXPECTED_HELD_OUT_SURVIVOR_COUNT:
        raise ArithmeticError("held-out direction-survival count drifted")
    retrospective = max(
        survivors,
        key=lambda row: (
            row[5],
            tuple(-part for part in _candidate_complexity(row[0])[:3]),
        ),
    )
    retrospective_orientation = 1 if retrospective[1]["contrast"] > 0 else -1
    retrospective_coefficients = tuple(
        retrospective_orientation * value for value in retrospective[0]
    )
    retrospective_scores = {
        q: _candidate_field_score(retrospective_coefficients, summaries[q])
        for q in FROZEN_Q_VALUES
    }
    if retrospective_coefficients != (2, 3, -2, -1):
        raise ArithmeticError("retrospective surviving direction sentinel drifted")
    if not (retrospective_scores[7]["correlation_squared"] < Fraction(1, 6_000)):
        raise ArithmeticError("retrospective held-out collapse bound drifted")
    return {
        "winner_q7_score": {
            key: _fraction_pair(value) for key, value in winner_holdout.items()
        },
        "training_oriented_contrast_sign": training_sign,
        "held_out_contrast_sign": holdout_sign,
        "winner_direction_verdict": (
            "REVERSES_ON_HELD_OUT_Q7"
            if holdout_sign != training_sign
            else "SURVIVES_Q7"
        ),
        "training_eligible_direction_count": len(eligible),
        "direction_survivor_count_on_q7": len(survivors),
        "direction_reversal_or_zero_count_on_q7": len(eligible) - len(survivors),
        "retrospective_best_training_rank_among_q7_survivors": {
            "warning": "uses held-out labels post hoc and is not a designed replacement",
            "oriented_coefficients_in_raw_pool_order": list(retrospective_coefficients),
            "expression": "2*I_(1,7)+3*I_(1,9)-2*I_(2,4)-I_(2,8)",
            "field_scores": {
                str(q): {
                    key: _fraction_pair(value)
                    for key, value in retrospective_scores[q].items()
                }
                for q in FROZEN_Q_VALUES
            },
            "held_out_squared_correlation_bound": "strictly_less_than_1/6000",
        },
    }


def _score_packet(score: Mapping[str, Fraction]) -> dict[str, list[int]]:
    return {name: _fraction_pair(value) for name, value in score.items()}


def build_payload() -> dict[str, object]:
    guard = ResourceGuard()
    families = _validated_families()
    engine = _load_locked_module(
        INTERFEROMETER_PATH,
        EXPECTED_LF_SHA256["interferometer_engine"],
        "_locked_inverse_design_interferometer_engine",
    )
    split_module = _load_locked_module(
        SPLIT_PREDICATE_PATH,
        EXPECTED_LF_SHA256["split_predicate"],
        "_locked_inverse_design_split_predicate",
    )
    if not callable(
        getattr(engine, "selector_values_from_squared_first_elementary", None)
    ):
        raise TypeError("locked interferometer root-free adapter is missing")
    if not callable(getattr(split_module, "classify_factorization", None)):
        raise TypeError("locked integral-split predicate is missing")

    compact = _compact_packet(engine)
    candidates = _candidate_vectors(guard)
    records = _build_records(families, engine, split_module, guard)
    summaries = {q: _feature_summary(records[q]) for q in FROZEN_Q_VALUES}
    design = design_on_q3_q5_only(
        candidates,
        {q: summaries[q] for q in TRAINING_Q_VALUES},
        guard,
    )
    oriented = tuple(int(value) for value in design["oriented_coefficients"])
    if oriented != EXPECTED_WINNER_CANONICAL:
        raise ArithmeticError("oriented winner sentinel drifted")
    exact_poly = winner_polynomial(oriented)
    if exact_poly != EXPECTED_WINNER_POLYNOMIAL:
        raise ArithmeticError("root-free winner polynomial drifted")
    for q, rows in records.items():
        for row in rows:
            guard.charge_contraction("adapter_crosscheck")
            expected = _linear_value(oriented, row.raw_values)
            actual = _evaluate_poly(
                exact_poly, Fraction(row.a * row.a, q), Fraction(row.b, q)
            )
            if actual != expected:
                raise ArithmeticError("root-free expanded adapter cross-check failed")

    # This call is intentionally sequenced after design_on_q3_q5_only.
    heldout_audit = _post_design_audit(candidates, design, summaries, guard)
    family_packets = [_family_packet(q, records[q], oriented) for q in FROZEN_Q_VALUES]
    benchmark_verdicts = {}
    for benchmark in BENCHMARK_ORDER:
        index = DETECTOR_ORDER.index(benchmark)
        contrasts = {
            q: Fraction(
                *family_packets[q_index]["detectors"][benchmark][
                    "split_minus_complement"
                ]
            )
            for q_index, q in enumerate(FROZEN_Q_VALUES)
        }
        benchmark_verdicts[benchmark] = {
            "contrast_by_q": {
                str(q): _fraction_pair(contrasts[q]) for q in FROZEN_Q_VALUES
            },
            "q3_q5_direction_agrees": contrasts[3] * contrasts[5] > 0,
            "q7_direction_matches_q3": contrasts[3] * contrasts[7] > 0,
        }
        if index < 1:
            raise ArithmeticError("benchmark index mapping drifted")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_inverse_designed_split_filter.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.INVERSE_DESIGNED_SPLIT_FILTER.TRAIN_Q3_Q5.HOLDOUT_Q7.V1",
        "status": "EXACT_BOUNDED_TRAINING_WINNER_REVERSES_ON_HELD_OUT_Q7",
        "scope": (
            "member-uniform monic squarefree quintics over F_q for exactly q=3,5,7, replayed only from complete locked coefficient histograms"
        ),
        "source_locks": {
            "required_lf_sha256": dict(EXPECTED_LF_SHA256),
            "input_payload_sha256": EXPECTED_INPUT_PAYLOAD_SHA256,
            "member_coefficient_ledger_sha256": {
                str(q): digest for q, digest in EXPECTED_MEMBER_LEDGER_SHA256.items()
            },
        },
        "compact_group_design_space": compact,
        "design_contract": {
            "training_q_values": list(TRAINING_Q_VALUES),
            "held_out_q_value": HELD_OUT_Q,
            "heldout_exclusion": (
                "design_on_q3_q5_only accepts a mapping whose keys must be exactly (3,5); q=7 is first consulted by _post_design_audit after the winner is frozen"
            ),
            "raw_pool_order": list(RAW_POOL_NAMES),
            "candidate_lattice": (
                "primitive integer coefficient vectors modulo overall sign, first nonzero coefficient positive, L1<=8"
            ),
            "candidate_count": len(candidates),
            "objective": (
                "among candidates with the same nonzero conditional-mean-difference sign at q=3 and q=5, lexicographically maximize min(rho_3^2,rho_5^2), then rho_3^2+rho_5^2; break exact ties by lower L1, support, max coefficient, absolute vector, coefficient vector"
            ),
            "rho_squared_definition": (
                "pi_q*(1-pi_q)*(mean_split-mean_complement)^2/Var_all, the exact squared point-biserial correlation"
            ),
        },
        "training_search_result": {
            "training_eligible_candidate_count": design["eligible_candidate_count"],
            "winning_objective_tie_count": design["winning_objective_tie_count"],
            "rejected_opposite_or_zero_training_direction_count": design[
                "rejected_training_direction_count"
            ],
            "canonical_coefficients_in_raw_pool_order": list(
                design["canonical_coefficients"]
            ),
            "training_oriented_coefficients_in_raw_pool_order": list(oriented),
            "winner_expression": ("F_star=2*I_(1,7)+4*I_(1,9)-I_(2,4)+I_(2,8)"),
            "complexity": {
                "L1": sum(abs(value) for value in oriented),
                "support": sum(value != 0 for value in oriented),
                "maximum_absolute_coefficient": max(abs(value) for value in oriented),
            },
            "objective": {
                "minimum_training_rho_squared": _fraction_pair(design["objective"][0]),
                "sum_training_rho_squared": _fraction_pair(design["objective"][1]),
            },
            "field_scores": {
                str(q): _score_packet(design["field_scores"][q])
                for q in TRAINING_Q_VALUES
            },
        },
        "held_out_evaluation": heldout_audit,
        "benchmark_direction_comparison": benchmark_verdicts,
        "exact_family_diagnostics": {
            "detector_order": list(DETECTOR_ORDER),
            "families": family_packets,
        },
        "root_free_reciprocal_quartic_adapter": {
            "source_quartic": "T^4+a_D*T^3+b_D*T^2+q*a_D*T+q^2",
            "normalized_quartic": "Z^4-e1*Z^3+e2*Z^2-e1*Z+1",
            "rational_coordinates": "A=e1^2=a_D^2/q and e=e2=b_D/q",
            "recurrence": (
                "p_n=e1*p_(n-1)-e2*p_(n-2)+e1*p_(n-3)-p_(n-4), represented exactly as p_n=e1^(n mod 2)*Q_n(A,e)"
            ),
            "winner_polynomial_terms": [
                [a_power, e_power, exact_poly[a_power, e_power]]
                for a_power, e_power in sorted(exact_poly, reverse=True)
            ],
            "root_finding": False,
            "square_root_construction": False,
        },
        "interpretation_firewall": {
            "exact_claim": (
                "a deterministic bounded classifier-design experiment and exact held-out q=7 evaluation on three frozen member-complete histograms"
            ),
            "negative_result": (
                "the unique maximin q=3,5 winner reverses its split-versus-complement conditional-mean direction at q=7; 769 of 849 training-eligible directions reverse or vanish"
            ),
            "forbidden_inference": (
                "finite discrimination, sign, covariance, or tail enrichment does not certify a subgroup, split Jacobian, endomorphism algebra, motive, monodromy group, all-q law, or RH/GRH consequence"
            ),
            "predicate_scope": (
                "integral factorization of the reciprocal quartic into two +q elliptic-form quadratics is a coefficient predicate, not a polarization or geometric decomposition theorem"
            ),
        },
        "resource_contract": {
            "finite_field_enumeration": False,
            "curve_or_member_enumeration": False,
            "root_finding": False,
            "random_sampling": False,
            "external_data": False,
            **guard.packet(),
        },
    }
    if _has_float(payload):
        raise TypeError("claim payload contains a forbidden float")
    return payload


def build_fixture() -> dict[str, object]:
    payload = build_payload()
    fixture = dict(payload)
    fixture["payload_sha256"] = _canonical_sha256(payload)
    return fixture


def _check_committed() -> dict[str, object]:
    expected = build_fixture()
    if not OUTPUT_PATH.is_file():
        raise FileNotFoundError(f"committed fixture is missing: {OUTPUT_PATH}")
    observed = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    unhashed = dict(observed)
    claimed = unhashed.pop("payload_sha256", None)
    if claimed != _canonical_sha256(unhashed):
        raise ArithmeticError("committed fixture payload hash failed")
    if observed != expected:
        raise ArithmeticError("committed fixture differs from deterministic replay")
    return observed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write deterministic JSON")
    parser.add_argument("--check", action="store_true", help="check committed JSON")
    parser.add_argument("--show", action="store_true", help="print deterministic JSON")
    arguments = parser.parse_args()
    if sum((arguments.write, arguments.check, arguments.show)) > 1:
        parser.error("choose at most one of --write, --check, and --show")
    if arguments.write:
        fixture = build_fixture()
        OUTPUT_PATH.write_text(
            json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    elif arguments.show:
        fixture = build_fixture()
        print(json.dumps(fixture, indent=2, sort_keys=True))
    else:
        fixture = _check_committed()
    print(
        "genus2 inverse-designed split filter: ok "
        f"candidates={fixture['design_contract']['candidate_count']} "
        f"verdict={fixture['held_out_evaluation']['winner_direction_verdict']} "
        f"payload_sha256={fixture['payload_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
