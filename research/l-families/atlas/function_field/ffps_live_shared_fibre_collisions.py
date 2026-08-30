#!/usr/bin/env python3
"""Exact live FFPS support collisions and fixed Boolean-history variance.

The replay checks fixed source witnesses, not a conductor-family search.  It
never infers native coefficient-family freedom from support noninjectivity.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import comb, gcd, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_LIVE_SHARED_FIBRE_COLLISIONS.md"
FIXTURE_PATH = HERE / "ffps_live_shared_fibre_collisions.json"
SOURCE_LOCK_PATH = HERE / "ffps_live_shared_fibre_collisions.sources.json"
TEST_PATH = ROOT / "tests" / "test_ffps_live_shared_fibre_collisions.py"
MAX_PRIME = 5000
MAX_SUPPORT = 6
MAX_LITERAL_ATOMS = 100
MAX_SOURCE_BYTES = 131072
MAX_HORIZON = 2**60

SOURCE_BLOBS = {
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102883-balanced-vaughan-free-energy-and-equal-product-cost-are-subpower.md",
    ): "b8a6eed2c8dda7d0ed28a8dd18fc57387e4c2e7b",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102887-horizon-safe-pair-gauge-eliminates-the-largest-two-smooth-boundary.md",
    ): "383aa27fee269645e45c26c12fbd4a97a6b337a8",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102958-ratioeight-comparability-pays-both-opposite-owner-products.md",
    ): "3b72653ea5f05405c587be165faf7ab2c52c3f2b",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102962-canonical-equal-pair-gauge-is-horizon-safe-on-the-boolean-balanced-source.md",
    ): "d8f4557df6dc37e6b605b1821c5b8ab028136398",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
    ): "346cc52420ec65457c2a5accc045d4a85635cc24",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106131-wick-normal-ordering-additive-kummer-decomposition.md",
    ): "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106191-source-dual-centered-double-incidence-correlation.md",
    ): "85c4ef92ead7d8b235f9c195c3c0acd16d16030f",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    (
        "99163530fdd311f42e138e33851a94e26c6b0f32",
        "research/l-families/atlas/function_field/FFPS_FROZEN_SOURCE_TERMINAL_HORIZON_AUDIT.md",
    ): "5540f451b41c234066d024d577de50701cf715c7",
    (
        "6675c19f20760301d8c91dedc4a7836170003512",
        "research/l-families/atlas/function_field/FFPS_SHARED_FIBRE_WICK_OCCUPANCY_SPECTRUM.md",
    ): "3e7fff53f5cdbb3a660b24b2e765f4ac35c434c3",
}

ARITHMETIC_CONTROL = {
    "name": "Y_2_30_43_47",
    "horizon": 2**30,
    "g": 37,
    "ell": 43,
    "rho": 47,
    "left_owners": ((5, 31), (2, 101)),
    "right_owners": ((3, 137), (7, 71)),
}
ARITHMETIC_HELD_OUT = {
    "name": "Y_2_33_59_61_held_out",
    "horizon": 2**33,
    "g": 53,
    "ell": 59,
    "rho": 61,
    "left_owners": ((7, 19), (2, 97)),
    "right_owners": ((5, 103), (3, 211)),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def plain_int(value: int, name: str, minimum: int, maximum: int) -> int:
    require(
        type(value) is int and minimum <= value <= maximum,
        f"{name} must be an integer in [{minimum}, {maximum}]",
    )
    return value


def is_prime(value: int) -> bool:
    if type(value) is not int or not 2 <= value <= MAX_PRIME:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def validate_support(labels: tuple[int, ...]) -> tuple[int, ...]:
    require(type(labels) is tuple, "support must be a tuple")
    require(len(labels) <= MAX_SUPPORT, "Boolean support cap exceeded")
    require(all(is_prime(label) for label in labels), "support must use primes")
    require(len(set(labels)) == len(labels), "support must be squarefree")
    return tuple(sorted(labels))


def floor_sixth_root(horizon: int) -> int:
    plain_int(horizon, "horizon", 1, MAX_HORIZON)
    low, high = 0, 1 << ((horizon.bit_length() + 5) // 6)
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**6 <= horizon:
            low = middle
        else:
            high = middle
    if high**6 <= horizon:
        return high
    return low


@lru_cache(maxsize=4096)
def _a_u(labels: tuple[int, ...], cutoff: int) -> int:
    if not labels:
        return 0
    divisor_sum = 0
    for choices in product((0, 1), repeat=len(labels)):
        divisor = prod(label for label, chosen in zip(labels, choices) if chosen)
        if divisor <= cutoff:
            divisor_sum += -1 if sum(choices) % 2 else 1
    return -divisor_sum


def boolean_a_u(labels: tuple[int, ...], cutoff: int) -> int:
    labels = validate_support(labels)
    plain_int(cutoff, "cutoff", 1, MAX_PRIME)
    return _a_u(labels, cutoff)


def balanced_representations(
    labels: tuple[int, ...], cutoff: int
) -> tuple[dict[str, object], ...]:
    """Literal ordered a_U star a_U star mu histories, without aggregation."""

    labels = validate_support(labels)
    plain_int(cutoff, "cutoff", 1, MAX_PRIME)
    rows: list[dict[str, object]] = []
    for assignment in product((0, 1, 2), repeat=len(labels)):
        first = tuple(label for label, slot in zip(labels, assignment) if slot == 0)
        second = tuple(label for label, slot in zip(labels, assignment) if slot == 1)
        tail = tuple(label for label, slot in zip(labels, assignment) if slot == 2)
        if not first or not second:
            continue
        first_coefficient = _a_u(first, cutoff)
        second_coefficient = _a_u(second, cutoff)
        if not first_coefficient or not second_coefficient:
            continue
        tail_coefficient = -1 if len(tail) % 2 else 1
        coefficient = first_coefficient * second_coefficient * tail_coefficient
        rows.append(
            {
                "first": list(first),
                "second": list(second),
                "tail": list(tail),
                "first_product": prod(first),
                "second_product": prod(second),
                "tail_product": prod(tail),
                "first_coefficient": first_coefficient,
                "second_coefficient": second_coefficient,
                "tail_mu": tail_coefficient,
                "coefficient": coefficient,
            }
        )
    return tuple(rows)


def balanced_vaughan_coefficient(labels: tuple[int, ...], cutoff: int) -> int:
    """Independent coefficient: mu - 2 mu_U + mu_U star mu_U star 1."""

    labels = validate_support(labels)
    plain_int(cutoff, "cutoff", 1, MAX_PRIME)
    mu = -1 if len(labels) % 2 else 1
    truncated_mu = mu if prod(labels) <= cutoff else 0
    type_one = 0
    for assignment in product((0, 1, 2), repeat=len(labels)):
        first = tuple(label for label, slot in zip(labels, assignment) if slot == 0)
        second = tuple(label for label, slot in zip(labels, assignment) if slot == 1)
        if prod(first) <= cutoff and prod(second) <= cutoff:
            type_one += -1 if (len(first) + len(second)) % 2 else 1
    return mu - 2 * truncated_mu + type_one


def rational_vector(values: tuple[int | Fraction, ...]) -> tuple[Fraction, ...]:
    require(type(values) is tuple, "coefficient vector must be a tuple")
    require(1 <= len(values) <= MAX_LITERAL_ATOMS, "literal atom cap exceeded")
    require(
        all(type(value) is int or isinstance(value, Fraction) for value in values),
        "coefficients must be exact integers or Fractions",
    )
    return tuple(Fraction(value) for value in values)


def vector_statistics(values: tuple[int | Fraction, ...]) -> dict[str, object]:
    vector = rational_vector(values)
    total = sum(vector, Fraction())
    energy = sum((value * value for value in vector), Fraction())
    mean_energy = total * total / len(vector)
    return {
        "count": len(vector),
        "sum": str(total),
        "literal_diagonal_energy": str(energy),
        "cell_mean_energy": str(mean_energy),
        "kernel_projection_energy": str(energy - mean_energy),
    }


def validate_conductors(ell: int, rho: int) -> None:
    require(
        is_prime(ell) and is_prime(rho) and ell != 2 and rho != 2 and ell != rho,
        "conductors must be distinct odd primes",
    )


def legendre_symbol(value: int, prime: int) -> int:
    require(type(value) is int, "Legendre input must be an integer")
    require(is_prime(prime) and prime != 2, "Legendre modulus must be odd prime")
    residue = value % prime
    if residue == 0:
        return 0
    power = pow(residue, (prime - 1) // 2, prime)
    require(power in (1, prime - 1), "Euler criterion failed")
    return 1 if power == 1 else -1


def physical_cell(ell: int, rho: int, p_owner: int, q_owner: int) -> tuple[int, int]:
    validate_conductors(ell, rho)
    plain_int(p_owner, "P", 1, MAX_PRIME**2)
    plain_int(q_owner, "Q", 1, MAX_PRIME**2)
    require(p_owner % rho != 0 and q_owner % ell != 0, "owner unit condition failed")
    return (-rho * rho * q_owner) % ell, (ell * ell * p_owner) % rho


def atomic_diagonal(ell: int, rho: int) -> Fraction:
    validate_conductors(ell, rho)
    return Fraction((ell - 1) * (rho - 1), ell * rho)


def same_cell_wick(ell: int, rho: int, values: tuple[int | Fraction, ...]) -> Fraction:
    vector = rational_vector(values)
    total = sum(vector, Fraction())
    energy = sum((value * value for value in vector), Fraction())
    return atomic_diagonal(ell, rho) * (total * total - energy)


def support_report(labels: tuple[int, ...], cutoff: int) -> dict[str, object]:
    labels = validate_support(labels)
    rows = balanced_representations(labels, cutoff)
    coefficients = tuple(int(row["coefficient"]) for row in rows)
    total = sum(coefficients)
    require(total == balanced_vaughan_coefficient(labels, cutoff), "Vaughan mismatch")
    return {
        "labels": list(labels),
        "core": prod(labels),
        "cutoff": cutoff,
        "ordered_histories": list(rows),
        "history_count": len(rows),
        "coefficient_histogram": {
            str(key): value for key, value in sorted(Counter(coefficients).items())
        },
        "balanced_coefficient": total,
        "coefficient_vector_statistics": vector_statistics(coefficients),
    }


def source_pair_record(
    horizon: int,
    common_labels: tuple[int, ...],
    ell: int,
    rho: int,
    left_owners: tuple[int, int],
    right_owners: tuple[int, int],
) -> dict[str, object]:
    plain_int(horizon, "horizon", 1, MAX_HORIZON)
    common_labels = validate_support(common_labels)
    validate_conductors(ell, rho)
    require(bool(common_labels), "common core must be nonempty in these witnesses")
    require(
        type(left_owners) is tuple
        and type(right_owners) is tuple
        and len(left_owners) == len(right_owners) == 2,
        "owners must be pairs",
    )
    owners = (*left_owners, *right_owners)
    require(all(is_prime(owner) for owner in owners), "owners must be primes")
    require(len(set(owners)) == 4, "source pair must have four distinct owner labels")
    core_labels = (*common_labels, ell, rho)
    require(len(set(core_labels)) == len(core_labels), "common/reduced cores overlap")
    require(not set(owners).intersection(core_labels), "owner/core cleanliness failed")
    require(67 not in (*owners, *core_labels), "marked-67 sector is excluded here")
    common = prod(common_labels)
    left_core, right_core = common * ell, common * rho
    p_owner, q_owner = prod(left_owners), prod(right_owners)
    physical_left = p_owner * left_core * left_core
    physical_right = q_owner * right_core * right_core
    require(gcd(left_core, right_core) == common, "exact common-core extraction failed")
    require(
        horizon < 8 * physical_left < 16 * horizon
        and horizon < 8 * physical_right < 16 * horizon,
        "source products must lie strictly inside the active [Y/8,2Y] window",
    )
    require(
        physical_left < 8 * physical_right and physical_right < 8 * physical_left,
        "ratio-eight source interaction failed",
    )
    require(
        physical_left % ell == 0
        and physical_right % ell != 0
        and physical_right % rho == 0
        and physical_left % rho != 0,
        "native two-phase incidence failed",
    )
    require(
        all(label * label <= 16 * horizon for label in (*owners, *core_labels)),
        "horizon-safe completion label bound failed",
    )
    return {
        "P": p_owner,
        "Q": q_owner,
        "left_owner_labels": list(left_owners),
        "right_owner_labels": list(right_owners),
        "g": common,
        "c": ell,
        "d": rho,
        "u": 1,
        "v": 1,
        "left_core": left_core,
        "right_core": right_core,
        "N": physical_left,
        "M": physical_right,
        "physical_ratio": str(Fraction(physical_left, physical_right)),
        "cell": list(physical_cell(ell, rho, p_owner, q_owner)),
        "sigma": legendre_symbol(q_owner, ell),
        "tau": legendre_symbol(p_owner, rho),
    }


def arithmetic_panel(
    *,
    name: str,
    horizon: int,
    g: int,
    ell: int,
    rho: int,
    left_owners: tuple[tuple[int, int], tuple[int, int]],
    right_owners: tuple[tuple[int, int], tuple[int, int]],
) -> dict[str, object]:
    cutoff = floor_sixth_root(horizon)
    validate_conductors(ell, rho)
    require(is_prime(g) and g > cutoff, "common prime must exceed the frozen cutoff")
    require(ell > cutoff and rho > cutoff, "reduced primes must exceed the cutoff")
    require(
        type(left_owners) is tuple
        and type(right_owners) is tuple
        and len(left_owners) == len(right_owners) == 2
        and all(
            type(pair) is tuple and len(pair) == 2
            for pair in (*left_owners, *right_owners)
        ),
        "two-by-two owner panel required",
    )
    owner_labels = tuple(
        label for pair in (*left_owners, *right_owners) for label in pair
    )
    require(all(is_prime(owner) for owner in owner_labels), "owners must be primes")
    require(
        len(owner_labels) == len(set(owner_labels)) == 8,
        "eight owner labels must be distinct",
    )
    left_products = tuple(prod(pair) for pair in left_owners)
    right_products = tuple(prod(pair) for pair in right_owners)
    require(left_products[0] != left_products[1], "left owner products must differ")
    require(right_products[0] != right_products[1], "right owner products must differ")
    require(
        left_products[0] % rho == left_products[1] % rho, "left owner congruence failed"
    )
    require(
        right_products[0] % ell == right_products[1] % ell,
        "right owner congruence failed",
    )
    left_source = support_report((g, ell), cutoff)
    right_source = support_report((g, rho), cutoff)
    require(
        left_source["balanced_coefficient"]
        == right_source["balanced_coefficient"]
        == 2,
        "two-prime balanced source coefficient failed",
    )
    records = [
        source_pair_record(horizon, (g,), ell, rho, left, right)
        for left, right in product(left_owners, right_owners)
    ]
    cells = {tuple(record["cell"]) for record in records}
    require(len(cells) == 1, "arithmetic panel is not in one residue cell")
    for side in ("P", "Q", "N", "M"):
        require(
            len({int(record[side]).bit_length() for record in records}) == 1,
            f"{side} leaves its common dyadic block",
        )
    pair_labels = {(record["N"], record["M"]) for record in records}
    require(len(pair_labels) == 4, "physical pair labels were collapsed")
    require(
        len({record["physical_ratio"] for record in records}) == 4,
        "physical ratios must be distinct",
    )
    require(
        len({int(record["N"]) * int(record["M"]) for record in records}) == 4,
        "physical pair products must be distinct",
    )
    require(
        len({int(record["N"]) - int(record["M"]) for record in records}) == 4,
        "physical differences must be distinct",
    )
    histories_per_pair = int(left_source["history_count"]) * int(
        right_source["history_count"]
    )
    literal_count = len(records) * histories_per_pair
    require(literal_count <= MAX_LITERAL_ATOMS, "literal panel cap exceeded")
    arbitrary_kernel_vector = (1, -1) + (0,) * (literal_count - 2)
    require(
        same_cell_wick(ell, rho, arbitrary_kernel_vector)
        == -2 * atomic_diagonal(ell, rho),
        "same-cell kernel replay failed",
    )
    return {
        "name": name,
        "horizon": horizon,
        "frozen_cutoff": cutoff,
        "common_core": g,
        "ell": ell,
        "rho": rho,
        "sigma": records[0]["sigma"],
        "tau": records[0]["tau"],
        "cell": records[0]["cell"],
        "left_owner_difference_over_rho": (left_products[1] - left_products[0]) // rho,
        "right_owner_difference_over_ell": (right_products[1] - right_products[0])
        // ell,
        "left_boolean_source": left_source,
        "right_boolean_source": right_source,
        "equal_pair_share_per_history": str(Fraction(1, comb(4, 2))),
        "aggregate_equal_pair_share_per_side": str(Fraction(2, comb(4, 2))),
        "arithmetic_atoms_after_one_sided_equal_product_aggregation": records,
        "same_cell_arithmetic_atom_lower_bound": len(records),
        "same_cell_literal_history_atom_lower_bound": literal_count,
        "kernel_dimension_lower_bound_after_history_aggregation": len(records) - 1,
        "kernel_dimension_lower_bound_at_literal_history_resolution": literal_count - 1,
        "literal_same_cell_principal_submatrix_spectrum": [
            {
                "eigenvalue": str((literal_count - 1) * atomic_diagonal(ell, rho)),
                "multiplicity": 1,
            },
            {
                "eigenvalue": str(-atomic_diagonal(ell, rho)),
                "multiplicity": literal_count - 1,
            },
        ],
        "native_coefficient_shape": "z_ij(t)=conjugate(A_i(t))*B_j(t); no free coefficient coordinates are inferred",
        "native_coefficient_family_nonfactorization": "NOT_PROVED",
        "scope": "source support and single-side equal-product survival, not the full live occupancy census or a bound for the native signed fibre",
    }


def history_calibration() -> dict[str, object]:
    horizon, cutoff = 2**24, 16
    require(floor_sixth_root(horizon) == cutoff, "calibration cutoff drift")
    record = source_pair_record(horizon, (17,), 43, 47, (2, 3), (5, 7))
    left = support_report((17, 43), cutoff)
    right = support_report((17, 47), cutoff)
    coefficients = tuple(
        int(first["coefficient"]) * int(second["coefficient"])
        for first, second in product(
            left["ordered_histories"], right["ordered_histories"]
        )
    )
    require(coefficients == (1, 1, 1, 1), "calibration is not the four equal histories")
    return {
        "horizon": horizon,
        "frozen_cutoff": cutoff,
        "physical_pair": record,
        "left_source": left,
        "right_source": right,
        "bilateral_history_coefficient_ratios": list(coefficients),
        "coefficient_statistics": vector_statistics(coefficients),
        "scope": "literal swap multiplicity exists; its fixed native vector is constant and has zero kernel projection",
    }


def signed_history_panel() -> dict[str, object]:
    horizon, cutoff = 2**54, 512
    require(floor_sixth_root(horizon) == cutoff, "signed-history cutoff drift")
    common = (11, 13, 17, 19)
    ell, rho = 1031, 521
    record = source_pair_record(horizon, common, ell, rho, (2, 3), (5, 7))
    left = support_report((*common, ell), cutoff)
    right = support_report((*common, rho), cutoff)
    for source in (left, right):
        require(
            source["coefficient_histogram"] == {"-1": 8, "3": 2},
            "signed-history histogram drift",
        )
        require(
            source["balanced_coefficient"] == -2, "signed-history source is not live"
        )
    coefficients = tuple(
        int(first["coefficient"]) * int(second["coefficient"])
        for first, second in product(
            left["ordered_histories"], right["ordered_histories"]
        )
    )
    stats = vector_statistics(coefficients)
    require(
        stats["sum"] == "4" and stats["literal_diagonal_energy"] == "676",
        "signed native statistics drift",
    )
    require(
        stats["kernel_projection_energy"] == "16896/25", "native source variance drift"
    )
    require(
        same_cell_wick(ell, rho, coefficients) == -660 * atomic_diagonal(ell, rho),
        "fixed-history Wick value drift",
    )
    selected = (-3, 1, 1, 1)
    require(
        all(
            Counter(selected)[key] <= Counter(coefficients)[key]
            for key in set(selected)
        ),
        "selected zero-sum histories do not occur",
    )
    return {
        "horizon": horizon,
        "frozen_cutoff": cutoff,
        "physical_pair": record,
        "left_source": left,
        "right_source": right,
        "equal_pair_share_per_side_history": str(Fraction(1, comb(7, 2))),
        "common_bilateral_owner_share": str(Fraction(1, comb(7, 2) ** 2)),
        "bilateral_native_coefficient_ratios": list(coefficients),
        "bilateral_coefficient_histogram": {
            str(key): value for key, value in sorted(Counter(coefficients).items())
        },
        "coefficient_statistics": stats,
        "fixed_history_subpacket_wick_over_common_scale_squared": str(
            same_cell_wick(ell, rho, coefficients)
        ),
        "wick_value_as_multiple_of_d": -660,
        "internal_zero_sum_subset": {
            "native_coefficient_ratios": list(selected),
            "statistics": vector_statistics(selected),
            "status": "INTERNAL_SUBSET_ONLY_NOT_AN_ADMISSIBLE_FULL_NATIVE_INPUT_PAIR",
        },
        "resolution": "ordered Boolean histories before one-sided equal-product aggregation; the arithmetic pair is one point after that aggregation",
        "native_coefficient_family_nonfactorization": "NOT_PROVED",
        "scope": "fixed source variance and a fixed tuple contribution only; neither the full fibre nor the complete signed source is evaluated",
    }


def validate_source_manifest(payload: object) -> None:
    require(type(payload) is dict, "source manifest must be an object")
    require(
        payload.get("schema")
        == "riemann.function_field.ffps_live_shared_fibre_collisions.sources.v1",
        "source manifest schema drift",
    )
    sources = payload.get("sources")
    require(
        type(sources) is list and len(sources) == len(SOURCE_BLOBS),
        "source lock cardinality drift",
    )
    actual = {}
    for source in sources:
        require(type(source) is dict, "source row must be an object")
        key = (source.get("commit"), source.get("path"))
        require(key not in actual, "duplicate source lock")
        actual[key] = source.get("git_blob")
    require(actual == SOURCE_BLOBS, "source lock content drift")


def check_source_locks() -> list[dict[str, str]]:
    require(
        SOURCE_LOCK_PATH.stat().st_size <= MAX_SOURCE_BYTES,
        "source manifest byte cap exceeded",
    )
    validate_source_manifest(json.loads(SOURCE_LOCK_PATH.read_text(encoding="utf-8")))
    rows = []
    for (commit, path), expected in SOURCE_BLOBS.items():
        result = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        require(result.stdout.strip() == expected, f"source blob mismatch: {path}")
        size = subprocess.run(
            ["git", "cat-file", "-s", expected],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        require(
            int(size.stdout.strip()) <= MAX_SOURCE_BYTES,
            "upstream source byte cap exceeded",
        )
        rows.append({"commit": commit, "path": path, "git_blob": expected})
    return rows


def check_note_contract() -> None:
    require(NOTE_PATH.stat().st_size <= MAX_SOURCE_BYTES, "note byte cap exceeded")
    note = NOTE_PATH.read_text(encoding="utf-8")
    for token in (
        "single-side equal-product aggregation",
        "native coefficient-family nonfactorization remains open",
        "two admissible native inputs",
        "fixed source variance",
        "not the complete native fibre",
        "RH and GRH remain unproved",
    ):
        require(token in note, f"note boundary token missing: {token}")


def artifact_source_hashes() -> dict[str, str]:
    """Bind source files using LF-normalized UTF-8 bytes for checkout stability."""

    result = {}
    for path in (Path(__file__).resolve(), TEST_PATH, NOTE_PATH, SOURCE_LOCK_PATH):
        require(
            path.stat().st_size <= MAX_SOURCE_BYTES, "artifact source byte cap exceeded"
        )
        data = path.read_bytes().replace(b"\r\n", b"\n")
        data.decode("utf-8", errors="strict")
        result[path.relative_to(ROOT).as_posix()] = sha256(data).hexdigest()
    return result


def build_fixture(*, authenticate: bool = True) -> dict[str, object]:
    source_rows = (
        check_source_locks()
        if authenticate
        else [
            {"commit": commit, "path": path, "git_blob": blob}
            for (commit, path), blob in SOURCE_BLOBS.items()
        ]
    )
    return {
        "schema": "riemann.function_field.ffps_live_shared_fibre_collisions.v1",
        "status": "EXACT_LIVE_SUPPORT_COLLISIONS_AND_FIXED_HISTORY_VARIANCE",
        "arithmetic_class": "MIXED",
        "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        "rounding_contract": "exact Python integers and fractions; no rounding",
        "artifact_source_sha256_lf_normalized": artifact_source_hashes(),
        "source_locks": source_rows,
        "history_calibration": history_calibration(),
        "arithmetic_control": arithmetic_panel(**ARITHMETIC_CONTROL),
        "arithmetic_held_out": arithmetic_panel(**ARITHMETIC_HELD_OUT),
        "signed_history_control": signed_history_panel(),
        "proved": [
            "a complete live shared fibre can contain duplicate physical residue cells",
            "four arithmetic atoms in one cell survive single-side equal-product aggregation in both locked owner panels",
            "literal ordered histories give at least sixteen same-cell atoms in each owner panel",
            "the corresponding live-support Wick operator has a nonzero minus-d eigenspace",
            "the signed-history control has exact nonzero fixed source variance",
        ],
        "not_proved": [
            "full live occupancy classification or a conductor-uniform multiplicity estimate",
            "two admissible native inputs with the same residue aggregate and different literal diagonal energy",
            "native coefficient-family nonfactorization",
            "a sign or noncancellation theorem for the complete native fibre",
            "WCADD, WCCORR, WCKUM, ONEPLACEWEIL, RELPARTFROB, RELTRACE, or principal binding",
            "RH or GRH",
        ],
        "resource_boundary": {
            "fixed_arithmetic_owner_panels": 2,
            "largest_boolean_support": 5,
            "largest_assignment_cube": 3**5,
            "largest_literal_coefficient_vector": 100,
            "authenticated_git_blobs": len(SOURCE_BLOBS),
            "maximum_prime_input": MAX_PRIME,
            "maximum_horizon_input": MAX_HORIZON,
            "floating_point_operations": 0,
            "live_source_family_enumerated": False,
            "conductor_family_searched_by_replay": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    check_note_contract()
    fixture = build_fixture()
    if args.check:
        require(
            json.loads(FIXTURE_PATH.read_text(encoding="utf-8")) == fixture,
            "canonical fixture drift",
        )
        print("PASS_FFPS_LIVE_SHARED_FIBRE_COLLISIONS")
    else:
        print(json.dumps(fixture, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
