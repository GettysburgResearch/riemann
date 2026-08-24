#!/usr/bin/env python3
"""Exact packet for the primitive weight-two factor of E x C.

The inputs are *only* the stored genus-one cubic and genus-two quintic
family fixtures.  No finite field is constructed and no curve is
enumerated here.  For

    P_E(T) = 1 + A*T + q*T^2,
    P_C(T) = 1 + a*T + b*T^2 + q*a*T^3 + q^2*T^4,

the packet studies the degree-eight polynomial on H^1(E) tensor H^1(C).
It proves the coefficient formulas by Newton recurrence, records the exact
rank-three coefficient hypersurface, evaluates the all-q trace moments
through degree four, and convolves the source-locked q=3,5,7 histograms.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "product_variety_tensor_family.json"
NOTE_PATH = HERE / "PRODUCT_VARIETY_TENSOR_FAMILY.md"
TEST_PATH = ROOT / "tests" / "test_product_variety_tensor_family.py"

GENUS1_FIXTURE_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_SOURCE_PATH = HERE / "genus1_cubic_family_laws.py"
BALANCED_FIXTURE_PATH = HERE / "balanced_control_family_scan.json"
BALANCED_SOURCE_PATH = HERE / "balanced_control_family_scan.py"
GENUS2_FIXTURE_PATH = HERE / "genus2_q_scan.json"
GENUS2_SOURCE_PATH = HERE / "genus2_q_scan.py"
MEASURE_FIXTURE_PATH = HERE / "genus2_family_measures.json"
MEASURE_SOURCE_PATH = HERE / "genus2_family_measures.py"

FROZEN_Q_VALUES = (3, 5, 7)
MAX_EXACT_OPERATIONS = 20_000
MAX_HAAR_ORDER = 8


@dataclass
class ResourceGuard:
    """Fail closed before the packet becomes a large computation."""

    atom_pair_operations: int = 0
    partition_transition_operations: int = 0

    def charge_atoms(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("resource charge must be nonnegative")
        self.atom_pair_operations += amount
        self._check()

    def charge_partitions(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("resource charge must be nonnegative")
        self.partition_transition_operations += amount
        self._check()

    def _check(self) -> None:
        if self.total > MAX_EXACT_OPERATIONS:
            raise RuntimeError(
                f"exact operation cap exceeded: {self.total}>{MAX_EXACT_OPERATIONS}"
            )

    @property
    def total(self) -> int:
        return self.atom_pair_operations + self.partition_transition_operations

    def snapshot(self) -> dict[str, int]:
        return {
            "atom_pair_operations": self.atom_pair_operations,
            "partition_transition_operations": self.partition_transition_operations,
            "total_exact_operations": self.total,
        }


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _fraction(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _load_locked_fixture(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    claimed = payload.get("payload_sha256")
    if not isinstance(claimed, str):
        raise ValueError(f"{path.name} has no payload_sha256")
    unhashed = dict(payload)
    unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != claimed:
        raise ValueError(f"{path.name} payload hash is stale")
    return payload


def _validate_locked_input_theorems(
    genus1: Mapping[str, object], genus2: Mapping[str, object]
) -> None:
    """Refuse to silently outlive the precise formulas used below."""

    genus1_normalization = genus1["normalization"]  # type: ignore[assignment]
    if genus1_normalization["trace"] != (
        "a_D=q+1-#E_D(F_q)=-sum_x quadratic_character(D(x))"
    ):
        raise ValueError("genus-one trace convention drifted")
    if genus1_normalization["l_polynomial"] != "L_D(T)=1-a_D*T+q*T^2":
        raise ValueError("genus-one L-polynomial sign convention drifted")

    genus1_theorem = genus1["all_q_moment_theorem"]  # type: ignore[assignment]
    if genus1_theorem["scope"] != "every odd prime power q and every integer n>=0":
        raise ValueError("genus-one all-q scope drifted")
    if genus1_theorem["odd_trace_and_character_moments"] != 0:
        raise ValueError("genus-one odd-moment theorem drifted")
    expected_stack_sums = {
        "W_2": "q^2-1",
        "W_4": "2*q^3-3*q-1",
    }
    for key, value in expected_stack_sums.items():
        if genus1_theorem["explicit_stack_sums"][key] != value:
            raise ValueError(f"genus-one {key} formula drifted")
    if genus1_theorem["model_average"] != "E_model[a_D^(2n)]=W_(2n)/q":
        raise ValueError("genus-one model normalization drifted")

    genus2_theorem = genus2["closed_formula_target"]  # type: ignore[assignment]
    expected_genus2 = {
        "mean_a_squared": "q-1+(q^2+q-2)/q^3",
        "mean_a_fourth": "3*q^2-7*q+5+12/q-14/q^2-11/q^3",
        "mean_a_squared_b": "(q+1)*(q^2-2*q+3)*(2*q^2-2*q-1)/q^3",
        "mean_b": "q-1+(q^2-1)/q^3",
        "mean_b_squared": "2*q^2-3*q+2+(q^2-3*q-1)/q^3",
    }
    if genus2_theorem["scope"] != "every odd prime power q":
        raise ValueError("genus-two all-q scope drifted")
    for key, value in expected_genus2.items():
        if genus2_theorem[key] != value:
            raise ValueError(f"genus-two {key} formula drifted")


def _prime_power_data(q: int) -> tuple[int, int]:
    if q < 3 or q % 2 == 0:
        raise ValueError("q must be an odd prime power")
    for candidate in range(2, math.isqrt(q) + 1):
        if q % candidate:
            continue
        if any(candidate % divisor == 0 for divisor in range(2, math.isqrt(candidate) + 1)):
            continue
        residue = q
        exponent = 0
        while residue % candidate == 0:
            residue //= candidate
            exponent += 1
        if residue != 1:
            raise ValueError("q must be a prime power")
        if candidate == 2:
            raise ValueError("q must be odd")
        return candidate, exponent
    return q, 1


def power_sums_from_characteristic_polynomial(
    coefficients: Sequence[int], maximum_degree: int
) -> list[int]:
    """Newton power sums for x^d+c1*x^(d-1)+...+cd."""

    if not coefficients or coefficients[0] != 1:
        raise ValueError("characteristic polynomial must be monic")
    if maximum_degree < 0:
        raise ValueError("maximum degree must be nonnegative")
    degree = len(coefficients) - 1
    if degree < 1:
        raise ValueError("positive polynomial degree required")
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
    """Return coefficients of product(1-root*T) from p_1,...,p_n."""

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


def tensor_coefficients_via_newton(
    a_e: int, a_c: int, b_c: int, q: int
) -> tuple[int, ...]:
    """Independent recurrence construction; a_e is A=-trace(E)."""

    _prime_power_data(q)
    elliptic = power_sums_from_characteristic_polynomial((1, a_e, q), 8)
    genus_two = power_sums_from_characteristic_polynomial(
        (1, a_c, b_c, q * a_c, q * q), 8
    )
    tensor_sums = [8] + [elliptic[index] * genus_two[index] for index in range(1, 9)]
    return coefficients_from_power_sums(tensor_sums)


def tensor_coefficients(
    a_e: int, a_c: int, b_c: int, q: int
) -> tuple[int, ...]:
    """Closed coefficient formula for H^1(E) tensor H^1(C), with A=-trace(E)."""

    _prime_power_data(q)
    c1 = -a_e * a_c
    c2 = a_e * a_e * b_c + q * a_c * a_c - 2 * q * b_c
    c3 = a_e * a_c * q * (-a_e * a_e - b_c + 3 * q)
    c4 = q * q * (
        a_e**4
        + a_e * a_e * a_c * a_c
        - 4 * q * a_e * a_e
        - 2 * q * a_c * a_c
        + b_c * b_c
        + 2 * q * q
    )
    return (1, c1, c2, c3, c4, q**2 * c3, q**4 * c2, q**6 * c1, q**8)


def tensor_hypersurface_residual(coefficients: Sequence[int], q: int) -> int:
    """Integral form of the rank-three coefficient hypersurface."""

    if len(coefficients) != 9 or coefficients[0] != 1:
        raise ValueError("a degree-eight tensor polynomial is required")
    c1, c2, c3, c4 = coefficients[1:5]
    return (
        c1 * c1 * c4
        - q * q * c1**4
        + 2 * q * q * c1 * c1 * c2
        + q**4 * c1 * c1
        - 2 * q * q * c1 * c3
        - c3 * c3
    )


def genus1_normalized_trace_moment(order: int, q: int) -> Fraction:
    _prime_power_data(q)
    if order < 0 or order > 4:
        raise ValueError("locked all-q genus-one evaluator supports orders 0..4")
    if order == 0:
        return Fraction(1)
    if order % 2:
        return Fraction(0)
    if order == 2:
        return Fraction(q * q - 1, q * q)
    return Fraction(2 * q**3 - 3 * q - 1, q**3)


def genus2_normalized_trace_moment(order: int, q: int) -> Fraction:
    _prime_power_data(q)
    if order < 0 or order > 4:
        raise ValueError("locked all-q genus-two evaluator supports orders 0..4")
    if order == 0:
        return Fraction(1)
    if order % 2:
        return Fraction(0)
    if order == 2:
        return Fraction(q - 1, q) + Fraction(q * q + q - 2, q**4)
    return (
        Fraction(3 * q * q - 7 * q + 5, q * q)
        + Fraction(12, q**3)
        - Fraction(14, q**4)
        - Fraction(11, q**5)
    )


def tensor_normalized_trace_moment(order: int, q: int) -> Fraction:
    """Exact product-model moment of Tr(A tensor B)/q, through order four."""

    return genus1_normalized_trace_moment(order, q) * genus2_normalized_trace_moment(order, q)


def _genus2_normalized_inputs(q: int) -> dict[str, Fraction]:
    """All-q normalized input moments locked by genus2_q_scan.json."""

    a2 = Fraction(q - 1, q) + Fraction(q * q + q - 2, q**4)
    a4 = genus2_normalized_trace_moment(4, q)
    b = Fraction(q - 1, q) + Fraction(q * q - 1, q**4)
    b2 = Fraction(2 * q * q - 3 * q + 2, q * q) + Fraction(q * q - 3 * q - 1, q**5)
    a2b = Fraction(
        (q + 1) * (q * q - 2 * q + 3) * (2 * q * q - 2 * q - 1),
        q**5,
    )
    return {"a2": a2, "a4": a4, "b": b, "b2": b2, "a2b": a2b}


def all_q_coefficient_fingerprint_means(q: int) -> dict[str, Fraction]:
    """Means of v=c2/q^2, h=c4/q^4, and u*w=c1*c3/q^4."""

    _prime_power_data(q)
    elliptic_a2 = genus1_normalized_trace_moment(2, q)
    elliptic_a4 = genus1_normalized_trace_moment(4, q)
    genus_two = _genus2_normalized_inputs(q)
    mean_v = elliptic_a2 * genus_two["b"] + genus_two["a2"] - 2 * genus_two["b"]
    mean_h = (
        elliptic_a4
        + elliptic_a2 * genus_two["a2"]
        - 4 * elliptic_a2
        - 2 * genus_two["a2"]
        + genus_two["b2"]
        + 2
    )
    mean_uw = (
        elliptic_a4 * genus_two["a2"]
        + elliptic_a2 * genus_two["a2b"]
        - 3 * elliptic_a2 * genus_two["a2"]
    )
    return {"mean_v": mean_v, "mean_h": mean_h, "mean_u_times_w": mean_uw}


def _partition_neighbors(partition: tuple[int, ...], rank: int) -> set[tuple[int, ...]]:
    neighbors: set[tuple[int, ...]] = set()
    padded = list(partition) + [0] * (rank - len(partition))
    for index in range(rank):
        if index == 0 or padded[index] < padded[index - 1]:
            added = list(padded)
            added[index] += 1
            while added and added[-1] == 0:
                added.pop()
            neighbors.add(tuple(added))
        if padded[index] and (index == rank - 1 or padded[index] > padded[index + 1]):
            removed = list(padded)
            removed[index] -= 1
            while removed and removed[-1] == 0:
                removed.pop()
            neighbors.add(tuple(removed))
    return neighbors


def symplectic_standard_haar_moment(
    rank: int, order: int, guard: ResourceGuard | None = None
) -> int:
    """Invariant paths for the standard representation of USp(2*rank)."""

    if rank < 1 or not 0 <= order <= MAX_HAAR_ORDER:
        raise ValueError("rank must be positive and order must lie in 0..8")
    paths: Counter[tuple[int, ...]] = Counter({(): 1})
    for _ in range(order):
        following: Counter[tuple[int, ...]] = Counter()
        for partition, multiplicity in paths.items():
            neighbors = _partition_neighbors(partition, rank)
            if guard is not None:
                guard.charge_partitions(len(neighbors))
            for neighbor in neighbors:
                following[neighbor] += multiplicity
        paths = following
    return paths.get((), 0)


def product_haar_trace_moment(order: int, guard: ResourceGuard | None = None) -> int:
    return symplectic_standard_haar_moment(1, order, guard) * symplectic_standard_haar_moment(2, order, guard)


def so8_standard_trace_haar_moment(order: int) -> int:
    """Stable Brauer-pairing moments below the degree-eight volume tensor."""

    if not 0 <= order <= 6:
        raise ValueError("SO(8) comparator is deliberately restricted to orders 0..6")
    if order % 2:
        return 0
    if order == 0:
        return 1
    return math.prod(range(1, order, 2))


def _coarse_stack_tv(
    stabilizer_histogram: Mapping[str, int], orbit_count: int, stack_mass: int
) -> Fraction:
    """TV between uniform coarse orbits and stabilizer-weighted stack orbits."""

    total = Fraction(0)
    for stabilizer, count in stabilizer_histogram.items():
        total += int(count) * abs(Fraction(1, orbit_count) - Fraction(1, stack_mass * int(stabilizer)))
    return total / 2


def _field_rows_by_q(rows: Iterable[Mapping[str, object]]) -> dict[int, Mapping[str, object]]:
    output = {int(row["q"]): row for row in rows}
    if set(output) < set(FROZEN_Q_VALUES):
        raise ValueError("a locked input is missing q=3,5,7")
    return output


def _fraction_mean(total: int, count: int, denominator: int = 1) -> Fraction:
    return Fraction(total, count * denominator)


def analyze_frozen_field(
    q: int,
    genus1_row: Mapping[str, object],
    genus2_row: Mapping[str, object],
    measure_row: Mapping[str, object],
    guard: ResourceGuard,
) -> dict[str, object]:
    if q not in FROZEN_Q_VALUES:
        raise ValueError(f"frozen convolution supports only {FROZEN_Q_VALUES}")
    elliptic_trace_histogram = {
        int(trace): int(count)
        for trace, count in genus1_row["model_trace_histogram"].items()  # type: ignore[union-attr]
    }
    # The genus-one fixture keys are geometric traces t_E in
    # 1-t_E*T+q*T^2.  This packet writes 1+A*T+q*T^2, so A=-t_E.
    elliptic_coefficient_histogram = {
        -trace: count for trace, count in elliptic_trace_histogram.items()
    }
    genus2_atoms = genus2_row["joint_a_D_b_D_law"]["atoms"]  # type: ignore[index]
    coefficient_histogram: Counter[tuple[int, int, int, int]] = Counter()
    trace_histogram: Counter[int] = Counter()
    middle_histogram: Counter[int] = Counter()
    total_pairs = 0
    recurrence_witnesses: list[dict[str, object]] = []

    for a_e, elliptic_count in sorted(elliptic_coefficient_histogram.items()):
        for genus2_atom in genus2_atoms:  # type: ignore[assignment]
            guard.charge_atoms()
            a_c = int(genus2_atom["a_D"])
            b_c = int(genus2_atom["b_D"])
            weight = elliptic_count * int(genus2_atom["member_count"])
            coefficients = tensor_coefficients(a_e, a_c, b_c, q)
            if tensor_hypersurface_residual(coefficients, q):
                raise ArithmeticError("tensor coefficient hypersurface failed")
            key = tuple(coefficients[1:5])
            coefficient_histogram[key] += weight
            trace_histogram[a_e * a_c] += weight
            middle_histogram[coefficients[4]] += weight
            total_pairs += weight

    expected_pairs = int(genus1_row["squarefree_model_count"]) * int(genus2_row["member_count"])
    if total_pairs != expected_pairs:
        raise ArithmeticError("histogram convolution lost product pairs")

    # Three independent Newton witnesses are enough to source-lock the closed
    # formula without spending recurrence work on every compressed atom.
    elliptic_trace_support = sorted(elliptic_trace_histogram)
    for trace_e, genus2_atom in zip(
        (elliptic_trace_support[0], 0, elliptic_trace_support[-1]),
        (genus2_atoms[0], genus2_atoms[len(genus2_atoms) // 2], genus2_atoms[-1]),
    ):
        a_e = -trace_e
        a_c = int(genus2_atom["a_D"])
        b_c = int(genus2_atom["b_D"])
        closed = tensor_coefficients(a_e, a_c, b_c, q)
        recurrence = tensor_coefficients_via_newton(a_e, a_c, b_c, q)
        if closed != recurrence:
            raise ArithmeticError("closed tensor coefficients disagree with Newton recurrence")
        recurrence_witnesses.append(
            {
                "source_trace_t_E": trace_e,
                "converted_A_E": a_e,
                "input_A_E_a_C_b_C": [a_e, a_c, b_c],
                "coefficients_c0_through_c8": list(closed),
            }
        )

    coefficient_atoms = []
    sum_v = Fraction(0)
    sum_h = Fraction(0)
    sum_uw = Fraction(0)
    sum_centered_h_squared = Fraction(0)
    sum_centered_uw_squared = Fraction(0)
    for (c1, c2, c3, c4), count in sorted(coefficient_histogram.items()):
        normalized = (
            Fraction(c1, q),
            Fraction(c2, q**2),
            Fraction(c3, q**3),
            Fraction(c4, q**4),
        )
        probability = Fraction(count, total_pairs)
        sum_v += probability * normalized[1]
        sum_h += probability * normalized[3]
        sum_uw += probability * normalized[0] * normalized[2]
        sum_centered_h_squared += probability * (normalized[3] - 1) ** 2
        sum_centered_uw_squared += probability * (normalized[0] * normalized[2] - 1) ** 2
        coefficient_atoms.append(
            {
                "coefficient_numerators_c1_to_c4": [c1, c2, c3, c4],
                "normalized_u_v_w_h": [_fraction(value) for value in normalized],
                "pair_count": count,
                "pair_fraction": _fraction(probability),
            }
        )

    exact_means = all_q_coefficient_fingerprint_means(q)
    if (sum_v, sum_h, sum_uw) != (
        exact_means["mean_v"],
        exact_means["mean_h"],
        exact_means["mean_u_times_w"],
    ):
        raise ArithmeticError("frozen coefficient means disagree with all-q formulas")

    trace_moments = []
    for order in range(9):
        numerator_sum = sum(count * numerator**order for numerator, count in trace_histogram.items())
        mean = _fraction_mean(numerator_sum, total_pairs, q**order)
        record: dict[str, object] = {
            "order": order,
            "sum_trace_numerator_to_order": numerator_sum,
            "family_mean_normalized_trace_to_order": _fraction(mean),
        }
        if order <= 4:
            theorem = tensor_normalized_trace_moment(order, q)
            if mean != theorem:
                raise ArithmeticError("frozen trace moment disagrees with all-q theorem")
            record["all_q_formula_checked"] = True
        if order <= 6:
            record["product_haar_moment"] = product_haar_trace_moment(order)
            record["so8_haar_moment"] = so8_standard_trace_haar_moment(order)
        trace_moments.append(record)

    genus1_full_affine = genus1_row["full_affine_branch_orbits"]  # type: ignore[assignment]
    genus1_branch_tv = _coarse_stack_tv(
        genus1_full_affine["stabilizer_order_histogram"],
        int(genus1_full_affine["orbit_count"]),
        q,
    )
    genus1_elliptic = genus1_row["elliptic_square_affine_orbits"]  # type: ignore[assignment]
    genus1_elliptic_tv = _coarse_stack_tv(
        genus1_elliptic["stabilizer_order_histogram"],
        int(genus1_elliptic["orbit_count"]),
        2 * q,
    )
    genus2_tv = Fraction(*measure_row["total_variation_uniform_orbits_vs_model_affine_stack"])  # type: ignore[arg-type]
    even_product_bound = genus1_branch_tv + genus2_tv - genus1_branch_tv * genus2_tv

    trace_atoms = [
        {
            "trace_numerator_a_E_times_a_C": numerator,
            "normalized_trace": _fraction(Fraction(numerator, q)),
            "pair_count": count,
            "pair_fraction": _fraction(Fraction(count, total_pairs)),
        }
        for numerator, count in sorted(trace_histogram.items())
    ]
    middle_atoms = [
        {
            "c4": c4,
            "normalized_h": _fraction(Fraction(c4, q**4)),
            "pair_count": count,
            "pair_fraction": _fraction(Fraction(count, total_pairs)),
        }
        for c4, count in sorted(middle_histogram.items())
    ]

    return {
        "q": q,
        "source_histogram_sizes": {
            "elliptic_trace_atoms": len(elliptic_coefficient_histogram),
            "genus2_joint_a_b_atoms": len(genus2_atoms),
            "cartesian_atom_pairs": len(elliptic_coefficient_histogram) * len(genus2_atoms),
        },
        "product_model_pair_count": total_pairs,
        "complete_tensor_coefficient_law": {
            "normalization": "u=c1/q, v=c2/q^2, w=c3/q^3, h=c4/q^4",
            "atom_count_after_exact_compression": len(coefficient_atoms),
            "atoms": coefficient_atoms,
        },
        "normalized_trace_law": {
            "support_size": len(trace_atoms),
            "atoms": trace_atoms,
            "moments_0_through_8": trace_moments,
        },
        "normalized_middle_coefficient_law": {
            "support_size": len(middle_atoms),
            "atoms": middle_atoms,
        },
        "coefficient_fingerprint_means": {
            "mean_v": _fraction(sum_v),
            "mean_h": _fraction(sum_h),
            "mean_u_times_w": _fraction(sum_uw),
            "mean_(h-1)^2_frozen_target": _fraction(sum_centered_h_squared),
            "mean_(u*w-1)^2_frozen_target": _fraction(sum_centered_uw_squared),
        },
        "newton_recurrence_witnesses": recurrence_witnesses,
        "measure_separation": {
            "model_law_used_here": "uniform independent marked equations; equivalently the product stabilizer-weighted stack law",
            "genus1_full_affine_branch_orbit_count": int(genus1_full_affine["orbit_count"]),
            "genus1_elliptic_isomorphism_class_count": int(genus1_elliptic["orbit_count"]),
            "genus2_full_affine_branch_orbit_count": int(measure_row["orbit_count"]),
            "genus1_model_vs_uniform_branch_coarse_tv": _fraction(genus1_branch_tv),
            "genus1_model_vs_uniform_elliptic_coarse_tv": _fraction(genus1_elliptic_tv),
            "genus2_model_vs_uniform_branch_coarse_tv": _fraction(genus2_tv),
            "even_coefficient_product_coarse_tv_upper_bound": _fraction(even_product_bound),
            "full_signed_tensor_polynomial_descends_to_independent_branch_orbits": False,
            "reason": "a nonsquare affine multiplier twists one H^1 factor and flips c1,c3; only c2,c4 descend after the two twist signs are forgotten independently",
            "simultaneous_quadratic_twist_leaves_tensor_polynomial_fixed": True,
            "coarse_signed_law_not_reconstructed": "the locked genus-two packet has no square-affine joint (a_C,b_C) orbit histogram, so this packet refuses to relabel model weights as uniform coarse weights",
        },
    }


def _source_locks(fixtures: Mapping[str, Mapping[str, object]]) -> dict[str, object]:
    paths = {
        "genus1_fixture": GENUS1_FIXTURE_PATH,
        "genus1_source": GENUS1_SOURCE_PATH,
        "balanced_fixture": BALANCED_FIXTURE_PATH,
        "balanced_source": BALANCED_SOURCE_PATH,
        "genus2_formula_fixture": GENUS2_FIXTURE_PATH,
        "genus2_formula_source": GENUS2_SOURCE_PATH,
        "genus2_measure_fixture": MEASURE_FIXTURE_PATH,
        "genus2_measure_source": MEASURE_SOURCE_PATH,
        "producer": Path(__file__).resolve(),
        "note": NOTE_PATH,
        "test": TEST_PATH,
    }
    locks = {
        name: {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256_lf_normalized": _lf_sha256(path),
        }
        for name, path in paths.items()
    }
    for name, fixture in fixtures.items():
        locks[name]["payload_sha256"] = fixture["payload_sha256"]  # type: ignore[index]
    return locks


def build_fixture(q_values: Sequence[int] = FROZEN_Q_VALUES) -> dict[str, object]:
    if tuple(q_values) != FROZEN_Q_VALUES:
        raise ValueError(f"fixture requires exactly q={FROZEN_Q_VALUES}")
    genus1 = _load_locked_fixture(GENUS1_FIXTURE_PATH)
    balanced = _load_locked_fixture(BALANCED_FIXTURE_PATH)
    genus2 = _load_locked_fixture(GENUS2_FIXTURE_PATH)
    measures = _load_locked_fixture(MEASURE_FIXTURE_PATH)
    _validate_locked_input_theorems(genus1, genus2)

    genus1_by_q = _field_rows_by_q(genus1["finite_regressions"])  # type: ignore[arg-type]
    balanced_by_q = _field_rows_by_q(balanced["frozen_enumeration_facts"]["families"])  # type: ignore[index]
    measure_by_q = _field_rows_by_q(measures["families"])  # type: ignore[arg-type]
    guard = ResourceGuard()
    families = [
        analyze_frozen_field(
            q,
            genus1_by_q[q],
            balanced_by_q[q],
            measure_by_q[q],
            guard,
        )
        for q in q_values
    ]

    product_haar = [product_haar_trace_moment(order, guard) for order in range(7)]
    so8_haar = [so8_standard_trace_haar_moment(order) for order in range(7)]
    if product_haar[:4] != so8_haar[:4] or product_haar[4] != 6 or so8_haar[4] != 3:
        raise ArithmeticError("compact-group fingerprint drifted")

    fixture: dict[str, object] = {
        "schema": "riemann.product-variety-tensor-family.v1",
        "raw_fixture_id": "product-variety-tensor-family-q3-q5-q7-v1",
        "status": "EXACT_ALGEBRA_ALL_Q_LOW_MOMENTS_AND_FROZEN_HISTOGRAM_CONVOLUTION",
        "rigor_level": {
            "tensor_polynomial_and_hypersurface": "PROVED_POINTWISE",
            "all_q_family_moments": "PROVED_FOR_EVERY_ODD_PRIME_POWER_FROM_LOCKED_INPUT_THEOREMS",
            "compact_group_baselines": "EXACT_REPRESENTATION_THEORY",
            "finite_laws": "EXACT_ONLY_FOR_Q_3_5_7_FROM_LOCKED_HISTOGRAMS",
            "higher_targets": "CONJECTURE_OR_OPEN_EVALUATION_ONLY",
        },
        "geometric_construction": {
            "variety": "E x C with E genus one and C genus two over the same F_q",
            "primitive_weight_two_factor": "H^1(E) tensor H^1(C)",
            "dimension": 8,
            "full_H2_local_factor": "(1-q*T)^2 times the recorded degree-eight tensor factor",
            "normalized_compact_image": "(USp(2) x USp(4))/{(+I,+I),(-I,-I)} -> SO(8)",
            "orthogonal_form_reason": "the tensor product of two alternating forms is symmetric",
            "source_group_dimension": 13,
            "so8_dimension": 28,
            "source_rank": 3,
            "so8_rank": 4,
        },
        "input_convention_bridge": {
            "genus1_fixture_trace": "t_E=q+1-#E(F_q), with L_E=1-t_E*T+q*T^2",
            "tensor_packet_coefficient": "A=-t_E, so P_E=1+A*T+q*T^2",
            "genus2_fixture_coefficient": "P_C=1+a*T+b*T^2+q*a*T^3+q^2*T^4",
            "frozen_histogram_conversion": "each genus-one trace key t_E is negated before tensor coefficient reconstruction",
        },
        "tensor_polynomial_theorem": {
            "input": "P_E=1+A*T+q*T^2; P_C=1+a*T+b*T^2+q*a*T^3+q^2*T^4",
            "output": "Q=1+c1*T+c2*T^2+c3*T^3+c4*T^4+q^2*c3*T^5+q^4*c2*T^6+q^6*c1*T^7+q^8*T^8",
            "c1": "-A*a",
            "c2": "A^2*b+q*a^2-2*q*b",
            "c3": "A*a*q*(-A^2-b+3*q)",
            "c4": "q^2*(A^4+A^2*a^2-4*q*A^2-2*q*a^2+b^2+2*q^2)",
            "derivation": "Newton power sums p_n(E tensor C)=p_n(E)*p_n(C)",
            "functional_equation": "c_(8-k)=q^(8-2*k)*c_k for k=0,1,2,3",
        },
        "rank_three_coefficient_hypersurface": {
            "normalization": "u=c1/q, v=c2/q^2, w=c3/q^3, h=c4/q^4",
            "equation": "u^2*h-u^4+2*u^2*v+u^2-2*u*w-w^2=0",
            "integral_equation": "c1^2*c4-q^2*c1^4+2*q^2*c1^2*c2+q^4*c1^2-2*q^2*c1*c3-c3^2=0",
            "zero_trace_stratum": "u=0 forces w=0 without division",
            "interpretation": "the rank-three tensor torus occupies a hypersurface in the rank-four SO(8) coefficient space",
            "status": "EXACT_MEMBERWISE_NOT_A_STATISTICAL_FIT",
        },
        "all_q_family_moments": {
            "measure": "independent uniform monic squarefree cubic and quintic models",
            "scope": "every odd prime power q",
            "normalized_trace": "Tr(H1(E) tensor H1(C))/q=A*a/q=-u",
            "orders_0_through_4": [
                {
                    "order": order,
                    "formula": {
                        0: "1",
                        1: "0",
                        2: "(q^2-1)*(q^4-q^3+q^2+q-2)/q^6",
                        3: "0",
                        4: "(2*q^3-3*q-1)*(3*q^5-7*q^4+5*q^3+12*q^2-14*q-11)/q^8",
                    }[order],
                }
                for order in range(5)
            ],
            "coefficient_fingerprints": {
                "mean_v": "-(q-1)*(q^3-q^2+q+1)/q^6",
                "mean_h": "(q^6-2*q^5+q^4-2*q^2-2*q+2)/q^6",
                "mean_u_times_w": "(q-1)*(q+1)^2*(q^4-4*q^3+5*q^2-q-5)/q^7",
                "product_haar_limits": {"mean_v": 0, "mean_h": 1, "mean_u_times_w": 1},
            },
        },
        "compact_group_baselines": {
            "orders_0_through_6": list(range(7)),
            "product_USp2_x_USp4_trace_moments": product_haar,
            "generic_SO8_trace_moments": so8_haar,
            "earliest_trace_moment_fingerprint": {
                "order": 4,
                "product_image": 6,
                "generic_SO8": 3,
                "proof": "dim Inv((V2 tensor V4)^tensor4)=2*3=6, while SO(8) has the three pair contractions",
            },
            "coefficient_fingerprints_at_same_representation_degree": {
                "mean_h_product_image": 1,
                "mean_h_SO8": 0,
                "mean_u_times_w_product_image": 1,
                "mean_u_times_w_SO8": 0,
                "proof": "the product image has one invariant in exterior^4(V2 tensor V4) and one copy of V2 tensor V4 inside exterior^3; generic SO(8) has neither",
            },
        },
        "frozen_histogram_convolutions": families,
        "strange_higher_targets": [
            {
                "name": "centered_middle_exterior_detector",
                "statistic": "h-1",
                "known": "all-q mean equals -2/q+1/q^2-2/q^4-2/q^5+2/q^6",
                "open": "prove an all-q second moment and identify its first nontrivial automorphic channel",
            },
            {
                "name": "exterior_one_three_correlation",
                "statistic": "u*w-1",
                "known": "all-q mean equals -3/q+7/q^3-7/q^4-9/q^5+6/q^6+5/q^7",
                "open": "evaluate its variance and covariance with h-1 across related and unrelated product families",
            },
            {
                "name": "hypersurface_defect",
                "statistic": "u^2*h-u^4+2*u^2*v+u^2-2*u*w-w^2",
                "known": "identically zero for every product tensor factor",
                "open": "use nonzero defect to separate genuinely rank-four orthogonal families from hidden tensor lifts",
            },
            {
                "name": "linked_factor_breaking",
                "statistic": "fourth trace moment minus the product of marginal fourth moments",
                "known": "zero here by independent Cartesian sampling",
                "open": "couple E and C by a shared cover, isogeny, or correspondence and measure the first mixed monodromy correction",
            },
            {
                "name": "zero_trace_singular_stratum",
                "statistic": "conditional law of (v,h) given u=w=0",
                "known": "the hypersurface becomes singular along part of this stratum",
                "open": "classify whether excess mass is caused by supersingularity, trace-zero twists, or geometric endomorphisms",
            },
        ],
        "producer_and_source_locks": {
            "no_field_enumeration": True,
            "input_method": "JSON histogram convolution only",
            "locks": _source_locks(
                {
                    "genus1_fixture": genus1,
                    "balanced_fixture": balanced,
                    "genus2_formula_fixture": genus2,
                    "genus2_measure_fixture": measures,
                }
            ),
        },
        "resource_contract": {
            "hard_exact_operation_cap": MAX_EXACT_OPERATIONS,
            "operation_ledger": guard.snapshot(),
            "maximum_input_cartesian_atom_pairs_in_one_field": max(
                row["source_histogram_sizes"]["cartesian_atom_pairs"] for row in families  # type: ignore[index]
            ),
            "field_or_curve_enumerations": 0,
            "random_samples": 0,
            "floating_point_results": 0,
        },
        "scope_firewall": {
            "no_generic_SO8_claim": "the tensor image is a proper rank-three subgroup, and the exact hypersurface forbids generic SO(8) coefficient law",
            "no_equidistribution_claim": "three frozen fields do not prove convergence to product Haar or any rate",
            "no_coarse_measure_substitution": "model/stack histograms are never relabeled as uniform coarse laws",
            "no_whole_H2_confusion": "the two Tate factors are omitted from the primitive degree-eight packet and displayed separately",
            "no_RH_or_GRH_claim": "finite-field local factor identities prove no zero statement for a global L-function",
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path, default=None)
    parser.add_argument("--check", type=Path, default=None)
    args = parser.parse_args()
    if args.write is not None and args.check is not None:
        raise SystemExit("choose at most one of --write and --check")
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
