#!/usr/bin/env python3
"""Wrap the exact F_3 genus-two pilot in DRAFT atlas records."""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

from atlas_core import ATLAS_ROOT, read_json, semantic_identity, sha256_hex, write_json
from run_pilot import (
    artifact_binding,
    hash_object,
    make_lfunction_spec,
    programme_ref,
    raw_sha256,
)


RAW_RESULT_SCHEMA = (
    "research/l-families/atlas/detectors/raw-schemas/"
    "function-field-genus2-result.schema.json"
)
GENUS2_PILOT = "research/l-families/atlas/function_field/genus2_pilot.py"
POLYNOMIAL_PILOT = "research/l-families/atlas/function_field/pilot.py"
GENUS2_FIXTURE = "research/l-families/atlas/function_field/genus2_f3_quintics.json"
FUNCTION_FIELD_SPEC_SLUG = "FUNCTION_FIELD.F3.QUADRATIC.QUINTIC_GENUS2_FAMILY"
DETECTOR_SLUG = "FUNCTION_FIELD.GENUS2.NORMALIZED_RECIPROCAL.HANKEL_MINOR_TOY"
EVALUATION_SLUG = "FUNCTION_FIELD.F3.QUINTIC.GENUS2.HANKEL_MINOR_TOY"

DETECTOR_DEFINITION = (
    "For P_D(u)=1+a_1u+a_2u^2+q*a_1u^3+q^2u^4 and "
    "1/P_D(u)=sum_(n>=0) B_D(n)u^n, put H_D(n)=q^(-n/2)B_D(n) and evaluate "
    "the toy reciprocal-coefficient minor det([[H_D(1),H_D(2)],[H_D(2),H_D(3)]]); "
    "equivalently q^2*det=q*a_1^2-a_2^2."
)


def content_binding(record: dict[str, Any]) -> dict[str, str]:
    return {"semantic_id": record["semantic_id"], "record_sha256": sha256_hex(record)}


def _load_genus2_pilot(repo_root: Path) -> ModuleType:
    path = repo_root / GENUS2_PILOT
    function_field_dir = str(path.parent)
    if function_field_dir not in sys.path:
        sys.path.insert(0, function_field_dir)
    module_spec = importlib.util.spec_from_file_location("_riemann_atlas_genus2_pilot", path)
    if module_spec is None or module_spec.loader is None:
        raise RuntimeError(f"cannot load exact genus-two pilot: {path}")
    module = importlib.util.module_from_spec(module_spec)
    sys.modules[module_spec.name] = module
    module_spec.loader.exec_module(module)
    return module


def _load_and_replay_fixture(root: Path) -> dict[str, Any]:
    repo_root = root.parents[2]
    fixture = read_json(repo_root / GENUS2_FIXTURE)
    claimed_payload_sha256 = fixture.get("payload_sha256")
    payload = dict(fixture)
    payload.pop("payload_sha256", None)
    if claimed_payload_sha256 != sha256_hex(payload):
        raise ValueError("genus-two fixture payload_sha256 mismatch")
    regenerated = _load_genus2_pilot(repo_root).build_fixture()
    if regenerated != fixture:
        raise ValueError("genus-two fixture differs from exact exhaustive replay")
    statistics = fixture["family_statistics"]
    expected = {
        "member_count": 162,
        "negative_member_count": 102,
        "zero_member_count": 12,
        "positive_member_count": 48,
        "toy_minor_numerator_mean": [-104, 27],
        "normalized_toy_minor_mean": [-104, 243],
    }
    observed = {"member_count": fixture["family"]["member_count"]}
    observed.update({key: statistics[key] for key in expected if key != "member_count"})
    if observed != expected:
        raise ValueError(f"unexpected frozen genus-two controls: {observed}")
    if not all(fixture["exact_checks"].values()):
        raise ValueError("genus-two fixture contains a failed exact check")
    if fixture["asymptotic_target"]["status"] != "CONJECTURAL_TARGET_NOT_A_THEOREM":
        raise ValueError("USp(4) statement lost its target-only status")
    return fixture


def build_lfunction_spec(
    root: Path,
    config: dict[str, Any],
    fixture: dict[str, Any],
) -> dict[str, Any]:
    """Build the dedicated finite-family identity used by this evaluation."""

    timestamp = config["run_timestamp_utc"]
    generator_binding = artifact_binding(
        root, GENUS2_PILOT, "exact_genus_two_generator", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    arithmetic_binding = artifact_binding(
        root, POLYNOMIAL_PILOT, "exact_polynomial_arithmetic", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    fixture_binding = artifact_binding(
        root, GENUS2_FIXTURE, "finite_family_result", "FINITE_COMPLETE", RAW_RESULT_SCHEMA
    )
    source_identifier = "GENERATED:F3:T:MONIC_SQUAREFREE_QUINTICS:GENUS2"
    return make_lfunction_spec(
        slug=FUNCTION_FIELD_SPEC_SLUG,
        title="All monic squarefree quintic quadratic characters over F_3[T]",
        programme_numbers=[737, 741],
        source_identifiers=[source_identifier],
        construction=(
            "Finite family D -> L(u,chi_D) for every monic squarefree quintic D in F_3[T], "
            "equivalently the genus-two numerator of y^2=D(x)"
        ),
        classification={
            "domain": "FUNCTION_FIELD",
            "degree": 1,
            "object_type": "FUNCTION_FIELD_DIRICHLET_L",
            "family_id": "FF3.QUADRATIC.QUINTIC.GENUS2",
            "automorphic_class": "GL1",
            "self_duality": "SELF_DUAL",
            "symmetry_type": "SYMPLECTIC",
            "motivic_weight": 0,
        },
        base_field={
            "label": "F_3(T)",
            "characteristic": 3,
            "constant_field_order": 3,
            "variable": "T",
        },
        conductor={
            "kind": "DEGREE_ONLY",
            "value": "monic squarefree quintic D in F_3[T]",
            "norm_decimal": "243",
            "degree": 5,
            "status": "PROVED_NATIVE",
        },
        completed_normalization={
            "normalization_id": "FF.QUADRATIC.ODD_CONDUCTOR.POLYNOMIAL_U",
            "critical_center": "|u|=3^(-1/2)",
            "exact_formula": (
                "P_D(u)=L(u,chi_D)=sum_{f monic}chi_D(f)u^deg(f)="
                "product_j(1-alpha_j*u)"
            ),
            "analytic_variable": "u=3^(-s)",
            "conductor_factor": "degree(D)=5; P_D has polynomial degree 4",
            "gamma_factors": [
                {
                    "kind": "FUNCTION_FIELD_NONE",
                    "shift": "0",
                    "multiplicity": 1,
                    "scale": "1",
                }
            ],
            "notes": (
                "The GL(1) quadratic-character L-polynomial is the degree-four genus-two zeta "
                "numerator; H_D(n)=3^(-n/2)B_D(n)."
            ),
        },
        analytic_properties={
            "analytic_continuation": "PROVED_NATIVE",
            "functional_equation": "PROVED_NATIVE",
            "euler_product": "PROVED_NATIVE",
            "source_ref": GENUS2_FIXTURE,
        },
        functional_equation={
            "exact_formula": "P_D(u)=9*u^4*P_D(1/(3*u)) for every frozen family member.",
            "root_number": "+1",
            "root_number_status": "PROVED_NATIVE",
            "source_ref": GENUS2_FIXTURE,
        },
        central_data={
            "assertion": "UNKNOWN",
            "value": None,
            "rigor_level": "DISCOVERY_ONLY",
            "source_ref": "NONE",
            "parity_forced": False,
            "notes": "No central vanishing order is computed or inferred by the finite coefficient pilot.",
        },
        euler_product={
            "good_factor_formula": "P_D(u)=product_P(1-chi_D(P)u^deg(P))^(-1)",
            "bad_factor_policy": "If P divides D then chi_D(P)=0, so the local reciprocal factor is 1.",
            "reciprocal_coefficient_definition": "B_D(n)=sum_deg(f)=n mu(f)chi_D(f)",
            "coverage": (
                "All 162 conductors and every monic f required through degree 4; direct Moebius "
                "coefficients are checked against formal inversion."
            ),
            "source_refs": [source_identifier, GENUS2_FIXTURE],
            "rigor_level": "RIGOROUS_CERTIFIED",
        },
        zero_data={
            "usage": "REQUIRED",
            "coverage_class": "COMPLETE",
            "rigor_level": "RIGOROUS_CERTIFIED",
            "source_refs": [GENUS2_FIXTURE],
            "window": "all four reciprocal roots for every one of the 162 family members",
            "precision": (
                "exact palindromy plus integer pair-trace discriminant and endpoint inequalities; "
                "no numerical root approximation"
            ),
            "central_zero_policy": "NOT_APPLICABLE",
        },
        data_sources=[
            {
                "role": "exact_generator",
                "source_kind": "GENERATED_EXACT",
                "identifier": "FUNCTION_FIELD.GENUS2.PILOT.V1",
                "locator": GENUS2_PILOT,
                "version_or_retrieved_utc": timestamp,
                "coverage": "Complete deterministic enumeration of all 243 monic candidates and 162 squarefree members.",
                "rigor_level": "RIGOROUS_CERTIFIED",
                "hashes": [hash_object(generator_binding["sha256"], "raw genus2_pilot.py bytes")],
                "retention": "CHECKED_IN",
                "notes": "Exact F_3/F_9 point counts and integer pair-trace purity certificates.",
            },
            {
                "role": "exact_arithmetic_library",
                "source_kind": "GENERATED_EXACT",
                "identifier": "FUNCTION_FIELD.POLYNOMIAL.PILOT.V1",
                "locator": POLYNOMIAL_PILOT,
                "version_or_retrieved_utc": timestamp,
                "coverage": "Polynomial arithmetic, quadratic symbols, Moebius values, and reciprocal recurrence.",
                "rigor_level": "RIGOROUS_CERTIFIED",
                "hashes": [hash_object(arithmetic_binding["sha256"], "raw pilot.py bytes")],
                "retention": "CHECKED_IN",
                "notes": "Python standard-library exact integer and rational arithmetic only.",
            },
            {
                "role": "finite_family_result",
                "source_kind": "GENERATED_EXACT",
                "identifier": fixture["raw_fixture_id"],
                "locator": GENUS2_FIXTURE,
                "version_or_retrieved_utc": timestamp,
                "coverage": "All 162 monic squarefree quintic conductors, compact histograms, and sign witnesses.",
                "rigor_level": "RIGOROUS_CERTIFIED",
                "hashes": [
                    hash_object(
                        fixture_binding["sha256"],
                        "canonical JSON exact genus-two fixture",
                        "CANONICAL_JSON_UTF8_NFC",
                    )
                ],
                "retention": "CHECKED_IN",
                "notes": "The wrapper regenerates the complete fixture before constructing atlas records.",
            },
        ],
        software=config["software"],
        assumptions=[],
        notes=(
            "This dedicated family spec binds the actual F_3 quintic subjects. The finite exact "
            "purity coverage does not include, imply, or use the proposed q-to-infinity USp(4) target."
        ),
    )


def build_detector(root: Path) -> dict[str, Any]:
    normalization = [
        "Use q=3 and polynomial degree as the native reciprocal-coefficient scale.",
        "Normalize H_D(n)=3^(-n/2)B_D(n) exactly; the 2x2 determinant has common scale 3^(-2).",
        "Count exactly one point at infinity for the odd-degree model y^2=D(x).",
        "Treat the matrix only as a toy coefficient Hankel minor, never as the analytic Pick/Loewner kernel, XD, or HCNC.",
    ]
    identity_kernel = {
        "version": 1,
        "slug": DETECTOR_SLUG,
        "mathematical_definition": DETECTOR_DEFINITION,
        "kernel_convention": "COEFFICIENT_DISPERSION",
        "central_zero_policy": "NOT_APPLICABLE",
        "normalization_requirements": normalization,
        "contract_revision": 1,
    }
    semantic_id, identity_sha256 = semantic_identity("DETECTOR", DETECTOR_SLUG, identity_kernel)
    return {
        "schema_version": "riemann.atlas.detector_contract.v1",
        "record_type": "DETECTOR_CONTRACT",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact genus-two reciprocal-coefficient Hankel-minor toy probe",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(737), programme_ref(741)],
        "scope_boundary": (
            "Exact finite coefficient arithmetic only for all 162 monic squarefree quintics over F_3; "
            "no analytic Pick/Loewner, XD, HCNC, number-field, or asymptotic conclusion."
        ),
        "supersedes": [],
        "detector_kind": "COEFFICIENT_DISPERSION",
        "mathematical_definition": DETECTOR_DEFINITION,
        "kernel_convention": "COEFFICIENT_DISPERSION",
        "central_zero_policy": "NOT_APPLICABLE",
        "required_inputs": [
            {
                "name": "lfunction_spec",
                "input_type": "LFUNCTION_SPEC",
                "required": True,
                "coverage_requirement": "COMPLETE",
            },
            {
                "name": "reciprocal_coefficients",
                "input_type": "RECIPROCAL_COEFFICIENTS",
                "required": True,
                "coverage_requirement": "FINITE_COMPLETE",
            },
            {
                "name": "exact_family_fixture",
                "input_type": "RAW_ARTIFACT",
                "required": True,
                "coverage_requirement": "FINITE_COMPLETE",
            },
        ],
        "parameters": [
            {
                "name": "q",
                "value_type": "INTEGER",
                "required": True,
                "domain": "odd prime; frozen value 3",
                "constraints": {"minimum": 3, "odd": True, "frozen_value": 3},
            },
            {
                "name": "conductor_degree",
                "value_type": "INTEGER",
                "required": True,
                "domain": "positive odd integer; frozen value 5",
                "constraints": {"minimum": 1, "odd": True, "frozen_value": 5},
            },
            {
                "name": "reciprocal_degree",
                "value_type": "INTEGER",
                "required": True,
                "domain": "integer at least 3; frozen value 4",
                "constraints": {"minimum": 3, "frozen_value": 4},
            },
            {
                "name": "statistic",
                "value_type": "ENUM",
                "required": True,
                "domain": "NORMALIZED_B1_B3_MINUS_B2_SQUARED",
                "constraints": {"enum_values": ["NORMALIZED_B1_B3_MINUS_B2_SQUARED"]},
            },
            {
                "name": "infinity_convention",
                "value_type": "ENUM",
                "required": True,
                "domain": "ONE_ODD_DEGREE_POINT",
                "constraints": {"enum_values": ["ONE_ODD_DEGREE_POINT"]},
            },
        ],
        "normalization_requirements": [
            {
                "field": "configuration.q",
                "requirement": normalization[0],
                "comparison_role": "IDENTITY",
            },
            {
                "field": "configuration.statistic",
                "requirement": normalization[1],
                "comparison_role": "SCALING",
            },
            {
                "field": "configuration.infinity_convention",
                "requirement": normalization[2],
                "comparison_role": "IDENTITY",
            },
            {
                "field": "detector_kind",
                "requirement": normalization[3],
                "comparison_role": "FIREWALL",
            },
        ],
        "invariances": [
            {
                "code": "RECIPROCAL_IDENTITY",
                "statement": "Direct Moebius sums equal the formal inverse through degree four for every frozen member.",
                "status": "PROVED",
            },
            {
                "code": "GENUS2_MINOR_IDENTITY",
                "statement": "B_1*B_3-B_2^2=q*a_1^2-a_2^2 follows exactly from the palindromic degree-four polynomial.",
                "status": "PROVED",
            },
            {
                "code": "TWIST_PARITY",
                "statement": "D(T)->-D(-T) changes B_n by (-1)^n and leaves the toy minor invariant.",
                "status": "PROVED",
            },
            {
                "code": "PURITY_FORCES_MEMBERWISE_SIGN",
                "statement": "Exact reciprocal-root purity forces a fixed memberwise sign for this toy minor.",
                "status": "FALSE",
            },
        ],
        "family_adapters": [
            {
                "family": "F3_QUADRATIC_QUINTIC_GENUS2",
                "status": "REQUIRED_AVAILABLE",
                "adapter_path": GENUS2_PILOT,
                "correction": "Use the exact odd-degree infinity convention, F_9 point-count check, and degree-four reciprocal recurrence.",
            },
            {
                "family": "NUMBER_FIELD",
                "status": "UNSUPPORTED",
                "adapter_path": None,
                "correction": "No transfer from this finite function-field coefficient minor is supplied.",
            },
        ],
        "theorem_links": [
            {
                "semantic_id": "NONE",
                "status": "NONE",
                "scope": "The finite sign audit uses an internal integer certificate rather than importing a root-modulus theorem.",
            },
            {
                "semantic_id": "PROPOSED.FUNCTION_FIELD.GENUS2.USP4.TOY_MINOR_MEAN",
                "status": "PROPOSED",
                "scope": "Possible q-to-infinity mean -1; recorded only as a target and not used by the evaluation.",
            },
        ],
        "failure_modes": [
            {
                "code": "TOY_KERNEL_CONFLATION",
                "description": "A reciprocal-coefficient Hankel matrix is mistaken for an analytic Pick/Loewner, XD, or HCNC kernel.",
                "hostile_control": "The contract and result carry an explicit four-way firewall.",
            },
            {
                "code": "PURITY_TO_SIGN",
                "description": "Exact reciprocal-root modulus is incorrectly promoted to a memberwise coefficient-minor sign.",
                "hostile_control": "The exhaustive artifact contains 102 negative, 12 zero, and 48 positive members.",
            },
            {
                "code": "FINITE_TO_ASYMPTOTIC",
                "description": "The q=3 mean is treated as a proof of the proposed USp(4) limit.",
                "hostile_control": "The raw status is CONJECTURAL_TARGET_NOT_A_THEOREM and the atlas record has no theorem claim ID.",
            },
        ],
        "output_contract": {
            "representations": ["HASHED_ARTIFACT"],
            "arithmetic_classes": ["CERTIFIED_INTEGER_COVERAGE"],
            "raw_schema_path": RAW_RESULT_SCHEMA,
            "global_claim_allowed": False,
        },
        "reference_implementation": {
            "path": GENUS2_PILOT,
            "entry_point": "reciprocal_hankel_numerator",
            "version": "1",
            "source_sha256": raw_sha256(root.parents[2] / GENUS2_PILOT),
        },
        "formalization_refs": [
            {
                "state": "DEFINITION_READY",
                "target": "Degree-four reciprocal recurrence, q*a_1^2-a_2^2 identity, and exact pair-trace interval certificate.",
                "path": None,
            }
        ],
        "notes": (
            "The exact finite counterexamples concern only a declared toy coefficient minor. "
            "The proposed USp(4) mean is intentionally outside the proved invariances."
        ),
    }


def make_evaluation(
    root: Path,
    config: dict[str, Any],
    spec: dict[str, Any],
    detector: dict[str, Any],
    fixture: dict[str, Any],
) -> dict[str, Any]:
    repo_root = root.parents[2]
    genus2_adapter = artifact_binding(
        root, GENUS2_PILOT, "genus_two_exact_adapter", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    polynomial_adapter = artifact_binding(
        root, POLYNOMIAL_PILOT, "polynomial_arithmetic_adapter", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    fixture_input = artifact_binding(
        root, GENUS2_FIXTURE, "exhaustive_family_fixture", "FINITE_COMPLETE", RAW_RESULT_SCHEMA
    )
    result_binding = artifact_binding(
        root, GENUS2_FIXTURE, "detector_result", "FINITE_COMPLETE", RAW_RESULT_SCHEMA
    )
    spec_binding = content_binding(spec)
    detector_binding = content_binding(detector)
    values = {
        "q": 3,
        "conductor_degree": 5,
        "reciprocal_degree": 4,
        "statistic": "NORMALIZED_B1_B3_MINUS_B2_SQUARED",
        "infinity_convention": "ONE_ODD_DEGREE_POINT",
    }
    input_fulfillments = [
        {
            "name": "lfunction_spec",
            "input_type": "LFUNCTION_SPEC",
            "coverage_class": "COMPLETE",
            "sources": [spec["semantic_id"]],
        },
        {
            "name": "reciprocal_coefficients",
            "input_type": "RECIPROCAL_COEFFICIENTS",
            "coverage_class": "FINITE_COMPLETE",
            "sources": [GENUS2_PILOT, POLYNOMIAL_PILOT, GENUS2_FIXTURE],
        },
        {
            "name": "exact_family_fixture",
            "input_type": "RAW_ARTIFACT",
            "coverage_class": "FINITE_COMPLETE",
            "sources": [GENUS2_FIXTURE],
        },
    ]
    implementation_relative = "research/l-families/atlas/core/wrap_genus2_pilot.py"
    implementation_sha256 = raw_sha256(repo_root / implementation_relative)
    identity_kernel = {
        "version": 1,
        "slug": EVALUATION_SLUG,
        "lfunction_spec_bindings": [spec_binding],
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [genus2_adapter, polynomial_adapter],
        "configuration_sha256": sha256_hex(values),
        "input_sha256s": [fixture_input["sha256"]],
        "input_fulfillments_sha256": sha256_hex(input_fulfillments),
        "implementation_commit": config["code_commit"],
        "implementation_sha256": implementation_sha256,
        "seed": None,
    }
    semantic_id, identity_sha256 = semantic_identity("EVAL", EVALUATION_SLUG, identity_kernel)
    statistics = fixture["family_statistics"]
    return {
        "schema_version": "riemann.atlas.evaluation_record.v1",
        "record_type": "EVALUATION_RECORD",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact exhaustive F_3[T] genus-two coefficient-minor sign audit",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(737), programme_ref(741)],
        "scope_boundary": (
            "Exactly all 162 monic squarefree quintics over F_3, reciprocal degrees 0 through 4, "
            "and the declared toy 2x2 coefficient minor."
        ),
        "supersedes": [],
        "subject": {
            "kind": "L_FUNCTION_SET",
            "description": "Complete frozen q=3 monic squarefree quintic genus-two hyperelliptic family",
        },
        "lfunction_spec_bindings": [spec_binding],
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [genus2_adapter, polynomial_adapter],
        "configuration": {"values": values, "canonical_sha256": sha256_hex(values)},
        "evaluation_scope": "FINITE_EXHAUSTIVE_FAMILY",
        "input_bindings": [fixture_input],
        "input_fulfillments": input_fulfillments,
        "arithmetic": {
            "class": "CERTIFIED_INTEGER_COVERAGE",
            "directed": False,
            "rounding_contract": "No floating point and no approximated roots; all counts, recurrences, inequalities, and signs are integral.",
            "serialization_contract": "Canonical UTF-8 NFC JSON; reduced integer pairs encode the two reported rational means.",
        },
        "coverage": {
            "class": "FINITE_COMPLETE",
            "statement": (
                "Every monic squarefree quintic D in F_3[T], both F_3/F_9 point counts, "
                "and every reciprocal coefficient B_0 through B_4."
            ),
            "omissions": [
                "other odd constant fields",
                "other conductor degrees",
                "analytic Pick/Loewner, XD, and HCNC kernels",
                "proof of the proposed USp(4) limit",
            ],
        },
        "rigor_level": "RIGOROUS_CERTIFIED",
        "software": config["software"],
        "run": {
            "timestamp_utc": config["run_timestamp_utc"],
            "command": "python research/l-families/atlas/core/wrap_genus2_pilot.py --check",
            "code_commit": config["code_commit"],
            "implementation_path": implementation_relative,
            "implementation_sha256": implementation_sha256,
        },
        "central_zero_policy_applied": "NOT_APPLICABLE",
        "result": {
            "representation": "HASHED_ARTIFACT",
            "predicate_outcome": "VIOLATED",
            "artifact": result_binding,
            "summary": (
                "Integer purity certificates pass for all 162 members, while the toy minor has "
                f"{statistics['negative_member_count']} negative, "
                f"{statistics['zero_member_count']} zero, and "
                f"{statistics['positive_member_count']} positive values; "
                "its exact normalized family mean is -104/243."
            ),
        },
        "result_hashes": [
            hash_object(
                result_binding["sha256"],
                "canonical JSON exact genus-two fixture",
                "CANONICAL_JSON_UTF8_NFC",
            )
        ],
        "interpretation": {
            "status": "REFUTATION",
            "statement": (
                "Within the exhaustive q=3 quintic family, exact reciprocal-root purity and the "
                "palindromic genus-two functional equation do not force a memberwise sign for the "
                "declared toy reciprocal-coefficient minor."
            ),
            "smallest_gap": (
                "Prove or disprove the proposed USp(4) family-mean limit across odd constant fields "
                "without identifying this toy minor with an analytic kernel."
            ),
            "theorem_claim_id": None,
        },
        "assumptions": [],
        "firewalls": [
            {
                "code": "TOY_NOT_ANALYTIC_KERNEL",
                "statement": "This coefficient minor is not the atlas analytic Pick/Loewner kernel, XD, or HCNC.",
            },
            {
                "code": "FINITE_NOT_ASYMPTOTIC",
                "statement": "The exhaustive q=3 mean does not prove the proposed q-to-infinity USp(4) target.",
            },
            {
                "code": "NO_NUMBER_FIELD_TRANSFER",
                "statement": "The finite function-field computation implies no theorem for number-field L-functions.",
            },
        ],
        "notes": (
            "The raw finite arithmetic is exact, exhaustively replayed, and bound to its dedicated "
            "F_3 quintic family spec. The USp(4) statement remains proposed only and is not used in "
            "the certified finite interpretation."
        ),
    }


def run(
    root: Path = ATLAS_ROOT,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    root = root.resolve()
    config = read_json(root / "config" / "pilot.json")
    fixture = _load_and_replay_fixture(root)
    spec = build_lfunction_spec(root, config, fixture)
    detector = build_detector(root)
    evaluation = make_evaluation(root, config, spec, detector, fixture)
    return spec, detector, evaluation, fixture


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ATLAS_ROOT)
    parser.add_argument("--check", action="store_true", help="recompute and compare without writing")
    args = parser.parse_args()
    root = args.root.resolve()
    spec, detector, evaluation, _fixture = run(root)
    spec_path = root / "specs" / f"{spec['semantic_id']}.json"
    detector_path = root / "detectors" / f"{detector['semantic_id']}.json"
    evaluation_path = root / "evaluations" / f"{evaluation['semantic_id']}.json"
    if args.check:
        expected = ((spec_path, spec), (detector_path, detector), (evaluation_path, evaluation))
        mismatches = [
            str(path) for path, value in expected if not path.is_file() or read_json(path) != value
        ]
        if mismatches:
            raise SystemExit(f"genus-two atlas artifacts differ: {mismatches}")
        print("OK: exact genus-two atlas artifacts match")
        return
    write_json(spec_path, spec)
    write_json(detector_path, detector)
    write_json(evaluation_path, evaluation)
    print(
        "PASS_GENUS2_ATLAS_WRAPPER "
        f"spec={spec['semantic_id']} detector={detector['semantic_id']} "
        f"evaluation={evaluation['semantic_id']} members=162"
    )


if __name__ == "__main__":
    main()
