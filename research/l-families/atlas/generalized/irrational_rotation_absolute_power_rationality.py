"""Exact replay for the irrational-rotation absolute-power obstruction.

The companion note contains the analytic dense-orbit and Fourier proof. This
dependency-free producer reuses the adjacent Laurent packet and recomputes
the finite even-power spectra, minimal-denominator controls, cusp controls,
hostile rational-rotation example, source manifest, and L0--L9 ledger.
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
OUTPUT_PATH = PACKET_ROOT / "irrational_rotation_absolute_power_rationality.json"
SOURCES_PATH = (
    PACKET_ROOT / "irrational_rotation_absolute_power_rationality.sources.json"
)
NOTE_PATH = PACKET_ROOT / "IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md"
TEST_PATH = (
    REPO_ROOT / "tests" / "test_irrational_rotation_absolute_power_rationality.py"
)
PARENT_PATH = PACKET_ROOT / "nonintegral_local_power_rationality.py"

EXPECTED_SOURCES_SHA256_LF = (
    "4f070750c83d04ed1ed74a5ddcdd42c6b6ce0746a548ce11a3086b6fc37da66b"
)
EXPECTED_BASE_COMMIT = "f2f8044fb867fa7f109be92350f3f194479d36c6"
EXPECTED_IMPORTED_PARENT_COMMIT = "6b5fe8f112b38e59bd73ad80b448d52fff2da2d6"
DEFAULT_MAX_M = 6
MAX_ALLOWED_M = 10
DEFAULT_RESOURCE_CAP_EXCLUSIVE = 50_000


def _load_parent_packet():
    spec = importlib.util.spec_from_file_location(
        "glo764_nonintegral_local_power_parent", PARENT_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load adjacent local-power packet")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARENT = _load_parent_packet()
Laurent = dict[int, int]


def _relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _canonical_sha256(value: object) -> str:
    return PARENT.ATLAS_CORE.sha256_hex(value)


def _git_blob_at(commit: str, path: str) -> str:
    return PARENT._git_blob_at(commit, path)


def _validate_m(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("m must be an integer")
    if value < 0:
        raise ValueError("m must be nonnegative")


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


def scaled_even_fourier_coefficients(m: int) -> Laurent:
    """Return 2^(2m) times the Fourier coefficients of sin(t)^(2m)."""
    _validate_m(m)
    return {
        frequency: (-1 if frequency % 2 else 1) * math.comb(2 * m, m - frequency)
        for frequency in range(-m, m + 1)
    }


def scaled_sine_power_sequence_laurent(m: int, index: int) -> Laurent:
    """Return 2^(2m) sin((index+1)theta)^(2m) as a Laurent polynomial in q."""
    _validate_m(m)
    if isinstance(index, bool) or not isinstance(index, int):
        raise TypeError("sequence index must be an integer")
    if index < 0:
        raise ValueError("sequence index must be nonnegative")
    return {
        frequency * (index + 1): coefficient
        for frequency, coefficient in scaled_even_fourier_coefficients(m).items()
    }


def alpha_even_laurent_to_q(value: Laurent) -> Laurent:
    if any(exponent % 2 for exponent in value):
        raise ArithmeticError("expected only even alpha exponents")
    return _clean_laurent(
        {exponent // 2: coefficient for exponent, coefficient in value.items()}
    )


def q_denominator(m: int) -> list[Laurent]:
    """Return coefficients of product_(k=-m)^m (1-q^k T)."""
    _validate_m(m)
    coefficients: list[Laurent] = [{0: 1}]
    for frequency in range(-m, m + 1):
        updated: list[Laurent] = [{} for _ in range(len(coefficients) + 1)]
        for degree, coefficient in enumerate(coefficients):
            updated[degree] = laurent_add(updated[degree], coefficient)
            shifted = {
                exponent + frequency: -value for exponent, value in coefficient.items()
            }
            updated[degree + 1] = laurent_add(updated[degree + 1], shifted)
        coefficients = updated

    inherited = [
        alpha_even_laurent_to_q(coefficient)
        for coefficient in PARENT.denominator_laurent(2 * m)
    ]
    if coefficients != inherited:
        raise ArithmeticError("q-denominator disagrees with inherited weight product")
    return coefficients


def scaled_sine_power_numerator(m: int) -> list[Laurent]:
    """Multiply the scaled sine-power series by its exact q-denominator."""
    _validate_m(m)
    denominator = q_denominator(m)
    order = 2 * m + 1
    coefficients: list[Laurent] = []
    for index in range(3 * order + 1):
        coefficient: Laurent = {}
        for degree in range(min(index, len(denominator) - 1) + 1):
            coefficient = laurent_add(
                coefficient,
                laurent_multiply(
                    denominator[degree],
                    scaled_sine_power_sequence_laurent(m, index - degree),
                ),
            )
        coefficients.append(coefficient)
    if any(coefficients[order:]):
        raise ArithmeticError("even-power q-denominator did not annihilate its tail")
    numerator = coefficients[:order]
    while len(numerator) > 1 and not numerator[-1]:
        numerator.pop()
    return numerator


def laurent_record(value: Laurent) -> list[dict[str, int]]:
    return [
        {"q_exponent": exponent, "coefficient": value[exponent]}
        for exponent in sorted(value)
    ]


def t_laurent_polynomial_record(coefficients: list[Laurent]) -> dict[str, object]:
    return {
        "coefficient_order": "ascending powers of T",
        "q_laurent_coefficients": [laurent_record(value) for value in coefficients],
    }


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def cusp_smoothness_control(value: Fraction) -> dict[str, object]:
    if value < 0:
        raise ValueError("lambda control must be nonnegative")
    if value.denominator == 1 and value.numerator % 2 == 0:
        return {
            "lambda": fraction_text(value),
            "smooth": True,
            "classification": "EVEN_NONNEGATIVE_INTEGER",
            "first_failed_derivative_order": None,
        }
    if value.denominator == 1:
        first_failure = value.numerator
        classification = "ODD_POSITIVE_INTEGER"
    else:
        first_failure = value.numerator // value.denominator + 1
        classification = "NONINTEGER_REAL_CONTROL"
    return {
        "lambda": fraction_text(value),
        "smooth": False,
        "classification": classification,
        "first_failed_derivative_order": first_failure,
    }


def rational_rotation_counterexample() -> dict[str, object]:
    return {
        "theta_over_pi": "1/2",
        "x": "0",
        "lambda": "1/2",
        "u_prefix": [1, 0, -1, 0, 1, 0, -1, 0],
        "absolute_power_pattern": ["1", "0", "1", "0"],
        "generating_function": "1/(1-T^2)",
        "verdict": "RATIONAL_DESPITE_NON_EVEN_LAMBDA",
        "purpose": "irrationality is essential; this case is outside the theorem",
    }


def verify_sources_manifest() -> dict[str, object]:
    if _lf_sha256(SOURCES_PATH) != EXPECTED_SOURCES_SHA256_LF:
        raise RuntimeError("sources manifest hash mismatch")
    manifest = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    if manifest.get("base_commit") != EXPECTED_BASE_COMMIT:
        raise RuntimeError("sources manifest base commit mismatch")
    if manifest.get("imported_parent_state_commit") != EXPECTED_IMPORTED_PARENT_COMMIT:
        raise RuntimeError("imported parent state commit mismatch")
    if manifest.get("schema") != (
        "riemann.atlas.generalized.irrational_rotation_absolute_power.sources.v1"
    ):
        raise RuntimeError("sources manifest schema mismatch")

    verified: list[dict[str, object]] = []
    for source_record in manifest["sources"]:
        path = REPO_ROOT / source_record["path"]
        actual_hash = _lf_sha256(path)
        if actual_hash != source_record["file_sha256_lf_normalized"]:
            raise RuntimeError(f"source hash mismatch: {source_record['path']}")
        actual_blob = _git_blob_at(
            manifest["imported_parent_state_commit"], source_record["path"]
        )
        if actual_blob != source_record["git_blob"]:
            raise RuntimeError(f"source git blob mismatch: {source_record['path']}")
        row: dict[str, object] = {
            "path": source_record["path"],
            "role": source_record["role"],
            "file_sha256_lf_normalized": actual_hash,
            "git_blob": actual_blob,
        }
        if "payload_sha256" in source_record:
            source = json.loads(path.read_text(encoding="utf-8"))
            if source.get("schema") != source_record["schema"]:
                raise RuntimeError(f"source schema mismatch: {source_record['path']}")
            unhashed = dict(source)
            claimed_payload = unhashed.pop("payload_sha256", None)
            actual_payload = _canonical_sha256(unhashed)
            if (
                claimed_payload != source_record["payload_sha256"]
                or actual_payload != claimed_payload
            ):
                raise RuntimeError(f"source payload mismatch: {source_record['path']}")
            row["schema"] = source["schema"]
            row["payload_sha256"] = actual_payload
        verified.append(row)

    return {
        "path": _relative(SOURCES_PATH),
        "file_sha256_lf_normalized": EXPECTED_SOURCES_SHA256_LF,
        "base_commit": manifest["base_commit"],
        "imported_parent_state_commit": manifest["imported_parent_state_commit"],
        "verified_sources": verified,
        "external_references": manifest["external_references"],
        "scope_firewall": manifest["scope_firewall"],
    }


def _even_power_row(m: int) -> dict[str, object]:
    coefficients = scaled_even_fourier_coefficients(m)
    roots = tuple(range(-m, m + 1))
    numerator = scaled_sine_power_numerator(m)
    inherited_numerator = PARENT.numerator_in_x(2 * m)
    denominator_record = t_laurent_polynomial_record(q_denominator(m))
    numerator_record = t_laurent_polynomial_record(numerator)
    inherited_numerator_record = PARENT.polynomial_in_t_record(inherited_numerator)
    return {
        "m": m,
        "lambda": 2 * m,
        "fourier_convention": "sin(t)^(2m)=2^(-2m)*sum_k c_k*exp(2*i*k*t)",
        "scaled_fourier_coefficients": [
            {"k": frequency, "c_k": coefficients[frequency]} for frequency in roots
        ],
        "all_fourier_coefficients_nonzero": all(coefficients.values()),
        "characteristic_root_exponents_k": list(roots),
        "roots_distinct_under_theta_over_pi_irrational": True,
        "minimal_recurrence_order": 2 * m + 1,
        "minimal_denominator_certificate": {
            "degree": 2 * m + 1,
            "canonical_payload_sha256": _canonical_sha256(denominator_record),
        },
        "scaled_sine_power_numerator_certificate": {
            "degree": len(numerator) - 1,
            "canonical_payload_sha256": _canonical_sha256(numerator_record),
        },
        "inherited_normalized_u_power_numerator_certificate": {
            "degree": len(inherited_numerator) - 1,
            "canonical_payload_sha256": _canonical_sha256(inherited_numerator_record),
        },
        "tail_annihilation_checked_through_index": 3 * (2 * m + 1),
    }


def _survival_ladder() -> dict[str, object]:
    levels = {
        "L0": "well-defined and branch-independent",
        "L1": "coefficient or local multiplicativity",
        "L2": "formal Euler product",
        "L3": "uniform bounded-degree rational local factors",
        "L4": "weight, determinant, duality, and ramified-prime coherence",
        "L5": "canonical conductor, gamma factors, and root number",
        "L6": "analytic continuation and functional equation",
        "L7": "twist, tensor, induction, and contragredient compatibility",
        "L8": "automorphic, motivic, spectral, dynamical, or categorical realization",
        "L9": "principled explicit formula, positivity, or zero theory",
    }
    rows = [
        {
            "object": "absolute power lambda=2m on an irrational tempered orbit",
            "statuses": {
                "L0": "PROVED_PASS",
                "L1": "PROVED_PASS_IF_THE_INPUT_COEFFICIENT_SYSTEM_IS_MULTIPLICATIVE",
                "L2": "PROVED_PASS_AS_A_FORMAL_EULER_PRODUCT_UNDER_L1",
                "L3": "PROVED_PASS_LOCALLY_WITH_MINIMAL_DEGREE_2M_PLUS_1",
                "L4": "NOT_ESTABLISHED_BY_THIS_PACKET",
                "L5": "NOT_ESTABLISHED",
                "L6": "NOT_ESTABLISHED",
                "L7": "NOT_ESTABLISHED",
                "L8": "NOT_ESTABLISHED",
                "L9": "NOT_ESTABLISHED",
            },
            "first_unresolved_level": "L4",
        },
        {
            "object": "absolute power lambda>=0 not an even integer",
            "statuses": {
                "L0": "PROVED_PASS_ON_THE_IRRATIONAL_ORBIT",
                "L1": "PROVED_PASS_IF_THE_INPUT_COEFFICIENT_SYSTEM_IS_MULTIPLICATIVE",
                "L2": "PROVED_PASS_AS_A_FORMAL_EULER_PRODUCT_UNDER_L1",
                "L3": "PROVED_FAIL_AT_EACH_IRRATIONAL_ROTATION_LOCAL_RECURRENCE",
                "L4": "NOT_REACHED",
                "L5": "NOT_REACHED",
                "L6": "NOT_REACHED",
                "L7": "NOT_REACHED",
                "L8": "NO_INFINITE_DIMENSIONAL_OR_CATEGORICAL_NO_GO",
                "L9": "NOT_REACHED",
            },
            "first_failure_level": "L3",
        },
    ]
    return {"levels": levels, "rows": rows}


def build_fixture(
    *,
    max_m: int = DEFAULT_MAX_M,
    resource_cap: int = DEFAULT_RESOURCE_CAP_EXCLUSIVE,
) -> dict[str, object]:
    if isinstance(max_m, bool) or not isinstance(max_m, int):
        raise TypeError("max_m must be an integer")
    if max_m < 4:
        raise ValueError("max_m must include m=0 through m=4 calibration rows")
    if max_m > MAX_ALLOWED_M:
        raise ValueError(f"max_m must not exceed {MAX_ALLOWED_M}")
    if isinstance(resource_cap, bool) or not isinstance(resource_cap, int):
        raise TypeError("resource_cap must be an integer")
    if resource_cap <= 0:
        raise ValueError("resource_cap must be positive")

    work_units = sum((2 * m + 1) ** 3 for m in range(max_m + 1)) + 400
    if work_units >= resource_cap:
        raise RuntimeError("declared exact replay would meet or exceed exclusive cap")

    sources_manifest = verify_sources_manifest()
    rows = [_even_power_row(m) for m in range(max_m + 1)]
    cusp_controls = [
        cusp_smoothness_control(value)
        for value in (
            Fraction(0),
            Fraction(1, 2),
            Fraction(1),
            Fraction(3, 2),
            Fraction(2),
            Fraction(5, 2),
            Fraction(3),
            Fraction(4),
        )
    ]

    fixture: dict[str, object] = {
        "schema": (
            "riemann.atlas.generalized."
            "irrational_rotation_absolute_power_rationality.v1"
        ),
        "status": "PROPOSED_EXACT_LOCAL_THEOREM_EXTERNAL_NOVELTY_UNREVIEWED",
        "programme_issue": 764,
        "claims": {
            "GLO764.IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": (
                    "theta in (0,pi), theta/pi irrational, "
                    "x=2*cos(theta), real lambda>=0"
                ),
                "statement": (
                    "sum_r |u_r(x)|^lambda*T^r is rational "
                    "iff lambda is an even nonnegative integer"
                ),
            },
            "GLO764.IRRATIONAL_ROTATION_EVEN_POWER_MINIMAL_DENOMINATOR": {
                "status": "PROVED_IN_COMPANION_NOTE_AND_EXACTLY_REPLAYED",
                "scope": "lambda=2m with m>=0 under the same irrationality hypothesis",
                "statement": (
                    "the reduced denominator is "
                    "product_(k=-m)^m(1-exp(2*i*k*theta)*T), of degree 2m+1"
                ),
            },
            "GLO764.DENSE_ORBIT_FINITE_SPECTRUM": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "continuous pi-periodic functions sampled on an irrational orbit",
                "statement": (
                    "an eventual constant-coefficient recurrence forces "
                    "finite Fourier support"
                ),
            },
        },
        "normalization": {
            "theta_domain": "theta in (0,pi) with theta/pi irrational",
            "trace": "x=2*cos(theta) in (-2,2)",
            "recurrence": "u_0=1; u_1=x; u_(r+2)=x*u_(r+1)-u_r",
            "trigonometric_form": "u_r=sin((r+1)*theta)/sin(theta)",
            "nonvanishing": "u_r!=0 for every r because theta/pi is irrational",
            "absolute_power": "a_r=|u_r|^lambda for real lambda>=0",
            "lambda_zero_convention": "a_r=1; no zero-to-zero ambiguity occurs",
        },
        "sources_manifest": sources_manifest,
        "dense_orbit_fourier_gate": {
            "eventual_recurrence_to_translate_identity": True,
            "tail_orbit_dense_modulo_pi": True,
            "continuity_extends_identity_to_all_translates": True,
            "fourier_multiplier": "P(exp(2*i*k*theta))*f_hat(k)=0",
            "multipliers_pairwise_distinct": True,
            "nonzero_polynomial_has_only_finitely_many_multiplier_zeros": True,
            "finite_fourier_support_implies_trigonometric_polynomial": True,
            "trigonometric_polynomial_is_C_infinity": True,
        },
        "even_power_replay": {
            "maximum_m": max_m,
            "rows": rows,
            "lambda_zero_handled_separately": {
                "sequence": "1,1,1,...",
                "generating_function": "1/(1-T)",
                "minimal_order": 1,
            },
        },
        "cusp_controls": {
            "local_model": "|sin(t)|^lambda=|t|^lambda*h_lambda(t)",
            "smooth_positive_factor": "h_lambda(t)=|sin(t)/t|^lambda near zero",
            "rows": cusp_controls,
            "general_classification_proved_in_note": (
                "C_infinity iff lambda is an even nonnegative integer"
            ),
        },
        "hostile_controls": {
            "rational_rotation_counterexample": rational_rotation_counterexample(),
            "finite_controls_are_not_the_dense_orbit_proof": True,
        },
        "survival_ladder": _survival_ladder(),
        "scope_firewall": {
            "one_unramified_determinant_one_local_recurrence": True,
            "tempered_irrational_rotation_only": True,
            "rational_rotations_excluded_and_can_be_counterexamples": True,
            "absolute_powers_erase_phase_and_are_not_complex_powers": True,
            "does_not_classify_signed_or_branched_noninteger_powers": True,
            "does_not_give_a_uniform_statement_over_primes": True,
            "does_not_construct_a_global_Euler_product": True,
            "does_not_supply_ramified_factors_completion_or_functional_equation": True,
            "does_not_prove_automorphy_motivic_origin_or_categorical_no_go": True,
            "no_RH_GRH_or_zero_distribution_consequence": True,
            "external_novelty_unreviewed": True,
        },
        "novelty_firewall": {
            "proof_uses_standard_recurrence_and_fourier_facts": True,
            "self_contained_proof_is_not_a_priority_claim": True,
            "external_specialist_novelty_review_required": True,
        },
        "resource_contract": {
            "arithmetic_class": "EXACT_RATIONAL",
            "exact_method": (
                "integer and rational Laurent-polynomial, Fourier, "
                "recurrence, cusp-control, and formal coefficient algebra"
            ),
            "theta_handling": "SYMBOLIC_IRRATIONAL_ROTATION_HYPOTHESIS",
            "maximum_m": max_m,
            "maximum_allowed_m": MAX_ALLOWED_M,
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
            raise SystemExit("stored irrational-rotation fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
