#!/usr/bin/env python3
"""Exact bounded source bridge for the FFPS Legendre checkerboard.

The producer proves that raw core Legendre parity does not survive varying
owner representations of one physical squareclass, constructs the repaired
quartic-oriented physical projector, identifies its top tensor mode with the
existing bilateral double-nonprincipal Kummer channel, and records the exact
hard/soft metric and Wick-normalization firewalls.

Only the residue fields F_5 and F_13 and a 12-coordinate integer Gram are
used.  No conductor family, L-function, curve, or zero set is enumerated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "ffps_checkerboard_source_bridge.json"
NOTE_PATH = HERE / "FFPS_CHECKERBOARD_SOURCE_BRIDGE.md"
TEST_PATH = ROOT / "tests" / "test_ffps_checkerboard_source_bridge.py"
CORRELATED_NOTE_PATH = HERE / "FFPS_CORRELATED_MASK_AMPLIFIER.md"
CORRELATED_JSON_PATH = HERE / "ffps_correlated_mask_amplifier.json"

LIVE_PR_751_HEAD = "98af0db6ec7f77d6333a77a3dac53c4698852f43"
CORRELATED_COMMIT = "12f52a2235cdcda5c3c6b43a82bfcadbbb08f73c"

MAX_EXACT_OPERATIONS = 20_000
MAX_MATRIX_CELLS = 4_096
MAX_RESIDUE_ATOMS = 2_048
MAX_GIT_OBJECTS = 16
MAX_SOURCE_FILES = 2
MAX_SOURCE_BYTES_EACH = 50_000
MAX_SOURCE_BYTES_TOTAL = 60_000
MAX_PACKET_FILE_BYTES = 65_536
MAX_WALL_SECONDS = 5.0

CORRELATED_LOCKS: dict[str, dict[str, object]] = {
    "correlated_note": {
        "path": CORRELATED_NOTE_PATH,
        "commit": CORRELATED_COMMIT,
        "git_blob": "4569c521e99e8c591f1694126605f8abee8a75f8",
        "lf_sha256": "38d178c0bed51daca67bd963523cd5db3cf35367f8b9474206b9f803325e7106",
        "role": "hard correlated checkerboard theorem and global firewall",
    },
    "correlated_json": {
        "path": CORRELATED_JSON_PATH,
        "commit": CORRELATED_COMMIT,
        "git_blob": "9fa4404f6740b2f545d56b81d4122cd636528bea",
        "lf_sha256": "d9d709997362f85d49156bc9669dd81c4f3b23379d03c65d4c91dbcd0ea4411b",
        "schema": "riemann.function_field.ffps_correlated_mask_amplifier.v1",
        "payload_sha256": "ee6c66844a15b4d6a29a6cf5dc252a5efdd5cc8b6052dcd9c27bf76dbe03269a",
        "role": "canonical exact restricted-Gram fixture",
    },
}

LIVE_CLAIM_LOCKS: dict[str, dict[str, str]] = {
    "L-106020": {
        "path": "claims/lemmas/L-106020-square-phase-gauss-mellin-identity.md",
        "git_blob": "dffea80b5cd7790779397fda1430d30260e79876",
        "role": "even-character Gauss-Mellin identity",
    },
    "L-106024": {
        "path": (
            "claims/lemmas/"
            "L-106024-local-squareclass-physical-occupancy-is-a-strict-contraction.md"
        ),
        "git_blob": "d94787dc2cd1cedd74d33ddc6269daf8de1cc061",
        "role": "local sign-pair Gram pI-J",
    },
    "L-106040": {
        "path": "claims/lemmas/L-106040-squarefree-composite-kummer-tensor-frame.md",
        "git_blob": "828d0fcde62c4029c448f33c0130fdb039700d31",
        "role": "formal composite Kummer tensor frame",
    },
    "T-106040": {
        "path": "claims/theorems/T-106040-composite-owner-conductor-kummer-frontier.md",
        "git_blob": "bd87d14b28d851d40db696a53cf00055070ea02c",
        "role": "bounded source-selected owner-conductor tensor and open assembly",
    },
    "L-106120": {
        "path": (
            "claims/lemmas/"
            "L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md"
        ),
        "git_blob": "a8d829dc10611adb7bfb4853902bdff0ab02a065",
        "role": "bilateral source variables and root-character channel",
    },
    "L-106121": {
        "path": (
            "claims/lemmas/"
            "L-106121-bilateral-tensor-moment-has-a-paid-atomic-diagonal.md"
        ),
        "git_blob": "955c3ed0363ca330439eedbae1bf0041a4c96468",
        "role": "principal atomic diagonal and source-dual moment",
    },
    "T-106121": {
        "path": (
            "claims/theorems/T-106121-bilateral-physical-squareclass-family-frontier.md"
        ),
        "git_blob": "9111983ae4bf199a8315310a9ce090561430c33b",
        "role": "corrected physical coordinates Pc^2 and Qd^2",
    },
    "R-106122": {
        "path": (
            "claims/refutations/"
            "R-106122-owner-only-product-collisions-do-not-survive-"
            "varying-core-characters.md"
        ),
        "git_blob": "dc51ae3add697ab4cec868ef8439f864ce77d71a",
        "role": "owner/core Kummer-coupling firewall",
    },
    "R-106123": {
        "path": (
            "claims/refutations/"
            "R-106123-local-core-large-sieve-does-not-pay-the-"
            "global-conductor-family.md"
        ),
        "git_blob": "f89cad68d67444280088d8bea7cbfb7c1eacc90d",
        "role": "varying-conductor positive-sum firewall",
    },
    "L-106126": {
        "path": (
            "claims/lemmas/"
            "L-106126-physical-squareclass-collisions-are-four-linear-core-lines.md"
        ),
        "git_blob": "b4dbebde403a11696c56a4689b2df8b53326a157",
        "role": "two/four physical collision lines",
    },
    "R-106131": {
        "path": (
            "claims/refutations/"
            "R-106131-complete-gauss-family-atomic-ledger-carries-"
            "phase-cardinality.md"
        ),
        "git_blob": "8dde14dd382e0c4fc1bb54d5da21de85ea002f41",
        "role": "complete-family atomic phase cardinality",
    },
    "L-106131": {
        "path": (
            "claims/lemmas/"
            "L-106131-wick-normal-ordering-additive-kummer-decomposition.md"
        ),
        "git_blob": "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
        "role": "exact Wick additive/Kummer decomposition",
    },
    "T-106140": {
        "path": (
            "claims/theorems/"
            "T-106140-wick-centered-additive-kummer-conjunction-frontier.md"
        ),
        "git_blob": "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
        "role": "live WCADD/WCKUM conjunction and summation discipline",
    },
}


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    matrix_cells: int = 0
    residue_atoms: int = 0
    git_objects: int = 0
    source_files: int = 0
    source_bytes: int = 0
    operation_counts: dict[str, int] = field(default_factory=dict)

    def operation(self, label: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount
        self.operation_counts[label] = self.operation_counts.get(label, 0) + amount

    def matrix(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("matrix increment must be nonnegative")
        if self.matrix_cells + amount > MAX_MATRIX_CELLS:
            raise RuntimeError("matrix-cell cap exceeded")
        self.matrix_cells += amount

    def atom(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("atom increment must be nonnegative")
        if self.residue_atoms + amount > MAX_RESIDUE_ATOMS:
            raise RuntimeError("residue-atom cap exceeded")
        self.residue_atoms += amount

    def git_object(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("git-object increment must be nonnegative")
        if self.git_objects + amount > MAX_GIT_OBJECTS:
            raise RuntimeError("git-object cap exceeded")
        self.git_objects += amount

    def source(self, size: int) -> None:
        if size < 0:
            raise ValueError("source size must be nonnegative")
        if size > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("per-source byte cap exceeded")
        if self.source_files + 1 > MAX_SOURCE_FILES:
            raise RuntimeError("source-file cap exceeded")
        if self.source_bytes + size > MAX_SOURCE_BYTES_TOTAL:
            raise RuntimeError("total source byte cap exceeded")
        self.source_files += 1
        self.source_bytes += size


@dataclass(frozen=True)
class Deadline:
    started: float = field(default_factory=time.monotonic)

    def check(self, label: str) -> None:
        if time.monotonic() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(f"wall-time cap exceeded at {label}")


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_sha256_bytes(raw: bytes) -> str:
    normalized = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _git_blob_sha1(raw: bytes) -> str:
    header = f"blob {len(raw)}\0".encode()
    return hashlib.sha1(header + raw).hexdigest()


def _fraction(value: Fraction | int) -> list[int]:
    item = Fraction(value)
    return [item.numerator, item.denominator]


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return value == divisor
        divisor += 1
    return True


def legendre(value: int, prime: int, guard: ResourceGuard | None = None) -> int:
    if not _is_prime(prime) or prime == 2:
        raise ValueError("Legendre symbol requires an odd prime")
    residue = value % prime
    if residue == 0:
        return 0
    if guard is not None:
        guard.operation("legendre_evaluations")
    power = pow(residue, (prime - 1) // 2, prime)
    if power == 1:
        return 1
    if power == prime - 1:
        return -1
    raise ArithmeticError("Euler criterion produced a non-sign")


def _require_eligible(prime: int) -> None:
    if not _is_prime(prime) or prime % 4 != 1:
        raise ValueError("checkerboard prime must be prime and 1 modulo 4")


def square_coset(prime: int, representative: int) -> tuple[int, ...]:
    _require_eligible(prime)
    if representative % prime == 0:
        raise ValueError("sector representative must be a unit")
    return tuple(
        sorted({representative * value * value % prime for value in range(1, prime)})
    )


def oriented_sign(
    physical: int,
    representative: int,
    prime: int,
    guard: ResourceGuard | None = None,
) -> int:
    """The root-free value xi(physical/representative) on one square coset."""
    _require_eligible(prime)
    physical %= prime
    representative %= prime
    if physical == 0 or representative == 0:
        raise ValueError("physical coordinate and representative must be units")
    ratio = physical * pow(representative, -1, prime) % prime
    if legendre(ratio, prime, guard) != 1:
        raise ValueError("physical coordinate is outside the declared sector")
    if guard is not None:
        guard.operation("quartic_oriented_signs")
    value = pow(ratio, (prime - 1) // 4, prime)
    if value == 1:
        return 1
    if value == prime - 1:
        return -1
    raise ArithmeticError("quartic orientation on a square was not real")


def owner_orientation(
    owner: int,
    representative: int,
    prime: int,
    guard: ResourceGuard | None = None,
) -> int:
    return oriented_sign(owner, representative, prime, guard)


def source_oriented_sign(
    owner: int,
    core: int,
    representative: int,
    prime: int,
    guard: ResourceGuard | None = None,
) -> int:
    physical = owner * core * core % prime
    direct = oriented_sign(physical, representative, prime, guard)
    factored = owner_orientation(owner, representative, prime, guard) * legendre(
        core, prime, guard
    )
    if direct != factored:
        raise ArithmeticError("quartic owner/core factorization failed")
    return direct


def primitive_root(prime: int, guard: ResourceGuard | None = None) -> int:
    _require_eligible(prime)
    order = prime - 1
    factors: set[int] = set()
    remaining = order
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.add(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.add(remaining)
    for candidate in range(2, prime):
        if guard is not None:
            guard.operation("primitive_root_candidates")
        if all(pow(candidate, order // factor, prime) != 1 for factor in factors):
            return candidate
    raise ArithmeticError("primitive root not found")


def quartic_character_exponent(
    value: int,
    prime: int,
    guard: ResourceGuard | None = None,
) -> int:
    """Return e mod 4 for xi(g^e)=i^e, using a tiny exact discrete log."""
    generator = primitive_root(prime, guard)
    target = value % prime
    if target == 0:
        raise ValueError("quartic character is defined on units")
    current = 1
    for exponent in range(prime - 1):
        if guard is not None:
            guard.operation("quartic_discrete_log_steps")
        if current == target:
            return exponent % 4
        current = current * generator % prime
    raise ArithmeticError("discrete logarithm not found")


def quartic_source_sign(
    owner: int,
    core: int,
    representative: int,
    prime: int,
    guard: ResourceGuard | None = None,
) -> int:
    exponent = (
        quartic_character_exponent(owner, prime, guard)
        - quartic_character_exponent(representative, prime, guard)
        + (0 if legendre(core, prime, guard) == 1 else 2)
    ) % 4
    if exponent == 0:
        return 1
    if exponent == 2:
        return -1
    raise ArithmeticError("normalized quartic source factor was not a sign")


def raw_collapse_counterexample(guard: ResourceGuard) -> dict[str, object]:
    prime = 5
    first = (1, 1)
    second = (4, 2)
    physical_first = first[0] * first[1] * first[1] % prime
    physical_second = second[0] * second[1] * second[1] % prime
    raw_first = legendre(first[1], prime, guard)
    raw_second = legendre(second[1], prime, guard)
    oriented_first = source_oriented_sign(*first, 1, prime, guard)
    oriented_second = source_oriented_sign(*second, 1, prime, guard)
    if physical_first != physical_second:
        raise ArithmeticError("mod-5 counterexample lost physical collision")
    if raw_first == raw_second:
        raise ArithmeticError("raw core signs unexpectedly survived collapse")
    if oriented_first != oriented_second:
        raise ArithmeticError("oriented signs failed physical invariance")
    return {
        "prime": prime,
        "sector_representative": 1,
        "first": {
            "owner": first[0],
            "core": first[1],
            "physical": physical_first,
            "raw_core_sign": raw_first,
            "oriented_sign": oriented_first,
        },
        "second": {
            "owner": second[0],
            "core": second[1],
            "physical": physical_second,
            "raw_core_sign": raw_second,
            "oriented_sign": oriented_second,
        },
        "conclusion": (
            "raw kappa(c) is not physical-collapse invariant; "
            "xi(P/u)*kappa(c)=xi(P*c^2/u) is invariant"
        ),
    }


def physical_invariance_audit(
    prime: int,
    representative: int,
    guard: ResourceGuard,
) -> dict[str, object]:
    owners = square_coset(prime, representative)
    grouped: dict[int, set[int]] = {}
    raw_grouped: dict[int, set[int]] = {}
    quartic_grouped: dict[int, set[int]] = {}
    representations = 0
    for owner in owners:
        for core in range(1, prime):
            guard.atom()
            representations += 1
            physical = owner * core * core % prime
            oriented = source_oriented_sign(owner, core, representative, prime, guard)
            quartic = quartic_source_sign(owner, core, representative, prime, guard)
            raw = legendre(core, prime, guard)
            grouped.setdefault(physical, set()).add(oriented)
            quartic_grouped.setdefault(physical, set()).add(quartic)
            raw_grouped.setdefault(physical, set()).add(raw)
    if any(len(values) != 1 for values in grouped.values()):
        raise ArithmeticError("oriented sign varied within a physical fibre")
    if grouped != quartic_grouped:
        raise ArithmeticError("quartic channel disagreed with physical orientation")
    physical_signs = tuple(next(iter(grouped[value])) for value in sorted(grouped))
    if sum(physical_signs) != 0:
        raise ArithmeticError("physical quartic orientation was not balanced")
    return {
        "prime": prime,
        "representative": representative,
        "owner_count": len(owners),
        "physical_coordinate_count": len(grouped),
        "source_representations_checked": representations,
        "oriented_fibres_are_singletons": True,
        "raw_core_sign_mixes_on_some_physical_fibre": any(
            len(values) > 1 for values in raw_grouped.values()
        ),
        "positive_coordinates": physical_signs.count(1),
        "negative_coordinates": physical_signs.count(-1),
        "quartic_root_channel_matches": True,
    }


def gauge_audit(
    prime: int,
    representative: int,
    gauge_root: int,
    guard: ResourceGuard,
) -> dict[str, object]:
    if legendre(gauge_root, prime, guard) != -1:
        raise ValueError("gauge control requires a nonsquare root")
    changed = representative * gauge_root * gauge_root % prime
    old_coset = square_coset(prime, representative)
    new_coset = square_coset(prime, changed)
    if old_coset != new_coset:
        raise ArithmeticError("gauge change left the owner sector")
    ratios = {
        oriented_sign(value, changed, prime, guard)
        * oriented_sign(value, representative, prime, guard)
        for value in old_coset
    }
    if ratios != {-1}:
        raise ArithmeticError("nonsquare gauge did not flip the whole sector")
    return {
        "prime": prime,
        "old_representative": representative,
        "gauge_root": gauge_root,
        "new_representative": changed,
        "constant_multiplier": -1,
        "effect": "swap the plus and minus projector labels",
        "other_quartic_root_effect": (
            "none after normalization, because x/u is a square"
        ),
    }


def local_gram(prime: int, guard: ResourceGuard) -> tuple[tuple[int, ...], ...]:
    size = (prime - 1) // 2
    guard.matrix(size * size)
    return tuple(
        tuple((prime if row == column else 0) - 1 for column in range(size))
        for row in range(size)
    )


def kronecker(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
    guard: ResourceGuard,
) -> tuple[tuple[int, ...], ...]:
    rows = len(left) * len(right)
    columns = len(left[0]) * len(right[0])
    guard.matrix(rows * columns)
    result: list[tuple[int, ...]] = []
    for left_row in left:
        for right_row in right:
            row: list[int] = []
            for left_value in left_row:
                row.extend(left_value * right_value for right_value in right_row)
            result.append(tuple(row))
    return tuple(result)


def checkerboard_signs(
    left_prime: int,
    right_prime: int,
    left_representative: int,
    right_representative: int,
    guard: ResourceGuard,
) -> tuple[int, ...]:
    left_coordinates = square_coset(left_prime, left_representative)
    right_coordinates = square_coset(right_prime, right_representative)
    signs: list[int] = []
    for left in left_coordinates:
        for right in right_coordinates:
            guard.atom()
            signs.append(
                oriented_sign(left, left_representative, left_prime, guard)
                * oriented_sign(right, right_representative, right_prime, guard)
            )
    if sum(signs) != 0:
        raise ArithmeticError("bilateral checkerboard was not balanced")
    return tuple(signs)


def support_energy(
    gram: tuple[tuple[int, ...], ...],
    support: tuple[int, ...],
    guard: ResourceGuard,
) -> tuple[int, tuple[int, ...]]:
    row_sums: list[int] = []
    for row in support:
        total = 0
        for column in support:
            guard.operation("support_energy_entries")
            total += gram[row][column]
        row_sums.append(total)
    return sum(row_sums), tuple(row_sums)


def checkerboard_metric_audit(
    left_prime: int,
    right_prime: int,
    guard: ResourceGuard,
) -> dict[str, object]:
    signs = checkerboard_signs(left_prime, right_prime, 1, 1, guard)
    support_plus = tuple(index for index, sign in enumerate(signs) if sign == 1)
    support_minus = tuple(index for index, sign in enumerate(signs) if sign == -1)
    gram = kronecker(
        local_gram(left_prime, guard),
        local_gram(right_prime, guard),
        guard,
    )
    energy_plus, rows_plus = support_energy(gram, support_plus, guard)
    energy_minus, rows_minus = support_energy(gram, support_minus, guard)
    left_size = (left_prime - 1) // 2
    right_size = (right_prime - 1) // 2
    native = left_size * right_size
    constant_eigenvalue = (left_size + 1) * (right_size + 1)
    top_eigenvalue = left_prime * right_prime
    closed_energy = native * (constant_eigenvalue + top_eigenvalue) // 4
    hard = Fraction(native * native, energy_plus)
    hard_closed = Fraction(
        4 * (left_prime - 1) * (right_prime - 1),
        5 * left_prime * right_prime + left_prime + right_prime + 1,
    )
    complete = Fraction(native, constant_eigenvalue)
    soft = complete + Fraction(native, top_eigenvalue)
    if energy_plus != energy_minus or energy_plus != closed_energy:
        raise ArithmeticError("checkerboard denominator formula failed")
    if hard != hard_closed or hard >= complete or soft <= complete:
        raise ArithmeticError("hard/soft metric separation failed")
    expected_row = (constant_eigenvalue + top_eigenvalue) // 2
    if set(rows_plus) != {expected_row} or set(rows_minus) != {expected_row}:
        raise ArithmeticError("uniform retained optimizer failed")
    weights = tuple(Fraction(native * row, energy_plus) for row in rows_plus)
    if set(weights) != {Fraction(2)}:
        raise ArithmeticError("checkerboard sharp weights were not uniformly two")
    return {
        "primes": [left_prime, right_prime],
        "native_coordinate_count": native,
        "support_size_each": len(support_plus),
        "constant_eigenvalue": constant_eigenvalue,
        "top_legendre_eigenvalue": top_eigenvalue,
        "restricted_denominator_each": energy_plus,
        "sharp_restricted_leverage": _fraction(hard),
        "closed_leverage_formula": ("4*(ell-1)*(rho-1)/(5*ell*rho+ell+rho+1)"),
        "uniform_retained_weight": _fraction(weights[0]),
        "complete_tensor_leverage": _fraction(complete),
        "same_soft_weight_in_complete_inverse_metric": _fraction(soft),
        "hard_improves_complete": hard < complete,
        "soft_worsens_complete": soft > complete,
        "metric_firewall": (
            "hard deletion uses inverse of G_A; soft mode weighting uses "
            "the complete G inverse"
        ),
    }


def atomic_firewall(
    left_prime: int,
    right_prime: int,
    hard_leverage: Fraction,
) -> dict[str, object]:
    phase_diagonal = (left_prime - 1) * (right_prime - 1)
    observation_diagonal = 4
    residual = hard_leverage * phase_diagonal - observation_diagonal
    if residual <= 0:
        raise ArithmeticError("declared atomic firewall was not positive")
    selected_character_weight = Fraction(2 * left_prime, left_prime - 1) * Fraction(
        2 * right_prime, right_prime - 1
    )
    if selected_character_weight >= 9:
        raise ArithmeticError("selected quartic channel lost bounded weight")
    return {
        "phase_atomic_coefficient": phase_diagonal,
        "doubled_observation_atomic_coefficient": observation_diagonal,
        "normal_ordering_residual": _fraction(residual),
        "five_thirteen_value": _fraction(Fraction(980, 43)),
        "selected_quartic_quartic_gauss_weight": _fraction(selected_character_weight),
        "selected_channel_atomic_weight_is_uniformly_bounded_by": 9,
        "conclusion": (
            "restricted leverage does not remove the R-106131 phase "
            "cardinality; one selected character has no family-dimension factor"
        ),
    }


def centered_projector_audit(signs: tuple[int, ...]) -> dict[str, object]:
    coefficients = tuple(
        Fraction((index % 7) - 3, (index % 3) + 1) for index in range(len(signs))
    )
    principal = sum(coefficients)
    high = sum(sign * value for sign, value in zip(signs, coefficients, strict=True))
    plus_values = tuple(
        value for sign, value in zip(signs, coefficients, strict=True) if sign == 1
    )
    minus_values = tuple(
        value for sign, value in zip(signs, coefficients, strict=True) if sign == -1
    )
    observed_plus = 2 * sum(plus_values)
    observed_minus = 2 * sum(minus_values)
    diagonal = sum(value * value for value in coefficients)
    diagonal_plus = sum(value * value for value in plus_values)
    diagonal_minus = sum(value * value for value in minus_values)
    principal_centered = principal * principal - diagonal
    high_centered = high * high - diagonal
    plus_centered = observed_plus * observed_plus - 4 * diagonal_plus
    minus_centered = observed_minus * observed_minus - 4 * diagonal_minus
    reconstructed = Fraction(plus_centered + minus_centered, 2) - high_centered
    if observed_plus != principal + high or observed_minus != principal - high:
        raise ArithmeticError("hard projectors did not give P plus/minus H")
    if reconstructed != principal_centered:
        raise ArithmeticError("centered projector identity failed")
    return {
        "control_coefficients": [_fraction(value) for value in coefficients],
        "principal": _fraction(principal),
        "selected_top_mode": _fraction(high),
        "doubled_plus_observation": _fraction(observed_plus),
        "doubled_minus_observation": _fraction(observed_minus),
        "principal_centered": _fraction(principal_centered),
        "reconstructed_centered": _fraction(reconstructed),
        "identity": "P_circ=(O_plus_circ+O_minus_circ)/2-H_circ",
        "atomic_cancellation": True,
    }


def _verify_correlated_sources(
    guard: ResourceGuard,
    deadline: Deadline,
) -> list[dict[str, object]]:
    manifest: list[dict[str, object]] = []
    for source_id, lock in CORRELATED_LOCKS.items():
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("correlated source path must be a Path")
        raw = path.read_bytes()
        guard.source(len(raw))
        deadline.check(f"correlated source {source_id}")
        if _lf_sha256_bytes(raw) != lock["lf_sha256"]:
            raise RuntimeError(f"LF hash mismatch for {source_id}")
        if _git_blob_sha1(raw) != lock["git_blob"]:
            raise RuntimeError(f"git blob mismatch for {source_id}")
        if source_id == "correlated_json":
            parsed = json.loads(raw.decode("utf-8"))
            if parsed.get("schema") != lock["schema"]:
                raise RuntimeError("correlated JSON schema drifted")
            if parsed.get("payload_sha256") != lock["payload_sha256"]:
                raise RuntimeError("correlated JSON payload drifted")
        manifest.append(
            {
                "id": source_id,
                "path": path.relative_to(ROOT).as_posix(),
                "commit": lock["commit"],
                "git_blob": lock["git_blob"],
                "lf_sha256": lock["lf_sha256"],
                "bytes": len(raw),
                "role": lock["role"],
            }
        )
    return manifest


def _resolve_git_locks(
    commit: str,
    locks: dict[str, dict[str, str]],
    guard: ResourceGuard,
    deadline: Deadline,
) -> list[dict[str, str]]:
    paths = [lock["path"] for lock in locks.values()]
    guard.git_object(len(paths))
    command = ["git", "ls-tree", "-r", commit, "--", *paths]
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=2.0,
    )
    deadline.check("git tree resolution")
    if completed.returncode != 0:
        raise RuntimeError(f"git ls-tree failed: {completed.stderr.strip()}")
    found: dict[str, str] = {}
    for line in completed.stdout.splitlines():
        metadata, path = line.split("\t", 1)
        mode, object_type, blob = metadata.split()
        if mode != "100644" or object_type != "blob":
            raise RuntimeError("live source lock did not resolve to a regular blob")
        found[path] = blob
    manifest: list[dict[str, str]] = []
    for claim_id, lock in locks.items():
        path = lock["path"]
        if found.get(path) != lock["git_blob"]:
            raise RuntimeError(f"live blob mismatch for {claim_id}")
        manifest.append(
            {
                "claim_id": claim_id,
                "path": path,
                "commit": commit,
                "git_blob": lock["git_blob"],
                "role": lock["role"],
            }
        )
    return manifest


def _packet_sizes() -> dict[str, int | None]:
    result: dict[str, int | None] = {}
    for label, path in (
        ("producer", SCRIPT_PATH),
        ("note", NOTE_PATH),
        ("test", TEST_PATH),
    ):
        if not path.exists():
            result[label] = None
            continue
        size = path.stat().st_size
        if size > MAX_PACKET_FILE_BYTES:
            raise RuntimeError(f"{label} file exceeds packet-size cap")
        result[label] = size
    return result


def build_fixture() -> dict[str, object]:
    deadline = Deadline()
    guard = ResourceGuard()

    counterexample = raw_collapse_counterexample(guard)
    invariance = [
        physical_invariance_audit(5, 1, guard),
        physical_invariance_audit(13, 1, guard),
    ]
    gauge = gauge_audit(13, 1, 2, guard)
    metric = checkerboard_metric_audit(5, 13, guard)
    hard = Fraction(*metric["sharp_restricted_leverage"])
    atomic = atomic_firewall(5, 13, hard)
    signs = checkerboard_signs(5, 13, 1, 1, guard)
    centered = centered_projector_audit(signs)
    deadline.check("exact algebra")

    correlated_manifest = _verify_correlated_sources(guard, deadline)
    live_manifest = _resolve_git_locks(
        LIVE_PR_751_HEAD, LIVE_CLAIM_LOCKS, guard, deadline
    )
    deadline.check("source locks")

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.ffps_checkerboard_source_bridge.v1",
        "status": "EXACT_FIXED_FIBRE_SOURCE_BRIDGE_WITH_WICK_FIREWALL",
        "generated_by": SCRIPT_PATH.relative_to(ROOT).as_posix(),
        "source_contract": {
            "correlated_commit": CORRELATED_COMMIT,
            "live_pr_751_head": LIVE_PR_751_HEAD,
            "correlated_sources": correlated_manifest,
            "live_claim_blobs": live_manifest,
        },
        "exact_theorems": {
            "raw_core_collapse_failure": counterexample,
            "quartic_oriented_physical_invariance": {
                "formula": (
                    "epsilon_p,sigma(P*c^2)=xi_p(P/u_p,sigma)*kappa_p(c)"
                    "=xi_p(P*c^2/u_p,sigma)"
                ),
                "root_free_formula": (
                    "epsilon_p,sigma(x)=(x/u_p,sigma)^((p-1)/4) in {+1,-1}"
                ),
                "finite_audits": invariance,
                "gauge_audit": gauge,
                "physical_collapse_commutes_with_projector": True,
            },
            "bilateral_projector": {
                "coordinates": {
                    "rho_side": "X=P*c^2 mod rho",
                    "ell_side": "Y=Q*d^2 mod ell",
                },
                "projectors": (
                    "Pi_plus/minus=(1 plus/minus epsilon_rho,tau(X)"
                    "*epsilon_ell,sigma(Y))/2"
                ),
                "crt_scope": (
                    "CRT on the normalized two-coordinate physical tuple; "
                    "not generally one integer's Jacobi symbol"
                ),
                "requires": "ell and rho are distinct primes congruent to 1 mod 4",
                "each_projector_has_half_the_complete_fixed_grid": True,
            },
            "existing_kummer_channel": {
                "L_106120_indices": {
                    "eta_mod_ell": "kappa_ell",
                    "theta_mod_rho": "kappa_rho",
                    "root_chi": "chi^2=kappa_ell",
                    "root_psi": "psi^2=kappa_rho",
                },
                "source_factor": ("chi(Q)*kappa_ell(d)*psi(P)*kappa_rho(c)"),
                "relation": (
                    "the checkerboard top mode differs only by the fixed "
                    "sector scalar chi(u_ell,sigma)*psi(u_rho,tau)"
                ),
                "spectrally_absorbed_by_even_character_family": True,
                "hard_restricted_gram_not_implied": True,
            },
            "hard_versus_soft_metric": metric,
            "wick_atomic_firewall": atomic,
            "centered_projector_identity": centered,
        },
        "scope": {
            "proved_source_realization": (
                "one fixed owner-class and conductor fibre after quartic "
                "orientation, with hard deletion by physical X,Y coordinates"
            ),
            "formal_only": (
                "the growing-d prime-prefix checkerboard; live bilateral "
                "T-106121 supplies only two marked phase primes per fibre"
            ),
            "open_arithmetic": [
                "globally recombined Wick-centered conditioned-current trace",
                "selected quartic-quartic off-atomic varying-conductor trace",
                "all owner/core/roughness/carrier/exceptional ledgers",
                "all conductor fibres not congruent to 1 modulo 4",
                "CBKM106130",
                "WCADD106140",
                "WCKUM106140",
                "BCI102990",
                "RH",
                "GRH",
            ],
            "smallest_analytic_lift": (
                "bound the globally recombined Wick-centered projector pair "
                "and the one selected quartic-quartic trace in the exact "
                "centered identity; the stronger existing alternative is "
                "WCADD106140 together with WCKUM106140"
            ),
            "forbidden_inference": (
                "soft control of one Kummer mode does not re-invert a hard "
                "restricted Gram, and local positive leverage does not remove "
                "the R-106131 atomic phase cardinality or R-106123 conductor sum"
            ),
        },
        "resource_budget": {
            "limits": {
                "exact_operations": MAX_EXACT_OPERATIONS,
                "matrix_cells": MAX_MATRIX_CELLS,
                "residue_atoms": MAX_RESIDUE_ATOMS,
                "git_objects": MAX_GIT_OBJECTS,
                "source_files": MAX_SOURCE_FILES,
                "source_bytes_each": MAX_SOURCE_BYTES_EACH,
                "source_bytes_total": MAX_SOURCE_BYTES_TOTAL,
                "packet_file_bytes_each": MAX_PACKET_FILE_BYTES,
                "wall_seconds": MAX_WALL_SECONDS,
            },
            "used": {
                "exact_operations": guard.exact_operations,
                "matrix_cells": guard.matrix_cells,
                "residue_atoms": guard.residue_atoms,
                "git_objects": guard.git_objects,
                "source_files": guard.source_files,
                "source_bytes": guard.source_bytes,
                "operation_counts": dict(sorted(guard.operation_counts.items())),
            },
            "packet_file_bytes": _packet_sizes(),
            "heavy_computation": False,
            "enumerated_conductors": 0,
            "enumerated_characters": 0,
            "enumerated_l_functions": 0,
            "largest_residue_prime": 13,
            "largest_matrix_dimension": 12,
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    deadline.check("final fixture")
    return fixture


def _render(fixture: dict[str, object]) -> str:
    return json.dumps(fixture, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare the exact fixture with the committed canonical JSON",
    )
    parser.add_argument(
        "--print-summary",
        action="store_true",
        help="print a compact theorem/resource summary",
    )
    arguments = parser.parse_args()
    fixture = build_fixture()
    rendered = _render(fixture)
    if arguments.check:
        if not OUTPUT_PATH.exists():
            raise SystemExit("canonical JSON is missing")
        if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            raise SystemExit("canonical JSON drifted")
    else:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    if arguments.print_summary:
        metric = fixture["exact_theorems"]["hard_versus_soft_metric"]
        used = fixture["resource_budget"]["used"]
        print(
            "hard_leverage="
            f"{metric['sharp_restricted_leverage']} "
            "soft_complete_metric="
            f"{metric['same_soft_weight_in_complete_inverse_metric']} "
            f"ops={used['exact_operations']} atoms={used['residue_atoms']}"
        )
    print("PASS_FFPS_CHECKERBOARD_SOURCE_BRIDGE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
