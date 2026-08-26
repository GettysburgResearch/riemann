#!/usr/bin/env python3
"""Exact source realization and hard/soft gate for cyclic FFPS masks.

The finite theorem lives on one fixed bilateral FFPS fibre.  An even
exact-order-k character has an exact-order-2k root, and that root orients the
physical Kummer coordinate P*c^2 inside a fixed owner quadratic sector.  The
resulting product mask is a hard physical restriction whose Fourier modes are
specific double-nonprincipal members of live L-106120.

Only the residue fields F_7 and F_13 and one 18-coordinate integer Gram are
inspected.  No conductor family, character family, L-function, finite-field
curve, or zero set is enumerated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "ffps_cyclic_source_realization_gate.json"
NOTE_PATH = HERE / "FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md"
TEST_PATH = ROOT / "tests" / "test_ffps_cyclic_source_realization_gate.py"

CYCLIC_NOTE_PATH = HERE / "FFPS_CYCLIC_CHARACTER_MASKS.md"
CYCLIC_JSON_PATH = HERE / "ffps_cyclic_character_masks.json"
BRIDGE_NOTE_PATH = HERE / "FFPS_CHECKERBOARD_SOURCE_BRIDGE.md"
BRIDGE_JSON_PATH = HERE / "ffps_checkerboard_source_bridge.json"

LIVE_PR_751_HEAD = "98af0db6ec7f77d6333a77a3dac53c4698852f43"
CYCLIC_PACKET_COMMIT = "5724d30a9ddd91a489312a9d09512587c4c028c1"
BRIDGE_PACKET_COMMIT = "09b74682ad6fce3ebfcc5012b246825c0fb5a740"

PREREQUISITE_LOCKS: dict[str, dict[str, object]] = {
    "cyclic_note": {
        "path": CYCLIC_NOTE_PATH,
        "commit": CYCLIC_PACKET_COMMIT,
        "git_blob": "80a56f847a1d272c43e092164503ecdfdd4c4b5d",
        "lf_sha256": "b37d5149bd53974f724d132c9b9e81060afab78816a4bec34fc8e0efcd10056c",
        "kind": "text",
        "role": "common-order cyclic quotient-fibre restricted-Gram theorem",
    },
    "cyclic_json": {
        "path": CYCLIC_JSON_PATH,
        "commit": CYCLIC_PACKET_COMMIT,
        "git_blob": "475a44f8ebb724fb47dcc22a6434bec3a1a85425",
        "lf_sha256": "b6f0034b8da4c82c2b921b0a191d12e77def31723a8a91da2f21ad9c33ad49fd",
        "kind": "json",
        "schema": "riemann.function_field.ffps_cyclic_character_masks.v1",
        "payload_sha256": "fa8b52ef39b7aa56eac02d7ed3d962282546c3cda7a262e5331683213b7947e1",
        "role": "canonical cyclic quotient and sharp hard-metric fixture",
    },
    "checkerboard_bridge_note": {
        "path": BRIDGE_NOTE_PATH,
        "commit": BRIDGE_PACKET_COMMIT,
        "git_blob": "15c32de6182407e65a6d41d593f7542945bf704e",
        "lf_sha256": "a22baad21815e6bcf7d41361861ccec8c09b0328fc55ec51c2f078b3fe77e4f2",
        "kind": "text",
        "role": "quadratic physical orientation and Wick firewall",
    },
    "checkerboard_bridge_json": {
        "path": BRIDGE_JSON_PATH,
        "commit": BRIDGE_PACKET_COMMIT,
        "git_blob": "6b38bb23a540bd9d1825cb8941de79f84f58a8f1",
        "lf_sha256": "8d8e3c374ab2fd55c438dfe2968d0faf9622e46ab0034bb7b278c636c92a6052",
        "kind": "json",
        "schema": "riemann.function_field.ffps_checkerboard_source_bridge.v1",
        "payload_sha256": "f158c471f3d3d80652bc370cd278f761c4b289db052c2a64d095c4d4367fcc68",
        "role": "canonical physical-collapse and hard-versus-soft seed",
    },
}

LIVE_CLAIM_LOCKS: dict[str, dict[str, str]] = {
    "L-106020": {
        "path": "claims/lemmas/L-106020-square-phase-gauss-mellin-identity.md",
        "git_blob": "dffea80b5cd7790779397fda1430d30260e79876",
        "role": "even-character Gauss--Mellin identity",
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
        "role": "bilateral source variables and root-character channels",
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
        "role": "corrected physical coordinates P*c^2 and Q*d^2",
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
        "role": "live WCKUM/WCADD conjunction and summation discipline",
    },
}

MAX_EXACT_OPERATIONS = 30_000
MAX_MATRIX_CELLS = 2_048
MAX_RESIDUE_ATOMS = 512
MAX_SOURCE_FILES = 4
MAX_SOURCE_BYTES_EACH = 32_768
MAX_SOURCE_BYTES_TOTAL = 80_000
MAX_GIT_OBJECTS = 20
MAX_PACKET_FILE_BYTES = 65_536
MAX_CONTROL_PRIME = 13
MAX_WALL_SECONDS = 5.0


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    matrix_cells: int = 0
    residue_atoms: int = 0
    source_files: int = 0
    source_bytes: int = 0
    git_objects: int = 0
    operation_counts: dict[str, int] = field(default_factory=dict)

    def operation(self, label: str, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("operation increment must be a nonnegative integer")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount
        self.operation_counts[label] = self.operation_counts.get(label, 0) + amount

    def matrix(self, amount: int) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("matrix increment must be a nonnegative integer")
        if self.matrix_cells + amount > MAX_MATRIX_CELLS:
            raise RuntimeError("matrix-cell cap exceeded")
        self.matrix_cells += amount

    def atom(self, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("atom increment must be a nonnegative integer")
        if self.residue_atoms + amount > MAX_RESIDUE_ATOMS:
            raise RuntimeError("residue-atom cap exceeded")
        self.residue_atoms += amount

    def source(self, amount: int) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("source byte count must be a nonnegative integer")
        if amount > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("per-source byte cap exceeded")
        if self.source_files + 1 > MAX_SOURCE_FILES:
            raise RuntimeError("source-file cap exceeded")
        if self.source_bytes + amount > MAX_SOURCE_BYTES_TOTAL:
            raise RuntimeError("total source byte cap exceeded")
        self.source_files += 1
        self.source_bytes += amount

    def git_object(self, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("git-object increment must be a nonnegative integer")
        if self.git_objects + amount > MAX_GIT_OBJECTS:
            raise RuntimeError("git-object cap exceeded")
        self.git_objects += amount


@dataclass(frozen=True)
class Deadline:
    started: float = field(default_factory=time.monotonic)

    def check(self, label: str) -> None:
        if time.monotonic() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(f"wall-time cap exceeded at {label}")


def _lf_bytes(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _lf_sha256(raw: bytes) -> str:
    return hashlib.sha256(_lf_bytes(raw)).hexdigest()


def _git_blob_sha1(raw: bytes) -> str:
    normalized = _lf_bytes(raw)
    header = f"blob {len(normalized)}\0".encode("ascii")
    return hashlib.sha1(header + normalized).hexdigest()


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
        if isinstance(item, tuple | list):
            return [normalize(entry) for entry in item]
        if isinstance(item, dict):
            return {
                unicodedata.normalize("NFC", str(key)): normalize(entry)
                for key, entry in item.items()
            }
        return item

    return json.dumps(
        normalize(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _fraction(value: int | Fraction) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _is_prime(value: int, guard: ResourceGuard | None = None) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if guard is not None:
            guard.operation("trial_divisions")
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def _require_character_panel(prime: int, order: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 3
        or prime > MAX_CONTROL_PRIME
        or prime % 2 == 0
    ):
        raise ValueError("control prime must be an odd prime within the cap")
    if not _is_prime(prime):
        raise ValueError("control prime must be prime")
    if isinstance(order, bool) or not isinstance(order, int) or order < 2:
        raise ValueError("character order must be an integer at least two")
    if (prime - 1) % (2 * order) != 0:
        raise ValueError("exact-order character requires p congruent to 1 mod 2k")


def primitive_root(prime: int, guard: ResourceGuard | None = None) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 3
        or prime > MAX_CONTROL_PRIME
        or prime % 2 == 0
    ):
        raise ValueError("primitive-root control requires a capped odd prime")
    if not _is_prime(prime, guard):
        raise ValueError("primitive-root control requires a prime")
    factors: set[int] = set()
    remaining = prime - 1
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
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise ArithmeticError("primitive root not found")


def discrete_log(value: int, prime: int, guard: ResourceGuard | None = None) -> int:
    generator = primitive_root(prime, guard)
    target = value % prime
    if target == 0:
        raise ValueError("discrete log is defined only on units")
    current = 1
    for exponent in range(prime - 1):
        if guard is not None:
            guard.operation("discrete_log_steps")
        if current == target:
            return exponent
        current = current * generator % prime
    raise ArithmeticError("unit not reached by primitive root")


def square_coset(prime: int, representative: int) -> tuple[int, ...]:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 3
        or prime > MAX_CONTROL_PRIME
        or prime % 2 == 0
    ):
        raise ValueError("square-coset control requires a capped odd prime")
    if not _is_prime(prime):
        raise ValueError("square-coset control requires a prime")
    representative %= prime
    if representative == 0:
        raise ValueError("sector representative must be a unit")
    return tuple(
        sorted({representative * value * value % prime for value in range(1, prime)})
    )


def cyclic_oriented_exponent(
    physical: int,
    representative: int,
    prime: int,
    order: int,
    guard: ResourceGuard | None = None,
) -> int:
    """Encode xi(physical/u) in mu_k as an exponent modulo k."""

    _require_character_panel(prime, order)
    physical %= prime
    representative %= prime
    if physical == 0 or representative == 0:
        raise ValueError("physical coordinate and representative must be units")
    ratio = physical * pow(representative, -1, prime) % prime
    exponent = discrete_log(ratio, prime, guard)
    if exponent % 2:
        raise ValueError("physical coordinate is outside the owner quadratic sector")
    if guard is not None:
        guard.operation("cyclic_orientations")
    return (exponent // 2) % order


def raw_core_exponent(
    core: int,
    prime: int,
    order: int,
    guard: ResourceGuard | None = None,
) -> int:
    _require_character_panel(prime, order)
    return discrete_log(core, prime, guard) % order


def source_cyclic_exponent(
    owner: int,
    core: int,
    representative: int,
    prime: int,
    order: int,
    guard: ResourceGuard | None = None,
) -> int:
    """Verify xi(P/u)*theta(c)=xi(P*c^2/u), in exponent notation."""

    physical = owner * core * core % prime
    direct = cyclic_oriented_exponent(physical, representative, prime, order, guard)
    owner_ratio = owner * pow(representative, -1, prime) % prime
    owner_log = discrete_log(owner_ratio, prime, guard)
    if owner_log % 2:
        raise ValueError("owner is outside the declared quadratic sector")
    factored = (owner_log // 2 + raw_core_exponent(core, prime, order, guard)) % order
    if direct != factored:
        raise ArithmeticError("2k-th-root owner/core factorization failed")
    return direct


def raw_collapse_counterexample(guard: ResourceGuard) -> dict[str, object]:
    prime = 7
    order = 3
    representative = 1
    first = (1, 1)
    second = (4, 3)
    rows: list[dict[str, object]] = []
    for owner, core in (first, second):
        guard.atom()
        physical = owner * core * core % prime
        rows.append(
            {
                "owner": owner,
                "core": core,
                "physical": physical,
                "raw_core_exponent_mod_3": raw_core_exponent(core, prime, order, guard),
                "oriented_physical_exponent_mod_3": source_cyclic_exponent(
                    owner, core, representative, prime, order, guard
                ),
            }
        )
    if rows[0]["physical"] != rows[1]["physical"]:
        raise ArithmeticError("ternary collision fixture missed the physical fibre")
    if rows[0]["raw_core_exponent_mod_3"] == rows[1]["raw_core_exponent_mod_3"]:
        raise ArithmeticError("ternary raw-core counterexample did not separate")
    if (
        rows[0]["oriented_physical_exponent_mod_3"]
        != rows[1]["oriented_physical_exponent_mod_3"]
    ):
        raise ArithmeticError("oriented ternary value did not survive collapse")
    return {
        "prime": prime,
        "character_order": order,
        "sector_representative": representative,
        "first": rows[0],
        "second": rows[1],
        "conclusion": (
            "raw theta(c) is not physical under varying owners; "
            "xi(P/u)*theta(c)=xi(P*c^2/u) is physical"
        ),
    }


def physical_invariance_audit(
    prime: int, order: int, representative: int, guard: ResourceGuard
) -> dict[str, object]:
    _require_character_panel(prime, order)
    owners = square_coset(prime, representative)
    fibres: dict[int, dict[str, set[int]]] = {}
    for owner in owners:
        for core in range(1, prime):
            guard.atom()
            physical = owner * core * core % prime
            row = fibres.setdefault(physical, {"oriented": set(), "raw": set()})
            row["oriented"].add(
                source_cyclic_exponent(owner, core, representative, prime, order, guard)
            )
            row["raw"].add(raw_core_exponent(core, prime, order, guard))
    oriented_singletons = all(len(row["oriented"]) == 1 for row in fibres.values())
    raw_mixes = any(len(row["raw"]) > 1 for row in fibres.values())
    distribution: dict[int, int] = {value: 0 for value in range(order)}
    for row in fibres.values():
        value = next(iter(row["oriented"]))
        distribution[value] += 1
    expected = len(fibres) // order
    if not oriented_singletons or not raw_mixes:
        raise ArithmeticError("physical invariance audit failed")
    if set(distribution.values()) != {expected}:
        raise ArithmeticError("cyclic orientation is not balanced")
    return {
        "prime": prime,
        "character_order": order,
        "sector_representative": representative,
        "physical_coordinates": len(fibres),
        "source_representations": len(owners) * (prime - 1),
        "oriented_fibres_are_singletons": oriented_singletons,
        "raw_core_character_mixes_on_some_physical_fibre": raw_mixes,
        "orientation_distribution": {
            str(key): value for key, value in distribution.items()
        },
    }


def gauge_audit(
    prime: int,
    order: int,
    representative: int,
    gauge_root: int,
    guard: ResourceGuard,
) -> dict[str, object]:
    _require_character_panel(prime, order)
    changed = representative * gauge_root * gauge_root % prime
    predicted_shift = -raw_core_exponent(gauge_root, prime, order, guard) % order
    shifts: set[int] = set()
    for physical in square_coset(prime, representative):
        guard.atom()
        old = cyclic_oriented_exponent(physical, representative, prime, order, guard)
        new = cyclic_oriented_exponent(physical, changed, prime, order, guard)
        shifts.add((new - old) % order)
    if shifts != {predicted_shift}:
        raise ArithmeticError("sector gauge was not one constant quotient rotation")
    return {
        "prime": prime,
        "character_order": order,
        "old_representative": representative,
        "gauge_root": gauge_root,
        "new_representative": changed,
        "constant_exponent_shift": predicted_shift,
        "multiplicative_formula": "epsilon_(u*r^2)=theta(r)^(-1)*epsilon_u",
        "root_choice": (
            "the two square roots xi and xi*kappa agree on x/u because x/u is a square"
        ),
        "mask_effect": "rotate S in mu_k; support labels change but all metric values do not",
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


def bilateral_exponents(
    left_prime: int,
    right_prime: int,
    order: int,
    guard: ResourceGuard,
) -> tuple[int, ...]:
    left = square_coset(left_prime, 1)
    right = square_coset(right_prime, 1)
    values: list[int] = []
    for left_coordinate in left:
        left_value = cyclic_oriented_exponent(
            left_coordinate, 1, left_prime, order, guard
        )
        for right_coordinate in right:
            guard.atom()
            right_value = cyclic_oriented_exponent(
                right_coordinate, 1, right_prime, order, guard
            )
            values.append((left_value + right_value) % order)
    return tuple(values)


def support_energy(
    gram: tuple[tuple[int, ...], ...],
    support: tuple[int, ...],
    guard: ResourceGuard,
) -> tuple[int, tuple[int, ...]]:
    rows: list[int] = []
    for row in support:
        total = 0
        for column in support:
            guard.operation("support_energy_cells")
            total += gram[row][column]
        rows.append(total)
    return sum(rows), tuple(rows)


def ternary_metric_audit(guard: ResourceGuard) -> dict[str, object]:
    left_prime = 7
    right_prime = 13
    order = 3
    retained = (0, 1)
    exponents = bilateral_exponents(left_prime, right_prime, order, guard)
    counts = {value: exponents.count(value) for value in range(order)}
    if set(counts.values()) != {6}:
        raise ArithmeticError("ternary product quotient is not balanced")
    support = tuple(index for index, value in enumerate(exponents) if value in retained)
    gram = kronecker(
        local_gram(left_prime, guard), local_gram(right_prime, guard), guard
    )
    energy, row_sums = support_energy(gram, support, guard)

    left_size = (left_prime - 1) // 2
    right_size = (right_prime - 1) // 2
    native = left_size * right_size
    constant_eigenvalue = (left_size + 1) * (right_size + 1)
    top_eigenvalue = left_prime * right_prime
    density = Fraction(len(retained), order)
    hard = Fraction(native * native, energy)
    hard_closed = Fraction(
        order * order * native,
        len(retained) ** 2 * constant_eigenvalue
        + len(retained) * (order - len(retained)) * top_eigenvalue,
    )
    complete = Fraction(native, constant_eigenvalue)
    soft = complete + Fraction(native * (1 - density), density * top_eigenvalue)
    expected_row_sum = Fraction(energy, len(support))
    if set(row_sums) != {expected_row_sum}:
        raise ArithmeticError("hard cyclic support did not have constant Gram row sum")
    if hard != hard_closed or not hard < complete < soft:
        raise ArithmeticError("ternary hard/complete/soft ordering failed")
    return {
        "primes": [left_prime, right_prime],
        "character_order": order,
        "retained_exponents": list(retained),
        "support_density": _fraction(density),
        "support_size": len(support),
        "quotient_value_counts": {str(key): value for key, value in counts.items()},
        "native_amplitude": native,
        "constant_tensor_eigenvalue_Q": constant_eigenvalue,
        "top_tensor_eigenvalue_P": top_eigenvalue,
        "restricted_gram_denominator": energy,
        "restricted_row_sum": _fraction(expected_row_sum),
        "sharp_uniform_retained_weight": _fraction(Fraction(order, len(retained))),
        "sharp_restricted_leverage": _fraction(hard),
        "complete_tensor_leverage": _fraction(complete),
        "same_zero_extended_weight_in_complete_inverse_metric": _fraction(soft),
        "strict_ordering": "hard < complete < soft",
    }


def ternary_centered_identity_audit(
    exponents: tuple[int, ...], guard: ResourceGuard
) -> dict[str, object]:
    if len(exponents) != 18 or set(exponents) != {0, 1, 2}:
        raise ValueError("ternary centered control requires the 18-coordinate grid")
    coefficients = tuple(
        Fraction((7 * index) % 17 - 8, index % 3 + 1) for index in range(len(exponents))
    )
    guard.operation("centered_control_coefficients", len(coefficients))
    diagonal = sum((value * value for value in coefficients), Fraction(0))
    principal = sum(coefficients, Fraction(0))
    principal_centered = principal * principal - diagonal

    observation_centered: list[Fraction] = []
    for shift in range(3):
        retained = {(shift + value) % 3 for value in (0, 1)}
        selected = [
            coefficient
            for exponent, coefficient in zip(exponents, coefficients, strict=True)
            if exponent in retained
        ]
        guard.operation("rotated_mask_terms", len(selected))
        observation = Fraction(3, 2) * sum(selected, Fraction(0))
        selected_diagonal = sum((value * value for value in selected), Fraction(0))
        observation_centered.append(
            observation * observation - Fraction(9, 4) * selected_diagonal
        )

    class_totals = [
        sum(
            (
                coefficient
                for exponent, coefficient in zip(exponents, coefficients, strict=True)
                if exponent == residue
            ),
            Fraction(0),
        )
        for residue in range(3)
    ]
    # If H=Z0+Z1*zeta+Z2*zeta^2 and zeta^2+zeta+1=0, then
    # |H|^2=(Z0-Z2)^2-(Z0-Z2)(Z1-Z2)+(Z1-Z2)^2.
    first = class_totals[0] - class_totals[2]
    second = class_totals[1] - class_totals[2]
    mode_norm = first * first - first * second + second * second
    mode_centered = mode_norm - diagonal
    reconstructed = (
        sum(observation_centered, Fraction(0)) / 3
        - Fraction(1, 4) * mode_centered
        - Fraction(1, 4) * mode_centered
    )
    if reconstructed != principal_centered:
        raise ArithmeticError("ternary Wick-centered projector identity failed")
    return {
        "control_coefficients": [_fraction(value) for value in coefficients],
        "principal": _fraction(principal),
        "literal_atomic_diagonal": _fraction(diagonal),
        "principal_centered": _fraction(principal_centered),
        "rotated_observations_centered": [
            _fraction(value) for value in observation_centered
        ],
        "H_1_centered": _fraction(mode_centered),
        "H_2_centered": _fraction(mode_centered),
        "fourier_weight_abs_squared": {"r=1": [1, 4], "r=2": [1, 4]},
        "reconstructed_centered": _fraction(reconstructed),
        "atomic_cancellation": True,
        "identity": ("P_circ=(O_0_circ+O_1_circ+O_2_circ)/3-(H_1_circ+H_2_circ)/4"),
    }


def ternary_wick_firewall(hard: Fraction) -> dict[str, object]:
    left_prime = 7
    right_prime = 13
    phase_atomic = (left_prime - 1) * (right_prime - 1)
    observation_atomic = Fraction(9, 4)
    residual = hard * phase_atomic - observation_atomic
    gauss_weight = Fraction(2 * left_prime, left_prime - 1) * Fraction(
        2 * right_prime, right_prime - 1
    )
    selected_weight = Fraction(1, 2) * gauss_weight
    if residual <= 0:
        raise ArithmeticError(
            "ternary hard gain unexpectedly removed the Wick residual"
        )
    if gauss_weight >= 9:
        raise ArithmeticError(
            "selected double-nonprincipal weight lost its uniform cap"
        )
    return {
        "phase_atomic_coefficient": phase_atomic,
        "hard_observation_atomic_coefficient": _fraction(observation_atomic),
        "normal_ordering_residual": _fraction(residual),
        "residual_is_positive": True,
        "each_selected_double_nonprincipal_gauss_weight": _fraction(gauss_weight),
        "sum_of_fourier_weight_squares": [1, 2],
        "coefficient_weighted_external_gauss_diagnostic": _fraction(selected_weight),
        "literal_centered_identity_atomic_coefficient": [1, 2],
        "diagnostic_firewall": (
            "91/36 is sum_r |c_r|^2 times the external L-106120 Gauss "
            "weight; the unweighted centered identity has literal coefficient 1/2"
        ),
        "selected_channel_count": 2,
        "conclusion": (
            "hard restriction retains a positive conductor-dimensional Wick residual; "
            "the centered three-projector/two-Kummer-mode identity cancels literal atoms"
        ),
    }


def atomic_threshold_audit(
    primes: Sequence[int], order: int, retained_count: int
) -> dict[str, object]:
    panel = tuple(primes)
    if not panel or len(set(panel)) != len(panel):
        raise ValueError("atomic-threshold panel must contain distinct primes")
    for prime in panel:
        _require_character_panel(prime, order)
    if (
        isinstance(retained_count, bool)
        or not isinstance(retained_count, int)
        or not 0 < retained_count < order
    ):
        raise ValueError("retained count must lie strictly between zero and k")
    dimensions = tuple((prime - 1) // 2 for prime in panel)
    native = 1
    constant = 1
    top = 1
    phase_atomic = 1
    for prime, dimension in zip(panel, dimensions, strict=True):
        native *= dimension
        constant *= dimension + 1
        top *= prime
        phase_atomic *= prime - 1
    normalized_constant = Fraction(constant, native)
    normalized_top = Fraction(top, native)
    density = Fraction(retained_count, order)
    leverage = 1 / (
        normalized_constant * density * density
        + normalized_top * density * (1 - density)
    )
    atomic_threshold = normalized_top / (
        phase_atomic - normalized_constant + normalized_top
    )
    improvement_threshold = normalized_constant / (normalized_top - normalized_constant)
    residual = leverage * phase_atomic - 1 / (density * density)
    improves = density > improvement_threshold
    if improves and residual <= 0:
        raise ArithmeticError("improving cyclic mask lost the universal Wick residual")
    return {
        "primes": list(panel),
        "character_order": order,
        "retained_count": retained_count,
        "density": _fraction(density),
        "A_equals_Q_over_N": _fraction(normalized_constant),
        "B_equals_P_over_N": _fraction(normalized_top),
        "phase_atomic_D0": phase_atomic,
        "leverage_improvement_threshold": _fraction(improvement_threshold),
        "positive_atomic_residual_threshold": _fraction(atomic_threshold),
        "improvement_threshold_exceeds_atomic_threshold": (
            improvement_threshold > atomic_threshold
        ),
        "strictly_improves_complete": improves,
        "hard_leverage": _fraction(leverage),
        "wick_residual": _fraction(residual),
        "wick_residual_positive": residual > 0,
    }


def universal_atomic_certificate() -> dict[str, object]:
    r_two = Fraction(25, 24)
    r_three = Fraction(49, 72)
    paired = r_two * r_three
    if paired != Fraction(1225, 1728) or paired >= 1:
        raise ArithmeticError("small-dimension product certificate failed")
    return {
        "normalized_variables": ("A=Q/N, B=P/N, D0=product_i(p_i-1)=2^d*N, rho=t/k"),
        "wick_residual": ("R=D0/(A*rho^2+B*rho*(1-rho))-rho^(-2)"),
        "positive_residual_threshold": "rho_atom=B/(D0-A+B)",
        "leverage_improvement_threshold": "rho_imp=A/(B-A)",
        "threshold_comparison": (
            "rho_imp>rho_atom iff A*D0>(B-A)^2 iff 2^d*Q*N^2>(P-Q)^2"
        ),
        "all_panel_proof": (
            "For d=1, 2*Q*N^2-(P-Q)^2=m^2*(2m+1)>0. "
            "For d>=2, put r(m)=(2m+1)^2/(2*m^2*(m+1)). "
            "It is strictly decreasing because d(log r)/dm="
            "4/(2m+1)-2/m-1/(m+1)<0. Every eligible m is at least 2; "
            "distinct primes permit m=2 at most once. If no m=2 then all "
            "r(m)<=r(3)<1. If m=2 occurs, pair it with one other factor: "
            "r(2)*r(3)=1225/1728<1. Hence P^2<2^d*Q*N^2, which is stronger."
        ),
        "r_2": _fraction(r_two),
        "r_3": _fraction(r_three),
        "r_2_times_r_3": _fraction(paired),
        "theorem": (
            "Every proper cyclic hard mask that strictly improves the complete "
            "tensor leverage has a strictly positive Wick atomic residual."
        ),
    }


def _read_prerequisites(
    guard: ResourceGuard, deadline: Deadline
) -> tuple[dict[str, object], list[dict[str, object]]]:
    parsed: dict[str, object] = {}
    manifest: list[dict[str, object]] = []
    for source_id, lock in PREREQUISITE_LOCKS.items():
        path = lock["path"]
        if not isinstance(path, Path) or not path.is_file():
            raise FileNotFoundError(f"missing prerequisite source: {source_id}")
        size = path.stat().st_size
        guard.source(size)
        raw = path.read_bytes()
        if len(raw) != size:
            raise RuntimeError(f"prerequisite size changed during read: {source_id}")
        if _lf_sha256(raw) != lock["lf_sha256"]:
            raise RuntimeError(f"LF hash mismatch for prerequisite: {source_id}")
        if _git_blob_sha1(raw) != lock["git_blob"]:
            raise RuntimeError(f"git blob mismatch for prerequisite: {source_id}")
        guard.git_object()
        completed = subprocess.run(
            [
                "git",
                "rev-parse",
                f"{lock['commit']}:{_relative(path)}",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=2.0,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"prerequisite git resolution failed: {completed.stderr.strip()}"
            )
        if completed.stdout.strip() != lock["git_blob"]:
            raise RuntimeError(f"committed blob mismatch for prerequisite: {source_id}")
        kind = lock["kind"]
        if kind == "json":
            value = json.loads(raw.decode("utf-8"))
            if value.get("schema") != lock["schema"]:
                raise RuntimeError(f"schema drift for prerequisite: {source_id}")
            if value.get("payload_sha256") != lock["payload_sha256"]:
                raise RuntimeError(f"payload drift for prerequisite: {source_id}")
            parsed[source_id] = value
        elif kind == "text":
            parsed[source_id] = _lf_bytes(raw).decode("utf-8")
        else:
            raise RuntimeError(f"unknown prerequisite kind: {kind}")
        manifest.append(
            {
                "id": source_id,
                "path": _relative(path),
                "commit": lock["commit"],
                "git_blob": lock["git_blob"],
                "lf_sha256": lock["lf_sha256"],
                "bytes_read": len(raw),
                "role": lock["role"],
            }
        )
        deadline.check(f"prerequisite {source_id}")
    return parsed, manifest


def _validate_prerequisites(sources: Mapping[str, object]) -> dict[str, object]:
    cyclic = sources.get("cyclic_json")
    bridge = sources.get("checkerboard_bridge_json")
    if not isinstance(cyclic, Mapping) or not isinstance(bridge, Mapping):
        raise TypeError("prerequisite JSON packets are malformed")
    cyclic_math = cyclic.get("exact_mathematics")
    bridge_math = bridge.get("exact_theorems")
    if not isinstance(cyclic_math, Mapping) or not isinstance(bridge_math, Mapping):
        raise TypeError("prerequisite exact mathematics is missing")
    union = cyclic_math.get("arbitrary_coset_union_theorem")
    bridge_channel = bridge_math.get("existing_kummer_channel")
    if not isinstance(union, Mapping) or not isinstance(bridge_channel, Mapping):
        raise TypeError("cyclic optimizer or checkerboard channel is missing")
    if union.get("unique_optimizer") != "alpha_opt=(k/t)*1_A, positive and uniform":
        raise RuntimeError("cyclic hard optimizer changed")
    if not bridge_channel.get("hard_restricted_gram_not_implied"):
        raise RuntimeError("checkerboard hard/soft firewall changed")
    return {
        "cyclic_payload": cyclic.get("payload_sha256"),
        "checkerboard_bridge_payload": bridge.get("payload_sha256"),
        "relationship": (
            "the cyclic packet supplies the hard quotient mask; the checkerboard "
            "packet supplies the k=2 physical orientation and Wick firewall; this "
            "packet proves the exact 2k-th-root source realization for every fixed k"
        ),
    }


def _resolve_live_claims(
    guard: ResourceGuard, deadline: Deadline
) -> list[dict[str, str]]:
    paths = [lock["path"] for lock in LIVE_CLAIM_LOCKS.values()]
    guard.git_object(len(paths))
    completed = subprocess.run(
        ["git", "ls-tree", "-r", LIVE_PR_751_HEAD, "--", *paths],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=2.0,
    )
    deadline.check("live git tree")
    if completed.returncode != 0:
        raise RuntimeError(f"git ls-tree failed: {completed.stderr.strip()}")
    found: dict[str, str] = {}
    for line in completed.stdout.splitlines():
        metadata, path = line.split("\t", 1)
        mode, object_type, blob = metadata.split()
        if mode != "100644" or object_type != "blob":
            raise RuntimeError("live claim did not resolve to a regular blob")
        found[path] = blob
    manifest: list[dict[str, str]] = []
    for claim_id, lock in LIVE_CLAIM_LOCKS.items():
        if found.get(lock["path"]) != lock["git_blob"]:
            raise RuntimeError(f"live blob mismatch for {claim_id}")
        manifest.append(
            {
                "claim_id": claim_id,
                "path": lock["path"],
                "commit": LIVE_PR_751_HEAD,
                "git_blob": lock["git_blob"],
                "role": lock["role"],
            }
        )
    return manifest


def _packet_lf_sha256(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"missing packet file: {path}")
    if path.stat().st_size > MAX_PACKET_FILE_BYTES:
        raise RuntimeError(f"packet file exceeds byte cap: {path.name}")
    return _lf_sha256(path.read_bytes())


def build_fixture() -> dict[str, object]:
    deadline = Deadline()
    guard = ResourceGuard()

    counterexample = raw_collapse_counterexample(guard)
    invariance = [
        physical_invariance_audit(7, 3, 1, guard),
        physical_invariance_audit(7, 3, 3, guard),
        physical_invariance_audit(13, 3, 1, guard),
        physical_invariance_audit(13, 3, 2, guard),
    ]
    gauge = gauge_audit(13, 3, 1, 2, guard)
    metric = ternary_metric_audit(guard)
    exponents = bilateral_exponents(7, 13, 3, guard)
    centered = ternary_centered_identity_audit(exponents, guard)
    hard = Fraction(*metric["sharp_restricted_leverage"])
    wick = ternary_wick_firewall(hard)
    universal_atomic = universal_atomic_certificate()
    atomic_controls = [
        atomic_threshold_audit((5, 13), 2, 1),
        atomic_threshold_audit((7, 13), 3, 2),
    ]
    deadline.check("exact algebra")
    operations_before_sources = guard.exact_operations
    matrix_before_sources = guard.matrix_cells
    atoms_before_sources = guard.residue_atoms

    prerequisites, prerequisite_manifest = _read_prerequisites(guard, deadline)
    prerequisite_relationship = _validate_prerequisites(prerequisites)
    live_manifest = _resolve_live_claims(guard, deadline)
    if guard.exact_operations != operations_before_sources:
        raise RuntimeError("source locks entered the exact-operation ledger")
    if guard.matrix_cells != matrix_before_sources:
        raise RuntimeError("source locks entered the matrix ledger")
    if guard.residue_atoms != atoms_before_sources:
        raise RuntimeError("source locks entered the residue-atom ledger")

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.ffps_cyclic_source_realization_gate.v1",
        "status": "EXACT_FIXED_FIBRE_CYCLIC_SOURCE_GATE_WITH_WICK_FIREWALL",
        "generated_by": _relative(SCRIPT_PATH),
        "source_contract": {
            "live_pr_751_head": LIVE_PR_751_HEAD,
            "prerequisites": prerequisite_manifest,
            "prerequisite_relationship": prerequisite_relationship,
            "live_claim_blobs": live_manifest,
        },
        "exact_theorems": {
            "exact_2k_root_orientation": {
                "hypothesis": (
                    "p is prime, k>=2, and 2k divides p-1; theta is one chosen "
                    "even exact-order-k character"
                ),
                "existence": (
                    "theta has an exact-order-2k root xi; its two square roots "
                    "differ by the quadratic character kappa"
                ),
                "order_certificate": (
                    "in the unique character subgroup <gamma> of order 2k, write "
                    "theta=gamma^(2a), gcd(a,k)=1; one of gamma^a and "
                    "gamma^(a+k) has exact order 2k"
                ),
                "physical_formula": "epsilon_(p,u)(x)=xi(x/u) in mu_k for x/u a square",
                "source_factorization": ("epsilon_(p,u)(P*c^2)=xi(P/u)*theta(c)"),
                "root_independence": (
                    "xi and xi*kappa agree on x/u because x/u is a square"
                ),
                "sector_gauge": (
                    "u->u*r^2 multiplies epsilon by theta(r)^(-1); this rotates "
                    "quotient labels and leaves support cardinality and metrics invariant"
                ),
                "primitive_character_gauge": (
                    "theta->theta^a, gcd(a,k)=1, applies the automorphism z->z^a; "
                    "the aligned k>2 mask is source-legitimate but noncanonical"
                ),
                "raw_core_failure": counterexample,
                "finite_invariance_audits": invariance,
                "finite_gauge_audit": gauge,
            },
            "live_L_106120_mode_identification": {
                "ell_side": ("epsilon_ell(Q*d^2)=chi(Q/u_ell)*eta(d), chi^2=eta"),
                "rho_side": ("epsilon_rho(P*c^2)=psi(P/u_rho)*theta(c), psi^2=theta"),
                "product": (
                    "Phi=epsilon_ell(Q*d^2)*epsilon_rho(P*c^2) differs from "
                    "the L-106120 coefficient chi(Q)*eta(d)*psi(P)*theta(c) "
                    "only by a fixed owner-sector scalar"
                ),
                "fourier_modes": (
                    "Phi^r is the L-106120 (eta^r,theta^r) channel with roots "
                    "(chi^r,psi^r), for 1<=r<k"
                ),
                "all_modes_double_nonprincipal": True,
                "composite_order_firewall": (
                    "exact common order k keeps eta^r and theta^r nonprincipal for "
                    "every 1<=r<k, although their exact orders may drop"
                ),
                "hard_support_not_supplied_by_WCKUM": True,
            },
            "hard_versus_soft_metric": metric,
            "wick_atomic_firewall": wick,
            "universal_improvement_implies_positive_wick_residual": {
                **universal_atomic,
                "finite_controls": atomic_controls,
            },
            "cyclic_centered_projector_identity": {
                "general_formula": (
                    "P_circ=(1/k)*sum_j O_j_circ-sum_(r=1)^(k-1)|c_r|^2*H_r_circ"
                ),
                "definitions": (
                    "O_j=(k/t)*sum_(Phi in zeta^j*S)z; "
                    "c_r=t^(-1)*sum_(s in S)s^(-r); H_r=sum Phi^r*z; "
                    "P=sum z, D=sum |z|^2, D_j=sum_(Phi in zeta^j*S)|z|^2"
                ),
                "parseval": "sum_(r=1)^(k-1)|c_r|^2=k/t-1",
                "literal_atoms_cancel": True,
                "ternary_control": centered,
            },
        },
        "scope": {
            "proved_source_realization": (
                "one fixed live bilateral fibre with two owner quadratic sectors and "
                "two marked primes satisfying 2k|(p-1)"
            ),
            "proved_metric": (
                "hard physical restriction before the phase square, and its exact "
                "distinction from soft complete-frame character weighting"
            ),
            "residue_fields_inspected": [7, 13],
            "finite_field_curve_families_enumerated": 0,
            "characters_enumerated": 0,
            "conductors_enumerated": 0,
            "l_functions_enumerated": 0,
            "random_samples": 0,
            "open_arithmetic": [
                "a source-admissible hard deletion/re-inversion across the complete varying-conductor assembly",
                "globally recombined Wick-centered cyclic conditioned-current estimates",
                "the selected off-atomic double-nonprincipal Kummer traces",
                "WCADD106140",
                "WCKUM106140",
                "BCI102990",
                "RH",
                "GRH",
            ],
            "forbidden_inference": (
                "spectral inclusion of every Phi^r in L-106120/WCKUM does not turn "
                "the complete inverse metric G^(-1) into the restricted metric G_A^(-1)"
            ),
        },
        "firewalls": [
            (
                "For k>2 the primitive characters, abstract mu_k alignments, sector "
                "representatives, and labelled retained set S are choices. Gauge changes "
                "rotate or automorphically relabel the quotient; no canonical global mask "
                "has been produced."
            ),
            (
                "The exact ternary gain occurs only after a hard physical restriction. "
                "A soft estimate for its two L-106120 character modes is not that restriction."
            ),
            (
                "Every cyclic hard mask that improves the complete tensor retains "
                "a strictly positive Wick atomic residual. The exact ternary residual "
                "is 7335/196."
            ),
            (
                "The centered projector identity is signed. It requires coherent global "
                "recombination; taking absolute values separately by conductor fibre is forbidden."
            ),
            (
                "Membership of selected modes among WCKUM summands does not imply a bound "
                "for their selected weighted subcombination."
            ),
            "No principal member is individualized; no RH or GRH claim is made.",
            "No external novelty claim is made.",
        ],
        "packet_manifest": {
            "producer": {
                "path": _relative(SCRIPT_PATH),
                "lf_sha256": _packet_lf_sha256(SCRIPT_PATH),
            },
            "note": {
                "path": _relative(NOTE_PATH),
                "lf_sha256": _packet_lf_sha256(NOTE_PATH),
            },
            "test": {
                "path": _relative(TEST_PATH),
                "lf_sha256": _packet_lf_sha256(TEST_PATH),
            },
        },
        "resource_contract": {
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "actual_exact_operations": guard.exact_operations,
            "operations_before_sources": operations_before_sources,
            "operation_counts": dict(sorted(guard.operation_counts.items())),
            "maximum_matrix_cells": MAX_MATRIX_CELLS,
            "actual_matrix_cells": guard.matrix_cells,
            "matrix_cells_before_sources": matrix_before_sources,
            "maximum_residue_atoms": MAX_RESIDUE_ATOMS,
            "actual_residue_atoms": guard.residue_atoms,
            "residue_atoms_before_sources": atoms_before_sources,
            "maximum_source_files": MAX_SOURCE_FILES,
            "actual_source_files": guard.source_files,
            "maximum_source_bytes_each": MAX_SOURCE_BYTES_EACH,
            "maximum_source_bytes_total": MAX_SOURCE_BYTES_TOTAL,
            "actual_source_bytes": guard.source_bytes,
            "maximum_git_objects": MAX_GIT_OBJECTS,
            "actual_git_objects": guard.git_objects,
            "maximum_control_prime": MAX_CONTROL_PRIME,
            "maximum_packet_file_bytes": MAX_PACKET_FILE_BYTES,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact integers and Fraction only; no floating point",
            "heavy_computation": False,
        },
    }
    deadline.check("fixture assembly")
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _render(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="refuse unless the fixture is current"
    )
    arguments = parser.parse_args(argv)
    rendered = _render(build_fixture()).encode("utf-8")
    if len(rendered) > MAX_PACKET_FILE_BYTES:
        raise RuntimeError("rendered fixture exceeds packet-file byte cap")
    if arguments.check:
        if not OUTPUT_PATH.is_file():
            raise FileNotFoundError(f"missing fixture: {OUTPUT_PATH}")
        if OUTPUT_PATH.stat().st_size > MAX_PACKET_FILE_BYTES:
            raise RuntimeError("existing fixture exceeds packet-file byte cap")
        if OUTPUT_PATH.read_bytes() != rendered:
            raise RuntimeError(f"fixture is stale: {OUTPUT_PATH}")
        print("PASS_FFPS_CYCLIC_SOURCE_REALIZATION_GATE")
        return 0
    OUTPUT_PATH.write_bytes(rendered)
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
