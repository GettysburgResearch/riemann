"""Exact replay for fixed-branch complex powers on an irrational rotation.

The companion note proves the analytic dense-orbit and cusp theorem.  This
producer checks integer Fourier spectra, minimal symbolic denominators, tail
annihilation, exact complex-rational cusp controls, source objects, and the
finite-state scope boundary without floating point.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from collections.abc import Sequence
from fractions import Fraction
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
PACKET_ROOT = SCRIPT_PATH.parent
REPO_ROOT = SCRIPT_PATH.parents[4]
OUTPUT_PATH = (
    PACKET_ROOT / "irrational_rotation_principal_complex_power_rationality.json"
)
SOURCES_PATH = (
    PACKET_ROOT / "irrational_rotation_principal_complex_power_rationality.sources.json"
)
NOTE_PATH = PACKET_ROOT / "IRRATIONAL_ROTATION_PRINCIPAL_COMPLEX_POWER_RATIONALITY.md"
TEST_PATH = (
    REPO_ROOT
    / "tests"
    / "test_irrational_rotation_principal_complex_power_rationality.py"
)
PARENT_PATH = PACKET_ROOT / "rational_rotation_branch_census.py"

EXPECTED_BASE_COMMIT = "834a24e71878a584e00215edf1e0c813faa9f578"
EXPECTED_SOURCES_SHA256_LF = (
    "ad891e0c0c87c49e0fb6fa592501aa19e2ff643650730699465ec76cb2ace52a"
)
EXPECTED_SOURCE_OBJECTS = {
    "research/l-families/atlas/generalized/RATIONAL_ROTATION_BRANCH_CENSUS.md": (
        "d0ff4d4d17787b6dffc4c8c1ccd14a20c69076d0"
    ),
    "research/l-families/atlas/generalized/rational_rotation_branch_census.py": (
        "a2fff9a394585fe91a1dacad429f68f99603e9a2"
    ),
    "research/l-families/atlas/generalized/rational_rotation_branch_census.json": (
        "c92c6e79df09bfcd34b992a56667655de530f11a"
    ),
    "research/l-families/atlas/generalized/rational_rotation_branch_census.sources.json": (
        "103a568fe71f08886b5b3837c944bc630ad4cf3d"
    ),
    "research/l-families/atlas/generalized/IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md": (
        "8f27df80a4983b4d393ee3a2477a744afaeb1d3a"
    ),
    "research/l-families/atlas/generalized/irrational_rotation_absolute_power_rationality.sources.json": (
        "3adf8f211fee7bd51e811520b31785af38ccd7c0"
    ),
}
DEFAULT_MAX_K = 10
MAX_ALLOWED_K = 18
DEFAULT_RESOURCE_CAP_EXCLUSIVE = 100_000


def _load_parent_packet():
    spec = importlib.util.spec_from_file_location(
        "glo764_rational_rotation_parent", PARENT_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load adjacent rational-rotation packet")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARENT = _load_parent_packet()
Laurent = dict[int, int]
ComplexRational = tuple[Fraction, Fraction]


def _relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _canonical_sha256(value: object) -> str:
    return PARENT._canonical_sha256(value)


def _git_blob_at(commit: str, path: str) -> str:
    return PARENT._git_blob_at(commit, path)


def _validate_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k < 0:
        raise ValueError("k must be nonnegative")


def _clean_laurent(value: Laurent) -> Laurent:
    return {
        exponent: coefficient for exponent, coefficient in value.items() if coefficient
    }


def laurent_add(left: Laurent, right: Laurent) -> Laurent:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, 0) + coefficient
    return _clean_laurent(result)


def laurent_multiply(left: Laurent, right: Laurent) -> Laurent:
    result: Laurent = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            result[exponent] = (
                result.get(exponent, 0) + left_coefficient * right_coefficient
            )
    return _clean_laurent(result)


def scaled_integer_fourier_coefficients(k: int) -> Laurent:
    """Return (2i)^k times the Fourier coefficients of sin(t)^k."""
    _validate_k(k)
    return {k - 2 * j: (-1 if j % 2 else 1) * math.comb(k, j) for j in range(k + 1)}


def scaled_integer_power_sequence_laurent(k: int, index: int) -> Laurent:
    """Return (2i)^k sin((index+1)theta)^k in alpha=e^(i theta)."""
    _validate_k(k)
    if isinstance(index, bool) or not isinstance(index, int):
        raise TypeError("sequence index must be an integer")
    if index < 0:
        raise ValueError("sequence index must be nonnegative")
    return {
        frequency * (index + 1): coefficient
        for frequency, coefficient in scaled_integer_fourier_coefficients(k).items()
    }


def alpha_denominator(k: int) -> list[Laurent]:
    """Return coefficients of product_(j=0)^k (1-alpha^(k-2j) T)."""
    _validate_k(k)
    coefficients: list[Laurent] = [{0: 1}]
    for frequency in range(k, -k - 1, -2):
        updated: list[Laurent] = [{} for _ in range(len(coefficients) + 1)]
        for degree, coefficient in enumerate(coefficients):
            updated[degree] = laurent_add(updated[degree], coefficient)
            shifted = {
                exponent + frequency: -value for exponent, value in coefficient.items()
            }
            updated[degree + 1] = laurent_add(updated[degree + 1], shifted)
        coefficients = updated
    return coefficients


def scaled_integer_power_numerator(k: int) -> list[Laurent]:
    _validate_k(k)
    denominator = alpha_denominator(k)
    order = k + 1
    coefficients: list[Laurent] = []
    for index in range(3 * order + 1):
        coefficient: Laurent = {}
        for degree in range(min(index, len(denominator) - 1) + 1):
            coefficient = laurent_add(
                coefficient,
                laurent_multiply(
                    denominator[degree],
                    scaled_integer_power_sequence_laurent(k, index - degree),
                ),
            )
        coefficients.append(coefficient)
    if any(coefficients[order:]):
        raise ArithmeticError("integer-power denominator failed tail annihilation")
    numerator = coefficients[:order]
    while len(numerator) > 1 and not numerator[-1]:
        numerator.pop()
    return numerator


def laurent_record(value: Laurent) -> list[dict[str, int]]:
    return [
        {"alpha_exponent": exponent, "coefficient": value[exponent]}
        for exponent in sorted(value)
    ]


def polynomial_record(coefficients: list[Laurent]) -> dict[str, object]:
    return {
        "coefficient_order": "ascending powers of T",
        "alpha_laurent_coefficients": [laurent_record(value) for value in coefficients],
    }


def _complex_multiply(left: ComplexRational, right: ComplexRational) -> ComplexRational:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def _fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _complex_record(value: ComplexRational) -> dict[str, str]:
    return {"real": _fraction_text(value[0]), "imaginary": _fraction_text(value[1])}


def cusp_control(
    real: Fraction, imaginary: Fraction = Fraction(0)
) -> dict[str, object]:
    if not isinstance(real, Fraction) or not isinstance(imaginary, Fraction):
        raise TypeError("cusp control parts must be Fraction values")
    if real < 0 or (real == 0 and imaginary != 0):
        raise ValueError("control domain is lambda=0 or Re(lambda)>0")
    if real == 0:
        return {
            "lambda": _complex_record((real, imaginary)),
            "classification": "SEPARATE_ZERO_EXPONENT",
            "smooth": True,
            "first_forced_divergent_derivative_order": None,
        }
    if imaginary == 0 and real.denominator == 1:
        return {
            "lambda": _complex_record((real, imaginary)),
            "classification": "POSITIVE_INTEGER",
            "smooth": True,
            "first_forced_divergent_derivative_order": None,
        }

    derivative_order = real.numerator // real.denominator + 1
    falling: ComplexRational = (Fraction(1), Fraction(0))
    value = (real, imaginary)
    for offset in range(derivative_order):
        falling = _complex_multiply(falling, (value[0] - offset, value[1]))
    if falling == (0, 0):
        raise ArithmeticError("noninteger cusp control has zero falling factorial")
    return {
        "lambda": _complex_record(value),
        "classification": (
            "GENUINELY_COMPLEX" if imaginary else "POSITIVE_REAL_NONINTEGER"
        ),
        "smooth": False,
        "first_forced_divergent_derivative_order": derivative_order,
        "falling_factorial": _complex_record(falling),
        "magnitude_power_at_zero": _fraction_text(real - derivative_order),
    }


def branch_control(
    real: Fraction, imaginary: Fraction = Fraction(0)
) -> dict[str, object]:
    if not isinstance(real, Fraction) or not isinstance(imaginary, Fraction):
        raise TypeError("branch control parts must be Fraction values")
    is_nonnegative_integer = (
        imaginary == 0 and real.denominator == 1 and real.numerator >= 0
    )
    return {
        "lambda": _complex_record((real, imaginary)),
        "all_fixed_branches_have_same_rationality_verdict": True,
        "coefficient_sequence_branch_independent": is_nonnegative_integer,
        "adjacent_branch_multiplier": "exp(2*pi*i*lambda)",
        "integer_multiplier_value": "1" if is_nonnegative_integer else None,
    }


def verify_sources_manifest() -> dict[str, object]:
    actual_hash = _lf_sha256(SOURCES_PATH)
    if actual_hash != EXPECTED_SOURCES_SHA256_LF:
        raise RuntimeError("principal-complex-power sources manifest hash mismatch")
    manifest = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    if manifest.get("base_commit") != EXPECTED_BASE_COMMIT:
        raise RuntimeError("principal-complex-power source base commit mismatch")
    sources = manifest.get("sources")
    if not isinstance(sources, list):
        raise TypeError("principal-complex-power sources must be a list")
    source_index = {row.get("path"): row for row in sources}
    if len(source_index) != len(sources) or set(source_index) != set(
        EXPECTED_SOURCE_OBJECTS
    ):
        raise RuntimeError("principal-complex-power source path set mismatch")

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
                "object": "noninteger complex power without branch datum",
                "L0": "FAIL_NEGATIVE_REAL_VALUES_AMBIGUOUS",
                "first_failure_level": "L0",
            },
            {
                "object": "fixed-branch noninteger power with Re(lambda)>0",
                "L0": "PASS_AFTER_J_IS_FIXED",
                "L1": "FAILS_IN_GENERAL",
                "L2": "NOT_REACHED_WHEN_L1_FAILS",
                "L3": "FAIL_EVERY_IRRATIONAL_TEMPERED_ROTATION",
                "first_failure_levels": ["L1", "L3"],
            },
            {
                "object": "integer k>=0",
                "L0": "PASS_BRANCH_INDEPENDENT",
                "L1": "PASS_SCALAR_MULTIPLICATIVITY",
                "L2": "FORMAL_IF_INPUT_COEFFICIENTS_ARE_MULTIPLICATIVE",
                "L3": "PASS_EXACT_DEGREE_k_PLUS_1",
                "first_unresolved_level": "L4",
            },
        ],
        "L4_through_L9_not_established": True,
    }


def build_fixture(
    *,
    max_k: int = DEFAULT_MAX_K,
    resource_cap: int = DEFAULT_RESOURCE_CAP_EXCLUSIVE,
) -> dict[str, object]:
    if isinstance(max_k, bool) or not isinstance(max_k, int):
        raise TypeError("max_k must be an integer")
    if not 6 <= max_k <= MAX_ALLOWED_K:
        raise ValueError(f"max_k must lie in [6, {MAX_ALLOWED_K}]")
    if isinstance(resource_cap, bool) or not isinstance(resource_cap, int):
        raise TypeError("resource_cap must be an integer")
    if resource_cap <= 0:
        raise ValueError("resource_cap must be positive")
    work_units = sum((k + 1) ** 3 for k in range(max_k + 1))
    if work_units >= resource_cap:
        raise RuntimeError("declared work reaches or exceeds exclusive cap")

    integer_rows = []
    representative_polynomials = []
    for k in range(max_k + 1):
        denominator = alpha_denominator(k)
        numerator = scaled_integer_power_numerator(k)
        denominator_record = polynomial_record(denominator)
        numerator_record = polynomial_record(numerator)
        integer_rows.append(
            {
                "k": k,
                "minimal_recurrence_order": k + 1,
                "characteristic_root_alpha_exponents": list(range(k, -k - 1, -2)),
                "scaled_fourier_coefficients": laurent_record(
                    scaled_integer_fourier_coefficients(k)
                ),
                "minimal_denominator_certificate": {
                    "canonical_payload_sha256": _canonical_sha256(denominator_record),
                },
                "scaled_numerator_certificate": {
                    "canonical_payload_sha256": _canonical_sha256(numerator_record),
                },
            }
        )
        if k in {0, 1, 2, 3, 6, max_k}:
            representative_polynomials.append(
                {
                    "k": k,
                    "minimal_denominator": denominator_record,
                    "scaled_numerator": numerator_record,
                }
            )

    cusp_controls = [
        cusp_control(Fraction(0)),
        cusp_control(Fraction(1, 2)),
        cusp_control(Fraction(1)),
        cusp_control(Fraction(3, 2)),
        cusp_control(Fraction(2)),
        cusp_control(Fraction(1), Fraction(1, 2)),
        cusp_control(Fraction(2), Fraction(-1, 3)),
        cusp_control(Fraction(7, 3), Fraction(5, 4)),
    ]
    branch_controls = [
        branch_control(Fraction(0)),
        branch_control(Fraction(1, 2)),
        branch_control(Fraction(1)),
        branch_control(Fraction(2)),
        branch_control(Fraction(1), Fraction(1, 2)),
    ]

    source_lock = verify_sources_manifest()
    fixture: dict[str, object] = {
        "schema": (
            "riemann.atlas.generalized."
            "irrational_rotation_principal_complex_power_rationality.v1"
        ),
        "programme_issue": 764,
        "status": "PROPOSED_EXACT_LOCAL_THEOREM_EXTERNAL_NOVELTY_UNREVIEWED",
        "claims": {
            "GLO764.IRRATIONAL_FIXED_BRANCH_COMPLEX_POWER_RATIONALITY": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "lambda=0 or Re(lambda)>0; every fixed real-axis branch J",
            },
            "GLO764.IRRATIONAL_PRINCIPAL_POWER_MINIMAL_DENOMINATOR": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "principal J=0; integer k>=0; theta/pi irrational",
            },
            "GLO764.NONINTEGER_POWER_FINITE_STATE_NO_GO": {
                "status": "PROVED_BY_CAYLEY_HAMILTON_FROM_RATIONALITY_THEOREM",
                "scope": "constant finite-dimensional complex linear state space only",
            },
        },
        "normalization": {
            "theta_domain": "0<theta<pi and theta/pi irrational",
            "recurrence": "u_0=1; u_1=2*cos(theta); u_(r+2)=2*cos(theta)*u_(r+1)-u_r",
            "closed_form": "u_r=sin((r+1)*theta)/sin(theta)",
            "branch": (
                "P_(lambda,J)(y<0)=exp(lambda*(log|y|+(2J+1)*pi*i)); "
                "principal convention J=0"
            ),
            "lambda_domain": "{0} union {Re(lambda)>0}",
            "rationality": "analytic germ at T=0 belongs to C(T)",
        },
        "source_lock": source_lock,
        "classification": {
            "rational_iff": "lambda is a nonnegative integer",
            "same_verdict_for_every_fixed_branch_J": True,
            "coefficient_sequence_branch_independent_iff": (
                "lambda is a nonnegative integer"
            ),
            "nonzero_lambda_with_Re_nonpositive": "EXCLUDED_NO_VERDICT",
        },
        "dense_orbit_fourier_gate": {
            "periodic_domain": "R/(2*pi*Z)",
            "eventual_recurrence_to_continuous_translate_identity": True,
            "tail_orbit_dense": True,
            "frequency_points_exp_i_n_theta_pairwise_distinct": True,
            "finite_fourier_support_implies_trigonometric_polynomial": True,
        },
        "integer_power_replay": {
            "maximum_k": max_k,
            "rows": integer_rows,
            "representative_polynomials": representative_polynomials,
            "lambda_zero_handled_separately": {
                "sequence": "1,1,1,...",
                "generating_function": "1/(1-T)",
                "minimal_order": 1,
            },
        },
        "cusp_controls": {
            "positive_side_model": "t^lambda*h_lambda(t)",
            "rows": cusp_controls,
            "all_domain_classification_proved_in_note": (
                "smooth and finite Fourier only for nonnegative integers"
            ),
        },
        "branch_controls": branch_controls,
        "non_scalar_parent": {
            "parent": "B_(k,theta)=Sym^k(diag(exp(i theta),exp(-i theta)))",
            "dimension": "k+1",
            "scalar_series": "trace(C_(k,theta)*(I-T*B_(k,theta))^-1)",
            "minimal_denominator": "det(I-T*B_(k,theta))",
            "not_equal_to_standard_determinant_inverse": True,
            "noninteger_no_go": (
                "no fixed finite-dimensional B,v,ell with a_r=ell(B^r v)"
            ),
            "infinite_dimensional_categorical_and_nonlinear_parents_not_ruled_out": True,
        },
        "survival_ladder": _survival_ladder(),
        "scope_firewall": {
            "one_unramified_determinant_one_local_recurrence": True,
            "tempered_irrational_rotation_only": True,
            "fixed_real_axis_branch_required_for_nonintegers": True,
            "lambda_zero_or_strictly_positive_real_part_only": True,
            "no_verdict_for_nonzero_lambda_with_nonpositive_real_part": True,
            "finite_dimensional_constant_state_space_no_go_only": True,
            "no_global_Euler_product_completion_or_functional_equation": True,
            "no_automorphy_motivic_or_infinite_dimensional_no_go": True,
            "no_RH_GRH_or_zero_distribution_consequence": True,
            "external_novelty_unreviewed": True,
        },
        "resource_contract": {
            "arithmetic_class": "EXACT_RATIONAL",
            "exact_method": (
                "integer Laurent-polynomial Fourier and recurrence algebra plus "
                "complex-rational cusp controls"
            ),
            "theta_handling": "SYMBOLIC_IRRATIONAL_ROTATION_HYPOTHESIS",
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
            raise SystemExit("stored principal-complex-power fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
