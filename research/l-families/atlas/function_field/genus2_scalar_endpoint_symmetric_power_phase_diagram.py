#!/usr/bin/env python3
"""Build the exact all-rank genus-two scalar-endpoint phase diagram.

The producer uses the scalar-orbit theorem frozen at commit 77c6a1b31 and
then performs only bounded exact integer arithmetic.  It enumerates no field,
curve, group, representation, or L-function family.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_scalar_endpoint_symmetric_power_phase_diagram.json"
NOTE_PATH = HERE / "GENUS2_SCALAR_ENDPOINT_SYMMETRIC_POWER_PHASE_DIAGRAM.md"
TEST_PATH = (
    ROOT / "tests" / ("test_genus2_scalar_endpoint_symmetric_power_phase_diagram.py")
)
SOURCE_PATH = HERE / "genus2_sym10_scalar_endpoint_realization.json"

SOURCE_LOCK: dict[str, object] = {
    "path": SOURCE_PATH,
    "commit": "77c6a1b31d6d2b475df0d87e187f32d9a09479e5",
    "git_blob": "ce5f1baba8c33e9243ac18e381fbd4824e7a5baa",
    "lf_sha256": "597d6b27503b0dfaa93b190ec73323ac63c76de7937d1b1bf9ba9cf3731a5313",
    "schema": "riemann.function_field.genus2_sym10_scalar_endpoint_realization.v1",
    "payload_sha256": (
        "bc2d9dcea68befbda0281ebc702b26dca805cb41676862e0c50be35ff66cf49a"
    ),
    "role": (
        "exact q=3^(4*k) seed, twist-orbit sizes, endpoint signs, and family "
        "cardinality"
    ),
}

MAX_EXACT_OPERATIONS = 4_096
MAX_SOURCE_BYTES = 32_768
MAX_OUTPUT_BYTES = 32_768
MAX_CONTROL_RANK = 100_000
MAX_WALL_SECONDS = 2.0


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    source_bytes: int = 0
    operation_counts: dict[str, int] = field(default_factory=dict)

    def operation(self, label: str, amount: int = 1) -> None:
        if (
            not isinstance(label, str)
            or not label
            or isinstance(amount, bool)
            or not isinstance(amount, int)
            or amount < 0
        ):
            raise ValueError("invalid exact-operation increment")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount
        self.operation_counts[label] = self.operation_counts.get(label, 0) + amount

    def source(self, byte_count: int) -> None:
        if (
            isinstance(byte_count, bool)
            or not isinstance(byte_count, int)
            or byte_count < 0
        ):
            raise ValueError("source-byte count must be a nonnegative integer")
        if byte_count > MAX_SOURCE_BYTES:
            raise RuntimeError("source-byte cap exceeded")
        self.source_bytes = byte_count


@dataclass(frozen=True)
class Deadline:
    started: float = field(default_factory=time.monotonic)

    def check(self, label: str) -> None:
        if not isinstance(label, str) or not label:
            raise ValueError("deadline label must be nonempty")
        elapsed = time.monotonic() - self.started
        if elapsed < 0:
            raise RuntimeError("monotonic clock moved backwards")
        if elapsed > MAX_WALL_SECONDS:
            raise RuntimeError(f"wall-time cap exceeded at {label}")


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _lf_bytes(raw: bytes) -> bytes:
    text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return unicodedata.normalize("NFC", text).encode("utf-8")


def _lf_sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(_lf_bytes(raw)).hexdigest()


def _git_blob_sha1(raw: bytes) -> str:
    header = f"blob {len(raw)}\0".encode()
    return hashlib.sha1(header + raw).hexdigest()


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _validate_nonnegative_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")


def symmetric_power_dimension(rank: int) -> int:
    """Return dim Sym^rank(C^4)=binom(rank+3,3) by a cubic formula."""

    _validate_nonnegative_integer("rank", rank)
    return (rank + 1) * (rank + 2) * (rank + 3) // 6


def scalar_character(rank: int, scalar_sign: int) -> int:
    """Return the Sym^rank character at scalar_sign times I_4."""

    _validate_nonnegative_integer("rank", rank)
    if scalar_sign not in (-1, 1):
        raise ValueError("scalar sign must be -1 or 1")
    return scalar_sign**rank * symmetric_power_dimension(rank)


def constructed_moment_contributions(
    rank: int, moment: int, q: int, tower_sign: int
) -> dict[str, Fraction]:
    """Return exact absolute and signed subtotals from the two locked orbits."""

    _validate_nonnegative_integer("rank", rank)
    if isinstance(moment, bool) or not isinstance(moment, int) or moment < 1:
        raise ValueError("moment must be a positive integer")
    if isinstance(q, bool) or not isinstance(q, int) or q < 1:
        raise ValueError("q must be a positive integer")
    if tower_sign not in (-1, 1):
        raise ValueError("tower sign must be -1 or 1")
    dimension = symmetric_power_dimension(rank)
    first = scalar_character(rank, tower_sign)
    second = scalar_character(rank, -tower_sign)
    denominator = 10 * q**3
    return {
        "absolute": Fraction(abs(first) ** moment + abs(second) ** moment, denominator),
        "signed": Fraction(first**moment + second**moment, denominator),
        "expected_absolute": Fraction(dimension**moment, 5 * q**3),
        "expected_signed": (
            Fraction(0)
            if (rank * moment) % 2
            else Fraction(dimension**moment, 5 * q**3)
        ),
    }


def _floor_log(base: int, target: int, guard: ResourceGuard) -> tuple[int, int]:
    if base <= 1 or target < 1:
        raise ValueError("floor-log requires base>1 and target>=1")
    exponent = 0
    power = 1
    while power * base <= target:
        power *= base
        exponent += 1
        guard.operation("floor_log")
    return exponent, power


def _integer_nth_root(value: int, degree: int, guard: ResourceGuard) -> int:
    if value < 0 or degree < 1:
        raise ValueError("integer root requires value>=0 and degree>=1")
    if value < 2:
        return value
    low = 1
    high = 2
    while high**degree <= value:
        low = high
        high *= 2
        guard.operation("root_bracket")
    while high - low > 1:
        middle = (low + high) // 2
        guard.operation("root_bisection")
        if middle**degree <= value:
            low = middle
        else:
            high = middle
    return low


def _rank_threshold(q: int, moment: int, guard: ResourceGuard) -> int:
    target = 5 * q**3
    low = 0
    high = 1
    while symmetric_power_dimension(high) ** moment <= target:
        low = high
        high *= 2
        guard.operation("rank_bracket")
        if high > MAX_CONTROL_RANK:
            raise RuntimeError("control-rank cap exceeded")
    while high - low > 1:
        middle = (low + high) // 2
        guard.operation("rank_bisection")
        if symmetric_power_dimension(middle) ** moment <= target:
            low = middle
        else:
            high = middle
    return low


def _fraction_json(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _fixed_rank_control(k: int, rank: int, guard: ResourceGuard) -> dict[str, object]:
    q = 3 ** (4 * k)
    dimension = symmetric_power_dimension(rank)
    target = 5 * q**3
    floor_m, floor_power = _floor_log(dimension, target, guard)
    below = Fraction(floor_power, target)
    above = Fraction(floor_power * dimension, target)
    if not (Fraction(1, dimension) < below <= 1 < above <= dimension):
        raise ArithmeticError("fixed-rank discrete crossover bounds failed")
    return {
        "k": k,
        "q": q,
        "rank": rank,
        "dimension": dimension,
        "target_5q3": target,
        "largest_m_with_constructed_subtotal_at_most_one": floor_m,
        "first_m_with_constructed_subtotal_above_one": floor_m + 1,
        "subtotal_at_floor_m": _fraction_json(below),
        "subtotal_at_next_m": _fraction_json(above),
        "exact_bounds": "1/d_r < C_(m_floor) <= 1 < C_(m_floor+1) <= d_r",
    }


def _fixed_moment_control(
    k: int, moment: int, guard: ResourceGuard
) -> dict[str, object]:
    q = 3 ** (4 * k)
    target = 5 * q**3
    rank = _rank_threshold(q, moment, guard)
    next_rank = rank + 1
    dimension = symmetric_power_dimension(rank)
    next_dimension = symmetric_power_dimension(next_rank)
    if not (dimension**moment <= target < next_dimension**moment):
        raise ArithmeticError("fixed-moment rank threshold failed")

    scaled_target = 6**moment * target
    x_floor = _integer_nth_root(scaled_target, 3 * moment, guard)
    lower_rank_bound = max(0, x_floor - 3)
    upper_rank_bound = x_floor - 1
    if not lower_rank_bound <= rank <= upper_rank_bound:
        raise ArithmeticError("cubic rank-window bound failed")
    return {
        "k": k,
        "q": q,
        "moment": moment,
        "target_5q3": target,
        "largest_rank_with_constructed_subtotal_at_most_one": rank,
        "first_rank_with_constructed_subtotal_above_one": next_rank,
        "dimension_at_rank": dimension,
        "dimension_at_next_rank": next_dimension,
        "floor_of_asymptotic_scale_X": x_floor,
        "exact_rank_window": [lower_rank_bound, upper_rank_bound],
        "scale_definition": "X=6^(1/3)*5^(1/(3m))*q^(1/m)",
    }


def _derive_all_rank_theorem(guard: ResourceGuard) -> dict[str, object]:
    dimension_rows = []
    for rank in (0, 1, 2, 3, 4, 5, 10, 20):
        dimension = symmetric_power_dimension(rank)
        guard.operation("dimension_control")
        dimension_rows.append({"rank": rank, "dimension": dimension})

    parity_rows = []
    for k, rank, moment in (
        (1, 1, 1),
        (1, 1, 2),
        (1, 2, 1),
        (2, 3, 1),
        (2, 3, 2),
        (3, 10, 5),
    ):
        q = 3 ** (4 * k)
        sign = (-1) ** k
        result = constructed_moment_contributions(rank, moment, q, sign)
        if (
            result["absolute"] != result["expected_absolute"]
            or result["signed"] != result["expected_signed"]
        ):
            raise ArithmeticError("endpoint parity control failed")
        guard.operation("parity_control", 4)
        parity_rows.append(
            {
                "k": k,
                "q": q,
                "rank": rank,
                "moment": moment,
                "tower_sign": sign,
                "first_character": scalar_character(rank, sign),
                "twist_character": scalar_character(rank, -sign),
                "absolute_subtotal": _fraction_json(result["absolute"]),
                "signed_subtotal": _fraction_json(result["signed"]),
            }
        )

    fixed_rank = [
        _fixed_rank_control(k, rank, guard)
        for k, rank in ((1, 1), (1, 2), (1, 10), (2, 3), (2, 10))
    ]
    fixed_moment = [
        _fixed_moment_control(k, moment, guard)
        for k, moment in ((1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3))
    ]

    sym10 = symmetric_power_dimension(10)
    if sym10 != 286:
        raise ArithmeticError("Sym10 specialization drifted")
    guard.operation("sym10_specialization", 4)

    return {
        "representation_identity": {
            "rank_domain": "every integer r>=0",
            "dimension": "d_r=dim Sym^r(C^4)=binom(r+3,3)",
            "expanded_dimension": "d_r=(r+1)*(r+2)*(r+3)/6",
            "reciprocal_normalization": (
                "if P_D(u)^(-1)=sum_r r_D(r)u^r, then r_D(r)=q^(r/2)*chi_r(U_D)"
            ),
            "scalar_action": "Sym^r(t*I_4)=t^r*I_(d_r)",
            "scalar_character": "chi_r(t*I_4)=t^r*d_r for t in {+1,-1}",
            "compact_bound": "|chi_r(U)|<=d_r for every U in USp(4)",
        },
        "locked_geometric_input": {
            "tower": "q=3^(4*k), k>=1",
            "tower_sign": "s=(-1)^k",
            "constructed_orbit_size_each": "q*(q-1)/10",
            "family_size": "q^4*(q-1)",
            "constructed_density_each": "1/(10*q^3)",
            "normalized_frobenius_classes": ["s*I_4", "-s*I_4"],
            "character_values": ["s^r*d_r", "(-s)^r*d_r"],
        },
        "moment_theorem": {
            "integer_moment_domain": "m>=1",
            "full_absolute_moment": "A_(r,m)(q)=E_D[|chi_r(U_D)|^m]",
            "constructed_absolute_subtotal": "d_r^m/(5*q^3)",
            "constructed_signed_subtotal": {
                "raw": "d_r^m*(s^(r*m)+(-s)^(r*m))/(10*q^3)",
                "r_times_m_odd": "0",
                "r_times_m_even": "d_r^m/(5*q^3)",
            },
            "full_absolute_moment_squeeze": ("d_r^m/(5*q^3)<=A_(r,m)(q)<=d_r^m"),
            "mth_root_squeeze": ("d_r*(5*q^3)^(-1/m)<=A_(r,m)(q)^(1/m)<=d_r"),
            "fixed_q_r_limit": "lim_(m->infinity) A_(r,m)(q)^(1/m)=d_r",
        },
        "phase_diagram": {
            "constructed_subtotal": "C_(r,m,q)=d_r^m/(5*q^3)",
            "exact_critical_surface": "m*log(d_r)=3*log(q)+log(5)",
            "rank_zero_exception": (
                "d_0=1, so C_(0,m,q)=1/(5*q^3) and no moment-order crossing occurs"
            ),
            "fixed_rank": {
                "continuous_crossover": ("m_*=(3*log(q)+log(5))/log(d_r), for r>=1"),
                "tower_form": ("m_*=(12*k*log(3)+log(5))/log(d_r) when q=3^(4*k)"),
                "discrete_control": (
                    "M=floor_log_(d_r)(5*q^3) is the largest integer with "
                    "C_(r,M,q)<=1; M+1 is the first with C>1"
                ),
            },
            "fixed_moment": {
                "exact_threshold": (
                    "R=max{r>=0: binom(r+3,3)^m<=5*q^3}; R+1 is supercritical"
                ),
                "asymptotic": ("R=6^(1/3)*5^(1/(3*m))*q^(1/m)+O(1)"),
                "exact_cubic_window": (
                    "if X=6^(1/3)*5^(1/(3*m))*q^(1/m), then floor(X)-3<=R<=floor(X)-1"
                ),
            },
        },
        "exact_controls": {
            "dimension_rows": dimension_rows,
            "parity_rows": parity_rows,
            "fixed_rank_crossovers": fixed_rank,
            "fixed_moment_crossovers": fixed_moment,
            "sym10_specialization": {
                "dimension": sym10,
                "absolute_subtotal": "286^m/(5*q^3)",
                "signed_subtotal": "286^m/(5*q^3) for every m>=1",
            },
        },
    }


def _read_locked_source(
    guard: ResourceGuard, deadline: Deadline
) -> tuple[dict[str, object], dict[str, object]]:
    deadline.check("before source read")
    path = SOURCE_LOCK["path"]
    if not isinstance(path, Path) or not path.is_file():
        raise RuntimeError("missing scalar-endpoint source lock")
    size = path.stat().st_size
    guard.source(size)
    raw = path.read_bytes()
    if len(raw) != size:
        raise RuntimeError("source changed while reading")
    if _lf_sha256_bytes(raw) != SOURCE_LOCK["lf_sha256"]:
        raise RuntimeError("source LF hash mismatch")
    if _git_blob_sha1(raw) != SOURCE_LOCK["git_blob"]:
        raise RuntimeError("source git-blob mismatch")
    value = json.loads(_lf_bytes(raw).decode("utf-8"))
    if not isinstance(value, dict) or value.get("schema") != SOURCE_LOCK["schema"]:
        raise RuntimeError("source schema mismatch")
    payload = dict(value)
    claimed = payload.pop("payload_sha256", None)
    if (
        claimed != SOURCE_LOCK["payload_sha256"]
        or _canonical_sha256(payload) != claimed
    ):
        raise RuntimeError("source canonical payload mismatch")
    manifest = {
        "path": _relative(path),
        "commit": SOURCE_LOCK["commit"],
        "git_blob": SOURCE_LOCK["git_blob"],
        "lf_sha256": SOURCE_LOCK["lf_sha256"],
        "schema": SOURCE_LOCK["schema"],
        "payload_sha256": SOURCE_LOCK["payload_sha256"],
        "role": SOURCE_LOCK["role"],
        "bytes": size,
    }
    return value, manifest


def _validate_source_semantics(source: dict[str, object]) -> dict[str, object]:
    exact = source.get("exact_certificate")
    if not isinstance(exact, dict):
        raise TypeError("source exact certificate missing")
    base_change = exact.get("base_change")
    orbit = exact.get("affine_orbits_and_moments")
    if not isinstance(base_change, dict) or not isinstance(orbit, dict):
        raise TypeError("source endpoint certificate malformed")
    if base_change.get("tower") != "q=3^(4*k), k>=1":
        raise RuntimeError("source tower drifted")
    if base_change.get("normalized_frobenius") != "U=(-1)^k*I_4":
        raise RuntimeError("source scalar sign drifted")
    family = orbit.get("family_and_density")
    decomposition = orbit.get("orbit_decomposition")
    twist = orbit.get("nonsquare_twist_sign_derivation")
    if not all(isinstance(item, dict) for item in (family, decomposition, twist)):
        raise RuntimeError("source orbit certificate malformed")
    if family.get("family_size") != "|H5(q)|=q^4*(q-1)":
        raise RuntimeError("source family size drifted")
    if family.get("constructed_members_each_endpoint_sign") != "q*(q-1)/10":
        raise RuntimeError("source orbit size drifted")
    if family.get("constructed_density_each_endpoint_sign") != "1/(10*q^3)":
        raise RuntimeError("source density drifted")
    if decomposition.get("number_of_square_affine_orbits_in_full_orbit") != 2:
        raise RuntimeError("source orbit count drifted")
    if "U maps to -U" not in str(twist.get("conclusion")):
        raise RuntimeError("source twist sign drifted")
    source_sym10 = base_change.get("sym10")
    if not isinstance(source_sym10, dict) or source_sym10.get("dimension") != 286:
        raise RuntimeError("source Sym10 specialization drifted")
    return {
        "validated_claims": [
            "q=3^(4*k), normalized seed Frobenius U=(-1)^k*I_4",
            "the nonsquare affine coset maps U to -U",
            "two square-affine orbits, each of size q*(q-1)/10",
            "|H5(q)|=q^4*(q-1), hence each orbit has density 1/(10*q^3)",
            "the r=10 specialization has d_10=286",
        ],
        "transitive_note": (
            "the locked scalar packet already pins its marked-stack and rare-event "
            "normalization sources; no second rare-event lock is needed here"
        ),
    }


def build_fixture() -> dict[str, object]:
    deadline = Deadline()
    guard = ResourceGuard()
    theorem = _derive_all_rank_theorem(guard)
    operations_before_source = guard.exact_operations
    source, manifest = _read_locked_source(guard, deadline)
    source_validation = _validate_source_semantics(source)
    guard.operation("source_semantics", 12)

    payload: dict[str, object] = {
        "schema": (
            "riemann.function_field."
            "genus2_scalar_endpoint_symmetric_power_phase_diagram.v1"
        ),
        "status": "EXACT_ALL_RANK_SCALAR_ENDPOINT_PHASE_DIAGRAM",
        "scope": {
            "family": "H5(q), monic squarefree quintics",
            "tower": "q=3^(4*k), k>=1",
            "symmetric_power_ranks": "every integer r>=0",
            "moment_orders": "every integer m>=1",
            "finite_fields_enumerated": 0,
            "curves_enumerated": 0,
            "group_elements_enumerated": 0,
            "representations_enumerated": 0,
            "random_samples": 0,
            "numerical_root_finding": 0,
        },
        "all_rank_theorem": theorem,
        "source_validation": source_validation,
        "source_manifest": [manifest],
        "source_order_firewall": {
            "all_rank_representation_and_phase_algebra_closed_before_source_read": True,
            "exact_operations_before_source": operations_before_source,
            "source_used_only_for_geometric_endpoint_and_orbit_premises": True,
        },
        "claim_boundaries": [
            "Every displayed endpoint contribution is the exact subtotal of two constructed orbits, not an asymptotic for the full family moment.",
            "The source proves lower bounds for endpoint densities, not a classification of all scalar-endpoint members.",
            "The fixed-rank and fixed-moment critical surfaces describe when the constructed subtotal crosses one; they are not asserted phase transitions for the remaining family.",
            "The signed subtotal can vanish by twist parity while the full signed moment remains unrestricted.",
            "The m-th-root limit is a fixed-(q,r) full absolute-moment statement from a positive endpoint atom and the compact character bound; it is not a q-asymptotic or equidistribution theorem.",
            "No motive, zero statistic, RH, GRH, or average-to-individual theorem is claimed.",
        ],
        "resource_contract": {
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "actual_exact_operations": guard.exact_operations,
            "operation_counts": dict(sorted(guard.operation_counts.items())),
            "maximum_source_bytes": MAX_SOURCE_BYTES,
            "actual_source_bytes": guard.source_bytes,
            "maximum_control_rank": MAX_CONTROL_RANK,
            "maximum_output_bytes": MAX_OUTPUT_BYTES,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": (
                "all theorem controls use exact integers and Fraction values; "
                "logs and asymptotic roots are recorded symbolically"
            ),
        },
        "replay": {
            "producer": _relative(Path(__file__).resolve()),
            "note": _relative(NOTE_PATH),
            "test": _relative(TEST_PATH),
            "write": (
                "python -B research/l-families/atlas/function_field/"
                "genus2_scalar_endpoint_symmetric_power_phase_diagram.py --write"
            ),
            "check": (
                "python -B research/l-families/atlas/function_field/"
                "genus2_scalar_endpoint_symmetric_power_phase_diagram.py --check"
            ),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if len(rendered.encode("utf-8")) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output-byte cap exceeded")
    deadline.check("after payload hash")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write canonical JSON")
    parser.add_argument("--check", action="store_true", help="check canonical JSON")
    args = parser.parse_args()
    if args.write == args.check:
        parser.error("choose exactly one of --write or --check")

    fixture = build_fixture()
    rendered = json.dumps(fixture, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.write:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {OUTPUT_PATH}")
        return
    if not OUTPUT_PATH.is_file():
        raise FileNotFoundError(f"missing canonical fixture: {OUTPUT_PATH}")
    if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
        raise RuntimeError(f"canonical fixture mismatch: {OUTPUT_PATH}")
    print(f"verified {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
