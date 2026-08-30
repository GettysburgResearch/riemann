#!/usr/bin/env python3
"""Bounded exact controls for fixed-conductor live source multiplicity.

The all-horizon prime-distribution theorem is proved in the companion note,
not by this finite replay. No native coefficient freedom is inferred.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb, gcd, isqrt, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "LIVE_FIXED_CONDUCTOR_MULTIPLICITY.md"
QUANTITATIVE_NOTE = HERE / "FIXED_CONDUCTOR_POWER_RANK_BARRIER.md"
LOCK = HERE / "live_fixed_conductor_multiplicity.sources.json"
FIXTURE = HERE / "live_fixed_conductor_multiplicity.json"
TEST = ROOT / "tests" / "test_live_fixed_conductor_multiplicity.py"
MAX_PRIME = 2_000_000
MAX_HORIZON = 2**72
MAX_OWNERS = 4
MAX_SEARCH_CANDIDATES = 20_000
MAX_SOURCE_BYTES = 131_072

SCOUTS = (
    {
        "name": "U256",
        "horizon": 2**48,
        "common_labels": (17, 19, 59),
        "left_range": (33_000, 34_000),
        "right_range": (17_000, 17_300),
    },
    {
        "name": "U1024_held_out",
        "horizon": 2**60,
        "common_labels": (37, 41, 223),
        "left_range": (420_000, 422_000),
        "right_range": (210_000, 211_000),
    },
)

# Frozen from a separately declared 5,578-candidate scout. They authenticate
# the general sufficient inequalities, not the narrower asymptotic intervals.
PANELS: tuple[dict[str, object], ...] = (
    {
        "name": "U256_three_by_three",
        "horizon": 2**48,
        "common_labels": (17, 19, 59),
        "left_owners": ((2, 16573), (3, 11093), (11, 3019)),
        "right_owners": ((13, 1327), (37, 463), (41, 421)),
    },
    {
        "name": "U1024_four_by_three_held_out",
        "horizon": 2**60,
        "common_labels": (37, 41, 223),
        "left_owners": ((2, 210011), (3, 140159), (11, 38201), (13, 32353)),
        "right_owners": ((17, 12373), (19, 11059), (23, 9137)),
    },
)

SOURCE_BLOBS = {
    (
        "a30276a5be049749ebb2147f30f000dd5659298b",
        "research/l-families/atlas/function_field/FFPS_LIVE_SHARED_FIBRE_COLLISIONS.md",
    ): "b12efe62a07fa12843937f715adaa87ae769f2e8",
    (
        "a30276a5be049749ebb2147f30f000dd5659298b",
        "research/l-families/atlas/function_field/FFPS_SIGNED_HISTORY_RECOMBINATION.md",
    ): "c5f77f48bd19cc9af39698d4de53ae266bd42e17",
    (
        "a30276a5be049749ebb2147f30f000dd5659298b",
        "research/riemann-structures/SOURCE_ALGEBRA_DIAGONAL_ADAMS_ADAPTER.md",
    ): "eb3aa1685d4593dc8a0a4de75368d4faaa1097d4",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102887-horizon-safe-pair-gauge-eliminates-the-largest-two-smooth-boundary.md",
    ): "383aa27fee269645e45c26c12fbd4a97a6b337a8",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102962-canonical-equal-pair-gauge-is-horizon-safe-on-the-boolean-balanced-source.md",
    ): "d8f4557df6dc37e6b605b1821c5b8ab028136398",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md",
    ): "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
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
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: int, name: str, low: int, high: int) -> int:
    require(type(value) is int and low <= value <= high, f"invalid {name}")
    return value


def is_prime(value: int) -> bool:
    if type(value) is not int or not 2 <= value <= MAX_PRIME:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % d for d in range(3, isqrt(value) + 1, 2))


def sixth_root(horizon: int) -> int:
    integer(horizon, "horizon", 1, MAX_HORIZON)
    low, high = 0, 1 << ((horizon.bit_length() + 5) // 6)
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**6 <= horizon:
            low = middle
        else:
            high = middle
    return high if high**6 <= horizon else low


def validate_labels(labels: tuple[int, ...]) -> tuple[int, ...]:
    require(type(labels) is tuple and 1 <= len(labels) <= 4, "label cap/type")
    require(all(is_prime(p) for p in labels), "labels must be capped primes")
    require(len(set(labels)) == len(labels), "labels must be distinct")
    return tuple(sorted(labels))


def a_u(labels: tuple[int, ...], cutoff: int) -> int:
    integer(cutoff, "cutoff", 1, MAX_PRIME)
    if not labels:
        return 0
    labels = validate_labels(labels)
    total = 0
    for bits in product((0, 1), repeat=len(labels)):
        if prod(p for p, take in zip(labels, bits) if take) <= cutoff:
            total += (-1) ** sum(bits)
    return -total


def histories(labels: tuple[int, ...], cutoff: int) -> list[dict[str, object]]:
    labels = validate_labels(labels)
    rows = []
    for assignment in product((0, 1, 2), repeat=len(labels)):
        factors = tuple(
            tuple(p for p, slot in zip(labels, assignment) if slot == i)
            for i in range(3)
        )
        coefficient = a_u(factors[0], cutoff) * a_u(factors[1], cutoff)
        coefficient *= (-1) ** len(factors[2])
        if coefficient:
            rows.append(
                {
                    "first": list(factors[0]),
                    "second": list(factors[1]),
                    "tail": list(factors[2]),
                    "coefficient": coefficient,
                }
            )
    return rows


def vaughan_coefficient(labels: tuple[int, ...], cutoff: int) -> int:
    """Independent mu - 2 mu_U + mu_U star mu_U star 1 coefficient."""
    labels = validate_labels(labels)
    integer(cutoff, "cutoff", 1, MAX_PRIME)
    total = (-1) ** len(labels) * (1 - 2 * int(prod(labels) <= cutoff))
    for assignment in product((0, 1, 2), repeat=len(labels)):
        first = tuple(p for p, slot in zip(labels, assignment) if slot == 0)
        second = tuple(p for p, slot in zip(labels, assignment) if slot == 1)
        if prod(first) <= cutoff and prod(second) <= cutoff:
            total += (-1) ** (len(first) + len(second))
    return total


def core_record(horizon: int, common_labels: tuple[int, int, int]) -> dict[str, object]:
    cutoff = sixth_root(horizon)
    require(cutoff**6 == horizon and cutoff & (cutoff - 1) == 0, "dyadic sixth horizon")
    require(
        type(common_labels) is tuple and len(common_labels) == 3, "three common primes"
    )
    a, b, c = common_labels
    validate_labels(common_labels)
    require(not {5, 7, 67}.intersection(common_labels), "excluded core label")
    require(a <= cutoff and b <= cutoff and c <= cutoff, "singleton cutoff")
    require(a * b > cutoff and 5 * c > cutoff, "balanced partition cutoff")
    require(7 * a <= cutoff and 7 * b <= cutoff, "competing partition cutoff")
    common = prod(common_labels)
    require(3 * common < cutoff**2, "common core must remain below U^2/3")
    row = {"cutoff": cutoff, "common_labels": list(common_labels), "g": common}
    for q in (5, 7):
        labels = (*common_labels, q)
        actual = histories(labels, cutoff)
        expected = [
            {
                "first": sorted((a, b)),
                "second": sorted((c, q)),
                "tail": [],
                "coefficient": 1,
            },
            {
                "first": sorted((c, q)),
                "second": sorted((a, b)),
                "tail": [],
                "coefficient": 1,
            },
        ]
        require(
            sorted(actual, key=str) == sorted(expected, key=str), "two-history formula"
        )
        require(vaughan_coefficient(labels, cutoff) == 2, "independent Vaughan formula")
        row[f"core_{q}"] = {
            "labels": sorted(labels),
            "histories": actual,
            "balanced_coefficient": 2,
            "full_depth": 6,
            "equal_pair_share": str(Fraction(1, comb(6, 2))),
        }
    return row


def exact_rank(matrix: list[list[Fraction]]) -> int:
    require(type(matrix) is list and len(matrix) <= 16, "matrix row cap")
    require(
        all(type(row) is list and len(row) == len(matrix) for row in matrix),
        "square matrix",
    )
    require(
        all(type(x) in (int, Fraction) for row in matrix for x in row), "exact matrix"
    )
    work = [list(map(Fraction, row)) for row in matrix]
    rank = 0
    for col in range(len(work)):
        pivot = next((i for i in range(rank, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][col]
        work[rank] = [x / pivot_value for x in work[rank]]
        for i in range(len(work)):
            if i != rank and work[i][col]:
                factor = work[i][col]
                work[i] = [x - factor * y for x, y in zip(work[i], work[rank])]
        rank += 1
    return rank


def corner_matrix(m: int, n: int) -> list[list[Fraction]]:
    integer(m, "left size", 1, MAX_OWNERS)
    integer(n, "right size", 1, MAX_OWNERS)
    cells = list(product(range(m), range(n)))
    return [
        [Fraction(24, 35) * int(i != k and j != l) for k, l in cells] for i, j in cells
    ]


def quadratic(
    matrix: list[list[Fraction]], vector: tuple[int | Fraction, ...]
) -> Fraction:
    require(len(matrix) == len(vector), "quadratic dimensions")
    require(all(type(x) in (int, Fraction) for x in vector), "exact vector")
    return sum(
        (
            matrix[i][j] * vector[i] * vector[j]
            for i in range(len(vector))
            for j in range(len(vector))
        ),
        Fraction(),
    )


def panel_record(spec: dict[str, object]) -> dict[str, object]:
    require(type(spec) is dict, "panel type")
    horizon = integer(spec["horizon"], "horizon", 1, MAX_HORIZON)
    core = core_record(horizon, spec["common_labels"])
    common, cutoff = core["g"], core["cutoff"]
    left, right = spec["left_owners"], spec["right_owners"]
    for owners in (left, right):
        require(
            type(owners) is tuple and 1 <= len(owners) <= MAX_OWNERS,
            "owner list cap/type",
        )
        require(
            all(type(pair) is tuple and len(pair) == 2 for pair in owners),
            "owner pair type",
        )
    labels = tuple(p for pair in (*left, *right) for p in pair)
    require(all(is_prime(p) for p in labels), "owners must be capped primes")
    require(len(set(labels)) == len(labels), "all owner labels must be distinct")
    require(
        not set(labels).intersection({5, 7, 67, *spec["common_labels"]}),
        "owner/core overlap",
    )
    require(
        all(small < cutoff < large for small, large in (*left, *right)),
        "owner scale separation",
    )
    sides = []
    for q, modulus, owners in ((5, 7, left), (7, 5, right)):
        products = [prod(pair) for pair in owners]
        require(all(p % modulus == 1 for p in products), "fixed owner congruence")
        require(all(p <= q * common for p in products), "owner/core inequality")
        physical = [p * (q * common) ** 2 for p in products]
        require(
            all(horizon < value and 10 * value < 11 * horizon for value in physical),
            "physical window",
        )
        require(len({p.bit_length() for p in products}) == 1, "owner dyadic block")
        require(len({p.bit_length() for p in physical}) == 1, "physical dyadic block")
        require(
            all(p * p <= 16 * horizon for pair in owners for p in pair),
            "owner horizon safety",
        )
        arguments = [Fraction(3 * horizon, 2 * p) for p in physical]
        require(
            all(Fraction(15, 11) < z < Fraction(3, 2) for z in arguments),
            "kernel argument window",
        )
        require(all(16 * z < 25 for z in arguments), "K_L strictly exceeds 3")
        sides.append(
            {
                "owners": [list(pair) for pair in owners],
                "products": products,
                "physical_products": physical,
                "owner_dyadic_exponent": products[0].bit_length() - 1,
                "physical_dyadic_exponent": physical[0].bit_length() - 1,
                "kernel_arguments_at_3Y_over_2": list(map(str, arguments)),
            }
        )
    require(
        all(p * p <= 16 * horizon for p in (*spec["common_labels"], 5, 7)),
        "core horizon safety",
    )
    entries = []
    for i, p in enumerate(sides[0]["products"]):
        for j, q in enumerate(sides[1]["products"]):
            n_physical = sides[0]["physical_products"][i]
            m_physical = sides[1]["physical_products"][j]
            require(
                n_physical < 8 * m_physical and m_physical < 8 * n_physical,
                "ratio-eight",
            )
            require(
                n_physical % 5 == 0 and m_physical % 5 != 0, "left marked incidence"
            )
            require(
                m_physical % 7 == 0 and n_physical % 7 != 0, "right marked incidence"
            )
            cell = ((-49 * q) % 5, (25 * p) % 7)
            require(cell == (1, 4), "same raw cell")
            require(gcd(5 * common, 7 * common) == common, "exact common core")
            entries.append(
                {
                    "index": [i, j],
                    "P": p,
                    "Q": q,
                    "cell": list(cell),
                    "literal_histories": 4,
                    "history_squared_source_dual_prefactor": str(
                        Fraction(1, 225**2 * common**2 * p * q)
                    ),
                }
            )
    m, n = len(left), len(right)
    matrix = corner_matrix(m, n)
    rank = exact_rank(matrix)
    require(rank == (m * n if m >= 2 and n >= 2 else 0), "corner rank formula")
    return {
        "name": spec["name"],
        "horizon": horizon,
        "core": core,
        "fixed_conductors": [5, 7],
        "varying_fibre": [common, 5, 7, 1, 1],
        "left": sides[0],
        "right": sides[1],
        "arithmetic_pairs": entries,
        "arithmetic_count": m * n,
        "literal_history_count": 4 * m * n,
        "residue_kernel_lower_bound_arithmetic": m * n - 1,
        "residue_kernel_lower_bound_literal": 4 * m * n - 1,
        "literal_source_difference_eigenvalue": "-24/35",
        "corner_operator_rank": rank,
        "corner_operator": [[str(x) for x in row] for row in matrix],
        "asymptotic_prime_intervals_required_for_fixture": False,
        "full_native_coefficient_family_replayed": False,
    }


def matrix_controls() -> list[dict[str, object]]:
    rows = []
    for m, n in ((1, 1), (1, 3), (2, 2), (3, 2), (3, 3), (4, 3)):
        matrix = corner_matrix(m, n)
        left = tuple(Fraction((-1) ** i * (i + 1), i + 2) for i in range(m))
        right = tuple(Fraction(j + 2, j + 1) for j in range(n))
        vector = tuple(a * b for a in left for b in right)
        direct = quadratic(matrix, vector)
        formula = Fraction(24, 35) * (sum(left) ** 2 - sum(x * x for x in left))
        formula *= sum(right) ** 2 - sum(x * x for x in right)
        require(direct == formula, "source-shaped factorization")
        rank = exact_rank(matrix)
        require(rank == (m * n if m >= 2 and n >= 2 else 0), "held-out rank formula")
        rows.append(
            {
                "m": m,
                "n": n,
                "rank": rank,
                "direct_quadratic": str(direct),
                "factorized": str(formula),
            }
        )
    return rows


def authenticate_sources() -> list[dict[str, object]]:
    raw = LOCK.read_bytes()
    require(len(raw) <= MAX_SOURCE_BYTES, "manifest size cap")
    data = json.loads(raw)
    require(
        data.get("schema")
        == "riemann.structures.fixed_conductor_multiplicity.sources.v1",
        "manifest schema",
    )
    rows = data.get("sources")
    require(
        type(rows) is list and len(rows) == len(SOURCE_BLOBS), "manifest source count"
    )
    actual = {}
    checked = []
    for row in rows:
        require(type(row) is dict, "source row type")
        key = (row.get("commit"), row.get("path"))
        require(
            key in SOURCE_BLOBS and key not in actual, "unknown or duplicate source"
        )
        expected = SOURCE_BLOBS[key]
        require(row.get("git_blob") == expected, "manifest blob mismatch")
        ref = f"{key[0]}:{key[1]}"
        resolved = subprocess.run(
            ["git", "rev-parse", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        require(resolved == expected, f"primitive source mismatch: {ref}")
        size = int(
            subprocess.run(
                ["git", "cat-file", "-s", resolved],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip()
        )
        require(0 < size <= MAX_SOURCE_BYTES, "primitive source size cap")
        actual[key] = expected
        checked.append(
            {"commit": key[0], "path": key[1], "git_blob": resolved, "bytes": size}
        )
    require(actual == SOURCE_BLOBS, "source coverage")
    return checked


def payload() -> dict[str, object]:
    sources = authenticate_sources()
    panels = [panel_record(spec) for spec in PANELS]
    controls = matrix_controls()
    d, p = Fraction(24, 35), Fraction(2, 35)
    require(d / p == 12 and (d - p) / p == 11, "fixed amplification ratios")
    owned = {}
    for path in (NOTE, QUANTITATIVE_NOTE, Path(__file__), TEST, LOCK):
        raw = path.read_bytes()
        require(len(raw) <= MAX_SOURCE_BYTES, "owned file cap")
        owned[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    return {
        "schema": "riemann.structures.fixed_conductor_multiplicity.v1",
        "status": "EXACT_FINITE_SOURCE_CONTROLS_WITH_SEPARATE_ALL_HORIZON_PROOF",
        "base_commit": "a30276a5be049749ebb2147f30f000dd5659298b",
        "arithmetic": {
            "class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "NONE",
        },
        "coverage": {
            "fixed_panels": len(PANELS),
            "max_owner_side": MAX_OWNERS,
            "max_matrix_dimension": 16,
            "boolean_assignments_per_core": 81,
            "max_prime": MAX_PRIME,
            "scout_candidates": 5578,
        },
        "sources": sources,
        "panels": panels,
        "matrix_controls": controls,
        "channel_weights": {
            "additive": str(d),
            "principal": str(p),
            "kummer": str(d - p),
            "additive_to_principal": "12",
            "kummer_to_principal": "11",
        },
        "proof_boundary": {
            "all_horizon_prime_existence_machine_proved": False,
            "external_import": "Unconditional fixed-modulus prime number theorem, q=1,5,7",
            "complete_source_or_conductor_sweep": False,
            "native_coefficient_freedom": False,
            "final_observation_noncancellation": False,
            "RH": "UNPROVED",
            "GRH": "UNPROVED",
        },
        "owned_file_sha256_lf": owned,
    }


def scout() -> dict[str, object]:
    """Discovery-only fixed panels; bounded before primality computation."""
    rows = []
    work = 0
    for spec in SCOUTS:
        core = core_record(spec["horizon"], spec["common_labels"])
        result = {"name": spec["name"], "core": core}
        forbidden = {5, 7, 67, *spec["common_labels"]}
        for side, modulus in (("left", 7), ("right", 5)):
            lo, hi = spec[f"{side}_range"]
            owners = []
            for small in (2, 3, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 61, 71):
                if small in forbidden:
                    continue
                lower, upper = lo // small + 1, (hi - 1) // small
                require(upper <= MAX_PRIME, "scout prime cap")
                count = max(0, upper - lower + 1)
                require(work + count <= MAX_SEARCH_CANDIDATES, "scout work cap")
                work += count
                matches = [
                    p
                    for p in range(lower, upper + 1)
                    if p not in forbidden
                    and p != small
                    and (small * p) % modulus == 1
                    and is_prime(p)
                ]
                if matches:
                    owners.append({"small": small, "partners": matches[:4]})
            result[side] = owners
        rows.append(result)
    return {
        "status": "DISCOVERY_ONLY_FIXED_SEARCH",
        "candidate_budget": MAX_SEARCH_CANDIDATES,
        "candidates": work,
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scout",
        action="store_true",
        help="run only the declared fixed bounded discovery",
    )
    parser.add_argument(
        "--write", action="store_true", help="write the exact canonical finite fixture"
    )
    parser.add_argument(
        "--check", action="store_true", help="require exact canonical equality"
    )
    args = parser.parse_args()
    if args.scout:
        require(not args.write and not args.check, "scout must be separate")
        print(json.dumps(scout(), indent=2))
        return
    require(not (args.write and args.check), "choose write or check")
    result = payload()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.write:
        FIXTURE.write_text(encoded, encoding="utf-8", newline="\n")
    else:
        require(
            FIXTURE.read_text(encoding="utf-8") == encoded, "canonical fixture mismatch"
        )
    print("PASS_FCM_FIXED_CONDUCTOR_LIVE_MULTIPLICITY")
    print(
        f"panels={len(PANELS)} sources={len(SOURCE_BLOBS)} proof_object={sha256(encoded.encode()).hexdigest()}"
    )
    print(
        "FINITE_REPLAY_ONLY; ALL_HORIZON_PROOF_IMPORTS_FIXED_MODULUS_PNT; RH_UNPROVEN"
    )


if __name__ == "__main__":
    main()
