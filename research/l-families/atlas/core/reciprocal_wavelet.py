from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
from typing import Any

from atlas_core import ATLAS_ROOT, read_json, semantic_identity, sha256_hex, write_json
from local_euler import elliptic_trace, primes_up_to, quadratic_character
from run_pilot import artifact_binding, hash_object, programme_ref, raw_sha256


FILTER_DEFINITION = (
    "For the classical-variable reciprocal coefficients mu_L^cl(n), let "
    "M_L^cl(Y)=sum_{1<=n<=Y} mu_L^cl(n) with inclusive integer endpoints and "
    "S_2 M(X)=M(floor(X/2)); evaluate W_L^cl(X)=(I-sqrt(2)S_2)(I-S_2)^2 M_L^cl(X)."
)
RAW_RESULT_SCHEMA = "research/l-families/atlas/detectors/raw-schemas/reciprocal-wavelet-result.schema.json"
EXPECTED_NUMBER_FIELD_SLUGS = (
    "ZETA.RIEMANN",
    "DIRICHLET.QUADRATIC.MOD5",
    "EC.11.R0",
    "EC.37.R1",
    "EC.389.R2",
)


def factor_integer(value: int, primes: list[int]) -> list[tuple[int, int]]:
    remaining = value
    factors: list[tuple[int, int]] = []
    for prime in primes:
        if prime * prime > remaining:
            break
        if remaining % prime:
            continue
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        factors.append((prime, exponent))
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def local_polynomial(metadata: dict[str, Any], prime: int) -> list[int]:
    kind = metadata["kind"]
    if kind == "zeta":
        return [1, -1]
    if kind == "quadratic_character":
        character = quadratic_character(prime, metadata["modulus"])
        return [1] if character == 0 else [1, -character]
    if kind == "elliptic_curve":
        if prime in metadata["bad_primes"]:
            return [1, -metadata["bad_local_trace"]]
        trace = elliptic_trace(prime, metadata["ainvs"])
        return [1, -trace, prime]
    raise ValueError(f"unsupported reciprocal adapter kind: {kind}")


def reciprocal_coefficients(metadata: dict[str, Any], bound: int) -> list[int]:
    primes = primes_up_to(bound)
    local = {prime: local_polynomial(metadata, prime) for prime in primes}
    coefficients = [0] * (bound + 1)
    coefficients[1] = 1
    for value in range(2, bound + 1):
        coefficient = 1
        for prime, exponent in factor_integer(value, primes):
            polynomial = local[prime]
            if exponent >= len(polynomial):
                coefficient = 0
                break
            coefficient *= polynomial[exponent]
        coefficients[value] = coefficient
    return coefficients


def qsqrt2_sign(rational: int, sqrt2: int) -> int:
    if rational == 0:
        return (sqrt2 > 0) - (sqrt2 < 0)
    if sqrt2 == 0 or (rational > 0) == (sqrt2 > 0):
        return (rational > 0) - (rational < 0)
    comparison = rational * rational - 2 * sqrt2 * sqrt2
    if comparison == 0:
        raise AssertionError("nonzero integer coordinates cannot cancel irrational sqrt(2)")
    dominant_sign = (rational > 0) - (rational < 0) if comparison > 0 else (sqrt2 > 0) - (sqrt2 < 0)
    return dominant_sign


def wavelet_rows(coefficients: list[int], endpoints: list[int]) -> list[dict[str, Any]]:
    if not endpoints or endpoints != sorted(set(endpoints)):
        raise ValueError("endpoints must be a nonempty strictly increasing list")
    if any(endpoint <= 0 or endpoint % 8 for endpoint in endpoints):
        raise ValueError("endpoints must be positive multiples of 8")
    if endpoints[-1] >= len(coefficients):
        raise ValueError("coefficient array does not cover the largest endpoint")
    partial = [0] * len(coefficients)
    running = 0
    for index in range(1, len(coefficients)):
        running += coefficients[index]
        partial[index] = running
    rows: list[dict[str, Any]] = []
    for endpoint in endpoints:
        values = [partial[endpoint // (2**shift)] for shift in range(4)]
        rational = values[0] - 2 * values[1] + values[2]
        sqrt2 = -values[1] + 2 * values[2] - values[3]
        rows.append({
            "X": endpoint,
            "partial_sums_X_X2_X4_X8": values,
            "wavelet_qsqrt2": {"rational": rational, "sqrt2": sqrt2},
            "field_norm": rational * rational - 2 * sqrt2 * sqrt2,
            "real_sign": qsqrt2_sign(rational, sqrt2),
        })
    return rows


Q2 = tuple[Fraction, Fraction]


def q2_add(left: Q2, right: Q2) -> Q2:
    return left[0] + right[0], left[1] + right[1]


def q2_mul(left: Q2, right: Q2) -> Q2:
    return left[0] * right[0] + 2 * left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def polynomial_product(left: list[Q2], right: list[Q2]) -> list[Q2]:
    result = [(Fraction(0), Fraction(0)) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] = q2_add(
                result[left_index + right_index], q2_mul(left_value, right_value)
            )
    return result


def polynomial_value(coefficients: list[Q2], value: Q2) -> Q2:
    result: Q2 = (Fraction(0), Fraction(0))
    for coefficient in reversed(coefficients):
        result = q2_add(q2_mul(result, value), coefficient)
    return result


def integer_q2(value: Q2) -> dict[str, int]:
    if value[0].denominator != 1 or value[1].denominator != 1:
        raise AssertionError(f"expected integral Q(sqrt(2)) coordinates, got {value}")
    return {"rational": value[0].numerator, "sqrt2": value[1].numerator}


def filter_controls() -> dict[str, Any]:
    linear = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1))]
    double_difference = [
        (Fraction(1), Fraction(0)),
        (Fraction(-2), Fraction(0)),
        (Fraction(1), Fraction(0)),
    ]
    coefficients = polynomial_product(linear, double_difference)
    derivative = [
        (Fraction(index) * value[0], Fraction(index) * value[1])
        for index, value in enumerate(coefficients[1:], start=1)
    ]
    controls = {
        "P_of_1": polynomial_value(coefficients, (Fraction(1), Fraction(0))),
        "P_prime_of_1": polynomial_value(derivative, (Fraction(1), Fraction(0))),
        "P_of_inverse_sqrt2": polynomial_value(coefficients, (Fraction(0), Fraction(1, 2))),
    }
    if any(value != (Fraction(0), Fraction(0)) for value in controls.values()):
        raise AssertionError(f"filter annihilation control failed: {controls}")
    return {
        "factorization": "(I-sqrt(2)S_2)(I-S_2)^2",
        "expanded_coefficients": [integer_q2(value) for value in coefficients],
        **{name: integer_q2(value) for name, value in controls.items()},
        "controls_pass": True,
    }


def metadata_for_specs(source_manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    metadata: dict[str, dict[str, Any]] = {
        "ZETA.RIEMANN": {"kind": "zeta", "motivic_weight": 0},
        "DIRICHLET.QUADRATIC.MOD5": {"kind": "quadratic_character", "modulus": 5, "motivic_weight": 0},
    }
    for record in source_manifest["records"]:
        rank = record["analytic_rank"]
        slug = f"EC.{record['curve_label'].split('.')[0].upper()}.R{rank}"
        metadata[slug] = {
            "kind": "elliptic_curve",
            "ainvs": record["ainvs"],
            "bad_primes": record["bad_primes"],
            "bad_local_trace": record["bad_local_trace"],
            "motivic_weight": 1,
        }
    return metadata


def build_detector(root: Path) -> dict[str, Any]:
    normalization = [
        "Use inclusive integer partial sums and S_2 M(X)=M(floor(X/2)).",
        "Use classical-variable reciprocal coefficients and record the map to each spec's unitary normalization.",
        "Use the full declared reciprocal Euler factor, including every explicit bad factor that lies in the coefficient window.",
        "Store W_L(X) as exact integer coordinates in Q(sqrt(2)).",
    ]
    identity_kernel = {
        "version": 1,
        "slug": "RECIPROCAL_L.MINIMAL_DYADIC_FILTER",
        "mathematical_definition": FILTER_DEFINITION,
        "kernel_convention": "RECIPROCAL_MELLIN",
        "central_zero_policy": "NOT_APPLICABLE",
        "normalization_requirements": normalization,
        "contract_revision": 1,
    }
    semantic_id, identity_sha256 = semantic_identity("DETECTOR", "RECIPROCAL_L.MINIMAL_DYADIC_FILTER", identity_kernel)
    implementation_relative = "research/l-families/atlas/core/reciprocal_wavelet.py"
    return {
        "schema_version": "riemann.atlas.detector_contract.v1",
        "record_type": "DETECTOR_CONTRACT",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact reciprocal-L minimal dyadic filter skeleton",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(738), programme_ref(741)],
        "scope_boundary": "Finite classical-variable coefficient-filter evaluation only; no weighted-L2 abscissa or zero-detection conclusion transfers across families.",
        "supersedes": [],
        "detector_kind": "RECIPROCAL_L_MELLIN_WAVELET",
        "mathematical_definition": FILTER_DEFINITION,
        "kernel_convention": "RECIPROCAL_MELLIN",
        "central_zero_policy": "NOT_APPLICABLE",
        "required_inputs": [
            {"name": "lfunction_spec", "input_type": "LFUNCTION_SPEC", "required": True, "coverage_requirement": "COMPLETE"},
            {"name": "reciprocal_coefficients", "input_type": "RECIPROCAL_COEFFICIENTS", "required": True, "coverage_requirement": "FINITE_COMPLETE"},
        ],
        "parameters": [
            {"name": "endpoints", "value_type": "INTEGER_LIST", "required": True, "domain": "positive multiples of 8", "constraints": {"nonempty": True, "unique": True, "strictly_increasing": True, "element_minimum": 1, "element_multiple_of": 8}},
            {"name": "endpoint_convention", "value_type": "ENUM", "required": True, "domain": "INCLUSIVE_FLOOR_DYADIC", "constraints": {"enum_values": ["INCLUSIVE_FLOOR_DYADIC"]}},
        ],
        "normalization_requirements": [
            {"field": "configuration.endpoint_convention", "requirement": normalization[0], "comparison_role": "IDENTITY"},
            {"field": "completed_normalization", "requirement": normalization[1], "comparison_role": "SCALING"},
            {"field": "euler_product.bad_factor_policy", "requirement": normalization[2], "comparison_role": "FIREWALL"},
            {"field": "result.wavelet_qsqrt2", "requirement": normalization[3], "comparison_role": "SCALING"},
        ],
        "invariances": [
            {"code": "FILTER_FACTORIZATION", "statement": "The expanded four-shell coefficients equal (I-sqrt(2)S_2)(I-S_2)^2.", "status": "PROVED"},
            {"code": "CONSTANT_DOUBLE_ANNIHILATION", "statement": "The filter has a double root at S_2=1.", "status": "PROVED"},
            {"code": "SQRT_SCALE_ANNIHILATION", "statement": "The filter vanishes at S_2=1/sqrt(2).", "status": "PROVED"},
        ],
        "family_adapters": [
            {"family": "GL1_ZETA_DIRICHLET", "status": "REQUIRED_AVAILABLE", "adapter_path": implementation_relative, "correction": "Use degree-one classical local reciprocal factors; weight zero makes the classical/unitary coefficient map trivial."},
            {"family": "GL2_ELLIPTIC", "status": "REQUIRED_AVAILABLE", "adapter_path": implementation_relative, "correction": "Use classical factors 1-a_pT+pT^2 (and explicit bad factors); the unitary reciprocal coefficient is mu_cl(n)/sqrt(n)."},
            {"family": "FUNCTION_FIELD", "status": "REQUIRED_OPEN", "adapter_path": None, "correction": "Derive a degree-shift kernel rather than copying integer dyadic endpoints."},
        ],
        "theorem_links": [
            {"semantic_id": "ARITH.WAVELET.MINIMAL_RATIO8", "status": "VERIFIED_WITH_FIXES", "scope": "The exact filter polynomial is reused with the declared endpoint convention."},
            {"semantic_id": "ARITH.WAVELET.SPECTRAL_ABSCISSA", "status": "VERIFIED_WITH_FIXES", "scope": "Zeta-specific analytic conclusion is not transferred to GL(1)/GL(2) rows."},
        ],
        "failure_modes": [
            {"code": "BAD_FACTOR_OMISSION", "description": "Dropping or guessing a conductor-prime factor changes the reciprocal series.", "hostile_control": "The three semistable bad traces are declared; factors at 11 and 37 are exercised inside the n<=256 window."},
            {"code": "CLASSICAL_UNITARY_CONFLATION", "description": "Integral classical reciprocal coefficients are not the unitary coefficients for positive motivic weight.", "hostile_control": "Every subject records its exact classical-to-unitary coefficient map."},
            {"code": "ENDPOINT_DRIFT", "description": "Changing <= to < or replacing floor dyadic endpoints changes finite rows.", "hostile_control": "The endpoint convention is a required singleton parameter."},
            {"code": "ZETA_ABSCISSA_TRANSFER", "description": "The reviewed zeta abscissa theorem does not automatically hold for another completion.", "hostile_control": "Evaluation interpretation is finite coefficient reconnaissance only."},
        ],
        "output_contract": {
            "representations": ["HASHED_ARTIFACT"],
            "arithmetic_classes": ["CERTIFIED_INTEGER_COVERAGE"],
            "raw_schema_path": RAW_RESULT_SCHEMA,
            "global_claim_allowed": False,
        },
        "reference_implementation": {
            "path": implementation_relative,
            "entry_point": "wavelet_rows",
            "version": "1",
            "source_sha256": raw_sha256(root.parents[2] / implementation_relative),
        },
        "formalization_refs": [{"state": "DEFINITION_READY", "target": "Q(sqrt(2)) filter expansion and three annihilation identities.", "path": None}],
        "notes": "This is the common coefficient-filter skeleton; analytic source/zero theorems remain family-specific adapters.",
    }


def run(root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    config = read_json(root / "config" / "pilot.json")
    source_manifest = read_json(root / "sources" / "lmfdb-curves.json")
    metadata = metadata_for_specs(source_manifest)
    available_specs = {
        spec["identity_kernel"]["slug"]: spec
        for path in sorted((root / "specs").glob("*.json"))
        for spec in [read_json(path)]
        if spec["classification"]["domain"] == "NUMBER_FIELD"
    }
    missing = sorted(set(EXPECTED_NUMBER_FIELD_SLUGS) - set(available_specs))
    if missing:
        raise ValueError(f"missing frozen Phase-0 number-field specs: {missing}")
    specs = [available_specs[slug] for slug in EXPECTED_NUMBER_FIELD_SLUGS]
    detector = build_detector(root)
    detector_binding = {"semantic_id": detector["semantic_id"], "record_sha256": sha256_hex(detector)}
    endpoints = [32, 64, 128, 256]
    raw_rows: list[dict[str, Any]] = []
    for spec in specs:
        slug = spec["identity_kernel"]["slug"]
        coefficients = reciprocal_coefficients(metadata[slug], max(endpoints))
        raw_rows.append({
            "semantic_id": spec["semantic_id"],
            "identity_slug": slug,
            "reciprocal_coefficient_convention": "CLASSICAL_EULER_VARIABLE",
            "classical_to_unitary_map": (
                "mu_unitary(n)=mu_classical(n)"
                if metadata[slug]["motivic_weight"] == 0
                else "mu_unitary(n)=mu_classical(n)/sqrt(n)"
            ),
            "nonzero_coefficient_count": sum(value != 0 for value in coefficients[1:]),
            "coefficient_bound": max(endpoints),
            "rows": wavelet_rows(coefficients, endpoints),
        })
    raw_result = {
        "schema": "riemann.atlas.raw.reciprocal_wavelet.v1",
        "definition": FILTER_DEFINITION,
        "filter_controls": filter_controls(),
        "subjects": raw_rows,
    }
    values = {"endpoints": endpoints, "endpoint_convention": "INCLUSIVE_FLOOR_DYADIC"}
    source_relative = "research/l-families/atlas/sources/lmfdb-curves.json"
    adapter_relative = "research/l-families/atlas/core/reciprocal_wavelet.py"
    local_relative = "research/l-families/atlas/core/local_euler.py"
    input_binding = artifact_binding(root, source_relative, "source_object_manifest", "PARTIAL", None)
    adapter_binding = artifact_binding(root, adapter_relative, "reciprocal_coefficient_adapter", "FINITE_COMPLETE", None, "RAW_BYTES")
    local_binding = artifact_binding(root, local_relative, "local_factor_arithmetic", "FINITE_COMPLETE", None, "RAW_BYTES")
    implementation_sha256 = raw_sha256(root.parents[2] / adapter_relative)
    spec_bindings = [
        {"semantic_id": spec["semantic_id"], "record_sha256": sha256_hex(spec)}
        for spec in specs
    ]
    input_fulfillments = [
        {"name": "lfunction_spec", "input_type": "LFUNCTION_SPEC", "coverage_class": "COMPLETE", "sources": [binding["semantic_id"] for binding in spec_bindings]},
        {"name": "reciprocal_coefficients", "input_type": "RECIPROCAL_COEFFICIENTS", "coverage_class": "FINITE_COMPLETE", "sources": [adapter_relative, local_relative, source_relative]},
    ]
    slug = "RECIPROCAL_L.NUMBER_FIELD_PHASE0.MINIMAL_FILTER"
    identity_kernel = {
        "version": 1,
        "slug": slug,
        "lfunction_spec_bindings": spec_bindings,
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [adapter_binding, local_binding],
        "configuration_sha256": sha256_hex(values),
        "input_sha256s": [input_binding["sha256"]],
        "input_fulfillments_sha256": sha256_hex(input_fulfillments),
        "implementation_commit": config["code_commit"],
        "implementation_sha256": implementation_sha256,
        "seed": None,
    }
    semantic_id, identity_sha256 = semantic_identity("EVAL", slug, identity_kernel)
    result_relative = f"research/l-families/atlas/results/{semantic_id}.json"
    result_binding = {
        "role": "detector_result",
        "path": result_relative,
        "sha256": sha256_hex(raw_result),
        "hash_mode": "CANONICAL_JSON_UTF8_NFC",
        "coverage_class": "FINITE_COMPLETE",
        "media_type": "application/json",
        "schema_path": RAW_RESULT_SCHEMA,
        "notes": "Content checked by the offline atlas validator.",
    }
    evaluation = {
        "schema_version": "riemann.atlas.evaluation_record.v1",
        "record_type": "EVALUATION_RECORD",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Five-object exact reciprocal-L minimal-filter reconnaissance",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(738), programme_ref(741)],
        "scope_boundary": "Five declared number-field objects, exact reciprocal coefficients n<=256, endpoints 32/64/128/256.",
        "supersedes": [],
        "subject": {"kind": "L_FUNCTION_SET", "description": "Zeta, quadratic chi_5, and elliptic-curve rank-stress rows 11.a2/37.a1/389.a1"},
        "lfunction_spec_bindings": spec_bindings,
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [adapter_binding, local_binding],
        "configuration": {"values": values, "canonical_sha256": sha256_hex(values)},
        "evaluation_scope": "MEMBERWISE_BATCH",
        "input_bindings": [input_binding],
        "input_fulfillments": input_fulfillments,
        "arithmetic": {
            "class": "CERTIFIED_INTEGER_COVERAGE",
            "directed": False,
            "rounding_contract": "All reciprocal coefficients and Q(sqrt(2)) coordinates are integers.",
            "serialization_contract": "Canonical UTF-8 NFC JSON with explicit inclusive endpoints.",
        },
        "coverage": {
            "class": "FINITE_COMPLETE",
            "statement": "Every classical reciprocal coefficient n<=256 and every declared local factor needed for the five objects.",
            "omissions": ["endpoints above 256", "zero data", "spectral abscissa", "family average"],
        },
        "rigor_level": "DISCOVERY_ONLY",
        "software": config["software"],
        "run": {
            "timestamp_utc": config["run_timestamp_utc"],
            "command": "python research/l-families/atlas/core/reciprocal_wavelet.py --check",
            "code_commit": config["code_commit"],
            "implementation_path": adapter_relative,
            "implementation_sha256": implementation_sha256,
        },
        "central_zero_policy_applied": "NOT_APPLICABLE",
        "result": {
            "representation": "HASHED_ARTIFACT",
            "predicate_outcome": "NOT_APPLICABLE",
            "artifact": result_binding,
            "summary": "Exact Q(sqrt(2)) coefficient-filter rows for four endpoints; no analytic zero conclusion.",
        },
        "result_hashes": [hash_object(result_binding["sha256"], "canonical JSON reciprocal-wavelet result", "CANONICAL_JSON_UTF8_NFC")],
        "interpretation": {
            "status": "EMPIRICAL",
            "statement": "The common finite classical-variable filter is computationally portable once the classical-to-unitary map and bad factors are explicit; its analytic meaning remains family-specific.",
            "smallest_gap": "Prove a completed-L Mellin identity and a family moment for one GL(2) twist adapter before using these rows as a zero detector.",
            "theorem_claim_id": None,
        },
        "assumptions": [{"code": "LMFDB_MODELS_IMPORTED", "statement": "The three Weierstrass models identify the intended elliptic L-functions.", "status": "HEURISTIC"}],
        "firewalls": [
            {"code": "FINITE_NOT_ABSCISSA", "statement": "Four finite endpoints do not determine a weighted-L2 abscissa."},
            {"code": "NO_ZERO_DATA", "statement": "No zero ordinate or completeness theorem enters the result."},
            {"code": "BAD_FACTORS_EXPLICIT", "statement": "The semistable conductor-prime factors are included, not silently dropped."},
        ],
        "notes": "Exact finite arithmetic is paired with discovery-only object metadata; no rank trend is inferred.",
    }
    return detector, evaluation, raw_result


def main() -> None:
    parser = argparse.ArgumentParser(description="Run and wrap the exact reciprocal-L minimal dyadic filter pilot.")
    parser.add_argument("--root", type=Path, default=ATLAS_ROOT)
    parser.add_argument("--check", action="store_true", help="Recompute and compare without modifying checked-in artifacts.")
    args = parser.parse_args()
    root = args.root.resolve()
    detector, evaluation, raw_result = run(root)
    detector_path = root / "detectors" / f"{detector['semantic_id']}.json"
    evaluation_path = root / "evaluations" / f"{evaluation['semantic_id']}.json"
    result_path = root.parents[2] / evaluation["result"]["artifact"]["path"]
    if args.check:
        expected = ((detector_path, detector), (evaluation_path, evaluation), (result_path, raw_result))
        mismatches = [str(path) for path, value in expected if not path.is_file() or read_json(path) != value]
        if mismatches:
            raise SystemExit(f"reciprocal-wavelet artifacts differ: {mismatches}")
        print("OK: exact reciprocal-wavelet artifacts match")
        return
    write_json(detector_path, detector)
    write_json(evaluation_path, evaluation)
    write_json(result_path, raw_result)
    print("PASS_RECIPROCAL_WAVELET subjects=5 endpoints=4 coefficient_bound=256")


if __name__ == "__main__":
    main()
