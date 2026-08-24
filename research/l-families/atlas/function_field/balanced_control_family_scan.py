#!/usr/bin/env python3
"""Bounded exact family scan for the balanced USp(4) coefficient control.

For every monic squarefree quintic D over F_q, for exactly q=3,5,7, set

    B_D = 2*a_D^2/q - b_D^2/q^2 = J_D/q^2,
    J_D = 2*q*a_D^2 - b_D^2.

The producer independently enumerates the family, reconstructs a_D and b_D
from the exact F_q and F_(q^2) character sums supplied by genus2_q_scan.py,
and records the joint (a_D,b_D) law, B_D support, signs, six moments, affine
orbit structure, and endpoint concentration.  In particular it recomputes
sum b_D^3, sum a_D^2*b_D^2, and sum b_D^4; it does not import those sums from
the earlier high-weight-channel fixture.

The finite enumeration is deliberately fail-closed: no field outside
q=3,5,7 is accepted and no field may require more than 20,000 monic
candidates.  All arithmetic affecting the result is integer or Fraction
arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import time
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Mapping, Sequence

import genus2_affine_orbits as affine_orbits
import genus2_q_scan as q_scan
import usp_coefficient_minor_rank_scan as rank_scan


Poly = tuple[int, ...]
FROZEN_Q_VALUES = (3, 5, 7)
DEFAULT_CANDIDATE_CAP = 20_000
MAX_WALL_SECONDS = 15.0
DEFAULT_GUARD_INTERVAL = 256
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "balanced_control_family_scan.json"
NOTE_PATH = HERE / "BALANCED_CONTROL_FAMILY_SCAN.md"
TEST_PATH = ROOT / "tests" / "test_balanced_control_family_scan.py"
Q_SCAN_PATH = HERE / "genus2_q_scan.py"
Q_SCAN_FIXTURE_PATH = HERE / "genus2_q_scan.json"
AFFINE_PATH = HERE / "genus2_affine_orbits.py"
AFFINE_FIXTURE_PATH = HERE / "genus2_affine_orbits.json"
MOMENT_NOTE_PATH = HERE / "GENUS2_MOMENT_IDENTITY.md"
MOMENT_CERTIFICATE_PATH = HERE / "genus2_moment_identity.py"
RANK_SCAN_PATH = HERE / "usp_coefficient_minor_rank_scan.py"
RANK_NOTE_PATH = HERE / "USP_COEFFICIENT_MINOR_RANK_SCAN.md"


@dataclass(frozen=True)
class MemberData:
    a: int
    b: int
    j: int


@dataclass(frozen=True)
class FieldAnalysis:
    payload: dict[str, object]
    raw_sums: dict[str, int]
    channel_means: dict[str, Fraction]
    orbit_size_histogram: dict[str, int]
    orbit_count: int


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _sign(value: int) -> str:
    return "negative" if value < 0 else "positive" if value > 0 else "zero"


def _histogram(counter: Mapping[int, int]) -> dict[str, int]:
    return {str(key): counter[key] for key in sorted(counter)}


def _guard(
    *,
    clock: Callable[[], float],
    deadline: float,
    q: int,
    stage: str,
    work_items: int,
) -> None:
    if clock() >= deadline:
        raise TimeoutError(
            f"q={q} balanced-control scan exceeded its monotonic wall deadline "
            f"during {stage} after {work_items} work items"
        )


def _validate_q(q: int, candidate_cap: int) -> None:
    if q not in FROZEN_Q_VALUES:
        raise ValueError(
            f"refusing q={q}; balanced-control scan supports only {FROZEN_Q_VALUES}"
        )
    if candidate_cap <= 0 or q**5 > candidate_cap:
        raise ValueError(
            f"q={q} requires {q**5} monic candidates, above per-field cap "
            f"{candidate_cap}"
        )


def balanced_mean_all_q(q: int) -> Fraction:
    """The proved all-odd-prime-power mean imported from the moment note."""

    if q <= 1:
        raise ValueError("q must exceed one")
    return (
        Fraction(1, q)
        + Fraction(1, q**3)
        - Fraction(1, q**4)
        + Fraction(1, q**5)
    )


def balanced_haar_moment(order: int) -> int:
    """Exact USp(4) Haar moment of B=2*e_1^2-e_2^2."""

    if order < 0:
        raise ValueError("moment order must be nonnegative")
    if order % 2:
        return 0
    r = order // 2
    return math.comb(2 * r, r) ** 2 // (r + 1)


def _derived_high_weight_channels(
    q: int,
    member_count: int,
    raw_sums: Mapping[str, int],
) -> dict[str, Fraction]:
    """Recover chi_(0,3), chi_(2,2), chi_(0,4) by triangular identities."""

    mean = lambda name: Fraction(raw_sums[name], member_count)  # noqa: E731
    mean_r3 = (
        mean("b_cubed") / q**3
        - mean("b_squared") / q**2
        - 2 * mean("a_squared_b") / q**2
        - mean("b") / q
        + 3 * mean("a_squared") / q
    )
    mean_r22 = (
        mean("a_squared_b_squared") / q**3
        - 3 * mean("a_squared_b") / q**2
        - mean("a_fourth") / q**2
        + 5 * mean("a_squared") / q
        - 1
    )
    mean_r4 = (
        mean("b_fourth") / q**4
        - 5 * mean("a_squared_b") / q**2
        - 2 * mean("a_fourth") / q**2
        + 14 * mean("a_squared") / q
        - 3 * mean("b_squared") / q**2
        - 2
    )
    chi_0_3 = mean_r3
    chi_2_2 = mean_r22 - chi_0_3
    chi_0_4 = mean_r4 - 3 * chi_2_2 - 4 * chi_0_3
    return {
        "chi_(0,3)": chi_0_3,
        "chi_(2,2)": chi_2_2,
        "chi_(0,4)": chi_0_4,
    }


def _signed_character_decomposition(
    polynomial: Mapping[tuple[int, int], int],
    engine: rank_scan.CnCharacterEngine,
) -> dict[tuple[int, int], int]:
    """Triangularly decompose a virtual C2 character with signed coefficients."""

    residual = dict(polynomial)
    decomposition: dict[tuple[int, int], int] = {}
    while residual:
        dominant = [
            weight
            for weight, coefficient in residual.items()
            if coefficient and weight[0] >= weight[1] >= 0
        ]
        if not dominant:
            raise ArithmeticError("virtual character residual has no dominant weight")
        highest = max(dominant)
        coefficient = residual[highest]
        decomposition[highest] = coefficient
        residual = rank_scan.add_scaled(
            residual,
            engine.character(highest),
            -coefficient,
            engine.guard,
        )
    return decomposition


def build_third_moment_reduction() -> dict[str, object]:
    """Verify the exact C2 decomposition which isolates the unresolved channel."""

    guard = rank_scan.ResourceGuard()
    engine = rank_scan.CnCharacterEngine(2, guard)
    balanced = rank_scan.add_scaled(
        engine.character((2, 0)),
        engine.character((2, 2)),
        -1,
        guard,
    )
    balanced_cubed = rank_scan.multiply(
        rank_scan.multiply(balanced, balanced, guard), balanced, guard
    )
    decomposition = _signed_character_decomposition(balanced_cubed, engine)
    expected = {
        (2, 0): 6,
        (2, 2): -6,
        (3, 3): -2,
        (5, 3): 2,
        (6, 0): 3,
        (6, 2): -3,
        (6, 4): 1,
        (6, 6): -1,
    }
    if decomposition != expected:
        raise ArithmeticError("balanced third-power character decomposition drifted")
    density = rank_scan.weyl_density(2, guard)
    if rank_scan.haar_constant_term(balanced_cubed, density, 2, guard) != 0:
        raise ArithmeticError("balanced third Haar moment must vanish")

    records = []
    for highest, coefficient in sorted(decomposition.items()):
        fundamental = rank_scan.fundamental_coordinates(highest)
        records.append(
            {
                "highest_weight_fundamental_basis": list(fundamental),
                "notation": f"chi_({fundamental[0]},{fundamental[1]})",
                "coefficient": coefficient,
            }
        )
    return {
        "status": "EXACT_POINTWISE_REDUCTION_ALL_Q_AVERAGE_UNRESOLVED",
        "first_unresolved_family_odd_moment": 3,
        "why_first": (
            "Every odd Haar moment is zero, while the finite-family first moment "
            "is proved for every odd prime power q; no all-q third-moment formula "
            "is proved in the locked sources."
        ),
        "raw_coefficient_identity": (
            "B_D^3=8*a_D^6/q^3-12*a_D^4*b_D^2/q^4+"
            "6*a_D^2*b_D^4/q^5-b_D^6/q^6"
        ),
        "character_decomposition": records,
        "character_identity": (
            "B^3=6*chi_(2,0)-6*chi_(0,2)-2*chi_(0,3)+"
            "2*chi_(2,3)+3*chi_(6,0)-3*chi_(4,2)+chi_(2,4)-chi_(0,6)"
        ),
        "reduced_identity": (
            "B^3=6*B-2*chi_(0,3)+R6, where "
            "R6=2*chi_(2,3)+3*chi_(6,0)-3*chi_(4,2)+"
            "chi_(2,4)-chi_(0,6)"
        ),
        "chi_(0,3)_coefficient_identity": (
            "chi_(0,3)=e^3-e^2-2*e*t^2-e+3*t^2, "
            "t=a_D/sqrt(q), e=b_D/q"
        ),
        "mean_reduction": (
            "mean(B_D^3)=6*(q^-1+q^-3-q^-4+q^-5)-"
            "2*mean(chi_(0,3))+mean(R6)"
        ),
        "remaining_all_q_burden": (
            "evaluate the single explicit weight-six virtual average mean(R6); "
            "the three frozen values below do not determine it for general q"
        ),
        "haar_check": {
            "third_moment": 0,
            "trivial_character_coefficient": decomposition.get((0, 0), 0),
        },
        "exact_character_engine_operations": guard.snapshot(),
    }


def _atom_record(
    j: int,
    q: int,
    histogram: Mapping[int, int],
    atom_orbit_records: Mapping[int, list[dict[str, object]]],
    member_count: int,
) -> dict[str, object]:
    return {
        "B_numerator_J": j,
        "B_D": _fraction_pair(Fraction(j, q**2)),
        "member_count": histogram[j],
        "member_fraction": _fraction_pair(Fraction(histogram[j], member_count)),
        "affine_orbit_count": len(atom_orbit_records[j]),
        "affine_orbits": atom_orbit_records[j],
    }


def analyze_q(
    q: int,
    *,
    candidate_cap: int = DEFAULT_CANDIDATE_CAP,
    wall_limit_seconds: float = MAX_WALL_SECONDS,
    guard_interval: int = DEFAULT_GUARD_INTERVAL,
    clock: Callable[[], float] = time.monotonic,
    deadline: float | None = None,
) -> FieldAnalysis:
    """Exhaust one frozen field and construct its exact balanced-control law."""

    _validate_q(q, candidate_cap)
    if not 0 < wall_limit_seconds <= MAX_WALL_SECONDS:
        raise ValueError(f"wall limit must lie in (0,{MAX_WALL_SECONDS}]")
    if guard_interval < 1:
        raise ValueError("guard interval must be positive")
    start = clock()
    local_deadline = start + wall_limit_seconds
    if deadline is not None:
        local_deadline = min(local_deadline, deadline)

    tables = q_scan.build_field_tables(q)
    members: dict[Poly, MemberData] = {}
    joint_histogram: Counter[tuple[int, int]] = Counter()
    j_histogram: Counter[int] = Counter()
    raw_sums = {
        "a_squared": 0,
        "a_fourth": 0,
        "a_sixth": 0,
        "a_squared_b": 0,
        "a_squared_b_squared": 0,
        "a_fourth_b_squared": 0,
        "a_squared_b_fourth": 0,
        "b": 0,
        "b_squared": 0,
        "b_cubed": 0,
        "b_fourth": 0,
        "b_sixth": 0,
    }
    moment_numerator_sums = {order: 0 for order in range(1, 7)}
    sign_witnesses: dict[str, Poly | None] = {
        "negative": None,
        "zero": None,
        "positive": None,
    }

    for candidate_index, coefficients in enumerate(
        itertools.product(range(q), repeat=5), start=1
    ):
        if candidate_index % guard_interval == 0:
            _guard(
                clock=clock,
                deadline=local_deadline,
                q=q,
                stage="candidate enumeration",
                work_items=candidate_index,
            )
        conductor = tuple(coefficients) + (1,)
        if not q_scan.is_squarefree_quintic(conductor, q):
            continue
        a, b = q_scan.coefficients_from_character_sums(conductor, tables)
        j = 2 * q * a * a - b * b
        members[conductor] = MemberData(a=a, b=b, j=j)
        joint_histogram[a, b] += 1
        j_histogram[j] += 1
        raw_sums["a_squared"] += a**2
        raw_sums["a_fourth"] += a**4
        raw_sums["a_sixth"] += a**6
        raw_sums["a_squared_b"] += a**2 * b
        raw_sums["a_squared_b_squared"] += a**2 * b**2
        raw_sums["a_fourth_b_squared"] += a**4 * b**2
        raw_sums["a_squared_b_fourth"] += a**2 * b**4
        raw_sums["b"] += b
        raw_sums["b_squared"] += b**2
        raw_sums["b_cubed"] += b**3
        raw_sums["b_fourth"] += b**4
        raw_sums["b_sixth"] += b**6
        for order in moment_numerator_sums:
            moment_numerator_sums[order] += j**order
        sign = _sign(j)
        if sign_witnesses[sign] is None:
            sign_witnesses[sign] = conductor

    _guard(
        clock=clock,
        deadline=local_deadline,
        q=q,
        stage="candidate enumeration",
        work_items=q**5,
    )
    member_count = len(members)
    expected_members = q**5 - q**4
    if member_count != expected_members:
        raise ArithmeticError(
            f"q={q} squarefree count {member_count} differs from {expected_members}"
        )
    if any(value is None for value in sign_witnesses.values()):
        raise ArithmeticError(f"q={q} did not realize all three B_D signs")

    group = affine_orbits.affine_elements(q)
    unseen = set(members)
    orbit_size_histogram: Counter[int] = Counter()
    orbit_sign_counts = {"negative": 0, "zero": 0, "positive": 0}
    atom_orbit_records: dict[int, list[dict[str, object]]] = {
        j: [] for j in j_histogram
    }
    orbit_count = 0
    while unseen:
        if orbit_count % guard_interval == 0:
            _guard(
                clock=clock,
                deadline=local_deadline,
                q=q,
                stage="affine orbit partition",
                work_items=orbit_count,
            )
        representative = min(unseen)
        orbit = {
            affine_orbits.affine_transform(representative, q, alpha, beta)
            for alpha, beta in group
        }
        if not orbit <= members.keys():
            raise ArithmeticError(f"q={q} affine orbit left the scanned family")
        data = members[representative]
        if any(members[member].j != data.j for member in orbit):
            raise ArithmeticError(f"q={q} B_D is not constant on an affine orbit")
        if any(members[member].b != data.b for member in orbit):
            raise ArithmeticError(f"q={q} b_D is not constant on an affine orbit")
        if any(members[member].a ** 2 != data.a**2 for member in orbit):
            raise ArithmeticError(f"q={q} a_D^2 is not constant on an affine orbit")
        if len(group) % len(orbit):
            raise ArithmeticError("orbit size does not divide the affine group order")
        stabilizer_order = len(group) // len(orbit)
        orbit_record = {
            "representative_coefficients_low_to_high": list(representative),
            "representative_a_D": data.a,
            "b_D": data.b,
            "orbit_size": len(orbit),
            "stabilizer_order": stabilizer_order,
        }
        atom_orbit_records[data.j].append(orbit_record)
        orbit_size_histogram[len(orbit)] += 1
        orbit_sign_counts[_sign(data.j)] += 1
        unseen.difference_update(orbit)
        orbit_count += 1
    _guard(
        clock=clock,
        deadline=local_deadline,
        q=q,
        stage="affine orbit partition",
        work_items=orbit_count,
    )
    if sum(
        record["orbit_size"]
        for records in atom_orbit_records.values()
        for record in records
    ) != member_count:
        raise ArithmeticError("affine orbit records do not reconstruct the family")

    sign_counts = {
        sign: sum(count for j, count in j_histogram.items() if _sign(j) == sign)
        for sign in ("negative", "zero", "positive")
    }
    moment_records = []
    for order in range(1, 7):
        mean = Fraction(
            moment_numerator_sums[order], member_count * q ** (2 * order)
        )
        haar = balanced_haar_moment(order)
        moment_records.append(
            {
                "order": order,
                "sum_of_J_D_to_order": moment_numerator_sums[order],
                "family_mean_B_D_to_order": _fraction_pair(mean),
                "haar_moment": haar,
                "family_minus_haar": _fraction_pair(mean - haar),
            }
        )
    if Fraction(*moment_records[0]["family_mean_B_D_to_order"]) != balanced_mean_all_q(q):
        raise ArithmeticError(f"q={q} first moment differs from the proved all-q formula")

    channel_means = _derived_high_weight_channels(q, member_count, raw_sums)
    chi_0_3 = channel_means["chi_(0,3)"]
    mean_b_cubed_expansion = (
        Fraction(raw_sums["b_cubed"], member_count * q**3)
        - Fraction(raw_sums["b_squared"], member_count * q**2)
        - 2 * Fraction(raw_sums["a_squared_b"], member_count * q**2)
        - Fraction(raw_sums["b"], member_count * q)
        + 3 * Fraction(raw_sums["a_squared"], member_count * q)
    )
    if chi_0_3 != mean_b_cubed_expansion:
        raise ArithmeticError("chi_(0,3) triangular reduction failed")
    third_mean = Fraction(*moment_records[2]["family_mean_B_D_to_order"])
    r6_mean = third_mean - 6 * balanced_mean_all_q(q) + 2 * chi_0_3

    support = []
    for j in sorted(j_histogram):
        support.append(
            {
                "B_numerator_J": j,
                "B_D": _fraction_pair(Fraction(j, q**2)),
                "member_count": j_histogram[j],
                "member_fraction": _fraction_pair(Fraction(j_histogram[j], member_count)),
                "affine_orbit_count": len(atom_orbit_records[j]),
            }
        )
    joint_law = []
    for (a, b), count in sorted(joint_histogram.items()):
        j = 2 * q * a * a - b * b
        joint_law.append(
            {
                "a_D": a,
                "b_D": b,
                "B_numerator_J": j,
                "B_D": _fraction_pair(Fraction(j, q**2)),
                "member_count": count,
                "member_fraction": _fraction_pair(Fraction(count, member_count)),
            }
        )

    lower_j = min(j_histogram)
    upper_j = max(j_histogram)
    absolute_extreme = max(abs(lower_j), abs(upper_j))
    absolute_extreme_js = sorted(j for j in j_histogram if abs(j) == absolute_extreme)
    endpoint_js = sorted({lower_j, upper_j})

    def moment_shares(atoms: Sequence[int]) -> dict[str, list[int]]:
        return {
            str(order): _fraction_pair(
                Fraction(
                    sum(j_histogram[j] * abs(j) ** order for j in atoms),
                    sum(count * abs(j) ** order for j, count in j_histogram.items()),
                )
            )
            for order in (2, 4, 6)
        }

    sign_comparison = {}
    haar_sign = {
        "negative": Fraction(1, 2),
        "zero": Fraction(0),
        "positive": Fraction(1, 2),
    }
    for sign in ("negative", "zero", "positive"):
        member_fraction = Fraction(sign_counts[sign], member_count)
        orbit_fraction = Fraction(orbit_sign_counts[sign], orbit_count)
        sign_comparison[sign] = {
            "member_count": sign_counts[sign],
            "member_fraction": _fraction_pair(member_fraction),
            "member_minus_haar": _fraction_pair(member_fraction - haar_sign[sign]),
            "affine_orbit_count": orbit_sign_counts[sign],
            "uniform_affine_orbit_fraction": _fraction_pair(orbit_fraction),
        }

    ledger = [
        [list(conductor), data.a, data.b, data.j]
        for conductor, data in sorted(members.items())
    ]
    witnesses = {
        sign: {
            "conductor_coefficients_low_to_high": list(conductor),
            "a_D": members[conductor].a,
            "b_D": members[conductor].b,
            "B_numerator_J": members[conductor].j,
            "B_D": _fraction_pair(Fraction(members[conductor].j, q**2)),
        }
        for sign, optional in sign_witnesses.items()
        for conductor in [optional]
        if conductor is not None
    }
    required_source_locked_sums = {
        name: {
            "sum": raw_sums[name],
            "mean": _fraction_pair(Fraction(raw_sums[name], member_count)),
        }
        for name in ("b_cubed", "a_squared_b_squared", "b_fourth")
    }
    sixth_order_raw_sums = {
        name: raw_sums[name]
        for name in (
            "a_sixth",
            "a_fourth_b_squared",
            "a_squared_b_fourth",
            "b_sixth",
        )
    }
    return FieldAnalysis(
        payload={
            "q": q,
            "candidate_count": q**5,
            "member_count": member_count,
            "expected_squarefree_count": expected_members,
            "member_coefficient_ledger_sha256": _canonical_sha256(ledger),
            "joint_a_D_b_D_law": {
                "support_size": len(joint_law),
                "atoms": joint_law,
            },
            "balanced_support": {
                "support_size": len(support),
                "minimum": _fraction_pair(Fraction(lower_j, q**2)),
                "maximum": _fraction_pair(Fraction(upper_j, q**2)),
                "contained_in_exact_haar_support_minus4_to4": (
                    lower_j >= -4 * q**2 and upper_j <= 4 * q**2
                ),
                "J_histogram": _histogram(j_histogram),
                "atoms": support,
            },
            "sign_law": {
                "haar_target": {
                    "negative": [1, 2],
                    "zero": [0, 1],
                    "positive": [1, 2],
                },
                "comparisons": sign_comparison,
            },
            "moments_1_through_6": moment_records,
            "source_locked_raw_aggregate_controls": required_source_locked_sums,
            "third_moment_raw_sums": sixth_order_raw_sums,
            "derived_high_weight_channel_means": {
                name: _fraction_pair(value) for name, value in channel_means.items()
            },
            "third_moment_reduction_frozen_evaluation": {
                "mean_B_D_cubed": _fraction_pair(third_mean),
                "mean_chi_(0,3)": _fraction_pair(chi_0_3),
                "known_6_mean_B_D_contribution": _fraction_pair(
                    6 * balanced_mean_all_q(q)
                ),
                "remaining_mean_R6": _fraction_pair(r6_mean),
                "identity_checked": (
                    third_mean
                    == 6 * balanced_mean_all_q(q) - 2 * chi_0_3 + r6_mean
                ),
            },
            "affine_orbit_analysis": {
                "action": "D(T)|_(alpha,beta)=alpha^-5*D(alpha*T+beta)",
                "group_order": len(group),
                "orbit_count": orbit_count,
                "orbit_size_histogram": _histogram(orbit_size_histogram),
                "B_D_invariant_on_every_orbit": True,
                "weighting_warning": (
                    "member-uniform and orbit-uniform laws are distinct when "
                    "stabilizers are nontrivial"
                ),
            },
            "tail_concentration": {
                "lower_endpoint": _atom_record(
                    lower_j, q, j_histogram, atom_orbit_records, member_count
                ),
                "upper_endpoint": _atom_record(
                    upper_j, q, j_histogram, atom_orbit_records, member_count
                ),
                "absolute_extreme_J_values": absolute_extreme_js,
                "absolute_extreme_atoms": [
                    _atom_record(j, q, j_histogram, atom_orbit_records, member_count)
                    for j in absolute_extreme_js
                ],
                "absolute_extreme_share_of_absolute_moments": moment_shares(
                    absolute_extreme_js
                ),
                "two_endpoint_share_of_absolute_moments": moment_shares(endpoint_js),
                "scope": (
                    "exact concentration in the frozen member law only; no limiting "
                    "tail theorem or orbit-equidistribution claim"
                ),
            },
            "sign_witnesses": witnesses,
        },
        raw_sums=raw_sums,
        channel_means=channel_means,
        orbit_size_histogram=_histogram(orbit_size_histogram),
        orbit_count=orbit_count,
    )


def _source_locks() -> dict[str, dict[str, str]]:
    paths = {
        "producer": Path(__file__).resolve(),
        "note": NOTE_PATH,
        "test": TEST_PATH,
        "coefficient_arithmetic": Q_SCAN_PATH,
        "all_q_mean_note": MOMENT_NOTE_PATH,
        "all_q_mean_certificate": MOMENT_CERTIFICATE_PATH,
        "affine_action": AFFINE_PATH,
        "haar_and_character_source": RANK_SCAN_PATH,
        "haar_and_character_note": RANK_NOTE_PATH,
    }
    return {
        name: {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256_lf_normalized": _lf_normalized_sha256(path),
        }
        for name, path in paths.items()
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
    analyses = [
        analyze_q(
            q,
            candidate_cap=candidate_cap,
            wall_limit_seconds=wall_limit_seconds,
            clock=clock,
            deadline=deadline,
        )
        for q in q_values
    ]
    third_reduction = build_third_moment_reduction()

    q_scan_fixture = json.loads(Q_SCAN_FIXTURE_PATH.read_text(encoding="utf-8"))
    affine_fixture = json.loads(AFFINE_FIXTURE_PATH.read_text(encoding="utf-8"))
    q_scan_by_q = {row["q"]: row for row in q_scan_fixture["families"]}
    affine_by_q = {row["q"]: row for row in affine_fixture["families"]}
    regression_controls: dict[str, object] = {}
    for analysis in analyses:
        family = analysis.payload
        q = int(family["q"])
        q_control = q_scan_by_q[q]
        affine_control = affine_by_q[q]
        checks = {
            "member_count_matches_q_scan": (
                family["member_count"] == q_control["member_count"]
            ),
            "sum_a_squared_matches_q_scan": (
                analysis.raw_sums["a_squared"]
                == q_control["moments"]["a_squared"]["sum"]
            ),
            "sum_a_fourth_matches_q_scan": (
                analysis.raw_sums["a_fourth"]
                == q_control["moments"]["a_fourth"]["sum"]
            ),
            "sum_a_squared_b_matches_q_scan": (
                analysis.raw_sums["a_squared_b"]
                == q_control["moments"]["a_squared_b"]["sum"]
            ),
            "sum_b_matches_q_scan": (
                analysis.raw_sums["b"] == q_control["moments"]["b"]["sum"]
            ),
            "sum_b_squared_matches_q_scan": (
                analysis.raw_sums["b_squared"]
                == q_control["moments"]["b_squared"]["sum"]
            ),
            "orbit_count_matches_affine_fixture": (
                analysis.orbit_count
                == affine_control["orbit_partition"]["orbit_count"]
            ),
            "orbit_size_histogram_matches_affine_fixture": (
                analysis.orbit_size_histogram
                == affine_control["orbit_partition"]["orbit_size_histogram"]
            ),
        }
        if not all(checks.values()):
            raise ArithmeticError(f"q={q} frozen source regression failed: {checks}")
        regression_controls[str(q)] = checks

    frozen_r6 = {
        str(family.payload["q"]): family.payload[
            "third_moment_reduction_frozen_evaluation"
        ]["remaining_mean_R6"]
        for family in analyses
    }
    payload: dict[str, object] = {
        "schema": "riemann.function_field.balanced_control_family_scan.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.BALANCED_CONTROL.Q3_Q5_Q7.V1",
        "status": "EXACT_FROZEN_SCAN_PLUS_LOCKED_ALL_Q_AND_HAAR_THEOREMS",
        "definition": {
            "family": "all monic squarefree quintics D in F_q[T]",
            "coefficient_normalization": (
                "L_D(u)=1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4"
            ),
            "balanced_control": "B_D=2*a_D^2/q-b_D^2/q^2=J_D/q^2",
            "integer_numerator": "J_D=2*q*a_D^2-b_D^2",
        },
        "proved_all_q_and_haar_facts": {
            "finite_family_mean": {
                "status": "PROVED_FOR_EVERY_ODD_PRIME_POWER_Q",
                "formula": "mean(B_D)=q^-1+q^-3-q^-4+q^-5",
                "derivation": (
                    "B=chi_(2,0)-chi_(0,2), with the locked all-q means "
                    "mean(chi_(2,0))=q^-3-q^-4 and "
                    "mean(chi_(0,2))=-q^-1-q^-5"
                ),
                "proof_dependencies": [
                    "research/l-families/atlas/function_field/GENUS2_MOMENT_IDENTITY.md",
                    "research/l-families/atlas/function_field/genus2_moment_identity.py",
                ],
                "not_inferred_from_frozen_fields": True,
            },
            "usp4_haar_law": {
                "status": "PROVED_EXACT_COMPACT_GROUP_LAW",
                "character_identity": "B=chi_(2,0)-chi_(0,2)",
                "torus_factorization": (
                    "B=-(x_1^2+x_1^-2)*(x_2^2+x_2^-2)"
                ),
                "law": (
                    "B has the law of A*S for independent arcsine A and "
                    "Wigner-semicircle S, both supported on [-2,2]"
                ),
                "support": [-4, 4],
                "sign_probabilities": {
                    "negative": [1, 2],
                    "zero": [0, 1],
                    "positive": [1, 2],
                },
                "odd_moments": 0,
                "even_moment_formula": (
                    "Haar(B^(2r))=binomial(2r,r)^2/(r+1)"
                ),
                "moments_1_through_6": [
                    balanced_haar_moment(order) for order in range(1, 7)
                ],
                "proof_dependencies": [
                    "research/l-families/atlas/function_field/USP_COEFFICIENT_MINOR_RANK_SCAN.md",
                    "research/l-families/atlas/function_field/usp_coefficient_minor_rank_scan.py",
                ],
            },
        },
        "frozen_enumeration_facts": {
            "status": "EXHAUSTIVE_ONLY_FOR_Q_3_5_7",
            "q_values": list(FROZEN_Q_VALUES),
            "coverage": (
                "every one of q^5 monic quintic candidates is tested for "
                "squarefreeness in each frozen field"
            ),
            "families": [analysis.payload for analysis in analyses],
            "regression_controls_against_locked_exact_sources": regression_controls,
        },
        "third_moment_reduction": {
            **third_reduction,
            "frozen_mean_R6_values": frozen_r6,
        },
        "conjectures_and_nonclaims": {
            "status": "NO_NEW_ALL_Q_FORMULA_CLAIMED",
            "observed_only": (
                "The first six frozen family moments move toward the symmetric "
                "Haar targets in several visible coordinates, but three fields "
                "do not establish convergence, monotonicity, a rate, or an all-q law."
            ),
            "third_moment": (
                "The three frozen values of mean(R6) are recorded evidence only; "
                "they are not interpolated into a conjectural rational function."
            ),
            "orbit_and_tail": (
                "Affine-orbit and endpoint concentrations are exact for the "
                "frozen polynomial presentation, not moduli-space or limiting laws."
            ),
        },
        "resource_contract": {
            "frozen_q_values": list(FROZEN_Q_VALUES),
            "candidate_cap_per_field": candidate_cap,
            "candidate_counts_per_field": {str(q): q**5 for q in FROZEN_Q_VALUES},
            "maximum_candidate_count_in_any_field": max(q**5 for q in FROZEN_Q_VALUES),
            "larger_field_policy": "REFUSE_EVERY_Q_OUTSIDE_3_5_7",
            "maximum_wall_seconds_for_full_build": wall_limit_seconds,
            "clock": "time.monotonic",
            "candidate_guard_interval": DEFAULT_GUARD_INTERVAL,
            "random_sampling": False,
            "floating_point_in_results": False,
            "numerical_root_finding": False,
        },
        "producer_and_source_locks": {
            "runtime": "Python 3.11+ standard library; exact integer/Fraction arithmetic",
            "input_provenance": "complete deterministic generation; no external data",
            "dependency_direction": (
                "this independent enumeration does not read or hash the earlier "
                "high-weight packet; downstream analyses may source-lock this fixture"
            ),
            "locks": _source_locks(),
        },
        "firewall": (
            "Only the displayed mean formula and compact-group law carry all-q/all-order "
            "quantifiers, and they come from separately locked proofs. Joint laws, signs, "
            "moments, raw sums, affine orbits, and tail concentrations are exhaustive frozen "
            "facts only for q=3,5,7. The third-moment character reduction is pointwise, but "
            "the remaining mean(R6) has no proved all-q evaluation. Nothing here proves "
            "USp(4) equidistribution or has an RH consequence."
        ),
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare against a frozen JSON fixture")
    parser.add_argument("--write", type=Path, help="write the exact JSON fixture")
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"balanced-control fixture mismatch: {args.check}")
        print(f"OK: exact balanced-control scan matches {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(
            json.dumps(fixture, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"OK: wrote exact balanced-control fixture {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
