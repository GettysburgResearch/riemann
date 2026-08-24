#!/usr/bin/env python3
"""Register the exact q=3,5,7 genus-two scan as DRAFT atlas records."""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any, Sequence

from atlas_core import ATLAS_ROOT, read_json, semantic_identity, sha256_hex, write_json
from run_pilot import (
    artifact_binding,
    hash_object,
    make_lfunction_spec,
    programme_ref,
    raw_sha256,
)


Q_VALUES = (3, 5, 7)
EXISTING_F3_SPEC_SLUG = "FUNCTION_FIELD.F3.QUADRATIC.QUINTIC_GENUS2_FAMILY"
Q_SCAN_SOURCE = "research/l-families/atlas/function_field/genus2_q_scan.py"
POLYNOMIAL_SOURCE = "research/l-families/atlas/function_field/pilot.py"
Q_SCAN_FIXTURE = "research/l-families/atlas/function_field/genus2_q_scan.json"
AFFINE_ORBIT_SOURCE = (
    "research/l-families/atlas/function_field/genus2_affine_orbits.py"
)
AFFINE_ORBIT_FIXTURE = (
    "research/l-families/atlas/function_field/genus2_affine_orbits.json"
)
MOMENT_IDENTITY_NOTE = (
    "research/l-families/atlas/function_field/GENUS2_MOMENT_IDENTITY.md"
)
MOMENT_IDENTITY_CERTIFICATE = (
    "research/l-families/atlas/function_field/genus2_moment_identity.py"
)
RAW_RESULT_SCHEMA = (
    "research/l-families/atlas/detectors/raw-schemas/"
    "function-field-genus2-q-scan-result.schema.json"
)
DETECTOR_SLUG = "FUNCTION_FIELD.GENUS2.TOY_MINOR.FINITE_FAMILY_MOMENTS"
EVALUATION_SLUG = "FUNCTION_FIELD.GENUS2.Q3_Q5_Q7.TOY_MINOR.MOMENT_SCAN"
FORMULA_STATUS = "PROVED_IN_DRAFT_RESEARCH_NOTE"
MEAN_LIMIT_STATUS = "PROVED_FROM_EXACT_FORMULA"
SIGN_DENSITY_STATUS = "PROVED_FROM_EXACT_MEAN_AND_USP4_RANGE"
AFFINE_ORBIT_STATUS = "PROVED_EXACTLY_AND_EXHAUSTIVELY_REPLAYED_ON_FROZEN_FIELDS"
DETECTOR_DEFINITION = (
    "For each monic squarefree quintic D over F_q, q in {3,5,7}, reconstruct "
    "P_D(u)=1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4 from exact F_q and F_(q^2) "
    "character sums, set K_D=q*a_D^2-b_D^2=B_D(1)B_D(3)-B_D(2)^2, and record "
    "the exact finite-family moments of K_D and K_D/q^2."
)


def content_binding(record: dict[str, Any]) -> dict[str, str]:
    return {"semantic_id": record["semantic_id"], "record_sha256": sha256_hex(record)}


def _load_q_scan_module(repo_root: Path) -> ModuleType:
    path = repo_root / Q_SCAN_SOURCE
    function_field_dir = str(path.parent)
    if function_field_dir not in sys.path:
        sys.path.insert(0, function_field_dir)
    module_spec = importlib.util.spec_from_file_location("_riemann_atlas_genus2_q_scan", path)
    if module_spec is None or module_spec.loader is None:
        raise RuntimeError(f"cannot load exact q-scan module: {path}")
    module = importlib.util.module_from_spec(module_spec)
    sys.modules[module_spec.name] = module
    module_spec.loader.exec_module(module)
    return module


def _load_affine_orbit_module(repo_root: Path) -> ModuleType:
    path = repo_root / AFFINE_ORBIT_SOURCE
    function_field_dir = str(path.parent)
    if function_field_dir not in sys.path:
        sys.path.insert(0, function_field_dir)
    module_spec = importlib.util.spec_from_file_location(
        "_riemann_atlas_genus2_affine_orbits", path
    )
    if module_spec is None or module_spec.loader is None:
        raise RuntimeError(f"cannot load exact affine-orbit module: {path}")
    module = importlib.util.module_from_spec(module_spec)
    sys.modules[module_spec.name] = module
    module_spec.loader.exec_module(module)
    return module


def load_and_replay_fixture(root: Path) -> dict[str, Any]:
    repo_root = root.parents[2]
    fixture = read_json(repo_root / Q_SCAN_FIXTURE)
    claimed_payload_sha256 = fixture.get("payload_sha256")
    payload = dict(fixture)
    payload.pop("payload_sha256", None)
    if claimed_payload_sha256 != sha256_hex(payload):
        raise ValueError("q-scan fixture payload hash mismatch")
    regenerated = _load_q_scan_module(repo_root).build_fixture()
    if regenerated != fixture:
        raise ValueError("q-scan fixture differs from its <=8-second exact replay")
    if fixture["closed_formula_target"]["status"] != FORMULA_STATUS:
        raise ValueError("closed formula lost its proof-backed status")
    if fixture["closed_formula_target"].get("not_a_theorem") is not False:
        raise ValueError("closed formula is not marked as a theorem in the DRAFT note")
    if fixture["usp4_limit_target"]["status"] != MEAN_LIMIT_STATUS:
        raise ValueError("first-moment limit lost its proof-backed status")
    if fixture["usp4_limit_target"].get("not_a_theorem") is not False:
        raise ValueError("first-moment limit is not marked as proved from the formula")
    sign_density = fixture.get("negative_proportion_corollary", {})
    if sign_density.get("status") != SIGN_DENSITY_STATUS:
        raise ValueError("negative-sign density corollary lost its proof-backed status")
    if sign_density.get("scope") != "every odd prime power q":
        raise ValueError("negative-sign density corollary scope drifted")
    if sign_density.get("range_lower_bound") != -20:
        raise ValueError("negative-sign density corollary lost the exact USp(4) range bound")
    if sign_density.get("liminf_lower_bound") != [1, 20]:
        raise ValueError("negative-sign density liminf lower bound drifted")
    if fixture["resource_contract"]["candidate_cap"] != 20_000:
        raise ValueError("q-scan candidate cap drifted")
    if fixture["resource_contract"].get("candidate_cap_scope") != "PER_FIELD_Q_SCAN":
        raise ValueError("q-scan candidate cap is not explicitly per-field")
    if fixture["resource_contract"]["maximum_wall_seconds"] > 8.0:
        raise ValueError("q-scan wall guard exceeds eight seconds")
    return fixture


def load_and_replay_affine_fixture(root: Path) -> dict[str, Any]:
    repo_root = root.parents[2]
    fixture = read_json(repo_root / AFFINE_ORBIT_FIXTURE)
    claimed_payload_sha256 = fixture.get("payload_sha256")
    payload = dict(fixture)
    payload.pop("payload_sha256", None)
    if claimed_payload_sha256 != sha256_hex(payload):
        raise ValueError("affine-orbit fixture payload hash mismatch")
    regenerated = _load_affine_orbit_module(repo_root).build_fixture()
    if regenerated != fixture:
        raise ValueError("affine-orbit fixture differs from its <=8-second exact replay")
    if fixture.get("exact_proof", {}).get("status") != AFFINE_ORBIT_STATUS:
        raise ValueError("affine coefficient law lost its exact proof status")
    transformation_law = fixture.get("action", {}).get("transformation_law", {})
    if transformation_law != {
        "a_D": "a_{D^{alpha,beta}}=chi_q(alpha)*a_D",
        "b_D": "b_{D^{alpha,beta}}=b_D",
        "K_D": "K_{D^{alpha,beta}}=K_D for K_D=q*a_D^2-b_D^2",
    }:
        raise ValueError("affine coefficient transformation law drifted")
    resource = fixture.get("resource_contract", {})
    if resource.get("frozen_q_values") != [3, 5, 7]:
        raise ValueError("affine-orbit fixture field scope drifted")
    if resource.get("candidate_cap") != 20_000:
        raise ValueError("affine-orbit candidate cap drifted")
    if resource.get("candidate_cap_scope") != "PER_FIELD":
        raise ValueError("affine-orbit candidate cap is not explicitly per-field")
    if resource.get("maximum_global_wall_seconds", 9.0) > 8.0:
        raise ValueError("affine-orbit wall guard exceeds eight seconds")
    expected = {
        3: (162, 6, 972, 29),
        5: (2500, 20, 50_000, 132),
        7: (14_406, 42, 605_052, 349),
    }
    families = fixture.get("families", [])
    if [family.get("q") for family in families] != [3, 5, 7]:
        raise ValueError("affine-orbit family ordering drifted")
    for family in families:
        q = int(family["q"])
        observed = (
            family.get("member_count"),
            family.get("group", {}).get("order"),
            family.get("action_checks", {}).get("member_action_pairs_checked"),
            family.get("orbit_partition", {}).get("orbit_count"),
        )
        if observed != expected[q]:
            raise ValueError(f"q={q} affine-orbit coverage summary drifted")
    regression_controls = fixture.get("q_scan_regression_controls", {})
    if set(regression_controls) != {"3", "5", "7"} or not all(
        all(checks.values()) for checks in regression_controls.values()
    ):
        raise ValueError("affine-orbit q-scan regression controls failed")
    return fixture


def load_existing_f3_spec(root: Path) -> dict[str, Any]:
    matches = []
    for path in sorted((root / "specs").glob("ATLAS.LFUNC.*.json")):
        record = read_json(path)
        if record.get("identity_kernel", {}).get("slug") == EXISTING_F3_SPEC_SLUG:
            matches.append(record)
    if len(matches) != 1:
        raise ValueError(
            f"expected exactly one existing F_3 genus-two spec, found {len(matches)}"
        )
    return matches[0]


def build_family_spec(
    root: Path,
    config: dict[str, Any],
    family: dict[str, Any],
) -> dict[str, Any]:
    q = int(family["q"])
    if q not in (5, 7):
        raise ValueError("only the new F_5 and F_7 specs are built here")
    source_identifier = f"GENERATED:F{q}:T:MONIC_SQUAREFREE_QUINTICS:GENUS2"
    timestamp = config["run_timestamp_utc"]
    generator_binding = artifact_binding(
        root, Q_SCAN_SOURCE, "exact_multi_q_generator", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    arithmetic_binding = artifact_binding(
        root, POLYNOMIAL_SOURCE, "exact_polynomial_arithmetic", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    fixture_binding = artifact_binding(
        root, Q_SCAN_FIXTURE, "finite_family_scan", "FINITE_COMPLETE", None
    )
    return make_lfunction_spec(
        slug=f"FUNCTION_FIELD.F{q}.QUADRATIC.QUINTIC_GENUS2_FAMILY",
        title=f"All monic squarefree quintic quadratic characters over F_{q}[T]",
        programme_numbers=[737, 741],
        source_identifiers=[source_identifier],
        construction=(
            f"Finite family D -> L(u,chi_D) for every monic squarefree quintic D in F_{q}[T], "
            "equivalently the genus-two numerator of y^2=D(x)"
        ),
        classification={
            "domain": "FUNCTION_FIELD",
            "degree": 1,
            "object_type": "FUNCTION_FIELD_DIRICHLET_L",
            "family_id": f"FF{q}.QUADRATIC.QUINTIC.GENUS2",
            "automorphic_class": "GL1",
            "self_duality": "SELF_DUAL",
            "symmetry_type": "SYMPLECTIC",
            "motivic_weight": 0,
        },
        base_field={
            "label": f"F_{q}(T)",
            "characteristic": q,
            "constant_field_order": q,
            "variable": "T",
        },
        conductor={
            "kind": "DEGREE_ONLY",
            "value": f"monic squarefree quintic D in F_{q}[T]",
            "norm_decimal": str(q**5),
            "degree": 5,
            "status": "PROVED_NATIVE",
        },
        completed_normalization={
            "normalization_id": "FF.QUADRATIC.ODD_CONDUCTOR.POLYNOMIAL_U",
            "critical_center": f"|u|={q}^(-1/2)",
            "exact_formula": (
                "P_D(u)=L(u,chi_D)=sum_(f monic)chi_D(f)u^deg(f)="
                "product_j(1-alpha_j*u)"
            ),
            "analytic_variable": f"u={q}^(-s)",
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
                "The registered experiment uses only exact finite character-sum coefficients a_D,b_D; "
                "it imports no zero coordinates."
            ),
        },
        analytic_properties={
            "analytic_continuation": "IMPORTED_THEOREM",
            "functional_equation": "IMPORTED_THEOREM",
            "euler_product": "IMPORTED_THEOREM",
            "source_ref": "CLASSICAL_FUNCTION_FIELD_CURVE_ZETA_THEORY",
        },
        functional_equation={
            "exact_formula": f"P_D(u)={q**2}*u^4*P_D(1/({q}*u)).",
            "root_number": "+1",
            "root_number_status": "IMPORTED_THEOREM",
            "source_ref": "CLASSICAL_FUNCTION_FIELD_CURVE_ZETA_THEORY",
        },
        central_data={
            "assertion": "UNKNOWN",
            "value": None,
            "rigor_level": "DISCOVERY_ONLY",
            "source_ref": "NONE",
            "parity_forced": False,
            "notes": "No central vanishing order is computed or inferred by this coefficient scan.",
        },
        euler_product={
            "good_factor_formula": "P_D(u)=product_P(1-chi_D(P)u^deg(P))^(-1)",
            "bad_factor_policy": "If P divides D then chi_D(P)=0, so the local reciprocal factor is 1.",
            "reciprocal_coefficient_definition": "B_D(n)=sum_deg(f)=n mu(f)chi_D(f)",
            "coverage": (
                f"The exact q-scan covers all {family['member_count']} monic squarefree quintics, "
                "using point-character sums rather than per-member Euler enumeration."
            ),
            "source_refs": [source_identifier, Q_SCAN_FIXTURE],
            "rigor_level": "RIGOROUS_CERTIFIED",
        },
        zero_data={
            "usage": "NOT_USED",
            "coverage_class": "NOT_APPLICABLE",
            "rigor_level": "DISCOVERY_ONLY",
            "source_refs": [],
            "window": None,
            "precision": None,
            "central_zero_policy": "NOT_APPLICABLE",
        },
        data_sources=[
            {
                "role": "exact_generator",
                "source_kind": "GENERATED_EXACT",
                "identifier": "FUNCTION_FIELD.GENUS2.Q_SCAN.V1",
                "locator": Q_SCAN_SOURCE,
                "version_or_retrieved_utc": timestamp,
                "coverage": "Frozen exact q=3,5,7 coefficient scan with a 20,000-candidate per-field cap and <=8-second global guard.",
                "rigor_level": "RIGOROUS_CERTIFIED",
                "hashes": [hash_object(generator_binding["sha256"], "raw genus2_q_scan.py bytes")],
                "retention": "CHECKED_IN",
                "notes": "No numerical roots, floating point, or family-wide Euler enumeration.",
            },
            {
                "role": "exact_arithmetic_library",
                "source_kind": "GENERATED_EXACT",
                "identifier": "FUNCTION_FIELD.POLYNOMIAL.PILOT.V1",
                "locator": POLYNOMIAL_SOURCE,
                "version_or_retrieved_utc": timestamp,
                "coverage": "Polynomial display and six sample Euler-coefficient cross-checks.",
                "rigor_level": "RIGOROUS_CERTIFIED",
                "hashes": [hash_object(arithmetic_binding["sha256"], "raw pilot.py bytes")],
                "retention": "CHECKED_IN",
                "notes": "The exhaustive family path uses precomputed finite-field character tables.",
            },
            {
                "role": "finite_family_result",
                "source_kind": "GENERATED_EXACT",
                "identifier": "FUNCTION_FIELD.GENUS2.Q3_Q5_Q7.EXACT_SCAN.V1",
                "locator": Q_SCAN_FIXTURE,
                "version_or_retrieved_utc": timestamp,
                "coverage": (
                    f"All {family['member_count']} q={q} members, exact moments, sign counts, "
                    "full K histogram, and witnesses."
                ),
                "rigor_level": "RIGOROUS_CERTIFIED",
                "hashes": [
                    hash_object(
                        fixture_binding["sha256"],
                        "canonical JSON q-scan fixture",
                        "CANONICAL_JSON_UTF8_NFC",
                    )
                ],
                "retention": "CHECKED_IN",
                "notes": "The atlas wrapper replays the complete fixture before writing records.",
            },
        ],
        software=config["software"],
        assumptions=[
            {
                "code": "CLASSICAL_FUNCTION_FIELD_CURVE_ZETA_THEORY",
                "statement": "The degree-four numerator and palindromic functional equation are imported classical theory.",
                "status": "IMPORTED",
            }
        ],
        notes=(
            "The finite a_D,b_D,K_D totals are exact native computations. Root-location claims are "
            "not inputs to this scan. A separately bound DRAFT proof note and exact Q[q] "
            "certificate establish the registered first-moment formulas for every odd prime power."
        ),
    )


def build_detector(root: Path) -> dict[str, Any]:
    normalization = [
        "Use exactly q_values=[3,5,7] and all monic squarefree quintics in each field.",
        "Use K_D=q*a_D^2-b_D^2 and normalize only by q^2 after the exact integer K_D is formed.",
        "Use a 20,000-candidate cap per field and a global monotonic wall guard no larger than eight seconds.",
        "Freeze candidate_cap_scope=PER_FIELD_Q_SCAN; the cap is not a combined-replay total.",
        "Under D^{alpha,beta}(T)=alpha^(-5)D(alpha*T+beta), require a' = chi(alpha)a, b' = b, and K' = K.",
        "Treat K_D only as a toy reciprocal-coefficient minor, not Pick/Loewner, XD, or HCNC.",
    ]
    identity_kernel = {
        "version": 1,
        "slug": DETECTOR_SLUG,
        "mathematical_definition": DETECTOR_DEFINITION,
        "kernel_convention": "COEFFICIENT_DISPERSION",
        "central_zero_policy": "NOT_APPLICABLE",
        "normalization_requirements": normalization,
        "contract_revision": 2,
    }
    semantic_id, identity_sha256 = semantic_identity("DETECTOR", DETECTOR_SLUG, identity_kernel)
    return {
        "schema_version": "riemann.atlas.detector_contract.v1",
        "record_type": "DETECTOR_CONTRACT",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact genus-two toy-minor finite-family moment scan",
        "revision": 2,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(737), programme_ref(741)],
        "scope_boundary": (
            "Exhaustive histograms only for q=3,5,7, plus proof-backed first-moment identities for "
            "every odd prime power and the consequent negative-sign density floor. The exact "
            "affine action law is replayed with complete orbit partitions only at q=3,5,7; no "
            "full sign law, asymptotic orbit law, higher-moment equidistribution, zero statement, "
            "analytic-kernel conclusion, or number-field transfer."
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
                "name": "exact_family_scan",
                "input_type": "RAW_ARTIFACT",
                "required": True,
                "coverage_requirement": "FINITE_COMPLETE",
            },
            {
                "name": "moment_identity_proof",
                "input_type": "RAW_ARTIFACT",
                "required": True,
                "coverage_requirement": "COMPLETE",
            },
            {
                "name": "affine_orbit_certificate",
                "input_type": "RAW_ARTIFACT",
                "required": True,
                "coverage_requirement": "FINITE_COMPLETE",
            },
        ],
        "parameters": [
            {
                "name": "q_values",
                "value_type": "INTEGER_LIST",
                "required": True,
                "domain": "exactly 3,5,7",
                "constraints": {
                    "nonempty": True,
                    "unique": True,
                    "strictly_increasing": True,
                    "element_minimum": 3,
                    "odd": True,
                    "frozen_value": [3, 5, 7],
                },
            },
            {
                "name": "conductor_degree",
                "value_type": "INTEGER",
                "required": True,
                "domain": "positive odd integer; frozen value 5",
                "constraints": {"minimum": 1, "odd": True, "frozen_value": 5},
            },
            {
                "name": "candidate_cap",
                "value_type": "INTEGER",
                "required": True,
                "domain": "positive per-field integer; frozen value 20000",
                "constraints": {"minimum": 16_807, "frozen_value": 20_000},
            },
            {
                "name": "candidate_cap_scope",
                "value_type": "ENUM",
                "required": True,
                "domain": "PER_FIELD_Q_SCAN",
                "constraints": {"enum_values": ["PER_FIELD_Q_SCAN"]},
            },
            {
                "name": "maximum_wall_seconds",
                "value_type": "DECIMAL_STRING",
                "required": True,
                "domain": "8.0",
                "constraints": {"frozen_value": "8.0"},
            },
            {
                "name": "statistic",
                "value_type": "ENUM",
                "required": True,
                "domain": "TOY_MINOR_K_AND_NORMALIZED_MOMENTS",
                "constraints": {"enum_values": ["TOY_MINOR_K_AND_NORMALIZED_MOMENTS"]},
            },
        ],
        "normalization_requirements": [
            {
                "field": "configuration.q_values",
                "requirement": normalization[0],
                "comparison_role": "IDENTITY",
            },
            {
                "field": "configuration.statistic",
                "requirement": normalization[1],
                "comparison_role": "SCALING",
            },
            {
                "field": "configuration.candidate_cap",
                "requirement": normalization[2],
                "comparison_role": "FIREWALL",
            },
            {
                "field": "configuration.candidate_cap_scope",
                "requirement": normalization[3],
                "comparison_role": "FIREWALL",
            },
            {
                "field": "result.artifact.affine_orbit_certificate",
                "requirement": normalization[4],
                "comparison_role": "IDENTITY",
            },
            {
                "field": "detector_kind",
                "requirement": normalization[5],
                "comparison_role": "FIREWALL",
            },
        ],
        "invariances": [
            {
                "code": "GENUS2_MINOR_IDENTITY",
                "statement": "B_1*B_3-B_2^2=q*a_1^2-a_2^2 for the palindromic degree-four numerator.",
                "status": "PROVED",
            },
            {
                "code": "FINITE_CHARACTER_RECONSTRUCTION",
                "statement": "a_D and b_D are reconstructed exactly from F_q and F_(q^2) character sums.",
                "status": "PROVED",
            },
            {
                "code": "CROSS_Q_CLOSED_FORM",
                "statement": "The displayed mean formulas hold for every odd prime power q.",
                "status": "PROVED",
            },
            {
                "code": "NEGATIVE_SIGN_DENSITY_FLOOR",
                "statement": (
                    "The exact mean and F(U)>=-20 imply rho_-(q)>=P(q)/(20*q^5) "
                    "for every odd prime power q, with liminf at least 1/20."
                ),
                "status": "PROVED",
            },
            {
                "code": "AFFINE_TOY_MINOR_INVARIANCE",
                "statement": (
                    "For D^{alpha,beta}(T)=alpha^(-5)D(alpha*T+beta), exact change of "
                    "variables gives a'=chi(alpha)a, b'=b, and K'=K."
                ),
                "status": "PROVED",
            },
        ],
        "family_adapters": [
            {
                "family": "F3_F5_F7_QUADRATIC_QUINTIC_GENUS2",
                "status": "REQUIRED_AVAILABLE",
                "adapter_path": Q_SCAN_SOURCE,
                "correction": "Use each field's exact F_(q^2) model and normalize K only after integer aggregation.",
            },
            {
                "family": "F3_F5_F7_QUINTIC_AFFINE_ORBITS",
                "status": "REQUIRED_AVAILABLE",
                "adapter_path": AFFINE_ORBIT_SOURCE,
                "correction": (
                    "Use the monic right action of AGL(1,F_q), exhaust every member-action "
                    "pair, and retain exact orbit-stabilizer and sign summaries."
                ),
            },
            {
                "family": "NUMBER_FIELD",
                "status": "UNSUPPORTED",
                "adapter_path": None,
                "correction": "No transfer from finite-field coefficient moments is supplied.",
            },
        ],
        "theorem_links": [
            {
                "semantic_id": "DRAFT.FUNCTION_FIELD.GENUS2.TOY_MINOR.MEAN_FORMULA",
                "status": "VERIFIED",
                "scope": (
                    "Proved in the bound DRAFT research note for every odd prime power by an "
                    "exact squarefree-Moebius character-correlation calculation."
                ),
            },
            {
                "semantic_id": "DRAFT.FUNCTION_FIELD.GENUS2.USP4.TOY_MINOR_FIRST_MOMENT",
                "status": "VERIFIED",
                "scope": (
                    "The normalized first moment tends to -1 immediately from the exact formula; "
                    "this is not a higher-moment equidistribution theorem."
                ),
            },
            {
                "semantic_id": "DRAFT.FUNCTION_FIELD.GENUS2.TOY_MINOR.NEGATIVE_SIGN_DENSITY",
                "status": "VERIFIED",
                "scope": (
                    "For every odd prime power, the exact first moment and exact lower range bound "
                    "give rho_-(q)>=P(q)/(20*q^5) and liminf rho_-(q)>=1/20; this is not a sign law."
                ),
            },
        ],
        "failure_modes": [
            {
                "code": "SCAN_MISTAKEN_FOR_PROOF",
                "description": "Agreement at q=3,5,7 is presented as the proof of the all-q identity.",
                "hostile_control": (
                    "The theorem is bound to a separate complete proof note and exact Q[q] "
                    "certificate; the scans are explicitly regression controls only."
                ),
            },
            {
                "code": "TOY_KERNEL_CONFLATION",
                "description": "The coefficient minor is identified with Pick/Loewner, XD, or HCNC.",
                "hostile_control": "The detector, result, and evaluation all retain the analytic-kernel firewall.",
            },
            {
                "code": "RESOURCE_SCOPE_DRIFT",
                "description": "A larger field silently expands the O(q^7) scan.",
                "hostile_control": "The implementation refuses q outside 3,5,7, caps each field at 20,000 candidates, and enforces a global <=8-second replay deadline.",
            },
            {
                "code": "DENSITY_FLOOR_MISTAKEN_FOR_SIGN_LAW",
                "description": "The lower bound on negative members is presented as a limiting sign distribution.",
                "hostile_control": (
                    "Every record states only the one-sided floor derived from the exact mean and "
                    "range, and explicitly withholds a sign law or equidistribution claim."
                ),
            },
            {
                "code": "FINITE_AFFINE_ORBITS_MISTAKEN_FOR_LIMIT_LAW",
                "description": "The q=3,5,7 orbit or stabilizer tables are extrapolated in q.",
                "hostile_control": (
                    "The affine packet hard-refuses every other q, retains its own global "
                    "<=8-second guard, and makes no asymptotic orbit claim."
                ),
            },
        ],
        "output_contract": {
            "representations": ["HASHED_ARTIFACT"],
            "arithmetic_classes": ["CERTIFIED_INTEGER_COVERAGE"],
            "raw_schema_path": RAW_RESULT_SCHEMA,
            "global_claim_allowed": False,
        },
        "reference_implementation": {
            "path": Q_SCAN_SOURCE,
            "entry_point": "build_fixture",
            "version": "1",
            "source_sha256": raw_sha256(root.parents[2] / Q_SCAN_SOURCE),
        },
        "formalization_refs": [
            {
                "state": "PARTIAL",
                "target": "Complete prose proof of the three genus-two first-moment identities.",
                "path": MOMENT_IDENTITY_NOTE,
            },
            {
                "state": "PARTIAL",
                "target": "Bounded exact Q[q] certificate for every polynomial identity in the proof.",
                "path": MOMENT_IDENTITY_CERTIFICATE,
            },
        ],
        "notes": (
            "The q=3,5,7 histograms are finite exact computations. The separately bound DRAFT "
            "proof establishes the displayed first-moment formulas and their normalized limit for "
            "every odd prime power; the separately replayed affine packet proves the exact action "
            "law and finite orbit partitions only at q=3,5,7. Higher moments and "
            "equidistribution remain proposed."
        ),
    }


def _compact_affine_family(family: dict[str, Any]) -> dict[str, Any]:
    partition = family["orbit_partition"]
    sign_summaries = family["sign_summaries"]
    return {
        "q": family["q"],
        "member_count": family["member_count"],
        "group_order": family["group"]["order"],
        "member_action_pairs_checked": family["action_checks"][
            "member_action_pairs_checked"
        ],
        "orbit_count": partition["orbit_count"],
        "orbit_size_histogram": partition["orbit_size_histogram"],
        "stabilizer_order_histogram": partition["stabilizer_order_histogram"],
        "free_orbit_count": partition["free_orbit_count"],
        "nontrivial_stabilizer_orbit_count": partition[
            "nontrivial_stabilizer_orbit_count"
        ],
        "sign_summaries": {
            sign: {
                "member_count": sign_summaries[sign]["member_count"],
                "orbit_count": sign_summaries[sign]["orbit_count"],
            }
            for sign in ("negative", "zero", "positive")
        },
    }


def build_raw_result(
    fixture: dict[str, Any],
    affine_fixture: dict[str, Any],
    specs: Sequence[dict[str, Any]],
    detector: dict[str, Any],
) -> dict[str, Any]:
    specs_by_q = {int(spec["base_field"]["constant_field_order"]): spec for spec in specs}
    families = []
    for family in fixture["families"]:
        q = int(family["q"])
        comparisons = family["formula_comparison"]
        families.append(
            {
                "q": q,
                "spec_semantic_id": specs_by_q[q]["semantic_id"],
                "candidate_count": family["candidate_count"],
                "member_count": family["member_count"],
                "moments": family["moments"],
                "sign_counts": family["sign_counts"],
                "formula_matches_at_this_q": {
                    key: bool(value["matches"]) for key, value in comparisons.items()
                },
            }
        )
    return {
        "schema": "riemann.atlas.raw.function_field_genus2_q_scan.v1",
        "definition": DETECTOR_DEFINITION,
        "detector_semantic_id": detector["semantic_id"],
        "source_fixture": {
            "path": Q_SCAN_FIXTURE,
            "canonical_sha256": sha256_hex(fixture),
            "payload_sha256": fixture["payload_sha256"],
        },
        "finite_result_status": "RIGOROUS_CERTIFIED",
        "families": families,
        "resource_controls": {
            "q_values": list(Q_VALUES),
            "candidate_cap": fixture["resource_contract"]["candidate_cap"],
            "candidate_cap_scope": fixture["resource_contract"]["candidate_cap_scope"],
            "maximum_wall_seconds": str(
                fixture["resource_contract"]["maximum_wall_seconds"]
            ),
            "larger_q_policy": fixture["resource_contract"]["larger_q_policy"],
        },
        "closed_formula_target": {
            "status": FORMULA_STATUS,
            "not_a_theorem": False,
            "scope": fixture["closed_formula_target"]["scope"],
            "mean_K": fixture["closed_formula_target"]["mean_K"],
            "normalized_mean_K": fixture["closed_formula_target"]["normalized_mean_K"],
            "all_three_frozen_fields_match": all(
                all(entry["matches"] for entry in family["formula_comparison"].values())
                for family in fixture["families"]
            ),
            "proof": fixture["closed_formula_target"]["proof"],
            "evidence": fixture["closed_formula_target"]["evidence"],
            "smallest_gap": fixture["closed_formula_target"]["smallest_gap"],
        },
        "usp4_limit_target": {
            "status": MEAN_LIMIT_STATUS,
            "not_a_theorem": False,
            "statement": fixture["usp4_limit_target"]["statement"],
            "proof": fixture["usp4_limit_target"]["proof"],
            "scope_boundary": fixture["usp4_limit_target"]["scope_boundary"],
        },
        "negative_proportion_corollary": fixture["negative_proportion_corollary"],
        "affine_orbit_certificate": {
            "status": AFFINE_ORBIT_STATUS,
            "scope": affine_fixture["scope"],
            "source_fixture": {
                "path": AFFINE_ORBIT_FIXTURE,
                "canonical_sha256": sha256_hex(affine_fixture),
                "payload_sha256": affine_fixture["payload_sha256"],
            },
            "action": {
                "definition": affine_fixture["action"]["definition"],
                "convention": affine_fixture["action"]["convention"],
                "a_D_law": affine_fixture["action"]["transformation_law"]["a_D"],
                "b_D_law": affine_fixture["action"]["transformation_law"]["b_D"],
                "K_D_law": affine_fixture["action"]["transformation_law"]["K_D"],
            },
            "resource_controls": {
                "q_values": affine_fixture["resource_contract"]["frozen_q_values"],
                "candidate_cap": affine_fixture["resource_contract"]["candidate_cap"],
                "candidate_cap_scope": affine_fixture["resource_contract"][
                    "candidate_cap_scope"
                ],
                "maximum_global_wall_seconds": str(
                    affine_fixture["resource_contract"]["maximum_global_wall_seconds"]
                ),
                "larger_q_policy": affine_fixture["resource_contract"][
                    "larger_q_policy"
                ],
            },
            "total_member_action_pairs_checked": sum(
                int(family["action_checks"]["member_action_pairs_checked"])
                for family in affine_fixture["families"]
            ),
            "families": [
                _compact_affine_family(family) for family in affine_fixture["families"]
            ],
            "q_scan_regressions_all_match": all(
                all(checks.values())
                for checks in affine_fixture["q_scan_regression_controls"].values()
            ),
            "firewall": (
                "The action law and orbit partitions are exact finite statements for q=3,5,7 "
                "only; they are not an asymptotic orbit law, equidistribution theorem, analytic "
                "kernel statement, or number-field transfer."
            ),
        },
        "firewalls": [
            "The all-q formula is proved by the separately bound DRAFT proof note and certificate, not inferred from three scans.",
            "Only the first-moment limit is proved; higher moments and USp(4) equidistribution remain proposed and are not theorems here.",
            "The negative-sign result is a one-sided density floor, not a sign law or equidistribution theorem.",
            "The affine action law is exact, but its q=3,5,7 orbit and stabilizer tables are finite only and not an asymptotic law.",
            "The toy coefficient minor is not Pick/Loewner, XD, or HCNC.",
            "No result transfers from these function fields to number-field L-functions.",
        ],
    }


def make_evaluation(
    root: Path,
    config: dict[str, Any],
    specs: Sequence[dict[str, Any]],
    detector: dict[str, Any],
    fixture: dict[str, Any],
    affine_fixture: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    repo_root = root.parents[2]
    qscan_adapter = artifact_binding(
        root, Q_SCAN_SOURCE, "exact_multi_q_adapter", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    polynomial_adapter = artifact_binding(
        root, POLYNOMIAL_SOURCE, "sample_euler_crosscheck_adapter", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    affine_adapter = artifact_binding(
        root,
        AFFINE_ORBIT_SOURCE,
        "exact_affine_orbit_adapter",
        "FINITE_COMPLETE",
        None,
        "RAW_BYTES",
    )
    fixture_binding = artifact_binding(
        root, Q_SCAN_FIXTURE, "exhaustive_three_family_scan", "FINITE_COMPLETE", None
    )
    affine_fixture_binding = artifact_binding(
        root,
        AFFINE_ORBIT_FIXTURE,
        "exact_affine_orbit_certificate",
        "FINITE_COMPLETE",
        None,
    )
    proof_note_binding = artifact_binding(
        root, MOMENT_IDENTITY_NOTE, "all_q_moment_identity_proof", "COMPLETE", None, "RAW_BYTES"
    )
    proof_note_binding["media_type"] = "text/markdown"
    proof_certificate_binding = artifact_binding(
        root,
        MOMENT_IDENTITY_CERTIFICATE,
        "exact_q_polynomial_certificate",
        "COMPLETE",
        None,
        "RAW_BYTES",
    )
    spec_bindings = [content_binding(spec) for spec in sorted(specs, key=lambda item: item["semantic_id"])]
    detector_binding = content_binding(detector)
    values = {
        "q_values": list(Q_VALUES),
        "conductor_degree": 5,
        "candidate_cap": 20_000,
        "candidate_cap_scope": "PER_FIELD_Q_SCAN",
        "maximum_wall_seconds": "8.0",
        "statistic": "TOY_MINOR_K_AND_NORMALIZED_MOMENTS",
    }
    input_fulfillments = [
        {
            "name": "lfunction_spec",
            "input_type": "LFUNCTION_SPEC",
            "coverage_class": "COMPLETE",
            "sources": [binding["semantic_id"] for binding in spec_bindings],
        },
        {
            "name": "exact_family_scan",
            "input_type": "RAW_ARTIFACT",
            "coverage_class": "FINITE_COMPLETE",
            "sources": [Q_SCAN_FIXTURE, Q_SCAN_SOURCE, POLYNOMIAL_SOURCE],
        },
        {
            "name": "moment_identity_proof",
            "input_type": "RAW_ARTIFACT",
            "coverage_class": "COMPLETE",
            "sources": [MOMENT_IDENTITY_NOTE, MOMENT_IDENTITY_CERTIFICATE],
        },
        {
            "name": "affine_orbit_certificate",
            "input_type": "RAW_ARTIFACT",
            "coverage_class": "FINITE_COMPLETE",
            "sources": [AFFINE_ORBIT_FIXTURE, AFFINE_ORBIT_SOURCE],
        },
    ]
    implementation_relative = "research/l-families/atlas/core/wrap_genus2_q_scan.py"
    implementation_sha256 = raw_sha256(repo_root / implementation_relative)
    identity_kernel = {
        "version": 1,
        "slug": EVALUATION_SLUG,
        "lfunction_spec_bindings": spec_bindings,
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [qscan_adapter, polynomial_adapter, affine_adapter],
        "configuration_sha256": sha256_hex(values),
        "input_sha256s": [
            fixture_binding["sha256"],
            affine_fixture_binding["sha256"],
            proof_note_binding["sha256"],
            proof_certificate_binding["sha256"],
        ],
        "input_fulfillments_sha256": sha256_hex(input_fulfillments),
        "implementation_commit": config["code_commit"],
        "implementation_sha256": implementation_sha256,
        "seed": None,
    }
    semantic_id, identity_sha256 = semantic_identity("EVAL", EVALUATION_SLUG, identity_kernel)
    raw_result = build_raw_result(fixture, affine_fixture, specs, detector)
    result_relative = f"research/l-families/atlas/results/{semantic_id}.json"
    result_binding = {
        "role": "detector_result",
        "path": result_relative,
        "sha256": sha256_hex(raw_result),
        "hash_mode": "CANONICAL_JSON_UTF8_NFC",
        "coverage_class": "FINITE_COMPLETE",
        "media_type": "application/json",
        "schema_path": RAW_RESULT_SCHEMA,
        "notes": (
            "Compact exact totals and affine summaries; the source-bound q-scan and affine "
            "fixtures retain full histograms, witnesses, orbit digests, and replay controls."
        ),
    }
    evaluation = {
        "schema_version": "riemann.atlas.evaluation_record.v1",
        "record_type": "EVALUATION_RECORD",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact q=3,5,7 genus-two toy-minor finite-family moment scan",
        "revision": 2,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(737), programme_ref(741)],
        "scope_boundary": (
            "Complete finite scans only at q=3,5,7; the bound proof establishes the named first-"
            "moment identities and consequent negative-sign density floor for every odd prime "
            "power, while the affine action and orbit partitions are exact only on the three "
            "frozen fields. There is no full sign law, asymptotic orbit law, higher-moment "
            "equidistribution, zero statement, analytic-kernel result, or number-field transfer."
        ),
        "supersedes": [],
        "subject": {
            "kind": "L_FUNCTION_SET",
            "description": "Three complete finite GL(1) quadratic-character families with genus-two degree-four numerators",
        },
        "lfunction_spec_bindings": spec_bindings,
        "detector_contract_binding": detector_binding,
        "adapter_bindings": [qscan_adapter, polynomial_adapter, affine_adapter],
        "configuration": {"values": values, "canonical_sha256": sha256_hex(values)},
        "evaluation_scope": "FAMILY_MOMENT",
        "input_bindings": [
            fixture_binding,
            affine_fixture_binding,
            proof_note_binding,
            proof_certificate_binding,
        ],
        "input_fulfillments": input_fulfillments,
        "arithmetic": {
            "class": "CERTIFIED_INTEGER_COVERAGE",
            "directed": False,
            "rounding_contract": "All field operations, character sums, moments, and rational reductions are exact.",
            "serialization_contract": "Canonical UTF-8 NFC JSON with integer sums and reduced numerator/denominator pairs.",
        },
        "coverage": {
            "class": "FINITE_COMPLETE",
            "statement": (
                "All 162, 2500, and 14406 family members at q=3,5,7 respectively, "
                "including every one of the 656024 member-affine-action pairs and each complete "
                "orbit partition."
            ),
            "omissions": [
                "q outside 3,5,7",
                "finite histograms outside q=3,5,7",
                "affine orbit and stabilizer tables outside q=3,5,7",
                "higher-moment formulas and equidistribution",
                "zero ordinates and analytic kernels",
                "number-field transfer",
            ],
        },
        "rigor_level": "RIGOROUS_CERTIFIED",
        "software": config["software"],
        "run": {
            "timestamp_utc": config["run_timestamp_utc"],
            "command": "python research/l-families/atlas/core/wrap_genus2_q_scan.py --check",
            "code_commit": config["code_commit"],
            "implementation_path": implementation_relative,
            "implementation_sha256": implementation_sha256,
        },
        "central_zero_policy_applied": "NOT_APPLICABLE",
        "result": {
            "representation": "HASHED_ARTIFACT",
            "predicate_outcome": "NOT_APPLICABLE",
            "artifact": result_binding,
            "summary": (
                "Exact normalized K means are -104/243, -1994/3125, and -12340/16807 "
                "for q=3,5,7. A separately bound proof gives E[K]=-(q-1)^2+(q+1)/q^3 "
                "for every odd prime power and hence E[K/q^2] tends to -1. Combined with the exact "
                "lower range -20, this proves rho_-(q)>=P(q)/(20*q^5) and liminf rho_-(q)>=1/20. "
                "The exact AGL(1,q) orbit counts are 29, 132, and 349."
            ),
        },
        "result_hashes": [
            hash_object(
                result_binding["sha256"],
                "canonical JSON compact genus-two q-scan result",
                "CANONICAL_JSON_UTF8_NFC",
            )
        ],
        "interpretation": {
            "status": "EXACT_FINITE",
            "statement": (
                "The three declared finite families have the exact registered moment totals and sign "
                "counts. Independently of those scans, the bound squarefree-Moebius proof and Q[q] "
                "certificate establish the displayed first-moment identities for every odd prime "
                "power and, with the exact USp(4) range, the stated negative-sign density floor."
                " The separately replayed affine certificate proves a'=chi(alpha)a, b'=b, K'=K "
                "and the complete finite q=3,5,7 orbit-stabilizer summaries."
            ),
            "smallest_gap": (
                "Translate the proof into a proof assistant or obtain frozen-head review; for the "
                "wider programme, prove higher-moment/equidistribution statements."
            ),
            "theorem_claim_id": None,
        },
        "assumptions": [],
        "firewalls": [
            {
                "code": "SCAN_NOT_PROOF",
                "statement": (
                    "The q=3,5,7 matches are regression controls; the all-q theorem depends on the "
                    "separately bound proof note and exact certificate."
                ),
            },
            {
                "code": "FIRST_MOMENT_NOT_EQUIDISTRIBUTION",
                "statement": "The proved first-moment limit is not a higher-moment or USp(4) equidistribution theorem.",
            },
            {
                "code": "DENSITY_FLOOR_NOT_SIGN_LAW",
                "statement": (
                    "The proved lower bound on the proportion with K_D<0 neither determines a "
                    "limiting sign distribution nor proves equidistribution."
                ),
            },
            {
                "code": "TOY_NOT_ANALYTIC_KERNEL",
                "statement": "K_D is a toy coefficient minor, not Pick/Loewner, XD, or HCNC.",
            },
            {
                "code": "RESOURCE_CAP_FIXED",
                "statement": (
                    "Both exact replays refuse q>7 and cap each field at 20,000 candidates; the "
                    "q-scan and affine computation each retain their own global monotonic "
                    "<=8-second deadline."
                ),
            },
            {
                "code": "AFFINE_FINITE_NOT_ASYMPTOTIC",
                "statement": (
                    "The exact affine law is algebraic, while the recorded orbit and stabilizer "
                    "counts are finite q=3,5,7 data and do not establish a limiting law."
                ),
            },
            {
                "code": "NO_NUMBER_FIELD_TRANSFER",
                "statement": "No finite function-field moment conclusion transfers to number-field L-functions.",
            },
        ],
        "notes": (
            "RIGOROUS_CERTIFIED covers the three exhaustive scans and exact certificate. The DRAFT "
            "research note proves the formula and first-moment limit; all higher-moment and "
            "equidistribution claims remain open. The negative-sign corollary is only the exact "
            "one-sided floor stated above. The affine source and fixture are independently "
            "content-bound and replayed under their own <=8-second wall guard."
        ),
    }
    return evaluation, raw_result


def run(
    root: Path = ATLAS_ROOT,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any], dict[str, Any], dict[str, Any]]:
    root = root.resolve()
    config = read_json(root / "config" / "pilot.json")
    fixture = load_and_replay_fixture(root)
    affine_fixture = load_and_replay_affine_fixture(root)
    families_by_q = {int(family["q"]): family for family in fixture["families"]}
    f3_spec = load_existing_f3_spec(root)
    new_specs = [build_family_spec(root, config, families_by_q[q]) for q in (5, 7)]
    specs = [f3_spec, *new_specs]
    detector = build_detector(root)
    evaluation, raw_result = make_evaluation(
        root, config, specs, detector, fixture, affine_fixture
    )
    return specs, new_specs, detector, evaluation, raw_result


def _records_with_slug(directory: Path, slug: str) -> list[Path]:
    paths: list[Path] = []
    for path in sorted(directory.glob("*.json")):
        try:
            record = read_json(path)
        except (OSError, ValueError):
            continue
        if record.get("identity_kernel", {}).get("slug") == slug:
            paths.append(path)
    return paths


def _stale_paths(
    root: Path,
    new_specs: Sequence[dict[str, Any]],
    detector: dict[str, Any],
    evaluation: dict[str, Any],
) -> list[Path]:
    expected_specs = {
        spec["identity_kernel"]["slug"]: root / "specs" / f"{spec['semantic_id']}.json"
        for spec in new_specs
    }
    stale_specs = [
        path
        for slug, expected in expected_specs.items()
        for path in _records_with_slug(root / "specs", slug)
        if path != expected
    ]
    expected_detector = root / "detectors" / f"{detector['semantic_id']}.json"
    stale_detectors = [
        path
        for path in _records_with_slug(root / "detectors", DETECTOR_SLUG)
        if path != expected_detector
    ]
    expected_evaluation = root / "evaluations" / f"{evaluation['semantic_id']}.json"
    stale_evaluations = [
        path
        for path in _records_with_slug(root / "evaluations", EVALUATION_SLUG)
        if path != expected_evaluation
    ]
    expected_result = root / "results" / f"{evaluation['semantic_id']}.json"
    stale_results = [
        path
        for path in sorted(
            (root / "results").glob(f"ATLAS.EVAL.{EVALUATION_SLUG}.H*.json")
        )
        if path != expected_result
    ]
    return stale_specs + stale_detectors + stale_evaluations + stale_results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ATLAS_ROOT)
    parser.add_argument("--check", action="store_true", help="replay and compare without writing")
    args = parser.parse_args()
    root = args.root.resolve()
    specs, new_specs, detector, evaluation, raw_result = run(root)
    spec_paths = [root / "specs" / f"{spec['semantic_id']}.json" for spec in new_specs]
    detector_path = root / "detectors" / f"{detector['semantic_id']}.json"
    evaluation_path = root / "evaluations" / f"{evaluation['semantic_id']}.json"
    result_path = root.parents[2] / evaluation["result"]["artifact"]["path"]
    expected = [
        *((path, spec) for path, spec in zip(spec_paths, new_specs, strict=True)),
        (detector_path, detector),
        (evaluation_path, evaluation),
        (result_path, raw_result),
    ]
    stale = _stale_paths(root, new_specs, detector, evaluation)
    if args.check:
        mismatches = [
            str(path) for path, value in expected if not path.is_file() or read_json(path) != value
        ]
        if stale:
            mismatches.extend(f"stale:{path}" for path in stale)
        if mismatches:
            raise SystemExit(f"genus-two q-scan atlas artifacts differ: {mismatches}")
        print("OK: exact genus-two q-scan atlas artifacts match; stale=0")
        return
    for path in stale:
        path.unlink()
    for path, value in expected:
        write_json(path, value)
    print(
        "PASS_GENUS2_Q_SCAN_ATLAS "
        f"specs={','.join(spec['semantic_id'] for spec in specs)} "
        f"detector={detector['semantic_id']} evaluation={evaluation['semantic_id']} "
        f"stale_removed={len(stale)}"
    )


if __name__ == "__main__":
    main()
