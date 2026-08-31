"""Exact replay for the rational-rotation zero and branch census.

The proof is in the companion note.  This dependency-free producer checks the
finite-orbit skeleton, fixed-branch period table, zero-exponent Fourier
support, grouped integer-power spectra, exact source objects, and L0--L9
firewalls without evaluating a trigonometric function numerically.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from collections.abc import Sequence
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
PACKET_ROOT = SCRIPT_PATH.parent
REPO_ROOT = SCRIPT_PATH.parents[4]
OUTPUT_PATH = PACKET_ROOT / "rational_rotation_branch_census.json"
SOURCES_PATH = PACKET_ROOT / "rational_rotation_branch_census.sources.json"
NOTE_PATH = PACKET_ROOT / "RATIONAL_ROTATION_BRANCH_CENSUS.md"
TEST_PATH = REPO_ROOT / "tests" / "test_rational_rotation_branch_census.py"
PARENT_PATH = PACKET_ROOT / "irrational_rotation_absolute_power_rationality.py"

EXPECTED_BASE_COMMIT = "cdaa8bcb863b0aa30044fc599efdf4ac549a5c38"
EXPECTED_SOURCES_SHA256_LF = (
    "c1d9ed9862fe572169ead10a9c909df63b4ddd0a5ae209fa1e9ab3ab7acaed0b"
)
EXPECTED_SOURCE_OBJECTS = {
    "research/l-families/atlas/generalized/IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md": (
        "8f27df80a4983b4d393ee3a2477a744afaeb1d3a"
    ),
    "research/l-families/atlas/generalized/irrational_rotation_absolute_power_rationality.py": (
        "aee0fd3ed26dbffb036440390801278c6426ea08"
    ),
    "research/l-families/atlas/generalized/irrational_rotation_absolute_power_rationality.json": (
        "d94b75287493134bdc0a9ca53dda1f81b61912cf"
    ),
    "research/l-families/atlas/generalized/irrational_rotation_absolute_power_rationality.sources.json": (
        "3adf8f211fee7bd51e811520b31785af38ccd7c0"
    ),
}
DEFAULT_MAX_B = 12
MAX_ALLOWED_B = 20
DEFAULT_MAX_K = 16
MAX_ALLOWED_K = 30
DEFAULT_RESOURCE_CAP_EXCLUSIVE = 200_000


def _load_parent_packet():
    spec = importlib.util.spec_from_file_location(
        "glo764_irrational_rotation_parent", PARENT_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load adjacent irrational-rotation packet")
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


def _validate_rotation(a: int, b: int) -> None:
    if isinstance(a, bool) or not isinstance(a, int):
        raise TypeError("a must be an integer")
    if isinstance(b, bool) or not isinstance(b, int):
        raise TypeError("b must be an integer")
    if b < 2:
        raise ValueError("b must be at least 2")
    if not 1 <= a < b:
        raise ValueError("a must satisfy 1 <= a < b")
    if math.gcd(a, b) != 1:
        raise ValueError("a/b must be in lowest terms")


def _validate_nonnegative_integer(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def sine_state(a: int, b: int, n: int) -> int:
    """Return sign(sin(pi*a*n/b)) in {-1, 0, 1}, using integer arithmetic."""
    _validate_rotation(a, b)
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be positive")
    quotient, remainder = divmod(a * n, b)
    if remainder == 0:
        return 0
    return -1 if quotient % 2 else 1


def orbit_skeleton(a: int, b: int) -> dict[str, object]:
    _validate_rotation(a, b)
    states = [sine_state(a, b, n) for n in range(1, 2 * b + 1)]
    first = states[:b]
    second = states[b:]
    expected_second = [((-1) ** a) * state for state in first]
    if second != expected_second:
        raise ArithmeticError("signed b-shift law failed")
    zero_indices = [index + 1 for index, state in enumerate(states) if state == 0]
    if zero_indices != [b, 2 * b]:
        raise ArithmeticError("unexpected zero pattern")
    if 1 not in states or -1 not in states:
        raise ArithmeticError("orbit must contain both nonzero signs")
    return {
        "a": a,
        "b": b,
        "theta_over_pi": f"{a}/{b}",
        "sine_signs_for_n_1_through_2b": states,
        "zero_n_indices": zero_indices,
        "u_zero_residue_r_mod_b": b - 1,
        "signed_b_shift_multiplier": -1 if a % 2 else 1,
        "absolute_minimal_period": b,
        "signed_orbit_minimal_period": 2 * b if a % 2 else b,
    }


def branch_minimal_period(a: int, b: int, phase_is_one: bool) -> int:
    _validate_rotation(a, b)
    if not isinstance(phase_is_one, bool):
        raise TypeError("phase_is_one must be boolean")
    if a % 2 == 0 or phase_is_one:
        return b
    return 2 * b


def branch_period_decision_table() -> list[dict[str, object]]:
    return [
        {
            "a_parity": "EVEN",
            "negative_phase_equals_one": phase,
            "period_multiplier_times_b": 1,
        }
        for phase in (True, False)
    ] + [
        {
            "a_parity": "ODD",
            "negative_phase_equals_one": True,
            "period_multiplier_times_b": 1,
        },
        {
            "a_parity": "ODD",
            "negative_phase_equals_one": False,
            "period_multiplier_times_b": 2,
        },
    ]


def zero_exponent_fourier_spectrum(b: int, zero_value: int) -> dict[str, object]:
    if isinstance(b, bool) or not isinstance(b, int):
        raise TypeError("b must be an integer")
    if b < 2:
        raise ValueError("b must be at least 2")
    if isinstance(zero_value, bool) or not isinstance(zero_value, int):
        raise TypeError("zero_value must be an integer control")

    modes: list[dict[str, int]] = []
    for k in range(b):
        if k == 0:
            scalar = b - 1 + zero_value
            omega_exponent = 0
        else:
            scalar = zero_value - 1
            omega_exponent = (-k * (b - 1)) % b
        if scalar:
            modes.append(
                {
                    "root_exponent_mod_b": k,
                    "fourier_scalar": scalar,
                    "fourier_omega_exponent_mod_b": omega_exponent,
                }
            )

    if zero_value == 1:
        denominator = "1-T"
        expected_order = 1
    elif zero_value == 1 - b:
        denominator = "(1-T^b)/(1-T)"
        expected_order = b - 1
    else:
        denominator = "1-T^b"
        expected_order = b
    if len(modes) != expected_order:
        raise ArithmeticError("zero-exponent support count disagrees with theorem")
    return {
        "b": b,
        "zero_value_z": zero_value,
        "block": [1] * (b - 1) + [zero_value],
        "nonzero_fourier_modes": modes,
        "reduced_denominator": denominator,
        "minimal_recurrence_order": expected_order,
    }


def grouped_binomial_coefficients(k: int, b: int) -> dict[int, int]:
    _validate_nonnegative_integer(k, "k")
    if isinstance(b, bool) or not isinstance(b, int):
        raise TypeError("b must be an integer")
    if b < 2:
        raise ValueError("b must be at least 2")
    grouped = {residue: 0 for residue in range(b)}
    for j in range(k + 1):
        grouped[j % b] += (-1 if j % 2 else 1) * math.comb(k, j)
    return grouped


def direct_scaled_integer_power_modes(a: int, b: int, k: int, r: int) -> dict[int, int]:
    """Return (alpha-alpha^-1)^k u_r^k in the group ring of zeta_(2b)."""
    _validate_rotation(a, b)
    _validate_nonnegative_integer(k, "k")
    _validate_nonnegative_integer(r, "r")
    result: dict[int, int] = {}
    modulus = 2 * b
    for j in range(k + 1):
        exponent = (a * (k - 2 * j) * (r + 1)) % modulus
        coefficient = (-1 if j % 2 else 1) * math.comb(k, j)
        result[exponent] = result.get(exponent, 0) + coefficient
    return {exponent: value for exponent, value in result.items() if value}


def grouped_scaled_integer_power_modes(
    a: int, b: int, k: int, r: int
) -> dict[int, int]:
    _validate_rotation(a, b)
    _validate_nonnegative_integer(k, "k")
    _validate_nonnegative_integer(r, "r")
    result: dict[int, int] = {}
    modulus = 2 * b
    for residue, coefficient in grouped_binomial_coefficients(k, b).items():
        if coefficient:
            exponent = (a * (k - 2 * residue) * (r + 1)) % modulus
            result[exponent] = result.get(exponent, 0) + coefficient
    return {exponent: value for exponent, value in result.items() if value}


def integer_power_spectrum(a: int, b: int, k: int) -> dict[str, object]:
    _validate_rotation(a, b)
    _validate_nonnegative_integer(k, "k")
    if k == 0:
        raise ValueError("integer-power spectrum uses k > 0; zero is in Section 4")
    grouped = grouped_binomial_coefficients(k, b)
    modes = [
        {
            "residue_c_mod_b": residue,
            "grouped_binomial_amplitude": coefficient,
            "root_exponent_mod_2b": (a * (k - 2 * residue)) % (2 * b),
        }
        for residue, coefficient in grouped.items()
        if coefficient
    ]
    root_exponents = [row["root_exponent_mod_2b"] for row in modes]
    if len(root_exponents) != len(set(root_exponents)):
        raise ArithmeticError("retained characteristic roots are not distinct")
    for r in range(2 * b + 2):
        if direct_scaled_integer_power_modes(a, b, k, r) != (
            grouped_scaled_integer_power_modes(a, b, k, r)
        ):
            raise ArithmeticError("grouped binomial spectrum failed exact replay")
    return {
        "a": a,
        "b": b,
        "k": k,
        "theta_over_pi": f"{a}/{b}",
        "all_grouped_binomial_amplitudes": [grouped[c] for c in range(b)],
        "retained_modes": modes,
        "minimal_recurrence_order": len(modes),
        "reduced_denominator": ("product_(retained c) (1-zeta_(2b)^(a*(k-2c))*T)"),
    }


def verify_sources_manifest() -> dict[str, object]:
    actual_hash = _lf_sha256(SOURCES_PATH)
    if actual_hash != EXPECTED_SOURCES_SHA256_LF:
        raise RuntimeError("rational-rotation sources manifest hash mismatch")
    manifest = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    if manifest.get("base_commit") != EXPECTED_BASE_COMMIT:
        raise RuntimeError("rational-rotation source base commit mismatch")
    sources = manifest.get("sources")
    if not isinstance(sources, list):
        raise TypeError("rational-rotation sources must be a list")
    source_index = {row.get("path"): row for row in sources}
    if len(source_index) != len(sources) or set(source_index) != set(
        EXPECTED_SOURCE_OBJECTS
    ):
        raise RuntimeError("rational-rotation source path set mismatch")

    verified: list[dict[str, object]] = []
    for path, expected_blob in EXPECTED_SOURCE_OBJECTS.items():
        row = source_index[path]
        if row.get("git_blob") != expected_blob:
            raise RuntimeError(f"manifest Git blob mismatch for {path}")
        actual_blob = _git_blob_at(EXPECTED_BASE_COMMIT, path)
        if actual_blob != expected_blob:
            raise RuntimeError(f"authenticated Git blob mismatch for {path}")
        current_path = REPO_ROOT / path
        if _lf_sha256(current_path) != row.get("file_sha256_lf_normalized"):
            raise RuntimeError(f"working-tree source hash mismatch for {path}")
        verified.append(dict(row))

    references = manifest.get("external_references")
    if not isinstance(references, list) or len(references) != 2:
        raise RuntimeError("expected two nearby-literature boundary records")
    return {
        "manifest": _relative(SOURCES_PATH),
        "file_sha256_lf_normalized": actual_hash,
        "base_commit": EXPECTED_BASE_COMMIT,
        "verified_sources": verified,
        "external_references": references,
        "scope_firewall": manifest["scope_firewall"],
    }


def _survival_ladder() -> dict[str, object]:
    return {
        "levels": [f"L{level}" for level in range(10)],
        "rows": [
            {
                "object": "absolute power with Re(lambda)>0",
                "L0": "PASS_BRANCH_FREE_WITH_ZERO_VALUE_ZERO",
                "L1": "PASS_FOR_ABSOLUTE_VALUE_MULTIPLICATION",
                "L2": "FORMAL_IF_INPUT_COEFFICIENTS_ARE_MULTIPLICATIVE",
                "L3": "PASS_POINTWISE; UNIFORM_BOUND_AT_EVEN_POSITIVE_INTEGERS",
                "first_unresolved_level": "UNIFORM_L3_OUTSIDE_EVEN_INTEGER_CHAMBER",
            },
            {
                "object": "fixed-branch signed power",
                "L0": "PASS_ONLY_AFTER_BRANCH_INDEX_J_IS_DATA",
                "L1": "FAILS_IN_GENERAL; REAL_SCALAR_MULTIPLICATIVITY_REQUIRES_c_SQUARED_1",
                "L2": "NOT_REACHED_WHEN_L1_FAILS",
                "L3": "ONE_RATIONAL_ORBIT_IS_PERIODIC",
                "first_failure_level": "L1",
            },
            {
                "object": "positive integer power",
                "L0": "PASS_BRANCH_INDEPENDENT",
                "L1": "PASS_SCALAR_MULTIPLICATIVITY",
                "L2": "FORMAL_IF_INPUT_COEFFICIENTS_ARE_MULTIPLICATIVE",
                "L3": "EXACT_FINITE_SPECTRUM_WITH_UNIFORM_ORDER_AT_MOST_k_PLUS_1",
                "first_unresolved_level": "L4",
            },
            {
                "object": "lambda zero without declared zero_value",
                "L0": "FAIL_0_POW_0_UNSPECIFIED",
                "first_failure_level": "L0",
            },
        ],
        "L4_through_L9_not_established": True,
    }


def _validate_bound(value: int, name: str, lower: int, upper: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if not lower <= value <= upper:
        raise ValueError(f"{name} must lie in [{lower}, {upper}]")


def build_fixture(
    *,
    max_b: int = DEFAULT_MAX_B,
    max_k: int = DEFAULT_MAX_K,
    resource_cap: int = DEFAULT_RESOURCE_CAP_EXCLUSIVE,
) -> dict[str, object]:
    _validate_bound(max_b, "max_b", 5, MAX_ALLOWED_B)
    _validate_bound(max_k, "max_k", 6, MAX_ALLOWED_K)
    if isinstance(resource_cap, bool) or not isinstance(resource_cap, int):
        raise TypeError("resource_cap must be an integer")
    if resource_cap <= 0:
        raise ValueError("resource_cap must be positive")

    rotations = [
        (a, b) for b in range(2, max_b + 1) for a in range(1, b) if math.gcd(a, b) == 1
    ]
    work_units = sum(2 * b for a, b in rotations) + len(rotations) * max_k
    if work_units >= resource_cap:
        raise RuntimeError("declared work reaches or exceeds exclusive cap")

    orbit_rows = [orbit_skeleton(a, b) for a, b in rotations]
    zero_rows = [
        zero_exponent_fourier_spectrum(b, zero_value)
        for b in range(2, max_b + 1)
        for zero_value in (1, 0, 1 - b, 2)
    ]
    spectrum_rows = [
        integer_power_spectrum(a, b, k)
        for a, b in rotations
        for k in range(1, max_k + 1)
    ]
    hostile_cancellations = [
        row
        for row in spectrum_rows
        if 0 in row["all_grouped_binomial_amplitudes"] and row["k"] >= row["b"]
    ]
    if not hostile_cancellations:
        raise ArithmeticError("expected at least one grouped collision cancellation")
    order_histogram: dict[str, int] = {}
    for row in spectrum_rows:
        order = str(row["minimal_recurrence_order"])
        order_histogram[order] = order_histogram.get(order, 0) + 1
    representative_keys = {(1, 2, 1), (1, 3, 3), (2, 3, 4), (1, 5, 5), (3, 8, 7)}
    representative_spectra = [
        row
        for row in spectrum_rows
        if (row["a"], row["b"], row["k"]) in representative_keys
    ]

    source_lock = verify_sources_manifest()
    fixture: dict[str, object] = {
        "schema": "riemann.atlas.generalized.rational_rotation_branch_census.v1",
        "programme_issue": 764,
        "status": "PROPOSED_EXACT_LOCAL_THEOREM_EXTERNAL_NOVELTY_UNREVIEWED",
        "claims": {
            "GLO764.RATIONAL_ROTATION_ZERO_PERIOD": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "reduced a/b, Re(lambda)>0, absolute power",
            },
            "GLO764.FIXED_BRANCH_POWER_PERIOD": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "fixed real-axis logarithm branch J and Re(lambda)>0",
            },
            "GLO764.ZERO_EXPONENT_CONVENTION_SPECTRUM": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "declared complex zero value z; integer controls exact",
            },
            "GLO764.INTEGER_POWER_COLLISION_SPECTRUM": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "positive integer k with exact root-of-unity collision sums",
            },
        },
        "normalization": {
            "theta_over_pi": "a/b with 1<=a<b and gcd(a,b)=1",
            "recurrence": "u_0=1; u_1=2*cos(theta); u_(r+2)=2*cos(theta)*u_(r+1)-u_r",
            "closed_form": "u_r=sin((r+1)*theta)/sin(theta)",
            "rationality": "analytic germ at T=0 belongs to C(T)",
        },
        "source_lock": source_lock,
        "orbit_skeleton": {
            "maximum_b": max_b,
            "reduced_rotation_count": len(rotations),
            "rows": orbit_rows,
        },
        "fixed_branch_period": {
            "negative_phase": "c_(lambda,J)=exp((2J+1)*pi*i*lambda)",
            "branch_independent_iff": "lambda is a positive integer",
            "principal_branch_period_b_for_odd_a_iff": (
                "lambda is a positive even integer"
            ),
            "decision_table": branch_period_decision_table(),
        },
        "zero_exponent_spectrum": {
            "zero_value_is_required_L0_data": True,
            "rows": zero_rows,
        },
        "integer_power_collision_spectrum": {
            "maximum_k": max_k,
            "exhaustive_row_count": len(spectrum_rows),
            "exhaustive_rows_digest": _canonical_sha256(spectrum_rows),
            "minimal_order_histogram": order_histogram,
            "representative_rows": representative_spectra,
            "hostile_cancellation_row_count": len(hostile_cancellations),
            "hostile_cancellation_digest": _canonical_sha256(hostile_cancellations),
            "specific_b3_k3": integer_power_spectrum(1, 3, 3),
        },
        "non_scalar_parent": {
            "rank_two_parent": "A_theta=diag(alpha,alpha^-1)",
            "integer_parent": "B_(k,theta)=Sym^k(A_theta), dimension k+1",
            "scalar_observable": "u_r^k=trace(C_(k,theta)*B_(k,theta)^r)",
            "scalar_denominator_can_merge_and_cancel_parent_weights": True,
            "not_identified_with_standard_symmetric_power_local_factor": True,
        },
        "survival_ladder": _survival_ladder(),
        "scope_firewall": {
            "one_unramified_determinant_one_local_recurrence": True,
            "tempered_rational_rotations_only": True,
            "fixed_branch_index_is_data_for_noninteger_signed_powers": True,
            "termwise_varying_branch_indices_excluded": True,
            "Re_lambda_nonpositive_excluded_except_declared_lambda_zero_family": True,
            "noninteger_uniform_local_degree_not_classified_in_this_packet": True,
            "no_global_Euler_product_completion_or_functional_equation": True,
            "no_automorphy_motivic_or_categorical_no_go": True,
            "no_RH_GRH_or_zero_distribution_consequence": True,
            "external_novelty_unreviewed": True,
        },
        "resource_contract": {
            "arithmetic_class": "EXACT_RATIONAL",
            "exact_method": (
                "integer sign residues, binomial collision sums, symbolic root-of-unity "
                "exponents, and canonical JSON hashing"
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
            "prime_curve_field_zero_or_conductor_enumerations": 0,
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
            raise SystemExit("stored rational-rotation fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
