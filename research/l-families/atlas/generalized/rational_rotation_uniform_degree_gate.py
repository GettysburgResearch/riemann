"""Exact replay for the rational-rotation uniform local-degree gate.

The companion note proves the analytic sampled-mode persistence theorem.  This
producer checks the exact first-absolute-power full spectrum, integer
polynomial uniform bounds and sharpness, alias controls, source objects, and
scope firewalls without floating point.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from collections.abc import Mapping, Sequence
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
PACKET_ROOT = SCRIPT_PATH.parent
REPO_ROOT = SCRIPT_PATH.parents[4]
OUTPUT_PATH = PACKET_ROOT / "rational_rotation_uniform_degree_gate.json"
SOURCES_PATH = PACKET_ROOT / "rational_rotation_uniform_degree_gate.sources.json"
NOTE_PATH = PACKET_ROOT / "RATIONAL_ROTATION_UNIFORM_DEGREE_GATE.md"
TEST_PATH = REPO_ROOT / "tests" / "test_rational_rotation_uniform_degree_gate.py"
PARENT_PATH = PACKET_ROOT / "rational_rotation_branch_census.py"

EXPECTED_BASE_COMMIT = "d8905affa82c0523fcf0ebac5107f4d257ea1284"
EXPECTED_SOURCES_SHA256_LF = (
    "5d69ab76861bf4a6ebfad8856247a2e4c799eb87372b25f2cf3b191b637cfe97"
)
EXPECTED_SOURCE_OBJECTS = {
    "research/l-families/atlas/generalized/RATIONAL_ROTATION_BRANCH_CENSUS.md": (
        "650933e62d3b467ffc3be0f253c9ac65a0bd2e48"
    ),
    "research/l-families/atlas/generalized/rational_rotation_branch_census.py": (
        "01254baba2032efa5d90e59f267ffea971803455"
    ),
    "research/l-families/atlas/generalized/rational_rotation_branch_census.json": (
        "31e6051f6efcf573ab346eec34a102f488562261"
    ),
    "research/l-families/atlas/generalized/IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md": (
        "8f27df80a4983b4d393ee3a2477a744afaeb1d3a"
    ),
    "research/l-families/atlas/generalized/IRRATIONAL_ROTATION_PRINCIPAL_COMPLEX_POWER_RATIONALITY.md": (
        "e6308d8e4b9122598f7857b34967f058a64a4f59"
    ),
    "research/l-families/atlas/generalized/irrational_rotation_principal_complex_power_rationality.sources.json": (
        "f946f4d12c01500958643d3f3984fe8dcf93f150"
    ),
}
DEFAULT_MAX_B = 18
MAX_ALLOWED_B = 32
DEFAULT_MAX_K = 14
MAX_ALLOWED_K = 24
DEFAULT_RESOURCE_CAP_EXCLUSIVE = 500_000


def _load_parent_packet():
    spec = importlib.util.spec_from_file_location(
        "glo764_rational_rotation_uniform_parent", PARENT_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load rational-rotation parent packet")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARENT = _load_parent_packet()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _canonical_sha256(value: object) -> str:
    return PARENT._canonical_sha256(value)


def _git_blob_at(commit: str, path: str) -> str:
    return PARENT._git_blob_at(commit, path)


def _validate_integer(value: int, name: str, lower: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < lower:
        raise ValueError(f"{name} must be at least {lower}")


def first_absolute_power_mode_certificate(b: int, k: int) -> dict[str, object]:
    """Certify that mode k of sin(pi*n/b), 0<=n<b, is nonzero."""
    _validate_integer(b, "b", 2)
    _validate_integer(k, "k", 0)
    if k >= b:
        raise ValueError("k must be smaller than b")

    modulus = 2 * b
    forward_ratio_exponent = (1 - 2 * k) % modulus
    backward_ratio_exponent = (-1 - 2 * k) % modulus
    ratios_have_bth_power_minus_one = (
        forward_ratio_exponent % 2 == 1 and backward_ratio_exponent % 2 == 1
    )
    denominators_nonzero = forward_ratio_exponent != 0 and backward_ratio_exponent != 0
    numerator_nonzero = forward_ratio_exponent != backward_ratio_exponent
    if not (
        ratios_have_bth_power_minus_one and denominators_nonzero and numerator_nonzero
    ):
        raise ArithmeticError("first-power DFT nonvanishing certificate failed")
    return {
        "b": b,
        "mode_k": k,
        "root_model": "eta=exp(pi*i/b), omega=eta^2",
        "forward_geometric_ratio_eta_exponent_mod_2b": forward_ratio_exponent,
        "backward_geometric_ratio_eta_exponent_mod_2b": backward_ratio_exponent,
        "both_ratios_have_bth_power": "-1",
        "both_geometric_denominators_nonzero": True,
        "difference_numerator_nonzero": True,
        "dft_mode_nonzero": True,
    }


def first_absolute_power_spectrum(b: int) -> dict[str, object]:
    _validate_integer(b, "b", 2)
    rows = [first_absolute_power_mode_certificate(b, k) for k in range(b)]
    if not all(row["dft_mode_nonzero"] for row in rows):
        raise ArithmeticError("not every first-power mode survived")
    return {
        "b": b,
        "angle": "theta=pi/b",
        "nonzero_mode_count": b,
        "minimal_recurrence_order": b,
        "mode_certificate_digest": _canonical_sha256(rows),
    }


def alias_support(coefficients: Mapping[int, int], modulus: int) -> dict[int, int]:
    """Group an exact finite Fourier spectrum modulo a sampling modulus."""
    _validate_integer(modulus, "modulus", 1)
    grouped: dict[int, int] = {}
    for frequency, coefficient in coefficients.items():
        if isinstance(frequency, bool) or not isinstance(frequency, int):
            raise TypeError("frequencies must be integers")
        if isinstance(coefficient, bool) or not isinstance(coefficient, int):
            raise TypeError("coefficients must be integers")
        residue = frequency % modulus
        grouped[residue] = grouped.get(residue, 0) + coefficient
    return {
        residue: coefficient
        for residue, coefficient in sorted(grouped.items())
        if coefficient
    }


def scaled_sine_power_modes(k: int) -> dict[int, int]:
    """Return (2i)^k times the Fourier coefficients of sin(t)^k."""
    _validate_integer(k, "k", 0)
    return {k - 2 * j: (-1 if j % 2 else 1) * math.comb(k, j) for j in range(k + 1)}


def alias_record(coefficients: Mapping[int, int], modulus: int) -> list[dict[str, int]]:
    return [
        {"residue_modulus": residue, "coefficient": coefficient}
        for residue, coefficient in alias_support(coefficients, modulus).items()
    ]


def integer_uniform_census(max_b: int, max_k: int) -> dict[str, object]:
    _validate_integer(max_b, "max_b", 2)
    _validate_integer(max_k, "max_k", 1)
    if max_b > MAX_ALLOWED_B:
        raise ValueError(f"max_b exceeds allowed maximum {MAX_ALLOWED_B}")
    if max_k > MAX_ALLOWED_K:
        raise ValueError(f"max_k exceeds allowed maximum {MAX_ALLOWED_K}")

    records: list[dict[str, int]] = []
    sharp_records: list[dict[str, int]] = []
    order_histogram: dict[str, int] = {}
    for b in range(2, max_b + 1):
        for a in range(1, b):
            if math.gcd(a, b) != 1:
                continue
            for k in range(1, max_k + 1):
                spectrum = PARENT.integer_power_spectrum(a, b, k)
                order = spectrum["minimal_recurrence_order"]
                if not isinstance(order, int):
                    raise TypeError("parent spectrum order must be an integer")
                if order > k + 1:
                    raise ArithmeticError("integer power exceeded k+1 modes")
                row = {"a": a, "b": b, "k": k, "order": order}
                records.append(row)
                order_histogram[str(order)] = order_histogram.get(str(order), 0) + 1
                if b > k:
                    if order != k + 1:
                        raise ArithmeticError(
                            "collision-free chamber did not attain k+1 modes"
                        )
                    sharp_records.append(row)

    return {
        "maximum_b": max_b,
        "maximum_k": max_k,
        "row_count": len(records),
        "rows_digest": _canonical_sha256(records),
        "order_histogram": order_histogram,
        "maximum_order_minus_k_plus_1": max(
            row["order"] - (row["k"] + 1) for row in records
        ),
        "collision_free_sharp_row_count": len(sharp_records),
        "collision_free_sharp_rows_digest": _canonical_sha256(sharp_records),
        "signed_integer_uniform_bound": "order<=k+1",
        "absolute_even_uniform_bound": "order<=2m+1 at k=2m",
    }


def verify_sources_manifest() -> dict[str, object]:
    actual_hash = _lf_sha256(SOURCES_PATH)
    if actual_hash != EXPECTED_SOURCES_SHA256_LF:
        raise RuntimeError("uniform-degree sources manifest hash mismatch")
    manifest = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    if manifest.get("base_commit") != EXPECTED_BASE_COMMIT:
        raise RuntimeError("uniform-degree source base commit mismatch")
    sources = manifest.get("sources")
    if not isinstance(sources, list):
        raise TypeError("uniform-degree sources must be a list")
    source_index = {row.get("path"): row for row in sources}
    if len(source_index) != len(sources) or set(source_index) != set(
        EXPECTED_SOURCE_OBJECTS
    ):
        raise RuntimeError("uniform-degree source path set mismatch")

    verified: list[dict[str, object]] = []
    for path, expected_blob in EXPECTED_SOURCE_OBJECTS.items():
        row = source_index[path]
        if row.get("git_blob") != expected_blob:
            raise RuntimeError(f"manifest Git blob mismatch for {path}")
        actual_blob = _git_blob_at(EXPECTED_BASE_COMMIT, path)
        if actual_blob != expected_blob:
            raise RuntimeError(f"authenticated Git blob mismatch for {path}")
        if _lf_sha256(REPO_ROOT / path) != row.get("file_sha256_lf_normalized"):
            raise RuntimeError(f"working-tree source hash mismatch for {path}")
        verified.append(dict(row))
    references = manifest.get("external_references")
    if not isinstance(references, list) or len(references) != 2:
        raise RuntimeError("expected two literature boundary records")
    return {
        "manifest": _relative(SOURCES_PATH),
        "file_sha256_lf_normalized": actual_hash,
        "base_commit": EXPECTED_BASE_COMMIT,
        "verified_sources": verified,
        "external_references": references,
        "scope_firewall": manifest["scope_firewall"],
    }


def _analytic_proof_obligations() -> dict[str, object]:
    return {
        "periodic_minimal_order": (
            "number of nonzero discrete Fourier modes, by distinct simple poles"
        ),
        "fixed_mode_grid_limit": (
            "normalized discrete coefficient is a Riemann sum converging to "
            "the continuous Fourier coefficient"
        ),
        "arbitrary_finite_mode_retention": (
            "choose finitely many nonzero continuous modes, then take q large "
            "enough for distinct residues and nonzero approximants"
        ),
        "absolute_finite_spectrum_iff": "lambda is a positive even integer",
        "fixed_branch_finite_spectrum_iff": "lambda is a positive integer",
        "finite_replay_is_not_universal_proof": True,
    }


def build_fixture(
    *,
    max_b: int = DEFAULT_MAX_B,
    max_k: int = DEFAULT_MAX_K,
    resource_cap: int = DEFAULT_RESOURCE_CAP_EXCLUSIVE,
) -> dict[str, object]:
    _validate_integer(max_b, "max_b", 2)
    _validate_integer(max_k, "max_k", 1)
    _validate_integer(resource_cap, "resource_cap", 1)
    if max_b > MAX_ALLOWED_B:
        raise ValueError(f"max_b exceeds allowed maximum {MAX_ALLOWED_B}")
    if max_k > MAX_ALLOWED_K:
        raise ValueError(f"max_k exceeds allowed maximum {MAX_ALLOWED_K}")

    reduced_angles = sum(
        1 for b in range(2, max_b + 1) for a in range(1, b) if math.gcd(a, b) == 1
    )
    work_units = sum(range(2, max_b + 1)) + reduced_angles * max_k
    if work_units >= resource_cap:
        raise RuntimeError(
            f"declared work {work_units} reaches exclusive cap {resource_cap}"
        )

    source_lock = verify_sources_manifest()
    first_power_rows = [first_absolute_power_spectrum(b) for b in range(2, max_b + 1)]
    integer_census = integer_uniform_census(max_b, max_k)
    fixture: dict[str, object] = {
        "schema": "riemann.atlas.generalized.rational_rotation_uniform_degree_gate.v1",
        "programme_issue": {
            "number": 764,
            "url": "https://github.com/gfreund123/riemann/issues/764",
        },
        "claims": {
            "GLO764.PERIODIC_DFT_MINIMAL_ORDER": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "arbitrary complex periodic sequence",
            },
            "GLO764.SAMPLED_MODE_PERSISTENCE": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "continuous complex periodic function sampled on full grids",
            },
            "GLO764.ABSOLUTE_UNIFORM_DEGREE_GATE": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "classification": (
                    "for Re(lambda)>0, uniformly bounded over rational rotations "
                    "iff lambda is a positive even integer"
                ),
                "sharp_integer_order": "2m+1 at lambda=2m",
            },
            "GLO764.FIXED_BRANCH_UNIFORM_DEGREE_GATE": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "classification": (
                    "for fixed J and Re(lambda)>0, uniformly bounded over "
                    "rational rotations iff lambda is a positive integer"
                ),
                "sharp_integer_order": "k+1 at lambda=k",
            },
            "GLO764.ABSOLUTE_FIRST_POWER_FULL_SPECTRUM": {
                "status": "PROVED_AND_EXACTLY_REPLAYED",
                "classification": "d_abs(1;1,b)=b for every b>=2",
            },
        },
        "source_lock": source_lock,
        "first_absolute_power_full_spectrum": {
            "row_count": len(first_power_rows),
            "all_orders_equal_b": all(
                row["minimal_recurrence_order"] == row["b"] for row in first_power_rows
            ),
            "rows_digest": _canonical_sha256(first_power_rows),
            "representative_rows": [
                first_power_rows[0],
                first_power_rows[min(3, len(first_power_rows) - 1)],
                first_power_rows[-1],
            ],
        },
        "integer_polynomial_controls": integer_census,
        "exact_alias_controls": {
            "no_collision": alias_record({-2: 1, 0: -2, 2: 1}, 7),
            "collision_with_cancellation": alias_record({0: 1, 3: -1}, 3),
            "sine_power_k_6_mod_5": alias_record(scaled_sine_power_modes(6), 5),
        },
        "analytic_proof_obligations": _analytic_proof_obligations(),
        "uniform_state_space_boundary": {
            "integer_signed_parent": "Sym^k, rank k+1",
            "integer_absolute_parent": "Sym^(2m), rank 2m+1",
            "noninteger_rational_orbits": (
                "each is finite state, but no dimension bound uniform in b"
            ),
            "obstruction_scope": "finite-dimensional constant state-space only",
        },
        "scope_firewall": {
            "one_unramified_determinant_one_local_recurrence": True,
            "tempered_rational_rotations_only": True,
            "fixed_exponent_with_strictly_positive_real_part": True,
            "lambda_zero_convention_family_excluded": True,
            "finite_dimensional_constant_state_space_obstruction_only": True,
            "no_quantitative_degree_growth_rate": True,
            "no_prime_indexed_global_family_constructed": True,
            "no_ramified_factors_completion_or_functional_equation": True,
            "no_automorphy_motive_or_infinite_dimensional_no_go": True,
            "no_RH_GRH_or_zero_distribution_consequence": True,
            "external_novelty_unreviewed": True,
        },
        "resource_contract": {
            "arithmetic_class": "EXACT_INTEGER_ROOT_EXPONENT",
            "exact_method": (
                "integer root exponents modulo 2b, grouped binomial sums, "
                "finite Fourier aliasing, and canonical JSON hashing"
            ),
            "maximum_b": max_b,
            "maximum_allowed_b": MAX_ALLOWED_B,
            "maximum_k": max_k,
            "maximum_allowed_k": MAX_ALLOWED_K,
            "declared_work_units": work_units,
            "work_unit_cap_exclusive": resource_cap,
            "float_operations": 0,
            "random_samples": 0,
            "external_symbolic_engine": False,
        },
        "producer": {
            "script": _relative(SCRIPT_PATH),
            "script_sha256_lf_normalized": _lf_sha256(SCRIPT_PATH),
            "note": _relative(NOTE_PATH),
            "note_sha256_lf_normalized": _lf_sha256(NOTE_PATH),
            "test": _relative(TEST_PATH),
            "test_sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _serialized_fixture() -> str:
    return json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail unless the stored JSON equals a fresh exact build",
    )
    args = parser.parse_args(argv)
    serialized = _serialized_fixture()
    if args.check:
        if (
            not OUTPUT_PATH.exists()
            or OUTPUT_PATH.read_text(encoding="utf-8") != serialized
        ):
            raise SystemExit("stored uniform-degree fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
