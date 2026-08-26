#!/usr/bin/env python3
"""Exact cyclic-character correlated masks for the corrected FFPS tensor Gram.

The theorem is finite Fourier algebra on sign-pair groups
H_p=F_p^*/{+/-1}.  If every H_p has a character of one common exact order
k, a union of t product-character fibres has Fourier support only on the
constant tensor line and all-primes nonconstant lines.  This gives its exact
restricted-Gram denominator and its unique positive uniform optimizer.

Only two tiny cyclic grids are inspected directly.  No finite field,
character family, conductor family, L-function, or zero set is enumerated.
The algebra closes before the frozen correlated-mask packet is read.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from fractions import Fraction
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "ffps_cyclic_character_masks.json"
NOTE_PATH = HERE / "FFPS_CYCLIC_CHARACTER_MASKS.md"
TEST_PATH = ROOT / "tests" / "test_ffps_cyclic_character_masks.py"

CORRELATED_COMMIT = "12f52a2235cdcda5c3c6b43a82bfcadbbb08f73c"
CORRELATED_PAYLOAD = "ee6c66844a15b4d6a29a6cf5dc252a5efdd5cc8b6052dcd9c27bf76dbe03269a"
CORRELATED_JSON_PATH = HERE / "ffps_correlated_mask_amplifier.json"
CORRELATED_NOTE_PATH = HERE / "FFPS_CORRELATED_MASK_AMPLIFIER.md"
CORRELATED_SCRIPT_PATH = HERE / "ffps_correlated_mask_amplifier.py"
CORRELATED_TEST_PATH = ROOT / "tests" / "test_ffps_correlated_mask_amplifier.py"

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "correlated_json": {
        "path": CORRELATED_JSON_PATH,
        "commit": CORRELATED_COMMIT,
        "git_blob": "9fa4404f6740b2f545d56b81d4122cd636528bea",
        "lf_sha256": (
            "d9d709997362f85d49156bc9669dd81c4f3b23379d03c65d4c91dbcd0ea4411b"
        ),
        "kind": "json",
        "schema": "riemann.function_field.ffps_correlated_mask_amplifier.v1",
        "payload_sha256": CORRELATED_PAYLOAD,
        "role": "arbitrary-support optimizer and Legendre checkerboard seed",
    },
    "correlated_note": {
        "path": CORRELATED_NOTE_PATH,
        "commit": CORRELATED_COMMIT,
        "git_blob": "4569c521e99e8c591f1694126605f8abee8a75f8",
        "lf_sha256": (
            "38d178c0bed51daca67bd963523cd5db3cf35367f8b9474206b9f803325e7106"
        ),
        "kind": "text",
        "role": "proof-facing restricted-Gram and source-coordinate contract",
    },
    "correlated_producer": {
        "path": CORRELATED_SCRIPT_PATH,
        "commit": CORRELATED_COMMIT,
        "git_blob": "57e11d8f6332375eba62ec2738382ca6ce4182c3",
        "lf_sha256": (
            "fc2f92f4348296e86e5cf856ed6d3aa536dba2ae1776d56b941fd9b0cf70d215"
        ),
        "kind": "text",
        "role": "bounded exact implementation of the prerequisite theorem",
    },
    "correlated_test": {
        "path": CORRELATED_TEST_PATH,
        "commit": CORRELATED_COMMIT,
        "git_blob": "a8bc217918299436f35114a3b9b7617fce6108e5",
        "lf_sha256": (
            "43801f9abdf5e3981a88f52fc61452e8fd749fb95ec42ec107546e5278454c7a"
        ),
        "kind": "text",
        "role": "optimized-mode and source-lock regression surface",
    },
}

MAX_EXACT_OPERATIONS = 20_000
MAX_MATRIX_CELLS = 2_048
MAX_ENUMERATED_COORDINATES = 128
MAX_DIRECT_TENSOR_DIMENSION = 24
MAX_CONTROL_PRIME = 101
MAX_SOURCE_FILES = 4
MAX_SOURCE_BYTES_EACH = 65_536
MAX_SOURCE_BYTES_TOTAL = 150_000
MAX_PACKET_FILE_BYTES = 65_536
MAX_WALL_SECONDS = 4.0


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    matrix_cells: int = 0
    enumerated_coordinates: int = 0
    source_files: int = 0
    source_bytes: int = 0
    operation_counts: dict[str, int] = field(default_factory=dict)

    def operation(self, label: str, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("operation increment must be a nonnegative integer")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount
        self.operation_counts[label] = self.operation_counts.get(label, 0) + amount

    def matrix(self, cells: int) -> None:
        if isinstance(cells, bool) or not isinstance(cells, int) or cells < 0:
            raise ValueError("matrix-cell increment must be a nonnegative integer")
        if self.matrix_cells + cells > MAX_MATRIX_CELLS:
            raise RuntimeError("matrix-cell cap exceeded")
        self.matrix_cells += cells

    def coordinates(self, amount: int) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("coordinate increment must be a nonnegative integer")
        if self.enumerated_coordinates + amount > MAX_ENUMERATED_COORDINATES:
            raise RuntimeError("enumerated-coordinate cap exceeded")
        self.enumerated_coordinates += amount

    def source(self, byte_count: int) -> None:
        if (
            isinstance(byte_count, bool)
            or not isinstance(byte_count, int)
            or byte_count < 0
        ):
            raise ValueError("source byte count must be a nonnegative integer")
        if byte_count > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("per-source byte cap exceeded")
        if self.source_files + 1 > MAX_SOURCE_FILES:
            raise RuntimeError("source-file cap exceeded")
        if self.source_bytes + byte_count > MAX_SOURCE_BYTES_TOTAL:
            raise RuntimeError("total source byte cap exceeded")
        self.source_files += 1
        self.source_bytes += byte_count


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


def _fraction_pair(value: int | Fraction) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _product(values: Sequence[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


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


def _validate_panel(
    primes: Sequence[int], guard: ResourceGuard | None = None
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    panel = tuple(primes)
    if not panel:
        raise ValueError("prime panel must be nonempty")
    if len(set(panel)) != len(panel):
        raise ValueError("control primes must be distinct")
    for prime in panel:
        if (
            isinstance(prime, bool)
            or not isinstance(prime, int)
            or prime > MAX_CONTROL_PRIME
            or not _is_prime(prime, guard)
            or prime % 2 == 0
        ):
            raise ValueError("control panel must contain bounded distinct odd primes")
    return panel, tuple((prime - 1) // 2 for prime in panel)


def cyclic_union_closed_form(
    primes: Sequence[int],
    order: int,
    retained_values: int,
    guard: ResourceGuard | None = None,
) -> dict[str, object]:
    """Return the exact theorem data for a union of quotient-character fibres."""

    active_guard = guard if guard is not None else ResourceGuard()
    panel, dimensions = _validate_panel(primes, active_guard)
    if isinstance(order, bool) or not isinstance(order, int) or order < 2:
        raise ValueError("character order must be an integer at least two")
    if (
        isinstance(retained_values, bool)
        or not isinstance(retained_values, int)
        or not 1 <= retained_values < order
    ):
        raise ValueError("retained quotient values must lie strictly between 0 and k")
    if any(dimension % order != 0 for dimension in dimensions):
        raise ValueError("common exact character order must divide every |H_i|")

    active_guard.operation("closed_form_products", 4 * len(panel) + 18)
    native_amplitude = _product(dimensions)
    constant_eigenvalue = _product(tuple(dimension + 1 for dimension in dimensions))
    top_eigenvalue = _product(panel)
    support_size = native_amplitude * retained_values // order
    denominator_numerator = native_amplitude * (
        retained_values * retained_values * constant_eigenvalue
        + retained_values * (order - retained_values) * top_eigenvalue
    )
    denominator, remainder = divmod(denominator_numerator, order * order)
    if remainder != 0:
        raise ArithmeticError("closed cyclic denominator was not integral")
    sharp_leverage = Fraction(native_amplitude * native_amplitude, denominator)
    full_leverage = Fraction(native_amplitude, constant_eigenvalue)
    criterion_left = retained_values * top_eigenvalue
    criterion_right = (order + retained_values) * constant_eigenvalue
    restricted_row_sum = Fraction(
        retained_values * constant_eigenvalue
        + (order - retained_values) * top_eigenvalue,
        order,
    )
    power_orders = tuple(
        order // math.gcd(order, exponent) for exponent in range(1, order)
    )
    return {
        "primes": list(panel),
        "local_dimensions": list(dimensions),
        "tensor_order": len(panel),
        "character_order": order,
        "retained_quotient_values": retained_values,
        "support_density": _fraction_pair(Fraction(retained_values, order)),
        "native_amplitude": native_amplitude,
        "support_size": support_size,
        "constant_tensor_eigenvalue_Q": constant_eigenvalue,
        "top_tensor_eigenvalue_P": top_eigenvalue,
        "restricted_gram_denominator": denominator,
        "restricted_row_sum": _fraction_pair(restricted_row_sum),
        "sharp_positive_uniform_weight": _fraction_pair(
            Fraction(order, retained_values)
        ),
        "sharp_restricted_leverage": _fraction_pair(sharp_leverage),
        "complete_tensor_leverage": _fraction_pair(full_leverage),
        "strictly_improves_complete_tensor": criterion_left > criterion_right,
        "improvement_criterion": {
            "formula": "P*t>Q*(k+t)",
            "left_P_times_t": criterion_left,
            "right_Q_times_k_plus_t": criterion_right,
        },
        "nonzero_power_orders": list(power_orders),
        "every_nonzero_power_is_nontrivial_locally": all(
            power_order > 1 for power_order in power_orders
        ),
    }


def _balanced_square_sum(total: int, bins: int) -> int:
    quotient, remainder = divmod(total, bins)
    return bins * quotient * quotient + remainder * (2 * quotient + 1)


def direct_cyclic_grid_audit(
    primes: Sequence[int],
    order: int,
    retained_residues: Sequence[int],
    guard: ResourceGuard | None = None,
) -> dict[str, object]:
    """Directly inspect one tiny cyclic-coordinate grid using integer Grams."""

    active_guard = guard if guard is not None else ResourceGuard()
    panel, dimensions = _validate_panel(primes, active_guard)
    residues = tuple(retained_residues)
    if not residues or len(set(residues)) != len(residues):
        raise ValueError("retained quotient residues must be nonempty and distinct")
    closed = cyclic_union_closed_form(panel, order, len(residues), active_guard)
    if any(
        isinstance(residue, bool)
        or not isinstance(residue, int)
        or not 0 <= residue < order
        for residue in residues
    ):
        raise ValueError("retained quotient residues must be canonical modulo k")
    dimension = _product(dimensions)
    if dimension > MAX_DIRECT_TENSOR_DIMENSION:
        raise RuntimeError("direct tensor dimension cap exceeded")
    coordinates = tuple(product(*(range(size) for size in dimensions)))
    active_guard.coordinates(len(coordinates))
    support = tuple(
        coordinate for coordinate in coordinates if sum(coordinate) % order in residues
    )
    active_guard.matrix(len(support) * len(support))
    row_sums: list[int] = []
    for left in support:
        row_sum = 0
        for right in support:
            entry = 1
            for left_index, right_index, prime in zip(left, right, panel, strict=True):
                active_guard.operation("direct_gram_factor_multiplications")
                entry *= prime - 1 if left_index == right_index else -1
            row_sum += entry
            active_guard.operation("direct_gram_additions")
        row_sums.append(row_sum)

    expected_row_sum = Fraction(*closed["restricted_row_sum"])
    if expected_row_sum.denominator != 1:
        raise ArithmeticError("restricted row sum must be integral in a realized grid")
    if any(row_sum != expected_row_sum.numerator for row_sum in row_sums):
        raise ArithmeticError("direct cyclic grid lost its constant restricted row sum")
    direct_denominator = sum(row_sums)
    if direct_denominator != closed["restricted_gram_denominator"]:
        raise ArithmeticError("direct cyclic grid denominator disagrees with theorem")
    if len(support) != closed["support_size"]:
        raise ArithmeticError("cyclic quotient fibres are not equicardinal")

    result: dict[str, object] = {
        "closed_form": closed,
        "retained_residues": list(residues),
        "enumerated_full_coordinates": len(coordinates),
        "enumerated_support_coordinates": len(support),
        "distinct_restricted_row_sums": sorted(set(row_sums)),
        "direct_denominator": direct_denominator,
        "uniform_optimizer_verified": True,
    }
    if len(panel) == 2:
        active_guard.operation("two_prime_margin_formula", 20)
        rows, columns = dimensions
        size = len(support)
        p, q = panel
        fixed_size_maximum = (
            p * q * size
            + size * size
            - p * _balanced_square_sum(size, rows)
            - q * _balanced_square_sum(size, columns)
        )
        row_degrees = [0] * rows
        column_degrees = [0] * columns
        for row, column in support:
            row_degrees[row] += 1
            column_degrees[column] += 1
        result["two_prime_fixed_size_control"] = {
            "row_degrees": row_degrees,
            "column_degrees": column_degrees,
            "balanced_margin_maximum": fixed_size_maximum,
            "attains_global_fixed_size_maximum": (
                direct_denominator == fixed_size_maximum
            ),
        }
    return result


def fixed_d_limit(
    dimension_count: int, guard: ResourceGuard | None = None
) -> dict[str, object]:
    """Return the exact limiting density frontier for one fixed tensor order."""

    if (
        isinstance(dimension_count, bool)
        or not isinstance(dimension_count, int)
        or dimension_count < 2
        or dimension_count > 12
    ):
        raise ValueError("fixed tensor order must lie between 2 and 12")
    if guard is not None:
        guard.operation("fixed_d_closed_form", 18)
    c = 2**dimension_count
    optimal_density = Fraction(c, 2 * (c - 1))
    optimal_leverage = Fraction(4 * (c - 1), c * c)
    constructive_order = c - 1
    constructive_values = c // 2
    constructed_leverage = Fraction(
        constructive_order * constructive_order,
        constructive_values * constructive_values
        + constructive_values * (constructive_order - constructive_values) * c,
    )
    legendre_leverage = Fraction(4, c + 1)
    legendre_ratio = legendre_leverage / optimal_leverage
    if constructed_leverage != optimal_leverage:
        raise ArithmeticError("cyclic construction missed the fixed-d optimum")
    if legendre_ratio != Fraction(4**dimension_count, 4**dimension_count - 1):
        raise ArithmeticError("Legendre near-optimality ratio changed")
    return {
        "tensor_order_d": dimension_count,
        "large_local_dimension_top_eigenvalue": c,
        "continuous_optimal_density": _fraction_pair(optimal_density),
        "continuous_optimal_leverage": _fraction_pair(optimal_leverage),
        "constructive_character_order": constructive_order,
        "constructive_retained_values": constructive_values,
        "constructive_density": _fraction_pair(
            Fraction(constructive_values, constructive_order)
        ),
        "constructive_limiting_leverage": _fraction_pair(constructed_leverage),
        "legendre_limiting_leverage": _fraction_pair(legendre_leverage),
        "legendre_to_optimum_ratio": _fraction_pair(legendre_ratio),
    }


def _build_exact_mathematics(
    guard: ResourceGuard, deadline: Deadline
) -> dict[str, object]:
    ternary_kernel = direct_cyclic_grid_audit((7, 13), 3, (0,), guard)
    deadline.check("after ternary kernel")
    ternary_two_cosets = direct_cyclic_grid_audit((7, 13), 3, (0, 1), guard)
    deadline.check("after ternary union")
    legendre = cyclic_union_closed_form((5, 13), 2, 1, guard)
    composite = cyclic_union_closed_form((17, 41), 4, 2, guard)
    fixed_d = [fixed_d_limit(dimension_count, guard) for dimension_count in range(2, 7)]

    if legendre["sharp_restricted_leverage"] != [24, 43]:
        raise ArithmeticError("Legendre seed no longer matches the frozen packet")
    if ternary_kernel["closed_form"]["sharp_restricted_leverage"] != [27, 35]:
        raise ArithmeticError("ternary kernel control changed")
    if ternary_two_cosets["closed_form"]["sharp_restricted_leverage"] != [27, 49]:
        raise ArithmeticError("ternary two-coset control changed")
    if composite["nonzero_power_orders"] != [4, 2, 4]:
        raise ArithmeticError("composite-order power audit changed")
    if composite["sharp_restricted_leverage"] != [320, 443]:
        raise ArithmeticError("composite-order control changed")

    return {
        "cyclic_spectral_theorem": {
            "groups": "H_i=F_(p_i)^*/{+/-1}, |H_i|=m_i=(p_i-1)/2",
            "hypothesis": (
                "each psi_i:H_i->mu_k has the same exact order k; equivalently "
                "k divides every m_i"
            ),
            "quotient_map": "Phi(h_1,...,h_d)=product_i psi_i(h_i)",
            "fourier_basis": "w_r=Phi^r=tensor_i psi_i^r, 0<=r<k",
            "orthogonality": "<w_r,w_s>=N*delta_(r,s)",
            "eigenvalues": "G*w_0=Q*w_0 and G*w_r=P*w_r for every 1<=r<k",
            "composite_order_reason": (
                "exact order k implies psi_i^r is nontrivial for every 0<r<k; "
                "gcd(r,k)>1 can lower its order but cannot make it constant"
            ),
        },
        "arbitrary_coset_union_theorem": {
            "support": "A=Phi^(-1)(S), S subset mu_k, |S|=t, rho=t/k",
            "indicator_action": "G*1_A=P*1_A+(Q-P)*rho*1",
            "denominator": "E_A=N*(t^2*Q+t*(k-t)*P)/k^2",
            "unique_optimizer": "alpha_opt=(k/t)*1_A, positive and uniform",
            "sharp_leverage": "L_(k,t)=k^2*N/(t^2*Q+t*(k-t)*P)",
            "normalized_form": "L=1/(A0*rho^2+B0*rho*(1-rho)), A0=Q/N, B0=P/N",
            "full_tensor_improvement": "P*t>Q*(k+t)",
            "fixed_density_invariance": (
                "the exact leverage depends on k and t only through rho=t/k"
            ),
        },
        "kernel_corollary": {
            "support": "Phi=1 (t=1)",
            "denominator": "E=N*(Q+(k-1)*P)/k^2",
            "optimizer": "alpha_opt=k",
            "leverage": "k^2*N/(Q+(k-1)*P)",
            "improvement": "P>(k+1)*Q",
            "necessary_fixed_d_condition": "k+1<2^d",
            "order_comparison": (
                "on one common eligible panel, the kernel leverage is strictly "
                "increasing for real k>=2; the smallest available order is best"
            ),
        },
        "finite_dimension_density_frontier": {
            "when_P_exceeds_2Q": {
                "continuous_optimal_density": "rho*=P/(2*(P-Q))",
                "continuous_optimal_leverage": "L*=4*N*(P-Q)/P^2",
            },
            "when_P_at_most_2Q": (
                "no proper cyclic quotient-union mask improves the complete tensor"
            ),
            "improvement_interval": "rho>Q/(P-Q) and rho<1",
        },
        "fixed_d_large_local_dimension_frontier": {
            "limits": "Q/N->1 and P/N->2^d",
            "optimal_density": "2^(d-1)/(2^d-1)",
            "optimal_leverage": "(2^d-1)/4^(d-1)",
            "explicit_construction": (
                "take k=2^d-1 and retain t=2^(d-1) quotient values; for fixed d, "
                "primes p_i congruent to 1 mod 2k support the characters"
            ),
            "legendre_near_optimality": (
                "the k=2,t=1 limiting leverage exceeds the optimum by exactly "
                "4^d/(4^d-1)"
            ),
            "rows": fixed_d,
        },
        "prime_prefix_asymptotics": {
            "scope": "fixed k,t; primes p<=x with p congruent to 1 mod 2k",
            "exact_leading_reduction": (
                "L_(k,t)~[k^2/(t*(k-t))]*2^(-d)*product_p(1-1/p)"
            ),
            "mertens_progression_scale": ("Theta_(k,t)(2^(-d)*(log x)^(-1/phi(2k)))"),
            "conductor": "M=product_p p, log M~x/phi(2k), d~x/(phi(2k)*log x)",
            "conductor_scale": ("exp(-(log 2+o(1))*log(M)/log(log(M)))"),
            "nonuniformity_firewall": (
                "fixed-modulus PNT/Mertens in progressions gives no uniform theorem "
                "when k grows with x, d, or M"
            ),
            "choice_of_k": (
                "all fixed k share the leading conductor exponent; k=2 minimizes "
                "single-kernel leverage on any common panel and is canonical, but "
                "different progression constants forbid an exact finite-M ordering"
            ),
        },
        "product_mask_comparison": {
            "cartesian_support": (
                "every proper Cartesian product restriction has leverage strictly "
                "larger than the complete tensor"
            ),
            "cyclic_consequence": (
                "whenever P*t>Q*(k+t), the cyclic mask beats the complete tensor "
                "and therefore every proper product mask"
            ),
            "two_prime_strength": (
                "cyclic quotient unions have balanced row and column margins and "
                "attain the exact global fixed-size denominator maximum"
            ),
        },
        "finite_controls": {
            "legendre_5_13": legendre,
            "ternary_7_13_kernel": ternary_kernel,
            "ternary_7_13_two_cosets": ternary_two_cosets,
            "composite_order_17_41_half_union": composite,
        },
    }


def _read_locked_sources(
    guard: ResourceGuard, deadline: Deadline
) -> tuple[dict[str, object], list[dict[str, object]]]:
    parsed: dict[str, object] = {}
    manifest: list[dict[str, object]] = []
    for name, lock in SOURCE_LOCKS.items():
        path = lock["path"]
        if not isinstance(path, Path) or not path.is_file():
            raise FileNotFoundError(f"missing frozen source: {name}")
        raw = path.read_bytes()
        guard.source(len(raw))
        if _lf_sha256(raw) != lock["lf_sha256"]:
            raise RuntimeError(f"LF-SHA256 mismatch for frozen source: {name}")
        if _git_blob_sha1(raw) != lock["git_blob"]:
            raise RuntimeError(f"git blob mismatch for frozen source: {name}")
        kind = lock["kind"]
        if kind == "json":
            value = json.loads(raw.decode("utf-8"))
            if value.get("schema") != lock["schema"]:
                raise RuntimeError(f"schema mismatch for frozen source: {name}")
            if value.get("payload_sha256") != lock["payload_sha256"]:
                raise RuntimeError(f"payload mismatch for frozen source: {name}")
            parsed[name] = value
        elif kind == "text":
            parsed[name] = _lf_bytes(raw).decode("utf-8")
        else:
            raise RuntimeError(f"unknown frozen source kind: {kind}")
        manifest.append(
            {
                "name": name,
                "path": _relative(path),
                "commit": lock["commit"],
                "git_blob": lock["git_blob"],
                "lf_sha256": lock["lf_sha256"],
                "bytes_read": len(raw),
                "role": lock["role"],
            }
        )
        deadline.check(f"after source {name}")
    if guard.source_files != len(SOURCE_LOCKS):
        raise RuntimeError("not every frozen correlated-packet file was consumed")
    return parsed, manifest


def _validate_source_semantics(sources: Mapping[str, object]) -> dict[str, object]:
    correlated = sources.get("correlated_json")
    if not isinstance(correlated, Mapping):
        raise TypeError("frozen correlated JSON is malformed")
    if (
        correlated.get("status")
        != "EXACT_FORMAL_CORRELATED_RESTRICTED_GRAM_OPTIMIZATION"
    ):
        raise RuntimeError("correlated restricted-Gram theorem status changed")
    exact = correlated.get("exact_mathematics")
    if not isinstance(exact, Mapping):
        raise TypeError("frozen correlated exact mathematics is missing")
    checkerboard = exact.get("global_legendre_checkerboard")
    optimizer = exact.get("restricted_support_optimizer")
    if not isinstance(checkerboard, Mapping) or not isinstance(optimizer, Mapping):
        raise TypeError("Legendre seed or arbitrary-support optimizer is missing")
    if checkerboard.get("sharp_leverage") != (
        "4/(product_i((m_i+1)/m_i)+product_i(p_i/m_i))"
    ):
        raise RuntimeError("Legendre checkerboard seed formula changed")
    if optimizer.get("sharp_energy") != "N^2/(1_A^*G_A*1_A)":
        raise RuntimeError("frozen arbitrary-support optimizer changed")
    scope = correlated.get("scope")
    firewalls = correlated.get("firewalls")
    if not isinstance(scope, Mapping) or not isinstance(firewalls, list):
        raise TypeError("frozen correlated scope/firewalls are malformed")
    if scope.get("characters_enumerated") != 0:
        raise RuntimeError("frozen packet unexpectedly enumerated characters")
    if not any("varying owners or conductors" in str(item) for item in firewalls):
        raise RuntimeError("fixed-source versus varying-owner firewall disappeared")
    return {
        "dependency_commit": CORRELATED_COMMIT,
        "dependency_payload": CORRELATED_PAYLOAD,
        "legendre_case_recovered": True,
        "relationship": (
            "the frozen packet proves the general restricted optimizer and the "
            "quadratic checkerboard; this packet supplies the exact cyclic quotient "
            "spectrum and arbitrary union of quotient fibres"
        ),
    }


def _packet_lf_sha256(path: Path) -> str:
    if path.stat().st_size > MAX_PACKET_FILE_BYTES:
        raise RuntimeError(f"packet file exceeds byte cap: {path.name}")
    return _lf_sha256(path.read_bytes())


def build_fixture() -> dict[str, object]:
    deadline = Deadline()
    guard = ResourceGuard()
    exact_mathematics = _build_exact_mathematics(guard, deadline)
    operations_before_sources = guard.exact_operations
    matrices_before_sources = guard.matrix_cells
    coordinates_before_sources = guard.enumerated_coordinates
    sources, source_manifest = _read_locked_sources(guard, deadline)
    source_relationship = _validate_source_semantics(sources)
    if guard.exact_operations != operations_before_sources:
        raise RuntimeError("source reads entered the exact-operation ledger")
    if guard.matrix_cells != matrices_before_sources:
        raise RuntimeError("source reads entered the matrix-cell ledger")
    if guard.enumerated_coordinates != coordinates_before_sources:
        raise RuntimeError("source reads entered the coordinate ledger")

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.ffps_cyclic_character_masks.v1",
        "status": "EXACT_CYCLIC_QUOTIENT_RESTRICTED_GRAM_THEOREM",
        "scope": {
            "formal_gram": "G=tensor_i(p_i*I_(m_i)-J_(m_i)), m_i=(p_i-1)/2",
            "groups": "H_i=F_(p_i)^*/{+/-1}",
            "characters": "one chosen exact-order-k character on every H_i",
            "supports": "arbitrary unions of values of product_i psi_i",
            "finite_fields_enumerated": 0,
            "characters_enumerated": 0,
            "conductors_enumerated": 0,
            "l_functions_enumerated": 0,
            "random_samples": 0,
        },
        "exact_mathematics": exact_mathematics,
        "source_relationship": source_relationship,
        "source_manifest": source_manifest,
        "firewalls": [
            (
                "The quotient characters exist exactly when k divides every "
                "m_i. Higher-order choices and their common mu_k alignment are "
                "noncanonical; the quadratic Legendre choice is canonical."
            ),
            (
                "Common exact order is essential for the two-eigenvalue formula. "
                "If local orders merely divide k, nonzero Fourier powers can become "
                "constant in some factors and create lower tensor modes."
            ),
            (
                "The condition product_i psi_i=1, and any union of its value fibres, "
                "is a legitimate fixed CRT subset of the frozen unordered {c,-c} "
                "coordinates. This is not a varying-owner/conductor FFPS theorem."
            ),
            (
                "The fixed-d construction keeps d and k fixed while local primes grow. "
                "It is not uniform when d or k grows."
            ),
            (
                "Prime-prefix asymptotics import PNT and Mertens in one fixed "
                "arithmetic progression; they do not license a growing modulus "
                "when k grows with x, d, or M."
            ),
            (
                "No WCADD, WCKUM, BPOE, SOCM, mixed/double/principal FFPS moment, "
                "or conductor-uniform family estimate is proved."
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
            "matrix_cells_before_sources": matrices_before_sources,
            "maximum_enumerated_coordinates": MAX_ENUMERATED_COORDINATES,
            "actual_enumerated_coordinates": guard.enumerated_coordinates,
            "coordinates_before_sources": coordinates_before_sources,
            "maximum_direct_tensor_dimension": MAX_DIRECT_TENSOR_DIMENSION,
            "maximum_control_prime": MAX_CONTROL_PRIME,
            "maximum_source_files": MAX_SOURCE_FILES,
            "actual_source_files": guard.source_files,
            "maximum_source_bytes_each": MAX_SOURCE_BYTES_EACH,
            "maximum_source_bytes_total": MAX_SOURCE_BYTES_TOTAL,
            "actual_source_bytes": guard.source_bytes,
            "maximum_packet_file_bytes": MAX_PACKET_FILE_BYTES,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact integers and Fraction only; no floating point",
        },
    }
    deadline.check("after fixture assembly")
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
        raise RuntimeError("rendered fixture exceeds the packet-file byte cap")
    if arguments.check:
        if not OUTPUT_PATH.is_file():
            raise FileNotFoundError(f"missing fixture: {OUTPUT_PATH}")
        if OUTPUT_PATH.stat().st_size > MAX_PACKET_FILE_BYTES:
            raise RuntimeError("existing fixture exceeds the packet-file byte cap")
        if OUTPUT_PATH.read_bytes() != rendered:
            raise RuntimeError(f"fixture is stale: {OUTPUT_PATH}")
        print("PASS_FFPS_CYCLIC_CHARACTER_MASKS")
        return 0
    OUTPUT_PATH.write_bytes(rendered)
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
