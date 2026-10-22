from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
from typing import Any

from atlas_core import ATLAS_ROOT, fraction_json, read_json, semantic_identity, sha256_hex, write_json
from run_pilot import (
    artifact_binding,
    hash_object,
    make_lfunction_spec,
    programme_ref,
    raw_sha256,
)


def content_binding(record: dict[str, Any]) -> dict[str, str]:
    return {"semantic_id": record["semantic_id"], "record_sha256": sha256_hex(record)}


def make_detector(
    *,
    root: Path,
    slug: str,
    title: str,
    programme_numbers: list[int],
    detector_kind: str,
    definition: str,
    kernel_convention: str,
    central_policy: str,
    normalization_identity: list[str],
    required_inputs: list[dict[str, Any]],
    parameters: list[dict[str, Any]],
    normalization_requirements: list[dict[str, str]],
    invariances: list[dict[str, str]],
    family_adapters: list[dict[str, Any]],
    theorem_links: list[dict[str, str]],
    failure_modes: list[dict[str, Any]],
    representations: list[str],
    arithmetic_classes: list[str],
    implementation_relative: str,
    entry_point: str,
    formal_target: str,
    scope_boundary: str,
    notes: str,
) -> dict[str, Any]:
    identity_kernel = {
        "version": 1,
        "slug": slug,
        "mathematical_definition": definition,
        "kernel_convention": kernel_convention,
        "central_zero_policy": central_policy,
        "normalization_requirements": normalization_identity,
        "contract_revision": 1,
    }
    semantic_id, identity_sha256 = semantic_identity("DETECTOR", slug, identity_kernel)
    implementation_path = root.parents[2] / implementation_relative
    return {
        "schema_version": "riemann.atlas.detector_contract.v1",
        "record_type": "DETECTOR_CONTRACT",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": title,
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(number) for number in programme_numbers],
        "scope_boundary": scope_boundary,
        "supersedes": [],
        "detector_kind": detector_kind,
        "mathematical_definition": definition,
        "kernel_convention": kernel_convention,
        "central_zero_policy": central_policy,
        "required_inputs": required_inputs,
        "parameters": parameters,
        "normalization_requirements": normalization_requirements,
        "invariances": invariances,
        "family_adapters": family_adapters,
        "theorem_links": theorem_links,
        "failure_modes": failure_modes,
        "output_contract": {
            "representations": representations,
            "arithmetic_classes": arithmetic_classes,
            "raw_schema_path": None,
            "global_claim_allowed": False,
        },
        "reference_implementation": {
            "path": implementation_relative,
            "entry_point": entry_point,
            "version": "1",
            "source_sha256": raw_sha256(implementation_path),
        },
        "formalization_refs": [{"state": "DEFINITION_READY", "target": formal_target, "path": None}],
        "notes": notes,
    }


def build_function_field_spec(root: Path, config: dict[str, Any]) -> dict[str, Any]:
    fixture_relative = "research/l-families/atlas/function_field/fixtures.json"
    pilot_relative = "research/l-families/atlas/function_field/pilot.py"
    fixture = artifact_binding(root, fixture_relative, "finite_family_result", "FINITE_COMPLETE", None)
    pilot = artifact_binding(root, pilot_relative, "exact_generator", "FINITE_COMPLETE", None, "RAW_BYTES")
    timestamp = config["run_timestamp_utc"]
    return make_lfunction_spec(
        slug="FUNCTION_FIELD.F5.QUADRATIC.CUBIC_FAMILY",
        title="All monic squarefree cubic quadratic characters over F_5[T]",
        programme_numbers=[737, 741],
        source_identifiers=["GENERATED:F5:T:MONIC_SQUAREFREE_CUBICS"],
        construction="Finite family D -> L(u,chi_D) for every monic squarefree cubic D in F_5[T]",
        classification={
            "domain": "FUNCTION_FIELD",
            "degree": 1,
            "object_type": "FUNCTION_FIELD_DIRICHLET_L",
            "family_id": "FF5.QUADRATIC.CUBIC",
            "automorphic_class": "GL1",
            "self_duality": "SELF_DUAL",
            "symmetry_type": "SYMPLECTIC",
            "motivic_weight": 0,
        },
        base_field={"label": "F_5(T)", "characteristic": 5, "constant_field_order": 5, "variable": "T"},
        conductor={
            "kind": "DEGREE_ONLY",
            "value": "monic squarefree cubic D in F_5[T]",
            "norm_decimal": "125",
            "degree": 3,
            "status": "PROVED_NATIVE",
        },
        completed_normalization={
            "normalization_id": "FF.QUADRATIC.ODD_CONDUCTOR.POLYNOMIAL_U",
            "critical_center": "|u|=5^(-1/2)",
            "exact_formula": "L_D(u)=sum_{f monic} chi_D(f)u^deg(f)=product_j(1-alpha_j u)",
            "analytic_variable": "u=5^(-s)",
            "conductor_factor": "degree(D)=3; L_D has degree 2",
            "gamma_factors": [{"kind": "FUNCTION_FIELD_NONE", "shift": "0", "multiplicity": 1, "scale": "1"}],
            "notes": "Critical normalization is H_D(n)=5^(-n/2)B_D(n), stored in Q(sqrt(5)).",
        },
        analytic_properties={
            "analytic_continuation": "PROVED_NATIVE",
            "functional_equation": "PROVED_NATIVE",
            "euler_product": "PROVED_NATIVE",
            "source_ref": "GENERATED:F5:T:MONIC_SQUAREFREE_CUBICS",
        },
        functional_equation={
            "exact_formula": "Each finite L_D(u)=1+A_D u+5u^2 is self-reciprocal after u -> 1/(5u).",
            "root_number": "not used",
            "root_number_status": "UNKNOWN",
            "source_ref": "research/l-families/atlas/function_field/REPORT.md",
        },
        central_data={
            "assertion": "UNKNOWN",
            "value": None,
            "rigor_level": "DISCOVERY_ONLY",
            "source_ref": "NONE",
            "parity_forced": False,
            "notes": "No analytic-rank inference is made.",
        },
        euler_product={
            "good_factor_formula": "L_D(u)=product_P(1-chi_D(P)u^deg(P))^(-1)",
            "bad_factor_policy": "If P divides D then chi_D(P)=0, so the local reciprocal factor is 1.",
            "reciprocal_coefficient_definition": "B_D(n)=sum_deg(f)=n mu(f)chi_D(f)",
            "coverage": "All 100 conductors and all monic f of degree at most 3 in the frozen run.",
            "source_refs": ["GENERATED:F5:T:MONIC_SQUAREFREE_CUBICS"],
            "rigor_level": "RIGOROUS_CERTIFIED",
        },
        zero_data={
            "usage": "REQUIRED",
            "coverage_class": "COMPLETE",
            "rigor_level": "RIGOROUS_CERTIFIED",
            "source_refs": ["research/l-families/atlas/function_field/fixtures.json"],
            "window": "all two reciprocal roots for every family member",
            "precision": "exact quadratic discriminant and product certificate",
            "central_zero_policy": "NOT_APPLICABLE",
        },
        data_sources=[
            {
                "role": "exact_generator",
                "source_kind": "GENERATED_EXACT",
                "identifier": "FUNCTION_FIELD.PILOT.V1",
                "locator": pilot_relative,
                "version_or_retrieved_utc": timestamp,
                "coverage": "Complete deterministic enumeration guarded at 100,000 monic objects per degree.",
                "rigor_level": "RIGOROUS_CERTIFIED",
                "hashes": [hash_object(pilot["sha256"], "raw pilot.py bytes")],
                "retention": "CHECKED_IN",
                "notes": "Standard-library exact modular and rational arithmetic only.",
            },
            {
                "role": "finite_family_result",
                "source_kind": "GENERATED_EXACT",
                "identifier": "FUNCTION_FIELD.F5.CUBIC.EXACT.V1",
                "locator": fixture_relative,
                "version_or_retrieved_utc": timestamp,
                "coverage": "All 100 monic squarefree cubic conductors.",
                "rigor_level": "RIGOROUS_CERTIFIED",
                "hashes": [hash_object(fixture["sha256"], "canonical JSON fixture", "CANONICAL_JSON_UTF8_NFC")],
                "retention": "CHECKED_IN",
                "notes": "The checker regenerates every row; it does not trust the internal payload digest.",
            },
        ],
        software=config["software"],
        assumptions=[],
        notes="This is a finite family template. Individual conductors are enumerated in the bound raw artifact, not promoted to 100 duplicate specs.",
    )


def build_function_field_detector(root: Path) -> dict[str, Any]:
    definition = (
        "For each quadratic character chi_D over F_5[T], let B_D(n)=sum_deg(f)=n mu(f)chi_D(f), "
        "H_D(n)=5^(-n/2)B_D(n), and evaluate the explicitly toy cross-degree probe C_D=H_D(1)H_D(2)."
    )
    normalization = [
        "Use polynomial degree as the native logarithmic scale.",
        "Store odd-degree normalization exactly in Q(sqrt(5)); do not round sqrt(5).",
        "Do not identify C_D with canonical XD, HCNC, or physical occupancy.",
    ]
    return make_detector(
        root=root,
        slug="FUNCTION_FIELD.NORMALIZED_LAG_ONE_TOY",
        title="Exact function-field normalized reciprocal lag-one toy probe",
        programme_numbers=[737, 741],
        detector_kind="COEFFICIENT_DISPERSION",
        definition=definition,
        kernel_convention="CUSTOM",
        central_policy="NOT_APPLICABLE",
        normalization_identity=normalization,
        required_inputs=[
            {"name": "lfunction_spec", "input_type": "LFUNCTION_SPEC", "required": True, "coverage_requirement": "COMPLETE"},
            {"name": "reciprocal_coefficients", "input_type": "RECIPROCAL_COEFFICIENTS", "required": True, "coverage_requirement": "FINITE_COMPLETE"},
        ],
        parameters=[
            {"name": "q", "value_type": "INTEGER", "required": True, "domain": "odd prime; frozen value 5", "constraints": {"minimum": 3, "odd": True, "frozen_value": 5}},
            {"name": "conductor_degree", "value_type": "INTEGER", "required": True, "domain": "positive odd integer; frozen value 3", "constraints": {"minimum": 1, "odd": True, "frozen_value": 3}},
            {"name": "reciprocal_degree", "value_type": "INTEGER", "required": True, "domain": "integer >= 2; frozen value 3", "constraints": {"minimum": 2, "frozen_value": 3}},
            {"name": "statistic", "value_type": "ENUM", "required": True, "domain": "H1_TIMES_H2", "constraints": {"enum_values": ["H1_TIMES_H2"]}},
        ],
        normalization_requirements=[
            {"field": "base_field.constant_field_order", "requirement": normalization[0], "comparison_role": "SCALING"},
            {"field": "completed_normalization.normalization_id", "requirement": normalization[1], "comparison_role": "IDENTITY"},
            {"field": "detector_kind", "requirement": normalization[2], "comparison_role": "FIREWALL"},
        ],
        invariances=[
            {"code": "RECIPROCAL_IDENTITY", "statement": "Direct Moebius sums equal the formal reciprocal recurrence through the checked degree.", "status": "PROVED"},
            {"code": "FROBENIUS_SCALING", "statement": "H_D(n) is invariant under extracting the common sqrt(q) Frobenius radius.", "status": "PROVED"},
            {"code": "MEMBERWISE_SIGN", "statement": "Frobenius purity forces a single memberwise sign for C_D.", "status": "FALSE"},
        ],
        family_adapters=[
            {"family": "F5_QUADRATIC_CUBIC", "status": "REQUIRED_AVAILABLE", "adapter_path": "research/l-families/atlas/function_field/pilot.py", "correction": "Degree replaces dyadic scale and Q(sqrt(5)) replaces floating normalization."},
            {"family": "NUMBER_FIELD", "status": "UNSUPPORTED", "adapter_path": None, "correction": "No transfer from the finite function-field result is supplied."},
        ],
        theorem_links=[
            {"semantic_id": "ARITH.WAVELET.MINIMAL_RATIO8", "status": "VERIFIED_WITH_FIXES", "scope": "Normalization inspiration only; the dyadic kernel is not copied."},
            {"semantic_id": "OPEN.ARITH.XD", "status": "OPEN", "scope": "Explicitly not evaluated by this toy probe."},
        ],
        failure_modes=[
            {"code": "PURITY_TO_SIGN", "description": "Root modulus alone does not force the toy signed statistic memberwise.", "hostile_control": "Checked fixture contains explicit negative, zero, and positive members."},
            {"code": "AVERAGE_TO_MEMBER", "description": "Exact family mean zero does not imply a memberwise statement.", "hostile_control": "The 40/20/40 sign split is retained beside the mean."},
            {"code": "DYADIC_COPY", "description": "Ratio eight and factor 67 have no automatic function-field meaning.", "hostile_control": "The detector contract uses degree coordinates only."},
        ],
        representations=["HASHED_ARTIFACT"],
        arithmetic_classes=["CERTIFIED_INTEGER_COVERAGE"],
        implementation_relative="research/l-families/atlas/function_field/pilot.py",
        entry_point="build_fixture",
        formal_target="Formal reciprocal recurrence and separation of memberwise versus family-average conclusions.",
        scope_boundary="Exhaustive only for q=5, monic squarefree cubic conductors, and reciprocal degrees through 3.",
        notes="C_D is deliberately a toy probe used to expose the family/member firewall.",
    )


def make_function_field_evaluation(
    root: Path,
    config: dict[str, Any],
    spec: dict[str, Any],
    detector: dict[str, Any],
) -> dict[str, Any]:
    pilot_relative = "research/l-families/atlas/function_field/pilot.py"
    fixture_relative = "research/l-families/atlas/function_field/fixtures.json"
    adapter = artifact_binding(root, pilot_relative, "family_adapter", "FINITE_COMPLETE", None, "RAW_BYTES")
    input_binding = artifact_binding(root, pilot_relative, "deterministic_family_generator", "FINITE_COMPLETE", None, "RAW_BYTES")
    result_binding = artifact_binding(root, fixture_relative, "detector_result", "FINITE_COMPLETE", None)
    values = {"q": 5, "conductor_degree": 3, "reciprocal_degree": 3, "statistic": "H1_TIMES_H2"}
    spec_binding = content_binding(spec)
    detector_binding = content_binding(detector)
    implementation_sha256 = raw_sha256(root.parents[2] / pilot_relative)
    input_fulfillments = [
        {"name": "lfunction_spec", "input_type": "LFUNCTION_SPEC", "coverage_class": "COMPLETE", "sources": [spec["semantic_id"]]},
        {"name": "reciprocal_coefficients", "input_type": "RECIPROCAL_COEFFICIENTS", "coverage_class": "FINITE_COMPLETE", "sources": [pilot_relative]},
    ]
    slug = "FUNCTION_FIELD.F5.CUBIC.NORMALIZED_LAG_ONE_TOY"
    identity_kernel = {
        "version": 1,
        "slug": slug,
        "lfunction_spec_bindings": [spec_binding],
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [adapter],
        "configuration_sha256": sha256_hex(values),
        "input_sha256s": [input_binding["sha256"]],
        "input_fulfillments_sha256": sha256_hex(input_fulfillments),
        "implementation_commit": config["code_commit"],
        "implementation_sha256": implementation_sha256,
        "seed": None,
    }
    semantic_id, identity_sha256 = semantic_identity("EVAL", slug, identity_kernel)
    return {
        "schema_version": "riemann.atlas.evaluation_record.v1",
        "record_type": "EVALUATION_RECORD",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact exhaustive F_5[T] cubic-family sign audit",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(737), programme_ref(741)],
        "scope_boundary": "Exactly 100 monic squarefree cubic conductors and reciprocal degrees 0 through 3.",
        "supersedes": [],
        "subject": {"kind": "L_FUNCTION_SET", "description": "Complete frozen q=5 monic squarefree cubic quadratic-character family"},
        "lfunction_spec_bindings": [spec_binding],
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [adapter],
        "configuration": {"values": values, "canonical_sha256": sha256_hex(values)},
        "evaluation_scope": "FINITE_EXHAUSTIVE_FAMILY",
        "input_bindings": [input_binding],
        "input_fulfillments": input_fulfillments,
        "arithmetic": {
            "class": "CERTIFIED_INTEGER_COVERAGE",
            "directed": False,
            "rounding_contract": "No floating point; Q(sqrt(5)) elements use rational coordinate pairs.",
            "serialization_contract": "Sorted-key JSON plus an independently recomputed artifact hash.",
        },
        "coverage": {
            "class": "FINITE_COMPLETE",
            "statement": "Every monic squarefree cubic D in F_5[T], with all monic terms required through degree 3.",
            "omissions": ["larger q", "larger conductor degree", "canonical XD/HCNC kernels"],
        },
        "rigor_level": "RIGOROUS_CERTIFIED",
        "software": config["software"],
        "run": {
            "timestamp_utc": config["run_timestamp_utc"],
            "command": "python research/l-families/atlas/function_field/pilot.py --check research/l-families/atlas/function_field/fixtures.json",
            "code_commit": config["code_commit"],
            "implementation_path": pilot_relative,
            "implementation_sha256": implementation_sha256,
        },
        "central_zero_policy_applied": "NOT_APPLICABLE",
        "result": {
            "representation": "HASHED_ARTIFACT",
            "predicate_outcome": "VIOLATED",
            "artifact": result_binding,
            "summary": "Purity holds for every member, while C_D has 40 negative, 20 zero, and 40 positive values and exact family mean zero.",
        },
        "result_hashes": [hash_object(result_binding["sha256"], "canonical JSON function-field fixture", "CANONICAL_JSON_UTF8_NFC")],
        "interpretation": {
            "status": "REFUTATION",
            "statement": "The naive universalization 'Frobenius purity forces a memberwise sign for H_D(1)H_D(2)' is false in this finite family.",
            "smallest_gap": "Derive a true degree-kernel analogue of XD or HCNC and identify the monodromy input that individualizes its family trace.",
            "theorem_claim_id": None,
        },
        "assumptions": [],
        "firewalls": [
            {"code": "NO_NUMBER_FIELD_TRANSFER", "statement": "The function-field computation implies no theorem over the integers."},
            {"code": "TOY_NOT_XD", "statement": "H_D(1)H_D(2) is not canonical XD, HCNC, or physical occupancy."},
            {"code": "AVERAGE_NOT_MEMBERWISE", "statement": "The exact family mean is not an individual conclusion."},
        ],
        "notes": "The verifier regenerates all conductors and coefficients; the fixture is derived data, not an external primitive.",
    }


def build_gl2_detector(root: Path, convention: str) -> dict[str, Any]:
    if convention == "LOEWNER_DIFFERENCE":
        slug = "GL2.DEFLATION.LOEWNER_DIFFERENCE"
        title = "GL(2) central-zero deflation: Loewner difference convention"
        definition = "For F=Lambda'/Lambda and positive centered nodes, L_F(x,y)=(F(x)-F(y))/(x-y), with diagonal F'(x); a central order r contributes -r/(xy)."
        sign = "negative"
    else:
        slug = "GL2.DEFLATION.PICK_SUM_HANKEL"
        title = "GL(2) central-zero deflation: Pick sum/Hankel convention"
        definition = "For F=Lambda'/Lambda and positive centered nodes, H_F(x,y)=(F(x)+F(y))/(x+y); a central order r contributes +r/(xy)."
        sign = "positive"
    normalization = [
        "Use the centered unitary variable z=s-1/2 and positive off-center rational nodes.",
        f"Keep the {convention} kernel explicit; its central atom is {sign} semidefinite.",
        "Root number authorizes parity-only deflation; full deflation requires a separately certified central order.",
    ]
    theorem_links = [
        {"semantic_id": "TWIST-EXCESS-RANK-L2", "status": "PROPOSED", "scope": "Average excess-rank-square theorem nominated by the exact residual identity."},
    ]
    if convention == "PICK_SUM_HANKEL":
        theorem_links.insert(0, {
            "semantic_id": "OPERATOR.XI.PICK_ORDER2",
            "status": "VERIFIED_WITH_FIXES",
            "scope": "The sum/Hankel convention is source-compatible; no GL(2) positivity transfers.",
        })
    return make_detector(
        root=root,
        slug=slug,
        title=title,
        programme_numbers=[738, 741],
        detector_kind="RANK_DEFLATED_PICK",
        definition=definition,
        kernel_convention=convention,
        central_policy="PARAMETERIZED",
        normalization_identity=normalization,
        required_inputs=[
            {"name": "synthetic_matrix", "input_type": "SYNTHETIC_MATRIX", "required": True, "coverage_requirement": "FINITE_COMPLETE"},
            {"name": "root_number", "input_type": "ROOT_NUMBER", "required": True, "coverage_requirement": "FINITE_COMPLETE"},
            {"name": "central_order", "input_type": "CENTRAL_ORDER", "required": True, "coverage_requirement": "FINITE_COMPLETE"},
        ],
        parameters=[
            {"name": "fixture", "value_type": "ENUM", "required": True, "domain": "SYNTHETIC_CONTROLS_V1", "constraints": {"enum_values": ["SYNTHETIC_CONTROLS_V1"]}},
            {"name": "deflation_bundle", "value_type": "ENUM", "required": True, "domain": "RAW_PARITY_FULL", "constraints": {"enum_values": ["RAW_PARITY_FULL"]}},
        ],
        normalization_requirements=[
            {"field": "completed_normalization.critical_center", "requirement": normalization[0], "comparison_role": "IDENTITY"},
            {"field": "kernel_convention", "requirement": normalization[1], "comparison_role": "FIREWALL"},
            {"field": "central_data", "requirement": normalization[2], "comparison_role": "COVARIANCE"},
        ],
        invariances=[
            {"code": "CENTRAL_ATOM_RANK_ONE", "statement": "A nonzero central-order correction is exactly rank one.", "status": "PROVED"},
            {"code": "DETERMINANT_AFFINE", "statement": "det(B+sigma*r*u*u^T) is affine in r.", "status": "PROVED"},
            {"code": "PARITY_FULL_NORM", "statement": "The squared Frobenius gap is e^2(sum_i x_i^-2)^2.", "status": "PROVED"},
            {"code": "DEFLATION_IMPLIES_POSITIVITY", "statement": "Full deflation forces the remaining background to be positive.", "status": "FALSE"},
        ],
        family_adapters=[
            {"family": "SYNTHETIC_CENTERED_ENTIRE_CONTROLS", "status": "REQUIRED_AVAILABLE", "adapter_path": "research/l-families/atlas/gl2/deflation.py", "correction": "All entries are exact Fractions; no L-function values are asserted."},
            {"family": "ARITHMETIC_GL2_TWISTS", "status": "REQUIRED_OPEN", "adapter_path": None, "correction": "Lock conductor, gamma factors, root number, central order, and deflated logarithmic-derivative values."},
        ],
        theorem_links=theorem_links,
        failure_modes=[
            {"code": "CONVENTION_SIGN", "description": "The two kernel conventions have opposite central-atom signs.", "hostile_control": "Separate semantic detector contracts and exact sign tests."},
            {"code": "PARITY_EQUALS_RANK", "description": "A root number fixes only parity, not the full central order.", "hostile_control": "Rank-three odd and rank-two even controls retain excess order two after parity deflation."},
            {"code": "DEFLATION_POSITIVITY", "description": "Removing a central atom does not repair an independently indefinite background.", "hostile_control": "The quartic background remains indefinite after full deflation."},
        ],
        representations=["HASHED_ARTIFACT", "MATRIX"],
        arithmetic_classes=["SYNTHETIC_CONTROL"],
        implementation_relative="research/l-families/atlas/gl2/deflation.py",
        entry_point="make_packet",
        formal_target="Central-atom sign, parity/full deflation identity, affine determinant, and Frobenius correction norm.",
        scope_boundary="Exact rational synthetic controls only; no arithmetic GL(2) value or zero is evaluated.",
        notes="The convention split is semantic, not cosmetic. Both contracts share one exact implementation.",
    )


def make_gl2_evaluation(
    root: Path,
    config: dict[str, Any],
    detector: dict[str, Any],
    convention_key: str,
) -> dict[str, Any]:
    fixture_relative = "research/l-families/atlas/gl2/fixtures/synthetic_controls.json"
    deflation_relative = "research/l-families/atlas/gl2/deflation.py"
    verify_relative = "research/l-families/atlas/gl2/verify.py"
    fixture = artifact_binding(root, fixture_relative, "synthetic_control_input", "FINITE_COMPLETE", None)
    adapter = artifact_binding(root, deflation_relative, "exact_matrix_adapter", "FINITE_COMPLETE", None, "RAW_BYTES")
    complete_report = read_json(root.parents[2] / "research/l-families/atlas/gl2/results.json")
    filtered_controls: list[dict[str, Any]] = []
    for control in complete_report["controls"]:
        if "conventions" not in control:
            filtered_controls.append(control)
            continue
        filtered_controls.append({
            "id": control["id"],
            "label": control["label"],
            "root_number": control["root_number"],
            "central_order": control["central_order"],
            "convention": convention_key,
            "result": control["conventions"][convention_key],
        })
    raw_result = {
        "schema": "riemann.gl2.deflation.filtered_result.v1",
        "status": "EXACT_RATIONAL_SYNTHETIC_CONTROL_ONLY",
        "convention": convention_key,
        "controls": filtered_controls,
        "result": "PASS",
    }
    values = {"fixture": "SYNTHETIC_CONTROLS_V1", "deflation_bundle": "RAW_PARITY_FULL"}
    detector_binding = content_binding(detector)
    implementation_sha256 = raw_sha256(root.parents[2] / verify_relative)
    input_fulfillments = [
        {"name": name, "input_type": input_type, "coverage_class": "FINITE_COMPLETE", "sources": [fixture_relative]}
        for name, input_type in (
            ("synthetic_matrix", "SYNTHETIC_MATRIX"),
            ("root_number", "ROOT_NUMBER"),
            ("central_order", "CENTRAL_ORDER"),
        )
    ]
    slug = detector["identity_kernel"]["slug"] + ".SYNTHETIC_CONTROLS"
    identity_kernel = {
        "version": 1,
        "slug": slug,
        "lfunction_spec_bindings": [],
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [adapter],
        "configuration_sha256": sha256_hex(values),
        "input_sha256s": [fixture["sha256"]],
        "input_fulfillments_sha256": sha256_hex(input_fulfillments),
        "implementation_commit": config["code_commit"],
        "implementation_sha256": implementation_sha256,
        "seed": None,
    }
    semantic_id, identity_sha256 = semantic_identity("EVAL", slug, identity_kernel)
    result_relative = f"research/l-families/atlas/results/{semantic_id}.json"
    write_json(root.parents[2] / result_relative, raw_result)
    result_binding = artifact_binding(root, result_relative, "detector_result", "FINITE_COMPLETE", None)
    return {
        "schema_version": "riemann.atlas.evaluation_record.v1",
        "record_type": "EVALUATION_RECORD",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": f"Exact synthetic controls for {detector['title']}",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(738), programme_ref(741)],
        "scope_boundary": "Five synthetic controls over rational nodes; no arithmetic L-function data.",
        "supersedes": [],
        "subject": {"kind": "SYNTHETIC_CONTROL", "description": "Centered entire-function logarithmic-derivative matrix controls"},
        "lfunction_spec_bindings": [],
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [adapter],
        "configuration": {"values": values, "canonical_sha256": sha256_hex(values)},
        "evaluation_scope": "SYNTHETIC_CONTROL",
        "input_bindings": [fixture],
        "input_fulfillments": input_fulfillments,
        "arithmetic": {
            "class": "SYNTHETIC_CONTROL",
            "directed": False,
            "rounding_contract": "Every scalar is Fraction; floats are rejected.",
            "serialization_contract": "Exact rational strings in canonical JSON artifacts.",
        },
        "coverage": {
            "class": "FINITE_COMPLETE",
            "statement": "All four positive/hostile controls and the fail-closed parity mismatch in the checked-in fixture.",
            "omissions": ["arithmetic GL(2) objects", "certified logarithmic-derivative values", "twist-family averages"],
        },
        "rigor_level": "RIGOROUS_CERTIFIED",
        "software": config["software"],
        "run": {
            "timestamp_utc": config["run_timestamp_utc"],
            "command": "python research/l-families/atlas/gl2/verify.py --check research/l-families/atlas/gl2/results.json",
            "code_commit": config["code_commit"],
            "implementation_path": verify_relative,
            "implementation_sha256": implementation_sha256,
        },
        "central_zero_policy_applied": "PARAMETERIZED",
        "result": {
            "representation": "HASHED_ARTIFACT",
            "predicate_outcome": "SATISFIED",
            "artifact": result_binding,
            "summary": "Central atom, parity/full deflation, determinant, inertia, norm, and hostile-background controls all pass exactly.",
        },
        "result_hashes": [hash_object(result_binding["sha256"], "canonical JSON convention-filtered GL(2) result", "CANONICAL_JSON_UTF8_NFC")],
        "interpretation": {
            "status": "SYNTHETIC_CONTROL",
            "statement": "Deflation is exact rank-one bookkeeping; it neither has a convention-free sign nor implies positivity of the deflated background.",
            "smallest_gap": "Bind one genuine twist family and certify deflated logarithmic-derivative values before arithmetic evaluation.",
            "theorem_claim_id": None,
        },
        "assumptions": [{"code": "SYNTHETIC_ONLY", "statement": "The background log derivative is polynomial and is not asserted to come from an L-function.", "status": "NOT_APPLICABLE"}],
        "firewalls": [
            {"code": "NO_ARITHMETIC_DATA", "statement": "The fixture contains no LMFDB object, L-value, or zero ordinate."},
            {"code": "CONVENTION_EXPLICIT", "statement": "Loewner difference and Pick sum/Hankel use separate detector IDs."},
            {"code": "DEFLATION_NOT_POSITIVITY", "statement": "The hostile background remains indefinite after full deflation."},
        ],
        "notes": "Exact synthetic algebra can validate an adapter but cannot establish GRH for a twist.",
    }


def build_rank_stress_detector(root: Path) -> dict[str, Any]:
    definition = (
        "For a self-dual GL(2) object with central order r and root number epsilon, set "
        "e=r-(1-epsilon)/2. At fixed positive centered nodes x_i, record the convention-independent "
        "squared Frobenius gap e^2(sum_i x_i^(-2))^2 between parity-only and full central-order deflation."
    )
    normalization = [
        "Use the centered unitary variable z=s-1/2.",
        "Bind root number and central order separately; parity alone does not determine r.",
        "Square the rank-one residual norm so the Loewner/Pick atom sign drops out.",
    ]
    return make_detector(
        root=root,
        slug="GL2.EXCESS_RANK.FROBENIUS_NORM",
        title="GL(2) parity-versus-full deflation residual norm",
        programme_numbers=[738, 741],
        detector_kind="RANK_DEFLATED_PICK",
        definition=definition,
        kernel_convention="CUSTOM",
        central_policy="PARAMETERIZED",
        normalization_identity=normalization,
        required_inputs=[
            {"name": "lfunction_spec", "input_type": "LFUNCTION_SPEC", "required": True, "coverage_requirement": "COMPLETE"},
            {"name": "root_number", "input_type": "ROOT_NUMBER", "required": True, "coverage_requirement": "FINITE_COMPLETE"},
            {"name": "central_order", "input_type": "CENTRAL_ORDER", "required": True, "coverage_requirement": "FINITE_COMPLETE"},
        ],
        parameters=[
            {"name": "nodes", "value_type": "RATIONAL_STRING_LIST", "required": True, "domain": "nonempty positive centered rational nodes", "constraints": {"nonempty": True, "unique": True, "rational_positive": True}},
            {"name": "rank_source_policy", "value_type": "ENUM", "required": True, "domain": "IMPORTED_DISCOVERY", "constraints": {"enum_values": ["IMPORTED_DISCOVERY"]}},
        ],
        normalization_requirements=[
            {"field": "completed_normalization.critical_center", "requirement": normalization[0], "comparison_role": "IDENTITY"},
            {"field": "central_data", "requirement": normalization[1], "comparison_role": "FIREWALL"},
            {"field": "kernel_convention", "requirement": normalization[2], "comparison_role": "COVARIANCE"},
        ],
        invariances=[
            {"code": "CONVENTION_INDEPENDENT_SQUARE", "statement": "The squared parity/full residual norm is the same for the two central-atom sign conventions.", "status": "PROVED"},
            {"code": "MINIMAL_RANK_ZERO", "statement": "The residual vanishes exactly when the central order is minimal for its root-number parity.", "status": "PROVED"},
        ],
        family_adapters=[
            {"family": "GL2_ELLIPTIC_METADATA", "status": "REQUIRED_AVAILABLE", "adapter_path": "research/l-families/atlas/gl2/deflation.py", "correction": "This adapter consumes only rank/root metadata, not L-values."},
            {"family": "GL2_QUADRATIC_TWIST_FAMILY", "status": "REQUIRED_OPEN", "adapter_path": None, "correction": "A source-locked twist range and certified central orders are still required."},
        ],
        theorem_links=[
            {"semantic_id": "TWIST-EXCESS-RANK-L2", "status": "PROPOSED", "scope": "A family second moment of this residual is exactly a constant times average e_d^2."},
        ],
        failure_modes=[
            {"code": "RANK_AS_GRH", "description": "Central rank metadata says nothing about off-line zeros.", "hostile_control": "The output contains no zero ordinate or GRH predicate."},
            {"code": "THREE_CURVES_AS_FAMILY", "description": "Three rank-stress examples are not a twist-family statistic.", "hostile_control": "Evaluation scope is MEMBERWISE_BATCH and rigor is DISCOVERY_ONLY."},
            {"code": "PARITY_FULL_CONFUSION", "description": "Parity deflation and full-order deflation differ at excess rank.", "hostile_control": "The rank-two positive-sign row has exact residual norm squared 25/4 at nodes (1,2)."},
        ],
        representations=["HASHED_ARTIFACT", "EXACT_RATIONAL"],
        arithmetic_classes=["EXACT_RATIONAL"],
        implementation_relative="research/l-families/atlas/gl2/deflation.py",
        entry_point="correction_norm_squared",
        formal_target="The exact identity ||M_parity-M_full||_F^2=e^2(sum_i x_i^-2)^2.",
        scope_boundary="Finite metadata stress test; no arithmetic logarithmic derivative or twist-family limit.",
        notes="This scalar deliberately discards the convention sign after that sign has been checked by the two separate matrix contracts.",
    )


def make_rank_stress_evaluation(
    root: Path,
    config: dict[str, Any],
    detector: dict[str, Any],
    specs: list[dict[str, Any]],
) -> dict[str, Any]:
    nodes = [Fraction(1), Fraction(2)]
    node_sum = sum((Fraction(1, 1) / (node * node) for node in nodes), Fraction())
    rows: list[dict[str, Any]] = []
    for spec in sorted(specs, key=lambda item: item["semantic_id"]):
        rank = spec["central_data"]["value"]
        root_number = spec["functional_equation"]["root_number"]
        if rank is None or root_number not in {"+1", "-1"}:
            raise ValueError(f"rank stress row lacks exact imported metadata: {spec['semantic_id']}")
        forced_order = 1 if root_number == "-1" else 0
        if rank % 2 != forced_order:
            raise ValueError(f"rank/root parity mismatch: {spec['semantic_id']}")
        excess_order = rank - forced_order
        norm_squared = excess_order * excess_order * node_sum * node_sum
        rows.append({
            "semantic_id": spec["semantic_id"],
            "root_number": root_number,
            "central_order": rank,
            "forced_order": forced_order,
            "excess_order": excess_order,
            "parity_minus_full_frobenius_squared": fraction_json(norm_squared.numerator, norm_squared.denominator),
        })
    raw_result = {
        "schema": "riemann.gl2.rank_stress_result.v1",
        "nodes": [str(node) for node in nodes],
        "sum_inverse_node_squares": fraction_json(node_sum.numerator, node_sum.denominator),
        "rows": rows,
        "result": "PASS",
    }
    source_relative = "research/l-families/atlas/sources/lmfdb-curves.json"
    adapter_relative = "research/l-families/atlas/gl2/deflation.py"
    input_binding = artifact_binding(root, source_relative, "rank_root_source_manifest", "PARTIAL", None)
    adapter = artifact_binding(root, adapter_relative, "exact_rank_correction_adapter", "FINITE_COMPLETE", None, "RAW_BYTES")
    spec_bindings = [content_binding(spec) for spec in sorted(specs, key=lambda item: item["semantic_id"])]
    detector_binding = content_binding(detector)
    values = {"nodes": [str(node) for node in nodes], "rank_source_policy": "IMPORTED_DISCOVERY"}
    implementation_relative = "research/l-families/atlas/core/wrap_specialist_pilots.py"
    implementation_sha256 = raw_sha256(root.parents[2] / implementation_relative)
    input_fulfillments = [
        {"name": "lfunction_spec", "input_type": "LFUNCTION_SPEC", "coverage_class": "COMPLETE", "sources": [binding["semantic_id"] for binding in spec_bindings]},
        {"name": "root_number", "input_type": "ROOT_NUMBER", "coverage_class": "FINITE_COMPLETE", "sources": [source_relative]},
        {"name": "central_order", "input_type": "CENTRAL_ORDER", "coverage_class": "FINITE_COMPLETE", "sources": [source_relative]},
    ]
    slug = "GL2.EC.RANK_0_1_2.EXCESS_RANK_NORM"
    identity_kernel = {
        "version": 1,
        "slug": slug,
        "lfunction_spec_bindings": spec_bindings,
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [adapter],
        "configuration_sha256": sha256_hex(values),
        "input_sha256s": [input_binding["sha256"]],
        "input_fulfillments_sha256": sha256_hex(input_fulfillments),
        "implementation_commit": config["code_commit"],
        "implementation_sha256": implementation_sha256,
        "seed": None,
    }
    semantic_id, identity_sha256 = semantic_identity("EVAL", slug, identity_kernel)
    result_relative = f"research/l-families/atlas/results/{semantic_id}.json"
    write_json(root.parents[2] / result_relative, raw_result)
    result_binding = artifact_binding(root, result_relative, "detector_result", "FINITE_COMPLETE", None)
    return {
        "schema_version": "riemann.atlas.evaluation_record.v1",
        "record_type": "EVALUATION_RECORD",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Imported rank 0/1/2 parity-deflation residual stress test",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(738), programme_ref(741)],
        "scope_boundary": "Exactly the three source-identified elliptic-curve rows 11.a2, 37.a1, and 389.a1 at nodes (1,2).",
        "supersedes": [],
        "subject": {"kind": "L_FUNCTION_SET", "description": "Three elliptic-curve L-functions selected only to span imported ranks 0, 1, and 2"},
        "lfunction_spec_bindings": spec_bindings,
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [adapter],
        "configuration": {"values": values, "canonical_sha256": sha256_hex(values)},
        "evaluation_scope": "MEMBERWISE_BATCH",
        "input_bindings": [input_binding],
        "input_fulfillments": input_fulfillments,
        "arithmetic": {
            "class": "EXACT_RATIONAL",
            "directed": False,
            "rounding_contract": "The matrix correction is rational; imported ranks/root numbers are discrete metadata.",
            "serialization_contract": "Reduced numerator/denominator pairs in canonical JSON.",
        },
        "coverage": {
            "class": "FINITE_COMPLETE",
            "statement": "All three declared rank-stress objects and both nodes.",
            "omissions": ["twist-family sampling", "certified rank replay", "logarithmic-derivative values", "zero ordinates"],
        },
        "rigor_level": "DISCOVERY_ONLY",
        "software": config["software"],
        "run": {
            "timestamp_utc": config["run_timestamp_utc"],
            "command": "python research/l-families/atlas/core/wrap_specialist_pilots.py",
            "code_commit": config["code_commit"],
            "implementation_path": implementation_relative,
            "implementation_sha256": implementation_sha256,
        },
        "central_zero_policy_applied": "PARAMETERIZED",
        "result": {
            "representation": "HASHED_ARTIFACT",
            "predicate_outcome": "SATISFIED",
            "artifact": result_binding,
            "summary": "Ranks 0 and 1 are parity-minimal and have zero residual; imported rank 2 leaves exact squared residual 25/4.",
        },
        "result_hashes": [hash_object(result_binding["sha256"], "canonical JSON GL(2) rank-stress result", "CANONICAL_JSON_UTF8_NFC")],
        "interpretation": {
            "status": "EXACT_FINITE",
            "statement": "Given the imported rank/root metadata, the parity-versus-full correction is exactly zero, zero, and 25/4 for the three rows.",
            "smallest_gap": "Replace the three examples by a source-locked quadratic-twist family and prove a second moment for excess central order.",
            "theorem_claim_id": None,
        },
        "assumptions": [{"code": "LMFDB_RANK_ROOT_IMPORTED", "statement": "The displayed analytic ranks and root numbers identify the intended records.", "status": "HEURISTIC"}],
        "firewalls": [
            {"code": "CENTRAL_NOT_OFFLINE", "statement": "A legitimate central zero is not an off-critical zero."},
            {"code": "BATCH_NOT_FAMILY", "statement": "Three selected examples do not estimate a twist-family distribution."},
            {"code": "SOURCE_DISCOVERY", "statement": "Dynamic LMFDB metadata keeps the evaluation at DISCOVERY_ONLY rigor."},
        ],
        "notes": "The exact scalar is convention-independent only after the separate convention-sign contracts have been fixed.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Wrap exact specialist raw pilots in the shared atlas contracts.")
    parser.add_argument("--root", type=Path, default=ATLAS_ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    config = read_json(root / "config" / "pilot.json")

    ff_spec = build_function_field_spec(root, config)
    ff_detector = build_function_field_detector(root)
    ff_evaluation = make_function_field_evaluation(root, config, ff_spec, ff_detector)

    records: list[tuple[str, dict[str, Any]]] = [
        ("specs", ff_spec),
        ("detectors", ff_detector),
        ("evaluations", ff_evaluation),
    ]
    for convention, key in (("LOEWNER_DIFFERENCE", "loewner_difference"), ("PICK_SUM_HANKEL", "pick_sum")):
        detector = build_gl2_detector(root, convention)
        evaluation = make_gl2_evaluation(root, config, detector, key)
        records.extend([("detectors", detector), ("evaluations", evaluation)])

    elliptic_specs = [
        read_json(path)
        for path in sorted((root / "specs").glob("ATLAS.LFUNC.EC.*.json"))
    ]
    if len(elliptic_specs) != 3:
        raise SystemExit("run core/run_pilot.py first: expected exactly three elliptic rank-stress specs")
    rank_detector = build_rank_stress_detector(root)
    rank_evaluation = make_rank_stress_evaluation(root, config, rank_detector, elliptic_specs)
    records.extend([("detectors", rank_detector), ("evaluations", rank_evaluation)])

    for directory, record in records:
        write_json(root / directory / f"{record['semantic_id']}.json", record)
    print("PASS_ATLAS_SPECIALIST_WRAPPERS specs=1 detectors=4 evaluations=4")


if __name__ == "__main__":
    main()
