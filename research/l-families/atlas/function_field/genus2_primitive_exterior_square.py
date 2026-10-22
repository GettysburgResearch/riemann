#!/usr/bin/env python3
"""Exact bounded packet for the primitive exterior square of genus-two H^1.

For

    P_C(T) = 1 + a*T + b*T^2 + q*a*T^3 + q^2*T^4,

the six-dimensional exterior square contains the canonical polarization Tate
line.  This script derives the remaining degree-five polynomial in two
independent ways, exposes its additional memberwise (1-q*T) factor, evaluates
low character moments from already-locked all-q formulas, and pushes forward
the complete q=3,5,7 (a,b) histograms.  It performs no finite-field or curve
enumeration.  All accepted numerical values are integers or Fractions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_primitive_exterior_square.json"
NOTE_PATH = HERE / "GENUS2_PRIMITIVE_EXTERIOR_SQUARE.md"
TEST_PATH = ROOT / "tests" / "test_genus2_primitive_exterior_square.py"

BALANCED_FIXTURE_PATH = HERE / "balanced_control_family_scan.json"
BALANCED_SOURCE_PATH = HERE / "balanced_control_family_scan.py"
GENUS2_FORMULA_FIXTURE_PATH = HERE / "genus2_q_scan.json"
GENUS2_FORMULA_SOURCE_PATH = HERE / "genus2_q_scan.py"
MOMENT_CERTIFICATE_PATH = HERE / "genus2_moment_identity.py"
MOMENT_NOTE_PATH = HERE / "GENUS2_MOMENT_IDENTITY.md"

FROZEN_Q_VALUES = (3, 5, 7)
MAX_FROZEN_MOMENT_ORDER = 8
MAX_SO5_HAAR_ORDER = 6
ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE = 10_000

# Pin exact inputs rather than accepting an arbitrary self-consistent fixture
# with the same schema and formulas.
EXPECTED_BALANCED_PAYLOAD_SHA256 = (
    "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c"
)
EXPECTED_GENUS2_FORMULA_PAYLOAD_SHA256 = (
    "80a28d820e45b2548e3e4b482982ef8313c8919f4a3fb9cc2c0b622b244870b5"
)
EXPECTED_MEMBER_LEDGER_SHA256 = {
    3: "e38543c4526e6b330f012274398a258f2d021ddae18442d2f0094d42ec229790",
    5: "69fe496e1cca2090ca62bf7622ff34c3ab3aef1b9268dfb41c4df94d380a9d0a",
    7: "c1d4ca30f45341de53af20ab4e4ca3f9bff79542146f1ac2230169eec9669655",
}
EXPECTED_ATOM_COUNTS = {3: 32, 5: 81, 7: 138}
EXPECTED_MEMBER_COUNTS = {3: 162, 5: 2_500, 7: 14_406}


@dataclass
class ResourceGuard:
    """Bound declared high-level visits and term products, not CPU instructions."""

    counts: Counter[str] = field(default_factory=Counter)

    def charge(self, name: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("resource charge must be nonnegative")
        prospective = sum(self.counts.values()) + amount
        if prospective >= ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE:
            raise RuntimeError(
                "accounted-work-unit exclusive cap 10000 would be reached or exceeded"
            )
        self.counts[name] += amount

    @property
    def total(self) -> int:
        return sum(self.counts.values())

    def snapshot(self) -> dict[str, int]:
        output = {name: self.counts[name] for name in sorted(self.counts)}
        output["total_accounted_work_units"] = self.total
        return output


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    return hashlib.sha256(encoded).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _prime_power_data(q: int) -> tuple[int, int]:
    if not isinstance(q, int) or q < 3 or q % 2 == 0:
        raise ValueError("q must be an odd prime power")
    for candidate in range(2, math.isqrt(q) + 1):
        if q % candidate:
            continue
        if any(
            candidate % divisor == 0
            for divisor in range(2, math.isqrt(candidate) + 1)
        ):
            continue
        residue = q
        exponent = 0
        while residue % candidate == 0:
            residue //= candidate
            exponent += 1
        if residue != 1 or candidate == 2:
            raise ValueError("q must be an odd prime power")
        return candidate, exponent
    return q, 1


def _load_locked_fixture(path: Path, expected_payload: str) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    claimed = payload.get("payload_sha256")
    unhashed = dict(payload)
    unhashed.pop("payload_sha256", None)
    if claimed != expected_payload or _canonical_sha256(unhashed) != claimed:
        raise ValueError(f"{path.name} payload/source pin mismatch")
    return payload


def _validate_locked_theorems(
    balanced: Mapping[str, object], genus2: Mapping[str, object]
) -> list[Mapping[str, object]]:
    if balanced.get("schema") != "riemann.function_field.balanced_control_family_scan.v1":
        raise ValueError("unexpected balanced-control schema")
    if genus2.get("schema") != "riemann.function_field.genus2_q_scan.v1":
        raise ValueError("unexpected genus-two formula schema")

    theorem = genus2["closed_formula_target"]  # type: ignore[assignment]
    expected = {
        "mean_a_squared": "q-1+(q^2+q-2)/q^3",
        "mean_a_fourth": "3*q^2-7*q+5+12/q-14/q^2-11/q^3",
        "mean_a_squared_b": "(q+1)*(q^2-2*q+3)*(2*q^2-2*q-1)/q^3",
        "mean_b": "q-1+(q^2-1)/q^3",
        "mean_b_squared": "2*q^2-3*q+2+(q^2-3*q-1)/q^3",
    }
    if theorem["scope"] != "every odd prime power q":
        raise ValueError("genus-two all-q scope drifted")
    if theorem["status"] != "PROVED_IN_DRAFT_RESEARCH_NOTE":
        raise ValueError("genus-two theorem status drifted")
    for name, formula in expected.items():
        if theorem[name] != formula:
            raise ValueError(f"locked {name} formula drifted")

    profile = theorem["low_weight_character_profile"]
    expected_profile = {
        "mean_chi_(0,1)": "-1/q+1/q^2-1/q^4",
        "mean_chi_(2,0)": "1/q^3-1/q^4",
        "normalization": (
            "b_D/q=1+chi_(0,1); a_D^2/q=1+chi_(0,1)+chi_(2,0); "
            "b_D^2/q^2=2+2*chi_(0,1)+chi_(2,0)+chi_(0,2); "
            "a_D^2*b_D/q^2=2+3*chi_(0,1)+3*chi_(2,0)+chi_(0,2)+chi_(2,1); "
            "a_D^4/q^2=3+5*chi_(0,1)+6*chi_(2,0)+2*chi_(0,2)+3*chi_(2,1)+chi_(4,0)"
        ),
    }
    for name, formula in expected_profile.items():
        if profile[name] != formula:
            raise ValueError(f"locked character profile {name} drifted")

    frozen = balanced["frozen_enumeration_facts"]  # type: ignore[assignment]
    if tuple(frozen["q_values"]) != FROZEN_Q_VALUES:
        raise ValueError("balanced-control q ladder drifted")
    if frozen["status"] != "EXHAUSTIVE_ONLY_FOR_Q_3_5_7":
        raise ValueError("balanced-control coverage status drifted")
    families = sorted(frozen["families"], key=lambda row: int(row["q"]))
    if tuple(int(row["q"]) for row in families) != FROZEN_Q_VALUES:
        raise ValueError("balanced-control family rows drifted")
    for row in families:
        q = int(row["q"])
        atoms = row["joint_a_D_b_D_law"]["atoms"]
        if len(atoms) != EXPECTED_ATOM_COUNTS[q]:
            raise ValueError(f"q={q} joint histogram atom count drifted")
        if int(row["member_count"]) != EXPECTED_MEMBER_COUNTS[q]:
            raise ValueError(f"q={q} member count drifted")
        if row["member_coefficient_ledger_sha256"] != EXPECTED_MEMBER_LEDGER_SHA256[q]:
            raise ValueError(f"q={q} complete-member ledger drifted")
    return families


def root_power_sums(coefficients: Sequence[int], maximum_degree: int) -> list[int]:
    """Power sums for roots of x^d+c1*x^(d-1)+...+cd."""

    if not coefficients or coefficients[0] != 1:
        raise ValueError("a monic positive-degree polynomial is required")
    degree = len(coefficients) - 1
    if degree < 1 or maximum_degree < 0:
        raise ValueError("a monic positive-degree polynomial is required")
    output = [degree]
    for order in range(1, maximum_degree + 1):
        total = 0
        for index in range(1, min(order, degree) + 1):
            if index == order:
                total += index * coefficients[index]
            else:
                total += coefficients[index] * output[order - index]
        output.append(-total)
    return output


def coefficients_from_power_sums(power_sums: Sequence[int]) -> tuple[int, ...]:
    """Coefficients of product(1-root*T) from p_1,...,p_n."""

    if not power_sums or power_sums[0] != len(power_sums) - 1:
        raise ValueError("power_sums[0] must equal the requested polynomial degree")
    coefficients = [1]
    for order in range(1, len(power_sums)):
        numerator = -sum(
            coefficients[order - index] * power_sums[index]
            for index in range(1, order + 1)
        )
        if numerator % order:
            raise ArithmeticError("Newton coefficient lost integrality")
        coefficients.append(numerator // order)
    return tuple(coefficients)


def exterior_square_coefficients_via_newton(a: int, b: int, q: int) -> tuple[int, ...]:
    """Independent pairwise-eigenvalue derivation of the degree-six factor."""

    _prime_power_data(q)
    original = root_power_sums((1, a, b, q * a, q * q), 12)
    exterior_power_sums = [6]
    for order in range(1, 7):
        numerator = original[order] ** 2 - original[2 * order]
        if numerator % 2:
            raise ArithmeticError("pairwise power sum lost integrality")
        exterior_power_sums.append(numerator // 2)
    return coefficients_from_power_sums(exterior_power_sums)


def exterior_square_coefficients_closed(a: int, b: int, q: int) -> tuple[int, ...]:
    """Closed degree-six factor on exterior^2 H^1."""

    _prime_power_data(q)
    return (
        1,
        -b,
        q * (a * a - q),
        -2 * q * q * (a * a - b),
        q**3 * (a * a - q),
        -q**4 * b,
        q**6,
    )


def divide_by_one_minus_scalar_t(
    coefficients: Sequence[int], scalar: int
) -> tuple[tuple[int, ...], int]:
    """Return quotient and remainder for P(T)/(1-scalar*T)."""

    if not coefficients or coefficients[0] != 1:
        raise ValueError("a polynomial with constant coefficient one is required")
    quotient = [1]
    for coefficient in coefficients[1:-1]:
        quotient.append(coefficient + scalar * quotient[-1])
    remainder = coefficients[-1] + scalar * quotient[-1]
    return tuple(quotient), remainder


def primitive_exterior_square_coefficients_closed(
    a: int, b: int, q: int
) -> tuple[int, ...]:
    """Degree-five factor after removing the canonical polarization line."""

    _prime_power_data(q)
    return (
        1,
        q - b,
        q * (a * a - b),
        -q * q * (a * a - b),
        q**3 * (b - q),
        -q**5,
    )


def primitive_exterior_square_coefficients_via_newton(
    a: int, b: int, q: int
) -> tuple[int, ...]:
    full = exterior_square_coefficients_via_newton(a, b, q)
    quotient, remainder = divide_by_one_minus_scalar_t(full, q)
    if remainder:
        raise ArithmeticError("the polarization Tate line did not divide exterior square")
    return quotient


def moving_local_eigenline_quotient(a: int, b: int, q: int) -> tuple[int, ...]:
    """Quartic after the additional memberwise Frobenius-stable (1-q*T)."""

    primitive = primitive_exterior_square_coefficients_closed(a, b, q)
    quotient, remainder = divide_by_one_minus_scalar_t(primitive, q)
    if remainder:
        raise ArithmeticError("the SO(5) pointwise eigenvalue q disappeared")
    return quotient


def moving_local_eigenline_quotient_closed(
    a: int, b: int, q: int
) -> tuple[int, ...]:
    _prime_power_data(q)
    return (
        1,
        2 * q - b,
        q * (a * a - 2 * b + 2 * q),
        q * q * (2 * q - b),
        q**4,
    )


def all_q_input_moments(q: int) -> dict[str, Fraction]:
    """The five exact coefficient moments imported from the locked theorem."""

    _prime_power_data(q)
    return {
        "a2": Fraction(q - 1) + Fraction(q * q + q - 2, q**3),
        "a4": Fraction(3 * q * q - 7 * q + 5)
        + Fraction(12, q)
        - Fraction(14, q * q)
        - Fraction(11, q**3),
        "a2b": Fraction(
            (q + 1) * (q * q - 2 * q + 3) * (2 * q * q - 2 * q - 1),
            q**3,
        ),
        "b": Fraction(q - 1) + Fraction(q * q - 1, q**3),
        "b2": Fraction(2 * q * q - 3 * q + 2)
        + Fraction(q * q - 3 * q - 1, q**3),
    }


def all_q_primitive_character_moments(q: int) -> dict[str, Fraction]:
    """Moments for s=Tr(W)/q and k=e2(W)/q^2 from locked inputs."""

    moments = all_q_input_moments(q)
    mean_s = moments["b"] / q - 1
    mean_s2 = moments["b2"] / q**2 - 2 * moments["b"] / q + 1
    mean_k = (moments["a2"] - moments["b"]) / q
    mean_k2 = (
        moments["a4"] - 2 * moments["a2b"] + moments["b2"]
    ) / q**2
    mean_sk = (
        (moments["a2b"] - moments["b2"]) / q**2
        - (moments["a2"] - moments["b"]) / q
    )
    return {
        "mean_s": mean_s,
        "mean_s_squared": mean_s2,
        "mean_k": mean_k,
        "mean_k_squared": mean_k2,
        "mean_s_times_k": mean_sk,
    }


LaurentPolynomial = dict[tuple[int, int], int]


def _laurent_multiply(
    left: Mapping[tuple[int, int], int],
    right: Mapping[tuple[int, int], int],
    guard: ResourceGuard | None = None,
) -> LaurentPolynomial:
    if guard is not None:
        guard.charge("weyl_laurent_term_products", len(left) * len(right))
    output: Counter[tuple[int, int]] = Counter()
    for (left_x, left_y), left_value in left.items():
        for (right_x, right_y), right_value in right.items():
            output[(left_x + right_x, left_y + right_y)] += left_value * right_value
    return {exponent: value for exponent, value in output.items() if value}


def so5_standard_haar_trace_moments(
    maximum_order: int = MAX_SO5_HAAR_ORDER,
    guard: ResourceGuard | None = None,
) -> list[int]:
    """Exact B2 Weyl constant terms for the SO(5) standard character."""

    if not 0 <= maximum_order <= MAX_SO5_HAAR_ORDER:
        raise ValueError("SO(5) Haar evaluator is deliberately restricted to 0..6")
    # Standard weights 0,+/-e1,+/-e2.
    character: LaurentPolynomial = {
        (0, 0): 1,
        (1, 0): 1,
        (-1, 0): 1,
        (0, 1): 1,
        (0, -1): 1,
    }
    # Positive B2 roots e1-e2,e2,e1,e1+e2.  Each pair contributes
    # (1-e^alpha)(1-e^-alpha)=2-e^alpha-e^-alpha.
    denominator: LaurentPolynomial = {(0, 0): 1}
    for root_x, root_y in ((1, -1), (0, 1), (1, 0), (1, 1)):
        denominator = _laurent_multiply(
            denominator,
            {(0, 0): 2, (root_x, root_y): -1, (-root_x, -root_y): -1},
            guard,
        )

    power: LaurentPolynomial = {(0, 0): 1}
    output = []
    for order in range(maximum_order + 1):
        if guard is not None:
            guard.charge("weyl_constant_term_pairs", len(power))
        constant_term = sum(
            value * denominator.get((-exponent[0], -exponent[1]), 0)
            for exponent, value in power.items()
        )
        if constant_term % 8:
            raise ArithmeticError("B2 Weyl constant term not divisible by |W|=8")
        output.append(constant_term // 8)
        if order != maximum_order:
            power = _laurent_multiply(power, character, guard)
    return output


def _source_locks() -> dict[str, object]:
    paths = {
        "balanced_fixture": BALANCED_FIXTURE_PATH,
        "balanced_source": BALANCED_SOURCE_PATH,
        "genus2_formula_fixture": GENUS2_FORMULA_FIXTURE_PATH,
        "genus2_formula_source": GENUS2_FORMULA_SOURCE_PATH,
        "all_q_moment_certificate": MOMENT_CERTIFICATE_PATH,
        "all_q_moment_note": MOMENT_NOTE_PATH,
        "producer": Path(__file__).resolve(),
        "note": NOTE_PATH,
        "test": TEST_PATH,
    }
    locks = {
        name: {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256_lf_normalized": _lf_normalized_sha256(path),
        }
        for name, path in paths.items()
    }
    locks["balanced_fixture"]["payload_sha256"] = EXPECTED_BALANCED_PAYLOAD_SHA256
    locks["genus2_formula_fixture"][
        "payload_sha256"
    ] = EXPECTED_GENUS2_FORMULA_PAYLOAD_SHA256
    return locks


def _formula_strings() -> dict[str, str]:
    return {
        "mean_s": "-1/q+1/q^2-1/q^4",
        "mean_s_squared": "1-1/q+1/q^3-1/q^4-1/q^5",
        "mean_k": "1/q^3-1/q^4",
        "mean_k_squared": "1-2/q+1/q^2+3/q^3-3/q^4-6/q^5",
        "mean_s_times_k": "-1/q+1/q^2+3/q^3-3/q^4-2/q^5",
    }


def _expected_character_moments(q: int) -> dict[str, Fraction]:
    return {
        "mean_s": -Fraction(1, q) + Fraction(1, q**2) - Fraction(1, q**4),
        "mean_s_squared": Fraction(1)
        - Fraction(1, q)
        + Fraction(1, q**3)
        - Fraction(1, q**4)
        - Fraction(1, q**5),
        "mean_k": Fraction(1, q**3) - Fraction(1, q**4),
        "mean_k_squared": Fraction(1)
        - Fraction(2, q)
        + Fraction(1, q**2)
        + Fraction(3, q**3)
        - Fraction(3, q**4)
        - Fraction(6, q**5),
        "mean_s_times_k": -Fraction(1, q)
        + Fraction(1, q**2)
        + Fraction(3, q**3)
        - Fraction(3, q**4)
        - Fraction(2, q**5),
    }


def analyze_frozen_family(
    row: Mapping[str, object], guard: ResourceGuard, so5_haar: Sequence[int]
) -> dict[str, object]:
    q = int(row["q"])
    if q not in FROZEN_Q_VALUES:
        raise ValueError("frozen transform supports only q=3,5,7")
    source_atoms = row["joint_a_D_b_D_law"]["atoms"]  # type: ignore[index]
    total_members = int(row["member_count"])
    coefficient_histogram: Counter[tuple[int, int]] = Counter()
    trace_histogram: Counter[int] = Counter()
    signed_histogram: dict[tuple[int, int], int] = {}
    raw_input_sums: Counter[str] = Counter()
    zero_a_members = 0
    witnesses: list[dict[str, object]] = []

    for index, atom in enumerate(source_atoms):
        guard.charge("histogram_atom_visits")
        a = int(atom["a_D"])
        b = int(atom["b_D"])
        count = int(atom["member_count"])
        signed_histogram[(a, b)] = count
        if a == 0:
            zero_a_members += count

        full_closed = exterior_square_coefficients_closed(a, b, q)
        full_newton = exterior_square_coefficients_via_newton(a, b, q)
        primitive_closed = primitive_exterior_square_coefficients_closed(a, b, q)
        primitive_newton = primitive_exterior_square_coefficients_via_newton(a, b, q)
        moving_closed = moving_local_eigenline_quotient_closed(a, b, q)
        moving_division = moving_local_eigenline_quotient(a, b, q)
        guard.charge("newton_atom_checks")
        if full_closed != full_newton:
            raise ArithmeticError("closed exterior-square formula disagrees with Newton")
        if primitive_closed != primitive_newton:
            raise ArithmeticError("closed primitive formula disagrees with Tate quotient")
        if moving_closed != moving_division:
            raise ArithmeticError("moving-eigenline quartic formula disagrees with division")

        s_numerator = b - q
        k_numerator = a * a - b
        coefficient_histogram[(s_numerator, k_numerator)] += count
        trace_histogram[s_numerator] += count
        raw_input_sums["members"] += count
        raw_input_sums["a2"] += count * a * a
        raw_input_sums["a4"] += count * a**4
        raw_input_sums["a2b"] += count * a * a * b
        raw_input_sums["b"] += count * b
        raw_input_sums["b2"] += count * b * b

        if index in (0, len(source_atoms) // 2, len(source_atoms) - 1):
            witnesses.append(
                {
                    "input_a_b": [a, b],
                    "full_exterior_square_coefficients": list(full_closed),
                    "primitive_coefficients": list(primitive_closed),
                    "pointwise_quartic_quotient": list(moving_closed),
                }
            )

    if raw_input_sums["members"] != total_members:
        raise ArithmeticError("histogram transform lost family members")
    if any(
        signed_histogram.get((-a, b)) != count
        for (a, b), count in signed_histogram.items()
    ):
        raise ArithmeticError("source signed histogram lost a -> -a symmetry")

    locked_inputs = all_q_input_moments(q)
    for name in ("a2", "a4", "a2b", "b", "b2"):
        if Fraction(raw_input_sums[name], total_members) != locked_inputs[name]:
            raise ArithmeticError(f"q={q} frozen {name} sum disagrees with all-q theorem")

    exact_characters = all_q_primitive_character_moments(q)
    if exact_characters != _expected_character_moments(q):
        raise ArithmeticError("derived primitive-character formula simplification drifted")

    frozen_character_sums = {
        "mean_s": Fraction(0),
        "mean_s_squared": Fraction(0),
        "mean_k": Fraction(0),
        "mean_k_squared": Fraction(0),
        "mean_s_times_k": Fraction(0),
    }
    coefficient_atoms = []
    for (s_numerator, k_numerator), count in sorted(coefficient_histogram.items()):
        guard.charge("coefficient_character_terms", 5)
        probability = Fraction(count, total_members)
        s_value = Fraction(s_numerator, q)
        k_value = Fraction(k_numerator, q)
        frozen_character_sums["mean_s"] += probability * s_value
        frozen_character_sums["mean_s_squared"] += probability * s_value**2
        frozen_character_sums["mean_k"] += probability * k_value
        frozen_character_sums["mean_k_squared"] += probability * k_value**2
        frozen_character_sums["mean_s_times_k"] += probability * s_value * k_value
        b = s_numerator + q
        a_squared = k_numerator + b
        primitive = primitive_exterior_square_coefficients_closed(
            math.isqrt(a_squared), b, q
        )
        if math.isqrt(a_squared) ** 2 != a_squared:
            raise ArithmeticError("compressed exterior-square state lost square a^2")
        quotient = moving_local_eigenline_quotient_closed(math.isqrt(a_squared), b, q)
        coefficient_atoms.append(
            {
                "source_twist_quotient_a_squared_b": [a_squared, b],
                "trace_s": _fraction_pair(s_value),
                "second_character_k": _fraction_pair(k_value),
                "primitive_coefficients_c0_through_c5": list(primitive),
                "pointwise_quartic_coefficients_d0_through_d4": list(quotient),
                "member_count": count,
                "member_fraction": _fraction_pair(probability),
            }
        )
    if frozen_character_sums != exact_characters:
        raise ArithmeticError("frozen character moments disagree with all-q formulas")

    trace_moments = []
    for order in range(MAX_FROZEN_MOMENT_ORDER + 1):
        raw_sum = 0
        for numerator, count in trace_histogram.items():
            guard.charge("frozen_trace_moment_terms")
            raw_sum += count * numerator**order
        mean = Fraction(raw_sum, total_members * q**order)
        record: dict[str, object] = {
            "order": order,
            "raw_sum_(b-q)^order": raw_sum,
            "family_mean_s_power": _fraction_pair(mean),
        }
        if order <= MAX_SO5_HAAR_ORDER:
            record["SO5_Haar_moment"] = int(so5_haar[order])
            record["finite_minus_Haar"] = _fraction_pair(mean - so5_haar[order])
        if order == 0:
            record["all_q_formula_checked"] = True
        elif order == 1:
            if mean != exact_characters["mean_s"]:
                raise ArithmeticError("first frozen trace moment formula failed")
            record["all_q_formula_checked"] = True
        elif order == 2:
            if mean != exact_characters["mean_s_squared"]:
                raise ArithmeticError("second frozen trace moment formula failed")
            record["all_q_formula_checked"] = True
        trace_moments.append(record)

    trace_atoms = [
        {
            "trace_numerator_b_minus_q": numerator,
            "normalized_trace_s": _fraction_pair(Fraction(numerator, q)),
            "member_count": count,
            "member_fraction": _fraction_pair(Fraction(count, total_members)),
        }
        for numerator, count in sorted(trace_histogram.items())
    ]

    return {
        "q": q,
        "source_joint_atom_count": len(source_atoms),
        "member_count": total_members,
        "complete_primitive_coefficient_law": {
            "parameterization": (
                "s=(b-q)/q=chi_(0,1), k=(a^2-b)/q=chi_(2,0); "
                "the primitive polynomial is 1-s*z+k*z^2-k*z^3+s*z^4-z^5"
            ),
            "support_size_after_a_sign_compression": len(coefficient_atoms),
            "atoms": coefficient_atoms,
        },
        "normalized_trace_law": {
            "support_size": len(trace_atoms),
            "atoms": trace_atoms,
            "moments_0_through_8": trace_moments,
        },
        "all_q_character_moment_regression": {
            name: _fraction_pair(value)
            for name, value in frozen_character_sums.items()
        },
        "twist_kernel_check": {
            "signed_histogram_invariant_under_a_to_minus_a": True,
            "primitive_polynomial_depends_only_on_a_squared_and_b": True,
            "members_on_a_equals_zero_fixed_locus": zero_a_members,
            "source_signed_support_size": len(signed_histogram),
            "twist_quotient_support_size": len(coefficient_atoms),
        },
        "newton_and_division_witnesses": witnesses,
    }


def build_fixture(q_values: Sequence[int] = FROZEN_Q_VALUES) -> dict[str, object]:
    if tuple(q_values) != FROZEN_Q_VALUES:
        raise ValueError(f"fixture requires exactly q={FROZEN_Q_VALUES}")
    balanced = _load_locked_fixture(
        BALANCED_FIXTURE_PATH, EXPECTED_BALANCED_PAYLOAD_SHA256
    )
    genus2 = _load_locked_fixture(
        GENUS2_FORMULA_FIXTURE_PATH, EXPECTED_GENUS2_FORMULA_PAYLOAD_SHA256
    )
    source_families = _validate_locked_theorems(balanced, genus2)

    guard = ResourceGuard()
    so5_haar = so5_standard_haar_trace_moments(MAX_SO5_HAAR_ORDER, guard)
    if so5_haar != [1, 0, 1, 0, 3, 1, 15]:
        raise ArithmeticError("SO(5) Weyl baseline drifted")
    frozen = [
        analyze_frozen_family(row, guard, so5_haar) for row in source_families
    ]

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.genus2_primitive_exterior_square.v1",
        "raw_fixture_id": "genus2-primitive-exterior-square-q3-q5-q7-v1",
        "status": "EXACT_ALL_Q_ALGEBRA_LOW_MOMENTS_AND_FROZEN_HISTOGRAM_TRANSFORM",
        "rigor_level": {
            "polynomial_identities": "PROVED_POINTWISE_BY_TWO_EXACT_DERIVATIONS",
            "all_q_moments": "PROVED_FOR_EVERY_ODD_PRIME_POWER_FROM_LOCKED_INPUT_THEOREM",
            "SO5_Haar_baseline": "EXACT_B2_WEYL_CONSTANT_TERM",
            "finite_laws": "EXACT_ONLY_FOR_Q_3_5_7_FROM_COMPLETE_LOCKED_HISTOGRAMS",
            "monodromy_and_global_analytic_claims": "NOT_ASSERTED",
        },
        "geometric_representation": {
            "input": "H^1(C), dimension 4, symplectic similitude of weight one",
            "decomposition": "exterior^2 H^1(C) = Q_l(-1) direct_sum W",
            "canonical_ambient_Tate_lines_removed": 1,
            "primitive_W_dimension": 5,
            "primitive_weight": 2,
            "normalized_compact_representation": (
                "USp(4)/{+I,-I} isomorphic to SO(5), with W the standard 5-dimensional representation"
            ),
            "center_kernel": "-I acts trivially on exterior^2, explaining a -> -a blindness",
            "dynkin_label_convention": (
                "character labels use C2 conventions: C2 (0,1) corresponds to "
                "B2 (1,0), the 5-dimensional standard representation, while "
                "C2 (2,0) corresponds to B2 (0,2), the 10-dimensional adjoint"
            ),
            "monodromy_firewall": (
                "this identifies the ambient Sp4/SO5 representation; it does not prove "
                "that the actual quintic-family local system has full SO(5) geometric "
                "or arithmetic monodromy or no additional invariant subsystem"
            ),
        },
        "polynomial_theorem": {
            "input": "P_C(T)=1+a*T+b*T^2+q*a*T^3+q^2*T^4",
            "full_exterior_square_degree_6": (
                "1-b*T+q*(a^2-q)*T^2-2*q^2*(a^2-b)*T^3+q^3*(a^2-q)*T^4-q^4*b*T^5+q^6*T^6"
            ),
            "canonical_polarization_Tate_factor": "1-q*T",
            "primitive_degree_5": (
                "R(T)=1+(q-b)*T+q*(a^2-b)*T^2-q^2*(a^2-b)*T^3+q^3*(b-q)*T^4-q^5*T^5"
            ),
            "independent_derivations": [
                "closed elementary-symmetric coefficient calculation",
                "Newton recurrence with p_n(exterior^2)=(p_n(H1)^2-p_(2n)(H1))/2, followed by exact Tate division",
            ],
            "normalized_character_form": (
                "R(z/q)=1-s*z+k*z^2-k*z^3+s*z^4-z^5, with s=b/q-1=chi_(0,1) and k=(a^2-b)/q=chi_(2,0)"
            ),
            "coefficient_recovery": (
                "R determines b/q=1+s and a^2/q=1+s+k, but not the sign of a"
            ),
        },
        "pointwise_local_eigenline_without_forced_common_line": {
            "identity": "R(T)=(1-q*T)*Q_local(T) for every input polynomial",
            "quartic": (
                "Q_local(T)=1+(2*q-b)*T+q*(a^2-2*b+2*q)*T^2+q^2*(2*q-b)*T^3+q^4*T^4"
            ),
            "normalized_quartic": (
                "Q_local(z/q)=1+(1-s)*z+(1-s+k)*z^2+(1-s)*z^3+z^4"
            ),
            "group_reason": (
                "every element of odd-dimensional SO(5) has an eigenvalue 1: reciprocal eigenvalue pairs leave one unpaired eigenvalue and determinant one forces it to be 1"
            ),
            "torus_cross_eigenvalues": (
                "if normalized H1 has eigenvalues x,x^-1,y,y^-1, then Q_local has roots x*y,x/y,y/x,(x*y)^-1"
            ),
            "noncanonical_tensor_warning": (
                "the four cross roots resemble a 2-by-2 tensor product only after choosing and ordering two torus eigenvalue pairs; they do not define two global rank-two factors"
            ),
            "ambient_representation_level": (
                "Lambda^2(Std_Sp4)=1 direct_sum W, and W is irreducible as the "
                "ambient 5-dimensional SO(5) representation, so it has no forced "
                "SO(5)-common invariant vector"
            ),
            "actual_family_level": (
                "the family monodromy group is not determined here; it could be a "
                "proper subgroup, and special or endoscopic loci can acquire extra "
                "invariant subsystems"
            ),
            "individual_finite_field_fiber_level": (
                "Gal(F_qbar/F_q) is procyclic, so the q-eigenspace is an actual "
                "Frobenius-stable Q_l(-1) line on each fiber; it is canonical when "
                "the q eigenvalue has multiplicity one"
            ),
            "endoscopic_specialization": (
                "if H1=V1 direct_sum V2, then exterior^2 H1 contains the two Tate "
                "lines exterior^2 V1 and exterior^2 V2; after removing the diagonal "
                "polarization line, the primitive factor retains the anti-diagonal line"
            ),
            "why_not_a_forced_common_Tate_subrepresentation": (
                "the fixed axis varies with the SO(5) element, so ambient representation "
                "theory supplies no second common line; this does not rule out a line "
                "for a smaller actual family monodromy group"
            ),
            "formal_Euler_product_warning": (
                "the quotient is genuine for each procyclic finite-field fiber, but "
                "assembling the varying quartics across a family or across primes into "
                "a compatible representation, motive, or automorphic system remains "
                "formal; bad factors and analytic continuation are not analyzed"
            ),
        },
        "all_q_primitive_character_moments": {
            "scope": "every odd prime power q",
            "measure": "uniform monic squarefree quintic models",
            "characters": {
                "s": "Tr(W)/q=b/q-1=chi_(0,1), the SO(5) standard character",
                "k": "e2(W)/q^2=(a^2-b)/q=chi_(2,0), the exterior^2/adjoint character",
            },
            "formulas": _formula_strings(),
            "derivation": (
                "substitution into the five locked exact means of a^2,a^4,a^2*b,b,b^2; frozen fields are regression checks, not interpolation inputs"
            ),
            "SO5_Haar_Gram_target": {
                "mean_s": 0,
                "mean_s_squared": 1,
                "mean_k": 0,
                "mean_k_squared": 1,
                "mean_s_times_k": 0,
                "reason": "s and k are distinct nontrivial irreducible characters",
            },
        },
        "compact_SO5_baseline": {
            "orders_0_through_6": list(range(MAX_SO5_HAAR_ORDER + 1)),
            "standard_trace_moments": so5_haar,
            "derivation": (
                "B2 Weyl constant term for character 1+x+x^-1+y+y^-1 and all eight roots, divided by Weyl-group order 8"
            ),
            "orientation_fingerprint": {
                "order": 5,
                "SO5_moment": 1,
                "O5_moment": 0,
                "reason": "the SO(5) volume tensor is the first odd invariant; adjoining a reflection kills odd trace moments",
            },
            "frozen_fifth_moment_sign_reversal": {
                "rows": [
                    {
                        "q": int(row["q"]),
                        "family_mean_s_fifth": row["normalized_trace_law"][
                            "moments_0_through_8"
                        ][5]["family_mean_s_power"],
                        "SO5_Haar_target": 1,
                        "sign": "negative",
                    }
                    for row in frozen
                ],
                "status": (
                    "EXACT_FROZEN_SIGN_REVERSAL_ONLY; no all-q fifth-moment formula, monotonicity, convergence rate, or asymptotic sign is inferred"
                ),
            },
        },
        "literature_boundary": {
            "classical_context": (
                "the degree-five standard GSp(4) local factor and its unit "
                "eigenvalue are classical; this packet does not claim their discovery"
            ),
            "primary_reference": (
                "Daniel File, On the degree five L-function for GSp(4), "
                "arXiv:1201.2783, https://arxiv.org/abs/1201.2783"
            ),
            "project_specific_contribution": (
                "exact pushforward of the locked marked-quintic coefficient laws, "
                "the all-q finite character Gram defects, and the frozen orientation "
                "moment anomaly with reproducible source locks"
            ),
        },
        "frozen_histogram_transforms": frozen,
        "strange_next_targets": [
            {
                "name": "unisingular_local_global_gap",
                "known": (
                    "every primitive local polynomial has a q-eigenvalue, while the "
                    "ambient irreducible SO(5) representation forces no second common "
                    "line; special/endoscopic family loci may nevertheless have one"
                ),
                "open": (
                    "determine when the formal quartic Euler product has an independent automorphic or motivic realization and how any compensating zero/pole appears globally"
                ),
            },
            {
                "name": "orientation_moment",
                "known": "the compact SO(5) fifth trace moment is 1, unlike O(5)",
                "open": (
                    "obtain an all-q evaluation or power-saving estimate for mean((b/q-1)^5) and isolate its epsilon-tensor contribution"
                ),
            },
            {
                "name": "finite_character_Gram_matrix",
                "known": (
                    "the exact means of s,s^2,k,k^2,s*k quantify failure of finite-family character orthogonality through order two"
                ),
                "open": (
                    "diagonalize higher character Gram blocks and identify which corrections are boundary, endoscopic, or automorphic"
                ),
            },
            {
                "name": "twist_quotient_family",
                "known": "the primitive factor records exactly a^2 and b, losing only the signed a coordinate",
                "open": (
                    "compare its natural stack measure with uniform coarse twist-orbits without substituting one for the other"
                ),
            },
        ],
        "producer_and_source_locks": {
            "input_method": "complete JSON (a,b) histogram pushforward only",
            "no_field_or_curve_enumeration": True,
            "locks": _source_locks(),
        },
        "resource_contract": {
            "exclusive_accounted_work_unit_cap": ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE,
            "accounted_work_unit_ledger": guard.snapshot(),
            "unit_definition": (
                "declared high-level histogram visits, formula terms, Newton comparisons, "
                "division checks, and Laurent-term products; not literal arithmetic "
                "instructions or a wall-clock complexity bound"
            ),
            "field_or_curve_enumerations": 0,
            "random_samples": 0,
            "floating_point_results": 0,
            "maximum_polynomial_degree": 6,
            "maximum_frozen_moment_order": MAX_FROZEN_MOMENT_ORDER,
        },
        "scope_firewall": {
            "no_forced_second_common_Tate_line": (
                "ambient SO(5) representation theory forces only the canonical "
                "polarization line; every individual finite-field fiber has a genuine "
                "q-eigenline, while the actual family monodromy and its possible extra "
                "sub-local-systems remain undetermined"
            ),
            "no_full_monodromy_claim": (
                "the representation factors through SO(5), but this packet does not prove Zariski-dense family monodromy"
            ),
            "no_frozen_to_asymptotic_inference": (
                "q=3,5,7 laws are complete finite facts and are not fitted to a convergence rate or new all-q formula"
            ),
            "no_measure_substitution": (
                "uniform marked quintic/model-stack weights are not relabeled as uniform coarse curve or twist-orbit weights"
            ),
            "no_analytic_or_RH_claim": (
                "local polynomial identities and compact Haar comparisons imply no analytic continuation, functional equation, zero-free region, RH, or GRH result"
            ),
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    output = parser.add_mutually_exclusive_group()
    output.add_argument(
        "--write", nargs="?", const=OUTPUT_PATH, type=Path, default=None
    )
    output.add_argument(
        "--check", nargs="?", const=OUTPUT_PATH, type=Path, default=None
    )
    args = parser.parse_args()
    fixture = build_fixture()
    encoded = json.dumps(fixture, indent=2, sort_keys=True) + "\n"
    if args.write is not None:
        args.write.write_text(encoded, encoding="utf-8")
        print(f"wrote {args.write}")
    elif args.check is not None:
        if args.check.read_text(encoding="utf-8") != encoded:
            raise SystemExit(f"stale fixture: {args.check}")
        print(f"fixture current: {args.check}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
