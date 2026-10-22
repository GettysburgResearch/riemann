#!/usr/bin/env python3
"""Exact bounded scan of Frobenius-power echoes of the balanced USp(4) control.

This producer never enumerates a finite field.  It consumes only the frozen
joint (a_D,b_D) member histograms in balanced_control_family_scan.json.  For

    P_D(T)=T^4+a_D*T^3+b_D*T^2+q*a_D*T+q^2

it derives the coefficients a_{D,r}, b_{D,r} of the polynomial whose roots
are the r-th powers of the roots of P_D, for 1 <= r <= 8, using exact Newton
recurrences.  It then studies

    B_{D,r}=2*a_{D,r}^2/q^r-b_{D,r}^2/q^(2r).

The compact-group comparison is independently reconstructed as a C2 Weyl
constant term; no character or Haar routine is imported.  Every result is an
integer or Fraction.  Histogram-atom and Laurent-operation guards fail closed
well below 20,000 operations.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import Mapping


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUT_PATH = HERE / "balanced_control_family_scan.json"
INPUT_PRODUCER_PATH = HERE / "balanced_control_family_scan.py"
OUTPUT_PATH = HERE / "frobenius_power_echoes.json"
NOTE_PATH = HERE / "FROBENIUS_POWER_ECHOES.md"
TEST_PATH = ROOT / "tests" / "test_frobenius_power_echoes.py"

FROZEN_Q_VALUES = (3, 5, 7)
MAX_POWER = 8
MAX_LAURENT_OPERATIONS = 20_000
MAX_HISTOGRAM_ATOM_STEPS = 20_000

Exponent = tuple[int, int]
Laurent = dict[Exponent, int]


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _sign(value: Fraction) -> str:
    return "negative" if value < 0 else "positive" if value > 0 else "zero"


@dataclass
class ResourceGuard:
    counts: Counter[str] = field(default_factory=Counter)

    def charge(self, name: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("resource charge must be nonnegative")
        self.counts[name] += amount
        if sum(self.counts.values()) > MAX_LAURENT_OPERATIONS:
            raise RuntimeError(
                f"Laurent-operation cap {MAX_LAURENT_OPERATIONS} exceeded"
            )

    def snapshot(self) -> dict[str, int]:
        result = {name: self.counts[name] for name in sorted(self.counts)}
        result["total"] = sum(self.counts.values())
        return result


def laurent_multiply(
    left: Mapping[Exponent, int],
    right: Mapping[Exponent, int],
    guard: ResourceGuard,
) -> Laurent:
    guard.charge("laurent_pair_products", len(left) * len(right))
    result: dict[Exponent, int] = defaultdict(int)
    for (left_x, left_y), left_coefficient in left.items():
        for (right_x, right_y), right_coefficient in right.items():
            result[left_x + right_x, left_y + right_y] += (
                left_coefficient * right_coefficient
            )
    return {
        exponent: coefficient
        for exponent, coefficient in result.items()
        if coefficient
    }


def laurent_power(
    polynomial: Mapping[Exponent, int],
    order: int,
    guard: ResourceGuard,
) -> Laurent:
    if order < 0:
        raise ValueError("Laurent power must be nonnegative")
    result: Laurent = {(0, 0): 1}
    for _ in range(order):
        result = laurent_multiply(result, polynomial, guard)
    return result


def c2_weyl_density(guard: ResourceGuard) -> Laurent:
    """Build prod_{alpha>0}(2-x^alpha-x^-alpha) for C2 from scratch."""

    density: Laurent = {(0, 0): 1}
    positive_roots = ((2, 0), (0, 2), (1, 1), (1, -1))
    for root_x, root_y in positive_roots:
        factor = {
            (0, 0): 2,
            (root_x, root_y): -1,
            (-root_x, -root_y): -1,
        }
        density = laurent_multiply(density, factor, guard)
    if density.get((0, 0)) != 8:
        raise ArithmeticError("C2 Weyl density has unexpected normalization")
    return density


def haar_constant_term(
    polynomial: Mapping[Exponent, int],
    density: Mapping[Exponent, int],
    guard: ResourceGuard,
) -> Fraction:
    """Return the exact USp(4) Haar integral of a torus Laurent polynomial."""

    guard.charge("constant_term_lookups", len(polynomial))
    numerator = sum(
        coefficient * density.get((-exponent[0], -exponent[1]), 0)
        for exponent, coefficient in polynomial.items()
    )
    return Fraction(numerator, 8)


def balanced_power_laurent(power: int) -> Laurent:
    """The exact torus restriction B(U^power)."""

    if power < 1:
        raise ValueError("Frobenius power must be positive")
    return {
        (sign_x * 2 * power, sign_y * 2 * power): -1
        for sign_x in (-1, 1)
        for sign_y in (-1, 1)
    }


def frobenius_power_coefficients(a: int, b: int, q: int, power: int) -> tuple[int, int]:
    """Derive (a_r,b_r) by Newton sums for the r-th-powered roots."""

    if q <= 1:
        raise ValueError("q must exceed one")
    if power < 1:
        raise ValueError("power must be positive")
    coefficients = (1, a, b, q * a, q**2)
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
        raise ArithmeticError("Newton recurrence produced a nonintegral b_r")
    return a_power, b_numerator // 2


def balanced_value(a_power: int, b_power: int, q: int, power: int) -> Fraction:
    return Fraction(
        2 * q**power * a_power**2 - b_power**2,
        q ** (2 * power),
    )


def conjectural_second_power_mean(q: int) -> Fraction:
    """Sparse three-field pattern; intentionally not used as an exact source."""

    if q <= 1:
        raise ValueError("q must exceed one")
    return -Fraction((q - 1) * (q**5 + q**2 - q + 1), q**7)


def echo_recurrence_profile(b_one: Fraction, b_two: Fraction, maximum: int) -> list[Fraction]:
    """Recover B_0,...,B_max from B_1 and B_2 alone."""

    if maximum < 3:
        raise ValueError("echo recurrence needs maximum >= 3")
    p = -b_one
    h = (b_one**2 + b_two) / 2
    values = [Fraction(-4), b_one, b_two]
    values.append(b_one**3 - 3 * h * b_one + 3 * b_one)
    for power in range(4, maximum + 1):
        values.append(
            p * values[power - 1]
            - h * values[power - 2]
            + p * values[power - 3]
            - values[power - 4]
        )
    return values


def _globally_periodic_echo(profile_zero_through_eight: list[Fraction]) -> dict[str, int | str] | None:
    """Certify period/antiperiod from four recurrence initials, not a visual fit."""

    for shift in range(1, 5):
        if all(
            profile_zero_through_eight[index + shift]
            == profile_zero_through_eight[index]
            for index in range(4)
        ):
            return {"type": "periodic", "shift": shift, "global_period_divides": shift}
        if all(
            profile_zero_through_eight[index + shift]
            == -profile_zero_through_eight[index]
            for index in range(4)
        ):
            return {
                "type": "antiperiodic",
                "shift": shift,
                "global_period_divides": 2 * shift,
            }
    return None


def build_haar_packet() -> tuple[dict[str, object], dict[str, int]]:
    guard = ResourceGuard()
    density = c2_weyl_density(guard)
    controls = {power: balanced_power_laurent(power) for power in range(1, MAX_POWER + 1)}

    moments: list[dict[str, object]] = []
    for power in range(1, MAX_POWER + 1):
        row = []
        for order in range(1, 5):
            moment = haar_constant_term(
                laurent_power(controls[power], order, guard), density, guard
            )
            row.append({"order": order, "haar_moment": _fraction_pair(moment)})
        moments.append({"power": power, "moments_1_through_4": row})

    cross_matrix: list[list[list[int]]] = []
    for left_power in range(1, MAX_POWER + 1):
        row = []
        for right_power in range(1, MAX_POWER + 1):
            product = laurent_multiply(
                controls[left_power], controls[right_power], guard
            )
            row.append(_fraction_pair(haar_constant_term(product, density, guard)))
        cross_matrix.append(row)

    mixed_with_first: list[dict[str, object]] = []
    b_one_squared = laurent_power(controls[1], 2, guard)
    for power in range(1, MAX_POWER + 1):
        first_squared_times_power = laurent_multiply(
            b_one_squared, controls[power], guard
        )
        first_times_power_squared = laurent_multiply(
            controls[1], laurent_power(controls[power], 2, guard), guard
        )
        mixed_with_first.append(
            {
                "power": power,
                "haar_mean_B1_squared_Br": _fraction_pair(
                    haar_constant_term(first_squared_times_power, density, guard)
                ),
                "haar_mean_B1_Br_squared": _fraction_pair(
                    haar_constant_term(first_times_power_squared, density, guard)
                ),
            }
        )

    nonzero_distinct_triples: list[dict[str, object]] = []
    distinct_triple_count = 0
    for left_power, middle_power, right_power in itertools.combinations(
        range(1, MAX_POWER + 1), 3
    ):
        distinct_triple_count += 1
        product = laurent_multiply(
            laurent_multiply(
                controls[left_power], controls[middle_power], guard
            ),
            controls[right_power],
            guard,
        )
        moment = haar_constant_term(product, density, guard)
        if moment:
            nonzero_distinct_triples.append(
                {
                    "powers": [left_power, middle_power, right_power],
                    "haar_mixed_third_moment": _fraction_pair(moment),
                    "additive_frequency_relation": (
                        left_power + middle_power == right_power
                    ),
                }
            )

    operations = guard.snapshot()
    packet = {
        "status": "EXACT_INDEPENDENT_C2_WEYL_CONSTANT_TERM",
        "normalization": (
            "(1/8)*CT[f*prod_{alpha in {(2,0),(0,2),(1,1),(1,-1)}}"
            "(2-x^alpha-x^-alpha)]"
        ),
        "balanced_power_torus_identity": (
            "B(U^r)=-(x^(2r)+x^(-2r))*(y^(2r)+y^(-2r))"
        ),
        "moments": moments,
        "pairwise_cross_moment_matrix": {
            "row_and_column_powers": list(range(1, MAX_POWER + 1)),
            "entries": cross_matrix,
        },
        "mixed_third_moments_with_B1": mixed_with_first,
        "strictly_distinct_mixed_third_moments": {
            "status": "EXACT_FOR_ALL_DISTINCT_POSITIVE_POWERS",
            "powers_scanned": list(range(1, MAX_POWER + 1)),
            "triple_count": distinct_triple_count,
            "zero_triple_count": distinct_triple_count
            - len(nonzero_distinct_triples),
            "nonzero_triples": nonzero_distinct_triples,
            "all_power_theorem": (
                "for every 1<=r<s<t, Haar(B_r*B_s*B_t) is zero unless "
                "r+s=t; on that additive resonance it is -2 when r=1 and "
                "-4 when r>=2"
            ),
            "proof": (
                "write B_r=-A_r(x)A_r(y), A_r(z)=z^(2r)+z^(-2r). "
                "The zero Fourier coefficient of A_r*A_s*A_t occurs exactly "
                "at r+s=t and equals 2. The C2 density changes the torus value "
                "-4 only when the next Fourier frequency is 4, which occurs "
                "exactly at r=1; its four axis terms contribute +2"
            ),
        },
        "deduced_pairwise_orthogonality": (
            "Haar(B(U^r)*B(U^s))=0 for 1<=r!=s<=8; the same support "
            "argument proves it for every distinct positive r,s"
        ),
        "scope": (
            "exact compact-group integrals; the pushforward U->U^r is not "
            "asserted to preserve Haar measure"
        ),
    }
    return packet, operations


def _recognized_factorization(q: int, state: tuple[int, int]) -> dict[str, str] | None:
    a_squared, b = state
    if a_squared == 0 and b == 0:
        return {
            "weil_polynomial": "T^4+q^2",
            "normalized_form": "Z^4+1=Phi_8(Z)",
            "spectral_statement": "every normalized root is an eighth root of unity",
        }
    if a_squared == 0 and b == 2 * q:
        return {
            "weil_polynomial": "(T^2+q)^2",
            "normalized_form": "(Z^2+1)^2",
            "spectral_statement": "every normalized root is a fourth root of unity",
        }
    if a_squared == 0 and b == -2 * q:
        return {
            "weil_polynomial": "(T^2-q)^2",
            "normalized_form": "(Z^2-1)^2",
            "spectral_statement": "every normalized root is plus or minus one",
        }
    if q == 3 and a_squared == 9 and b == 6:
        return {
            "weil_polynomial": "(T^2+3)*(T^2+a_D*T+3), a_D in {-3,3}",
            "normalized_form": "one order-4 pair and one order-12 pair",
            "spectral_statement": "all normalized roots are roots of unity",
        }
    return None


def _state_record(
    state: tuple[int, int], member_count: int, q: int
) -> dict[str, object]:
    result: dict[str, object] = {
        "a_D_squared": state[0],
        "b_D": state[1],
        "member_count": member_count,
    }
    factorization = _recognized_factorization(q, state)
    if factorization is not None:
        result["recognized_exact_spectral_form"] = factorization
    return result


def analyze_family(family: Mapping[str, object], atom_step_counter: list[int]) -> dict[str, object]:
    q = int(family["q"])
    atoms = family["joint_a_D_b_D_law"]["atoms"]  # type: ignore[index]
    member_count = int(family["member_count"])
    if sum(int(atom["member_count"]) for atom in atoms) != member_count:
        raise ArithmeticError(f"q={q} joint histogram does not have full member weight")

    moment_sums = {
        power: {order: Fraction(0) for order in range(1, 5)}
        for power in range(1, MAX_POWER + 1)
    }
    sign_counts = {
        power: Counter({"negative": 0, "zero": 0, "positive": 0})
        for power in range(1, MAX_POWER + 1)
    }
    supports = {power: set() for power in range(1, MAX_POWER + 1)}
    powered_coefficient_histograms: dict[int, Counter[tuple[int, int]]] = {
        power: Counter() for power in range(1, MAX_POWER + 1)
    }
    balanced_histograms: dict[int, Counter[Fraction]] = {
        power: Counter() for power in range(1, MAX_POWER + 1)
    }
    endpoint_counts = {
        power: Counter({"minus_four": 0, "plus_four": 0})
        for power in range(1, MAX_POWER + 1)
    }
    cross_sums = {power: Fraction(0) for power in range(1, MAX_POWER + 1)}
    mixed_sums = {
        power: {"B1_squared_Br": Fraction(0), "B1_Br_squared": Fraction(0)}
        for power in range(1, MAX_POWER + 1)
    }
    equal_b_one_counts = {power: 0 for power in range(1, MAX_POWER + 1)}
    negative_b_one_counts = {power: 0 for power in range(1, MAX_POWER + 1)}
    prefix_profiles = {power: set() for power in range(1, MAX_POWER + 1)}
    profile_states: dict[tuple[Fraction, ...], dict[tuple[int, int], int]] = defaultdict(
        lambda: defaultdict(int)
    )
    periodic_profiles: dict[
        tuple[str, int, int], dict[str, object]
    ] = {}

    for atom in atoms:
        a = int(atom["a_D"])
        b = int(atom["b_D"])
        weight = int(atom["member_count"])
        values: list[Fraction] = []
        for power in range(1, MAX_POWER + 1):
            atom_step_counter[0] += 1
            if atom_step_counter[0] > MAX_HISTOGRAM_ATOM_STEPS:
                raise RuntimeError(
                    f"histogram-atom cap {MAX_HISTOGRAM_ATOM_STEPS} exceeded"
                )
            a_power, b_power = frobenius_power_coefficients(a, b, q, power)
            value = balanced_value(a_power, b_power, q, power)
            if not Fraction(-4) <= value <= Fraction(4):
                raise ArithmeticError(f"q={q} power={power} left compact support")
            values.append(value)
            powered_coefficient_histograms[power][a_power, b_power] += weight
            balanced_histograms[power][value] += weight
            supports[power].add(value)
            sign_counts[power][_sign(value)] += weight
            endpoint_counts[power]["minus_four"] += weight if value == -4 else 0
            endpoint_counts[power]["plus_four"] += weight if value == 4 else 0
            for order in range(1, 5):
                moment_sums[power][order] += weight * value**order

        recurrence_values = echo_recurrence_profile(values[0], values[1], MAX_POWER)
        if recurrence_values[1:] != values:
            raise ArithmeticError(f"q={q} Newton and echo recurrences disagree")
        state = (a * a, b)
        profile = tuple(values)
        profile_states[profile][state] += weight
        for depth in range(1, MAX_POWER + 1):
            prefix_profiles[depth].add(profile[:depth])
        periodic = _globally_periodic_echo(recurrence_values)
        if periodic is not None:
            key = (
                str(periodic["type"]),
                int(periodic["shift"]),
                int(periodic["global_period_divides"]),
            )
            record = periodic_profiles.setdefault(
                key,
                {
                    **periodic,
                    "member_count": 0,
                    "coefficient_states": defaultdict(int),
                },
            )
            record["member_count"] = int(record["member_count"]) + weight
            record["coefficient_states"][state] += weight  # type: ignore[index]

        for power, value in enumerate(values, start=1):
            cross_sums[power] += weight * values[0] * value
            mixed_sums[power]["B1_squared_Br"] += weight * values[0] ** 2 * value
            mixed_sums[power]["B1_Br_squared"] += weight * values[0] * value**2
            equal_b_one_counts[power] += weight if value == values[0] else 0
            negative_b_one_counts[power] += weight if value == -values[0] else 0

    means = {
        power: moment_sums[power][1] / member_count
        for power in range(1, MAX_POWER + 1)
    }
    haar_second = {1: Fraction(2), **{power: Fraction(4) for power in range(2, MAX_POWER + 1)}}
    power_rows = []
    for power in range(1, MAX_POWER + 1):
        moments = []
        haar_targets = (0, haar_second[power], 0, 12 if power == 1 else 36)
        for order, haar_target in enumerate(haar_targets, start=1):
            family_moment = moment_sums[power][order] / member_count
            moments.append(
                {
                    "order": order,
                    "family_moment": _fraction_pair(family_moment),
                    "haar_moment": _fraction_pair(haar_target),
                    "family_minus_haar": _fraction_pair(family_moment - haar_target),
                }
            )
        cross = cross_sums[power] / member_count
        covariance = cross - means[1] * means[power]
        power_rows.append(
            {
                "power": power,
                "support_size": len(supports[power]),
                "support_minimum": _fraction_pair(min(supports[power])),
                "support_maximum": _fraction_pair(max(supports[power])),
                "powered_coefficient_joint_law": {
                    "support_size": len(powered_coefficient_histograms[power]),
                    "atom_columns": ["a_(D,r)", "b_(D,r)", "member_count"],
                    "atoms": [
                        [
                            a_power,
                            b_power,
                            powered_coefficient_histograms[power][a_power, b_power],
                        ]
                        for a_power, b_power in sorted(
                            powered_coefficient_histograms[power]
                        )
                    ],
                },
                "balanced_member_law": {
                    "support_size": len(balanced_histograms[power]),
                    "atom_columns": [
                        "B_numerator",
                        "B_denominator",
                        "member_count",
                    ],
                    "atoms": [
                        [
                            value.numerator,
                            value.denominator,
                            balanced_histograms[power][value],
                        ]
                        for value in sorted(balanced_histograms[power])
                    ],
                },
                "moments_1_through_4": moments,
                "sign_member_counts": dict(sign_counts[power]),
                "endpoint_member_counts": dict(endpoint_counts[power]),
                "mean_B1_Br": _fraction_pair(cross),
                "haar_mean_B1_Br": _fraction_pair(haar_second[1] if power == 1 else 0),
                "family_covariance_B1_Br": _fraction_pair(covariance),
                "mean_B1_squared_Br": _fraction_pair(
                    mixed_sums[power]["B1_squared_Br"] / member_count
                ),
                "mean_B1_Br_squared": _fraction_pair(
                    mixed_sums[power]["B1_Br_squared"] / member_count
                ),
                "member_count_Br_equals_B1": equal_b_one_counts[power],
                "member_count_Br_equals_minus_B1": negative_b_one_counts[power],
            }
        )

    collision_records = []
    for profile, states in sorted(profile_states.items()):
        if len(states) < 2:
            continue
        collision_records.append(
            {
                "echo_profile_B1_through_B8": [_fraction_pair(value) for value in profile],
                "distinct_coefficient_state_count": len(states),
                "member_count": sum(states.values()),
                "coefficient_states": [
                    _state_record(state, states[state], q) for state in sorted(states)
                ],
            }
        )

    periodic_records = []
    for key in sorted(periodic_profiles):
        raw = periodic_profiles[key]
        states = raw.pop("coefficient_states")
        periodic_records.append(
            {
                **raw,
                "coefficient_states": [
                    _state_record(state, states[state], q) for state in sorted(states)
                ],
            }
        )

    state_support = {(int(atom["a_D"]) ** 2, int(atom["b_D"])) for atom in atoms}
    if len(profile_states) != len({(profile[0], profile[1]) for profile in profile_states}):
        raise ArithmeticError("B1,B2 failed to distinguish complete echo profiles")

    return {
        "q": q,
        "status": "EXACT_MEMBER_WEIGHT_LAW_FROM_FROZEN_JOINT_HISTOGRAM",
        "member_count": member_count,
        "input_joint_atom_count": len(atoms),
        "twist_quotiented_coefficient_state_count": len(state_support),
        "complete_echo_profile_count": len(profile_states),
        "prefix_distinct_profile_counts": [
            {"depth": depth, "count": len(prefix_profiles[depth])}
            for depth in range(1, MAX_POWER + 1)
        ],
        "powers": power_rows,
        "distinct_coefficient_states_with_same_complete_echo": collision_records,
        "globally_periodic_or_antiperiodic_echoes": periodic_records,
        "resonance_firewall": (
            "periodicity here is an exact consequence of four initial equalities and "
            "the order-four echo recurrence; it is only a resonance signature. It does "
            "not by itself prove supersingularity, extra endomorphisms, or a cyclotomic "
            "factorization of the original Frobenius polynomial"
        ),
    }


def build_fixture() -> dict[str, object]:
    input_data = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    input_payload = dict(input_data)
    input_claimed_hash = input_payload.pop("payload_sha256", None)
    if input_claimed_hash != _canonical_sha256(input_payload):
        raise ValueError("balanced-control input payload hash mismatch")
    if input_data.get("schema") != "riemann.function_field.balanced_control_family_scan.v1":
        raise ValueError("unexpected balanced-control input schema")
    frozen = input_data["frozen_enumeration_facts"]
    if tuple(frozen["q_values"]) != FROZEN_Q_VALUES:
        raise ValueError("balanced-control input q ladder drifted")

    haar_packet, symbolic_operations = build_haar_packet()
    atom_step_counter = [0]
    families = [
        analyze_family(family, atom_step_counter)
        for family in sorted(frozen["families"], key=lambda row: int(row["q"]))
    ]
    if tuple(family["q"] for family in families) != FROZEN_Q_VALUES:
        raise ArithmeticError("finite family output q ladder drifted")
    second_power_pattern_evaluations = []
    for family in families:
        q = int(family["q"])
        observed = Fraction(*family["powers"][1]["moments_1_through_4"][0]["family_moment"])
        candidate = conjectural_second_power_mean(q)
        if observed != candidate:
            raise ArithmeticError("frozen second-power candidate evaluation drifted")
        second_power_pattern_evaluations.append(
            {
                "q": q,
                "observed_mean_B2": _fraction_pair(observed),
                "candidate_value": _fraction_pair(candidate),
                "matches": True,
            }
        )

    core: dict[str, object] = {
        "schema": "riemann.function_field.frobenius_power_echoes.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.FROBENIUS_POWER_ECHOES.Q3_Q5_Q7.V1",
        "status": "EXACT_FROZEN_HISTOGRAM_TRANSFORM_PLUS_EXACT_HAAR_BASELINE",
        "definition": {
            "source_polynomial": "T^4+a_D*T^3+b_D*T^2+q*a_D*T+q^2",
            "powered_polynomial": (
                "prod_i(T-alpha_i^r)=T^4+a_(D,r)*T^3+b_(D,r)*T^2+"
                "q^r*a_(D,r)*T+q^(2r)"
            ),
            "echo_control": "B_(D,r)=2*a_(D,r)^2/q^r-b_(D,r)^2/q^(2r)",
            "powers": list(range(1, MAX_POWER + 1)),
            "weighting": "uniform monic-squarefree-quintic member weighting inherited exactly from the input histogram",
        },
        "exact_echo_collapse_theorem": {
            "status": "EXACT_POINTWISE_FOR_EVERY_USP4_CONJUGACY_CLASS_AND_EVERY_R_GE_0",
            "angle_coordinates": (
                "put u=x^2+x^-2, v=y^2+y^-2 and C_0(z)=2, C_1(z)=z, "
                "C_r(z)=z*C_(r-1)(z)-C_(r-2)(z); then B_r=-C_r(u)C_r(v)"
            ),
            "two_invariants": (
                "p=u*v=-B_1 and h=u^2+v^2-2=(B_1^2+B_2)/2"
            ),
            "initials": (
                "B_0=-4; B_3=B_1^3-3*((B_1^2+B_2)/2)*B_1+3*B_1"
            ),
            "recurrence": (
                "B_r=p*B_(r-1)-h*B_(r-2)+p*B_(r-3)-B_(r-4), r>=4, "
                "p=-B_1, h=(B_1^2+B_2)/2"
            ),
            "coefficient_interpretation": (
                "u+v=(a_D^2-2*b_D)/q up to the sign convention for a_(D,2); "
                "the whole echo sequence sees only (u*v,(u+v)^2), hence loses "
                "the simultaneous sign (u,v)->(-u,-v)"
            ),
            "consequence": (
                "no B_r with r>=3 supplies an independent pointwise detector coordinate beyond (B_1,B_2)"
            ),
        },
        "exact_haar_baseline": haar_packet,
        "frozen_family_laws": {
            "status": "EXACT_ONLY_FOR_Q_3_5_7",
            "families": families,
        },
        "frozen_pattern_conjectures": {
            "mean_B2": {
                "status": "CONJECTURAL_SPARSE_FORM_MATCHING_ONLY_Q_3_5_7",
                "candidate": (
                    "mean(B_(D,2))=-(q-1)*(q^5+q^2-q+1)/q^7"
                ),
                "frozen_evaluations": second_power_pattern_evaluations,
                "why_recorded": (
                    "the reduced denominator is q^7 in all three fields and the "
                    "numerator has this low-complexity factored form"
                ),
                "why_not_a_theorem": (
                    "three field values do not determine a rational function of q"
                ),
                "smallest_proof_burden": (
                    "evaluate the exact family average of "
                    "2*(2*b_D-a_D^2)^2/q^2-"
                    "(b_D^2-2*q*a_D^2+2*q^2)^2/q^4"
                ),
            }
        },
        "firewall": {
            "proved": [
                "Newton derivation of every displayed a_(D,r), b_(D,r), and B_(D,r)",
                "the all-r two-coordinate echo collapse and recurrence",
                "the independent C2 Weyl constant terms and all displayed Haar comparisons",
                "all-power pairwise orthogonality and the additive-frequency mixed-third-moment theorem",
                "the member-weight q=3,5,7 transforms of the locked joint histograms",
                "global periodicity/antiperiodicity of any explicitly listed echo sequence, by recurrence",
            ],
            "not_proved": [
                "a formula in q for any r>=2 family moment",
                "equidistribution or an error term as q tends to infinity",
                "supersingularity, complex multiplication, or extra endomorphisms from an echo signature alone",
                "independence of B(U^r) under Haar; only displayed moments and pairwise orthogonality are proved",
                "any implication for RH or GRH",
            ],
        },
        "resource_contract": {
            "finite_field_enumeration": False,
            "input": "source-locked joint (a_D,b_D) histograms only",
            "maximum_power": MAX_POWER,
            "maximum_laurent_operations": MAX_LAURENT_OPERATIONS,
            "actual_laurent_operations": symbolic_operations,
            "maximum_histogram_atom_steps": MAX_HISTOGRAM_ATOM_STEPS,
            "actual_histogram_atom_steps": atom_step_counter[0],
            "floating_point_in_results": False,
            "random_sampling": False,
        },
        "producer_and_source_locks": {
            "runtime": "Python 3.11+ standard library; exact integer/Fraction arithmetic",
            "locks": {
                "input_fixture": {
                    "path": "research/l-families/atlas/function_field/balanced_control_family_scan.json",
                    "sha256_lf_normalized": _lf_normalized_sha256(INPUT_PATH),
                    "payload_sha256": input_claimed_hash,
                },
                "input_producer": {
                    "path": "research/l-families/atlas/function_field/balanced_control_family_scan.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(INPUT_PRODUCER_PATH),
                },
                "producer": {
                    "path": "research/l-families/atlas/function_field/frobenius_power_echoes.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(Path(__file__)),
                },
                "note": {
                    "path": "research/l-families/atlas/function_field/FROBENIUS_POWER_ECHOES.md",
                    "sha256_lf_normalized": _lf_normalized_sha256(NOTE_PATH),
                },
                "test": {
                    "path": "tests/test_frobenius_power_echoes.py",
                    "sha256_lf_normalized": _lf_normalized_sha256(TEST_PATH),
                },
            },
        },
    }
    core["payload_sha256"] = _canonical_sha256(core)
    return core


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write the deterministic JSON")
    mode.add_argument("--check", action="store_true", help="check the committed JSON")
    parser.add_argument("path", nargs="?", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    fixture = build_fixture()
    rendered = json.dumps(fixture, indent=2, sort_keys=True) + "\n"
    if args.write:
        args.path.write_text(rendered, encoding="utf-8", newline="\n")
        print(
            "frobenius-power echoes: "
            f"q={FROZEN_Q_VALUES} powers=1..{MAX_POWER} "
            f"payload_sha256={fixture['payload_sha256']}"
        )
        return 0
    if not args.path.exists() or args.path.read_text(encoding="utf-8") != rendered:
        print(f"stale or missing fixture: {args.path}")
        return 1
    print(
        "frobenius-power echoes check: ok "
        f"payload_sha256={fixture['payload_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
