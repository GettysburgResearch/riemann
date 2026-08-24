#!/usr/bin/env python3
"""Register the exact USp(4) toy-minor moment comparator as DRAFT atlas records."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import sys
from fractions import Fraction
from pathlib import Path
from types import ModuleType
from typing import Any, Mapping, Sequence

from atlas_core import ATLAS_ROOT, fraction_json, read_json, semantic_identity, sha256_hex, write_json
from run_pilot import artifact_binding, hash_object, programme_ref, raw_sha256


Q_VALUES = (3, 5, 7)
SPEC_SLUGS = {
    3: "FUNCTION_FIELD.F3.QUADRATIC.QUINTIC_GENUS2_FAMILY",
    5: "FUNCTION_FIELD.F5.QUADRATIC.QUINTIC_GENUS2_FAMILY",
    7: "FUNCTION_FIELD.F7.QUADRATIC.QUINTIC_GENUS2_FAMILY",
}
COMPARATOR_SOURCE = "research/l-families/atlas/function_field/usp4_toy_minor_moments.py"
COMPARATOR_FIXTURE = "research/l-families/atlas/function_field/usp4_toy_minor_moments.json"
Q_SCAN_SOURCE = "research/l-families/atlas/function_field/genus2_q_scan.py"
Q_SCAN_FIXTURE = "research/l-families/atlas/function_field/genus2_q_scan.json"
RAW_RESULT_SCHEMA = (
    "research/l-families/atlas/detectors/raw-schemas/"
    "function-field-usp4-toy-minor-moments-result.schema.json"
)
DETECTOR_SLUG = "FUNCTION_FIELD.GENUS2.USP4.TOY_MINOR.EXACT_MOMENT_COMPARATOR"
EVALUATION_SLUG = "FUNCTION_FIELD.GENUS2.USP4.TOY_MINOR.Q3_Q5_Q7.MOMENT_COMPARISON"
EXACT_STATUS = "RIGOROUS_CERTIFIED"
CONVERGENCE_STATUS = "CONJECTURAL_USP4_LIMIT_NOT_A_THEOREM"
FROZEN_PATTERN_STATUS = "EXACT_FOR_Q_3_5_7_ONLY"
SIGN_MAJORANT_STATUS = "PROVED_EXACT_DEGREE_SIX_MOMENT_BOUND"
HAAR_MOMENTS = (-1, 3, -11, 56, -374, 3117)
HAAR_CENTERED_MOMENTS = (0, 2, -4, 27, -178, 1533)
HAAR_CUMULANTS = (-1, 2, -4, 15, -98, 803)
POSITIVE_ROOTS = ((2, 0), (0, 2), (1, 1), (1, -1))
DETECTOR_DEFINITION = (
    "For U in USp(4), set F(U)=(Tr U)^2-e_2(U)^2. Prove the exact Laurent-character "
    "identity F=-(1+chi_{omega_2}+chi_{2*omega_2}), certify the exact range [-20,4/3], "
    "evaluate the first six Haar moments by the normalized C_2 Weyl constant-term formula, "
    "and compare them exactly with the complete q=3,5,7 histogram moments of K_D/q^2, "
    "where K_D=q*a_D^2-b_D^2. Use those six moments and an exact degree-six "
    "polynomial majorant to certify a lower bound for the negative-sign probability."
)


def content_binding(record: dict[str, Any]) -> dict[str, str]:
    return {"semantic_id": record["semantic_id"], "record_sha256": sha256_hex(record)}


def _load_module(repo_root: Path, relative_path: str, module_name: str) -> ModuleType:
    path = repo_root / relative_path
    source_dir = str(path.parent)
    if source_dir not in sys.path:
        sys.path.insert(0, source_dir)
    module_spec = importlib.util.spec_from_file_location(module_name, path)
    if module_spec is None or module_spec.loader is None:
        raise RuntimeError(f"cannot load exact module: {path}")
    module = importlib.util.module_from_spec(module_spec)
    sys.modules[module_spec.name] = module
    module_spec.loader.exec_module(module)
    return module


def _verify_payload_hash(fixture: Mapping[str, Any], label: str) -> None:
    claimed = fixture.get("payload_sha256")
    payload = dict(fixture)
    payload.pop("payload_sha256", None)
    if claimed != sha256_hex(payload):
        raise ValueError(f"{label} payload hash mismatch")


def _fraction(pair: Sequence[int], label: str) -> Fraction:
    if len(pair) != 2 or isinstance(pair[0], bool) or isinstance(pair[1], bool):
        raise ValueError(f"{label} is not an integer fraction pair")
    value = Fraction(int(pair[0]), int(pair[1]))
    if [value.numerator, value.denominator] != list(pair):
        raise ValueError(f"{label} is not reduced with positive denominator")
    return value


def load_and_replay_fixtures(root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    repo_root = root.parents[2]
    q_scan = read_json(repo_root / Q_SCAN_FIXTURE)
    _verify_payload_hash(q_scan, "q-scan fixture")
    q_scan_module = _load_module(
        repo_root, Q_SCAN_SOURCE, "_riemann_atlas_usp4_bound_genus2_q_scan"
    )
    if q_scan_module.build_fixture() != q_scan:
        raise ValueError("q-scan fixture differs from its exact guarded replay")
    if q_scan.get("resource_contract", {}).get("frozen_q_values") != list(Q_VALUES):
        raise ValueError("q-scan is not the frozen q=3,5,7 input")

    comparator = read_json(repo_root / COMPARATOR_FIXTURE)
    _verify_payload_hash(comparator, "USp(4) comparator fixture")
    comparator_module = _load_module(
        repo_root, COMPARATOR_SOURCE, "_riemann_atlas_usp4_toy_minor_moments"
    )
    regenerated = comparator_module.build_fixture(repo_root / Q_SCAN_FIXTURE)
    if regenerated != comparator:
        raise ValueError("USp(4) comparator fixture differs from its exact replay")
    if comparator.get("finite_source", {}).get("canonical_sha256") != sha256_hex(q_scan):
        raise ValueError("USp(4) comparator is not bound to the current q-scan fixture")
    if comparator.get("limit_target", {}).get("status") != CONVERGENCE_STATUS:
        raise ValueError("USp(4) convergence target lost its conjectural status")
    if comparator["limit_target"].get("not_a_theorem") is not True:
        raise ValueError("USp(4) convergence target must remain explicitly non-theorem")
    if comparator.get("character_identity", {}).get("formula") != (
        "F=-(1+chi_{omega_2}+chi_{2*omega_2})"
    ):
        raise ValueError("unexpected USp(4) character identity")
    producer = comparator.get("producer", {})
    comparator_text = (repo_root / COMPARATOR_SOURCE).read_text(encoding="utf-8").replace(
        "\r\n", "\n"
    )
    if producer.get("source") != COMPARATOR_SOURCE or producer.get(
        "source_sha256_lf_normalized"
    ) != hashlib.sha256(comparator_text.encode("utf-8")).hexdigest():
        raise ValueError("USp(4) comparator producer source lock mismatch")
    range_certificate = comparator.get("range_certificate", {})
    if range_certificate.get("status") != "PROVED_EXACT_ELEMENTARY_OPTIMIZATION":
        raise ValueError("USp(4) exact range certificate lost its proved status")
    if _fraction(range_certificate.get("minimum", []), "USp(4) range minimum") != -20:
        raise ValueError("USp(4) exact range minimum drifted")
    if _fraction(range_certificate.get("maximum", []), "USp(4) range maximum") != Fraction(
        4, 3
    ):
        raise ValueError("USp(4) exact range maximum drifted")
    for label in ("minimum_witnesses", "maximum_witnesses"):
        if not range_certificate.get(label):
            raise ValueError(f"USp(4) range certificate lacks {label}")
        for index, witness in enumerate(range_certificate[label]):
            x = _fraction(witness["X"], f"{label}[{index}].X")
            y = _fraction(witness["Y"], f"{label}[{index}].Y")
            value = comparator_module.statistic_in_trace_coordinates(x, y)
            target = -20 if label == "minimum_witnesses" else Fraction(4, 3)
            if value != target:
                raise ValueError(f"USp(4) range witness {label}[{index}] is invalid")
    certificate = comparator.get("weyl_certificate", {})
    if certificate.get("density_constant_term") != 8:
        raise ValueError("C2 Weyl density must have constant term 8")
    if certificate.get("positive_roots_as_exponent_pairs") != [list(root) for root in POSITIVE_ROOTS]:
        raise ValueError("C2 positive-root convention drifted")
    if certificate.get("haar_moments_orders_1_through_6") != list(HAAR_MOMENTS):
        raise ValueError("USp(4) Haar moments drifted")
    if certificate.get("haar_centered_moments_orders_1_through_6") != list(
        HAAR_CENTERED_MOMENTS
    ):
        raise ValueError("USp(4) Haar centered moments drifted")
    if certificate.get("haar_cumulants_orders_1_through_6") != list(HAAR_CUMULANTS):
        raise ValueError("USp(4) Haar cumulants drifted")
    if comparator.get("resource_contract") != {
        "maximum_moment": 6,
        "random_sampling": False,
        "numerical_integration": False,
        "external_dependencies": False,
    }:
        raise ValueError("USp(4) exact resource contract drifted")

    q_families = {int(family["q"]): family for family in q_scan["families"]}
    comparisons = {int(item["q"]): item for item in comparator["finite_comparisons"]}
    if set(q_families) != set(Q_VALUES) or set(comparisons) != set(Q_VALUES):
        raise ValueError("USp(4) finite comparisons must cover exactly q=3,5,7")
    for q in Q_VALUES:
        family = q_families[q]
        comparison = comparisons[q]
        histogram = {int(key): int(count) for key, count in family["K_histogram"].items()}
        if sum(histogram.values()) != int(family["member_count"]):
            raise ValueError(f"q={q} histogram count mismatch")
        if comparison["member_count"] != family["member_count"]:
            raise ValueError(f"q={q} comparison member count mismatch")
        for order, entry in enumerate(comparison["moments"], start=1):
            if entry["order"] != order or entry["usp4_haar_exact"] != HAAR_MOMENTS[order - 1]:
                raise ValueError(f"q={q} moment-order or Haar target mismatch")
            exact = Fraction(
                sum(count * value**order for value, count in histogram.items()),
                int(family["member_count"]) * q ** (2 * order),
            )
            if _fraction(entry["finite_exact"], f"q={q} moment {order}") != exact:
                raise ValueError(f"q={q} finite normalized moment mismatch at order {order}")
            if _fraction(entry["finite_minus_haar"], f"q={q} gap {order}") != (
                exact - HAAR_MOMENTS[order - 1]
            ):
                raise ValueError(f"q={q} moment gap mismatch at order {order}")
    frozen_pattern = comparator.get("frozen_moment_pattern", {})
    if frozen_pattern.get("status") != FROZEN_PATTERN_STATUS:
        raise ValueError("frozen directional moment pattern lost its finite-only status")
    if frozen_pattern.get("not_a_theorem_beyond_frozen_fields") is not True:
        raise ValueError("frozen directional moment pattern lost its theorem firewall")
    if frozen_pattern.get("q_values") != list(Q_VALUES):
        raise ValueError("frozen directional moment pattern q-values drifted")
    if [row.get("order") for row in frozen_pattern.get("per_order", [])] != list(
        range(1, 7)
    ):
        raise ValueError("frozen directional moment pattern orders drifted")
    if not all(
        all(value is True for key, value in row.items() if key != "order")
        for row in frozen_pattern["per_order"]
    ):
        raise ValueError("frozen directional moment pattern contains a failed exact check")

    sign_certificate = comparator.get("negative_sign_moment_certificate", {})
    if sign_certificate.get("status") != SIGN_MAJORANT_STATUS:
        raise ValueError("negative-sign moment certificate lost its exact status")
    majorant = sign_certificate.get("majorant", {})
    coefficients = tuple(
        _fraction(pair, f"sign majorant coefficient {index}")
        for index, pair in enumerate(majorant.get("coefficients_low_to_high", []))
    )
    if coefficients != comparator_module.SIGN_MAJORANT_COEFFICIENTS:
        raise ValueError("negative-sign majorant coefficients drifted")
    square = comparator_module.convolve_rational(coefficients, coefficients)
    stored_square = [
        _fraction(pair, f"sign majorant square coefficient {index}")
        for index, pair in enumerate(majorant.get("square_coefficients_low_to_high", []))
    ]
    if stored_square != square:
        raise ValueError("negative-sign majorant square coefficients drifted")
    if majorant.get("quadratic_endpoint_values_on_0_to_4_over_3") != [
        [5405, 1],
        [51445, 9],
    ]:
        raise ValueError("negative-sign majorant positivity certificate drifted")
    haar_sign = sign_certificate.get("haar", {})
    if _fraction(
        haar_sign.get("moment_majorant_nonnegative_upper_bound", []),
        "Haar nonnegative sign upper bound",
    ) != Fraction(7663, 12023):
        raise ValueError("Haar nonnegative sign upper bound drifted")
    if _fraction(
        haar_sign.get("negative_probability_lower_bound", []),
        "Haar negative sign lower bound",
    ) != Fraction(4360, 12023):
        raise ValueError("Haar negative sign lower bound drifted")
    finite_sign_rows = sign_certificate.get("finite_q_bounds", [])
    if [row.get("q") for row in finite_sign_rows] != list(Q_VALUES):
        raise ValueError("finite negative-sign moment rows drifted")
    for row in finite_sign_rows:
        q = int(row["q"])
        moments = [
            _fraction(entry["finite_exact"], f"q={q} sign moment")
            for entry in comparisons[q]["moments"]
        ]
        expected_upper = comparator_module.polynomial_moment(square, moments)
        stored_upper = _fraction(
            row["moment_majorant_nonnegative_upper_bound"],
            f"q={q} nonnegative sign upper bound",
        )
        stored_lower = _fraction(
            row["negative_probability_lower_bound"],
            f"q={q} negative sign lower bound",
        )
        observed = Fraction(
            int(q_families[q]["sign_counts"]["negative"]),
            int(q_families[q]["member_count"]),
        )
        if (
            stored_upper != expected_upper
            or stored_lower != 1 - expected_upper
            or _fraction(row["observed_negative_fraction"], f"q={q} observed sign")
            != observed
            or row.get("verified_bound_holds") is not True
            or not stored_lower <= observed
        ):
            raise ValueError(f"q={q} negative-sign moment certificate mismatch")
    conditional = sign_certificate.get("conditional_consequence", {})
    if conditional.get("status") != "CONDITIONAL_ON_FIRST_SIX_MOMENT_CONVERGENCE":
        raise ValueError("negative-sign liminf consequence lost its conditional status")
    if conditional.get("not_an_equidistribution_proof") is not True:
        raise ValueError("negative-sign conditional consequence lost its theorem firewall")
    return comparator, q_scan


def load_family_specs(root: Path) -> list[dict[str, Any]]:
    matches: dict[int, list[dict[str, Any]]] = {q: [] for q in Q_VALUES}
    for path in sorted((root / "specs").glob("ATLAS.LFUNC.*.json")):
        record = read_json(path)
        slug = record.get("identity_kernel", {}).get("slug")
        for q, expected_slug in SPEC_SLUGS.items():
            if slug == expected_slug:
                matches[q].append(record)
    for q, records in matches.items():
        if len(records) != 1:
            raise ValueError(f"expected exactly one existing F_{q} genus-two spec, found {len(records)}")
        if records[0].get("base_field", {}).get("constant_field_order") != q:
            raise ValueError(f"F_{q} genus-two spec has the wrong constant field")
    return [matches[q][0] for q in Q_VALUES]


def build_detector(root: Path) -> dict[str, Any]:
    normalization = [
        "Use the USp(4) torus eigenvalues x,x^-1,y,y^-1 and exactly the C2 positive roots (2,0),(0,2),(1,1),(1,-1).",
        "Normalize Haar integration by CT(product_(alpha>0)(1-X^alpha)(1-X^-alpha))=8.",
        "Compare F(U) only with K_D/q^2 and freeze moment orders 1 through 6 and q values 3,5,7.",
        "Keep exact Laurent and finite-histogram arithmetic separate from the proposed q-to-infinity convergence statement.",
        "Treat F as a toy reciprocal-coefficient statistic, not Pick/Loewner, XD, or HCNC.",
        "Use R(x)^2 only as an exact nonnegative-event majorant on [-20,4/3], and keep its liminf consequence conditional on six-moment convergence.",
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
        "title": "Exact USp(4) genus-two toy-minor moment comparator",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(737), programme_ref(741)],
        "scope_boundary": (
            "Exact character, Weyl constant-term, and q=3,5,7 histogram calculations through "
            "moment six only. Convergence is proposed, with no analytic-kernel conclusion or "
            "number-field transfer."
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
                "name": "exact_usp4_certificate",
                "input_type": "RAW_ARTIFACT",
                "required": True,
                "coverage_requirement": "FINITE_COMPLETE",
            },
            {
                "name": "finite_family_histograms",
                "input_type": "RAW_ARTIFACT",
                "required": True,
                "coverage_requirement": "FINITE_COMPLETE",
            },
        ],
        "parameters": [
            {
                "name": "torus_convention",
                "value_type": "STRING",
                "required": True,
                "domain": "x,x^-1,y,y^-1",
                "constraints": {"frozen_value": "x,x^-1,y,y^-1"},
            },
            {
                "name": "weyl_order",
                "value_type": "INTEGER",
                "required": True,
                "domain": "C2 Weyl-group order 8",
                "constraints": {"minimum": 8, "maximum": 8, "frozen_value": 8},
            },
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
                    "frozen_value": list(Q_VALUES),
                },
            },
            {
                "name": "maximum_moment",
                "value_type": "INTEGER",
                "required": True,
                "domain": "orders 1 through 6",
                "constraints": {"minimum": 1, "maximum": 6, "frozen_value": 6},
            },
            {
                "name": "statistic",
                "value_type": "ENUM",
                "required": True,
                "domain": "USP4_TOY_MINOR_F",
                "constraints": {"enum_values": ["USP4_TOY_MINOR_F"]},
            },
        ],
        "normalization_requirements": [
            {
                "field": "configuration.torus_convention",
                "requirement": normalization[0],
                "comparison_role": "IDENTITY",
            },
            {
                "field": "configuration.weyl_order",
                "requirement": normalization[1],
                "comparison_role": "SCALING",
            },
            {
                "field": "configuration.maximum_moment",
                "requirement": normalization[2],
                "comparison_role": "SCALING",
            },
            {
                "field": "result.convergence_target",
                "requirement": normalization[3],
                "comparison_role": "FIREWALL",
            },
            {
                "field": "detector_kind",
                "requirement": normalization[4],
                "comparison_role": "FIREWALL",
            },
            {
                "field": "result.negative_sign_moment_certificate",
                "requirement": normalization[5],
                "comparison_role": "FIREWALL",
            },
        ],
        "invariances": [
            {
                "code": "USP4_CHARACTER_IDENTITY",
                "statement": "F=-(1+chi_{omega_2}+chi_{2*omega_2}) as an exact Laurent polynomial.",
                "status": "PROVED",
            },
            {
                "code": "C2_WEYL_NORMALIZATION",
                "statement": "The chosen C2 Weyl density has constant term and Weyl order 8.",
                "status": "PROVED",
            },
            {
                "code": "USP4_EXACT_RANGE",
                "statement": "In trace coordinates X,Y in [-2,2], F has exact range [-20,4/3].",
                "status": "PROVED",
            },
            {
                "code": "FINITE_HISTOGRAM_RECONSTRUCTION",
                "statement": "Every stored finite moment is reconstructed exactly from the complete K histogram.",
                "status": "PROVED",
            },
            {
                "code": "FROZEN_DIRECTIONAL_MOMENT_PATTERN",
                "statement": (
                    "At q=3,5,7 and orders 1 through 6, finite moments have the Haar sign, "
                    "smaller increasing magnitude, and strictly decreasing absolute gap."
                ),
                "status": "PROVED",
            },
            {
                "code": "DEGREE_SIX_SIGN_MAJORANT",
                "statement": (
                    "The exact cubic R gives 1_{F>=0}<=R(F)^2 and therefore "
                    "Pr_Haar(F<0)>=4360/12023 from moments through order six."
                ),
                "status": "PROVED",
            },
            {
                "code": "FIXED_MOMENT_CONVERGENCE",
                "statement": "For each fixed order, finite K_D/q^2 moments converge to USp(4) Haar moments.",
                "status": "EXPECTED",
            },
        ],
        "family_adapters": [
            {
                "family": "USP4_HAAR_CLASS_FUNCTION",
                "status": "REQUIRED_AVAILABLE",
                "adapter_path": COMPARATOR_SOURCE,
                "correction": "Use the exact C2 Weyl constant-term formula; no random matrices or numerical integration.",
            },
            {
                "family": "F3_F5_F7_QUADRATIC_QUINTIC_GENUS2",
                "status": "REQUIRED_AVAILABLE",
                "adapter_path": Q_SCAN_SOURCE,
                "correction": "Use complete exact histograms and normalize K_D by q^2 before taking powers.",
            },
            {
                "family": "NUMBER_FIELD",
                "status": "UNSUPPORTED",
                "adapter_path": None,
                "correction": "No number-field transfer is supplied.",
            },
        ],
        "theorem_links": [
            {
                "semantic_id": "PROPOSED.FUNCTION_FIELD.GENUS2.USP4.FIXED_MOMENT_LIMIT",
                "status": "PROPOSED",
                "scope": "The exact q=3,5,7 comparisons do not prove equidistribution or convergence.",
            },
            {
                "semantic_id": "CONDITIONAL.FUNCTION_FIELD.GENUS2.NEGATIVE_SIGN.LIMINF",
                "status": "CONDITIONAL_EXACT",
                "scope": (
                    "Convergence of the first six raw moments implies "
                    "liminf Pr(K_D/q^2<0)>=4360/12023."
                ),
            },
        ],
        "failure_modes": [
            {
                "code": "WEYL_NORMALIZATION_LOSS",
                "description": "The C2 constant term is used without division by the Weyl order 8.",
                "hostile_control": "The replay requires density constant term 8 and the frozen exact six moments.",
            },
            {
                "code": "FINITE_TO_LIMIT_PROMOTION",
                "description": "Three finite fields are promoted to a q-to-infinity theorem.",
                "hostile_control": "The raw result requires a conjectural status and not_a_theorem=true.",
            },
            {
                "code": "SIGN_BOUND_AS_EXACT_PROBABILITY",
                "description": "The polynomial lower bound is reported as the exact Haar sign probability.",
                "hostile_control": (
                    "The raw certificate labels 4360/12023 as a lower bound and keeps the "
                    "q-to-infinity consequence conditional."
                ),
            },
            {
                "code": "TOY_KERNEL_CONFLATION",
                "description": "The coefficient statistic is identified with Pick/Loewner, XD, or HCNC.",
                "hostile_control": "Detector, result, and evaluation retain the analytic-kernel firewall.",
            },
            {
                "code": "NUMBER_FIELD_TRANSFER",
                "description": "The function-field comparison is transferred to number-field L-functions.",
                "hostile_control": "The number-field adapter is explicitly unsupported.",
            },
        ],
        "output_contract": {
            "representations": ["HASHED_ARTIFACT"],
            "arithmetic_classes": ["EXACT_RATIONAL"],
            "raw_schema_path": RAW_RESULT_SCHEMA,
            "global_claim_allowed": False,
        },
        "reference_implementation": {
            "path": COMPARATOR_SOURCE,
            "entry_point": "build_fixture",
            "version": "1",
            "source_sha256": raw_sha256(root.parents[2] / COMPARATOR_SOURCE),
        },
        "formalization_refs": [
            {
                "state": "DEFINITION_READY",
                "target": "C2 Weyl constant term and USp(4) Laurent-character identity.",
                "path": None,
            }
        ],
        "notes": (
            "Certified claims are the exact identity, constant terms, six Haar moments, finite "
            "histogram moments, and the degree-six sign lower bound. The limiting moment "
            "comparison remains proposed."
        ),
    }


def _fraction_record(pair: Sequence[int]) -> dict[str, int | str]:
    value = _fraction(pair, "raw-result fraction")
    return fraction_json(value.numerator, value.denominator)


def _witness_record(witness: Mapping[str, Sequence[int]]) -> dict[str, Any]:
    return {"X": _fraction_record(witness["X"]), "Y": _fraction_record(witness["Y"])}


def _sign_moment_certificate_record(source: Mapping[str, Any]) -> dict[str, Any]:
    majorant = source["majorant"]
    return {
        "status": source["status"],
        "event": source["event"],
        "support": {
            "minimum": _fraction_record(source["support"]["minimum"]),
            "maximum": _fraction_record(source["support"]["maximum"]),
        },
        "majorant": {
            "polynomial": majorant["polynomial"],
            "coefficients_low_to_high": [
                _fraction_record(pair) for pair in majorant["coefficients_low_to_high"]
            ],
            "square_coefficients_low_to_high": [
                _fraction_record(pair)
                for pair in majorant["square_coefficients_low_to_high"]
            ],
            "pointwise_statement": majorant["pointwise_statement"],
            "positive_interval_factorization": majorant[
                "positive_interval_factorization"
            ],
            "quadratic_endpoint_values_on_0_to_4_over_3": [
                _fraction_record(pair)
                for pair in majorant["quadratic_endpoint_values_on_0_to_4_over_3"]
            ],
            "proof": majorant["proof"],
            "construction": majorant["construction"],
        },
        "haar": {
            "moment_majorant_nonnegative_upper_bound": _fraction_record(
                source["haar"]["moment_majorant_nonnegative_upper_bound"]
            ),
            "negative_probability_lower_bound": _fraction_record(
                source["haar"]["negative_probability_lower_bound"]
            ),
        },
        "finite_q_bounds": [
            {
                "q": int(row["q"]),
                "moment_majorant_nonnegative_upper_bound": _fraction_record(
                    row["moment_majorant_nonnegative_upper_bound"]
                ),
                "negative_probability_lower_bound": _fraction_record(
                    row["negative_probability_lower_bound"]
                ),
                "observed_negative_fraction": _fraction_record(
                    row["observed_negative_fraction"]
                ),
                "verified_bound_holds": row["verified_bound_holds"],
            }
            for row in source["finite_q_bounds"]
        ],
        "conditional_consequence": dict(source["conditional_consequence"]),
        "scope": source["scope"],
    }


def build_raw_result(
    root: Path,
    specs: Sequence[dict[str, Any]],
    detector: dict[str, Any],
    comparator: dict[str, Any],
    q_scan: dict[str, Any],
) -> dict[str, Any]:
    repo_root = root.parents[2]
    specs_by_q = {int(spec["base_field"]["constant_field_order"]): spec for spec in specs}
    comparisons = []
    for item in comparator["finite_comparisons"]:
        q = int(item["q"])
        comparisons.append(
            {
                "q": q,
                "spec_semantic_id": specs_by_q[q]["semantic_id"],
                "member_count": int(item["member_count"]),
                "moments": [
                    {
                        "order": int(moment["order"]),
                        "finite_exact": _fraction_record(moment["finite_exact"]),
                        "usp4_haar_exact": int(moment["usp4_haar_exact"]),
                        "finite_minus_haar": _fraction_record(moment["finite_minus_haar"]),
                    }
                    for moment in item["moments"]
                ],
            }
        )
    return {
        "schema": "riemann.atlas.raw.function_field_usp4_toy_minor_moments.v1",
        "definition": DETECTOR_DEFINITION,
        "detector_semantic_id": detector["semantic_id"],
        "exact_result_status": EXACT_STATUS,
        "source_locks": {
            "comparator_source": {
                "path": COMPARATOR_SOURCE,
                "raw_sha256": raw_sha256(repo_root / COMPARATOR_SOURCE),
            },
            "comparator_fixture": {
                "path": COMPARATOR_FIXTURE,
                "canonical_sha256": sha256_hex(comparator),
                "payload_sha256": comparator["payload_sha256"],
            },
            "q_scan_source": {
                "path": Q_SCAN_SOURCE,
                "raw_sha256": raw_sha256(repo_root / Q_SCAN_SOURCE),
            },
            "q_scan_fixture": {
                "path": Q_SCAN_FIXTURE,
                "canonical_sha256": sha256_hex(q_scan),
                "payload_sha256": q_scan["payload_sha256"],
            },
        },
        "character_identity": {
            "status": comparator["character_identity"]["status"],
            "formula": comparator["character_identity"]["formula"],
            "dimensions_at_identity": comparator["character_identity"]["dimensions_at_identity"],
            "haar_mean_consequence": comparator["character_identity"]["haar_mean_consequence"],
        },
        "range_certificate": {
            "status": comparator["range_certificate"]["status"],
            "trace_coordinates": comparator["range_certificate"]["trace_coordinates"],
            "formula": comparator["range_certificate"]["formula"],
            "minimum": _fraction_record(comparator["range_certificate"]["minimum"]),
            "minimum_witnesses": [
                _witness_record(witness)
                for witness in comparator["range_certificate"]["minimum_witnesses"]
            ],
            "maximum": _fraction_record(comparator["range_certificate"]["maximum"]),
            "maximum_witnesses": [
                _witness_record(witness)
                for witness in comparator["range_certificate"]["maximum_witnesses"]
            ],
            "proof": comparator["range_certificate"]["proof"],
        },
        "weyl_certificate": {
            "root_system": comparator["weyl_certificate"]["root_system"],
            "positive_roots_as_exponent_pairs": comparator["weyl_certificate"][
                "positive_roots_as_exponent_pairs"
            ],
            "density_constant_term": comparator["weyl_certificate"]["density_constant_term"],
            "formula": comparator["weyl_certificate"]["formula"],
            "maximum_moment": comparator["weyl_certificate"]["maximum_moment"],
            "haar_moments_orders_1_through_6": comparator["weyl_certificate"][
                "haar_moments_orders_1_through_6"
            ],
            "haar_centered_moments_orders_1_through_6": comparator["weyl_certificate"][
                "haar_centered_moments_orders_1_through_6"
            ],
            "haar_cumulants_orders_1_through_6": comparator["weyl_certificate"][
                "haar_cumulants_orders_1_through_6"
            ],
            "arithmetic": comparator["weyl_certificate"]["arithmetic"],
        },
        "negative_sign_moment_certificate": _sign_moment_certificate_record(
            comparator["negative_sign_moment_certificate"]
        ),
        "finite_comparisons": comparisons,
        "frozen_moment_pattern": comparator["frozen_moment_pattern"],
        "convergence_target": {
            "status": CONVERGENCE_STATUS,
            "atlas_status": "PROPOSED",
            "not_a_theorem": True,
            "statement": comparator["limit_target"]["statement"],
            "evidence_scope": comparator["limit_target"]["evidence_scope"],
            "smallest_gap": (
                "Prove the relevant hyperelliptic-family equidistribution; for each fixed order, "
                "F(U)^m is continuous and bounded on compact USp(4)."
            ),
        },
        "firewalls": [
            "RIGOROUS_CERTIFIED covers the exact Laurent, Weyl, and finite-histogram arithmetic only; convergence is proposed and not a theorem.",
            "The directional finite-moment pattern is exact only for q=3,5,7 and does not assert monotonicity or a rate at another field.",
            "The degree-six polynomial gives a lower bound for the negative-sign probability, not its exact Haar value; its liminf consequence is conditional on six-moment convergence.",
            "The statistic is a toy reciprocal-coefficient minor, not Pick/Loewner, XD, or HCNC.",
            "No conclusion transfers from these function-field families to number-field L-functions.",
            "The finite comparison covers only q=3,5,7 and moment orders 1 through 6.",
        ],
    }


def make_evaluation(
    root: Path,
    config: dict[str, Any],
    specs: Sequence[dict[str, Any]],
    detector: dict[str, Any],
    comparator: dict[str, Any],
    q_scan: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    repo_root = root.parents[2]
    comparator_adapter = artifact_binding(
        root, COMPARATOR_SOURCE, "exact_usp4_laurent_adapter", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    qscan_adapter = artifact_binding(
        root, Q_SCAN_SOURCE, "exact_genus2_histogram_adapter", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    comparator_input = artifact_binding(
        root, COMPARATOR_FIXTURE, "exact_usp4_moment_certificate", "FINITE_COMPLETE", None
    )
    qscan_input = artifact_binding(
        root, Q_SCAN_FIXTURE, "complete_q3_q5_q7_histograms", "FINITE_COMPLETE", None
    )
    spec_bindings = [content_binding(spec) for spec in sorted(specs, key=lambda row: row["semantic_id"])]
    detector_binding = content_binding(detector)
    values = {
        "q_values": list(Q_VALUES),
        "maximum_moment": 6,
        "statistic": "USP4_TOY_MINOR_F",
        "torus_convention": "x,x^-1,y,y^-1",
        "weyl_order": 8,
    }
    input_fulfillments = [
        {
            "name": "lfunction_spec",
            "input_type": "LFUNCTION_SPEC",
            "coverage_class": "COMPLETE",
            "sources": [binding["semantic_id"] for binding in spec_bindings],
        },
        {
            "name": "exact_usp4_certificate",
            "input_type": "RAW_ARTIFACT",
            "coverage_class": "FINITE_COMPLETE",
            "sources": [COMPARATOR_SOURCE, COMPARATOR_FIXTURE],
        },
        {
            "name": "finite_family_histograms",
            "input_type": "RAW_ARTIFACT",
            "coverage_class": "FINITE_COMPLETE",
            "sources": [Q_SCAN_SOURCE, Q_SCAN_FIXTURE],
        },
    ]
    implementation_relative = "research/l-families/atlas/core/wrap_usp4_toy_minor_moments.py"
    implementation_sha256 = raw_sha256(repo_root / implementation_relative)
    adapters = [comparator_adapter, qscan_adapter]
    inputs = [comparator_input, qscan_input]
    identity_kernel = {
        "version": 1,
        "slug": EVALUATION_SLUG,
        "lfunction_spec_bindings": spec_bindings,
        "detector_contract_binding": detector_binding,
        "adapter_bindings": adapters,
        "configuration_sha256": sha256_hex(values),
        "input_sha256s": [binding["sha256"] for binding in inputs],
        "input_fulfillments_sha256": sha256_hex(input_fulfillments),
        "implementation_commit": config["code_commit"],
        "implementation_sha256": implementation_sha256,
        "seed": None,
    }
    semantic_id, identity_sha256 = semantic_identity("EVAL", EVALUATION_SLUG, identity_kernel)
    raw_result = build_raw_result(root, specs, detector, comparator, q_scan)
    result_relative = f"research/l-families/atlas/results/{semantic_id}.json"
    result_binding = {
        "role": "detector_result",
        "path": result_relative,
        "sha256": sha256_hex(raw_result),
        "hash_mode": "CANONICAL_JSON_UTF8_NFC",
        "coverage_class": "FINITE_COMPLETE",
        "media_type": "application/json",
        "schema_path": RAW_RESULT_SCHEMA,
        "notes": "Compact exact certificate; both source implementations and both full fixtures are separately bound.",
    }
    evaluation = {
        "schema_version": "riemann.atlas.evaluation_record.v1",
        "record_type": "EVALUATION_RECORD",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact USp(4) and q=3,5,7 genus-two toy-minor moment comparison",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(737), programme_ref(741)],
        "scope_boundary": (
            "Exact moment orders one through six for Haar USp(4) and the complete q=3,5,7 "
            "quintic families only; no convergence theorem or transfer beyond this scope."
        ),
        "supersedes": [],
        "subject": {
            "kind": "L_FUNCTION_SET",
            "description": (
                "The F_3, F_5, and F_7 quadratic-quintic genus-two families compared with the "
                "exact USp(4) Haar class-function model"
            ),
        },
        "lfunction_spec_bindings": spec_bindings,
        "detector_contract_binding": detector_binding,
        "adapter_bindings": adapters,
        "configuration": {"values": values, "canonical_sha256": sha256_hex(values)},
        "evaluation_scope": "FAMILY_MOMENT",
        "input_bindings": inputs,
        "input_fulfillments": input_fulfillments,
        "arithmetic": {
            "class": "EXACT_RATIONAL",
            "directed": False,
            "rounding_contract": "Integer Laurent convolution and reduced rational histogram moments only; no rounding.",
            "serialization_contract": "Canonical UTF-8 NFC JSON with exact integers and reduced rational records.",
        },
        "coverage": {
            "class": "FINITE_COMPLETE",
            "statement": (
                "All Haar moment orders 1 through 6 and all 162, 2500, and 14406 finite-family "
                "members at q=3,5,7 respectively."
            ),
            "omissions": [
                "moment orders above 6",
                "q outside 3,5,7",
                "proof of fixed-moment convergence",
                "analytic zero kernels and number-field transfer",
            ],
        },
        "rigor_level": EXACT_STATUS,
        "software": config["software"],
        "run": {
            "timestamp_utc": config["run_timestamp_utc"],
            "command": (
                "python research/l-families/atlas/core/wrap_usp4_toy_minor_moments.py --check"
            ),
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
                "F has exact USp(4) range [-20,4/3] and Haar moments -1, 3, -11, 56, "
                "-374, 3117. A degree-six moment majorant proves "
                "Pr_Haar(F<0)>=4360/12023. All six frozen moment gaps shrink directionally "
                "from q=3 to 5 to 7, without asserting monotonicity beyond those fields "
                "or convergence."
            ),
        },
        "result_hashes": [
            hash_object(
                result_binding["sha256"],
                "canonical JSON exact USp(4) toy-minor comparison result",
                "CANONICAL_JSON_UTF8_NFC",
            )
        ],
        "interpretation": {
            "status": "EXACT_FINITE",
            "statement": (
                "The character identity, range certificate, Weyl normalization, six Haar moments, "
                "three finite histogram moment sequences, and the six frozen directional gap "
                "checks are exact. The six-moment negative-sign lower bound is also exact; its "
                "liminf consequence and the proposed q-to-infinity moment relation are conditional "
                "and unproved, respectively."
            ),
            "smallest_gap": (
                "Prove the relevant hyperelliptic-family equidistribution; bounded continuity of "
                "each fixed power F(U)^m then gives moment convergence."
            ),
            "theorem_claim_id": None,
        },
        "assumptions": [],
        "firewalls": [
            {
                "code": "EXACT_NOT_CONVERGENCE",
                "statement": "Certified exact arithmetic does not certify the proposed fixed-moment limit.",
            },
            {
                "code": "SIGN_BOUND_NOT_SIGN_PROBABILITY",
                "statement": (
                    "The certified value 4360/12023 is a Haar lower bound, not the exact "
                    "negative-sign probability; the finite-family liminf remains conditional."
                ),
            },
            {
                "code": "TOY_NOT_ANALYTIC_KERNEL",
                "statement": "F and K_D are toy coefficient statistics, not Pick/Loewner, XD, or HCNC.",
            },
            {
                "code": "FINITE_Q_SCOPE",
                "statement": "The finite evidence contains exactly q=3,5,7 and moment orders 1 through 6.",
            },
            {
                "code": "NO_NUMBER_FIELD_TRANSFER",
                "statement": "No result transfers from these function fields to number-field L-functions.",
            },
        ],
        "notes": (
            "RIGOROUS_CERTIFIED applies to exact Laurent, Weyl, finite histogram, and polynomial-"
            "majorant arithmetic. The raw result separately marks moment convergence CONJECTURAL "
            "and PROPOSED, and the negative-sign liminf as conditional."
        ),
    }
    return evaluation, raw_result


def run(
    root: Path = ATLAS_ROOT,
) -> tuple[
    list[dict[str, Any]],
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
]:
    root = root.resolve()
    config = read_json(root / "config" / "pilot.json")
    comparator, q_scan = load_and_replay_fixtures(root)
    specs = load_family_specs(root)
    detector = build_detector(root)
    evaluation, raw_result = make_evaluation(
        root, config, specs, detector, comparator, q_scan
    )
    return specs, detector, evaluation, raw_result, comparator, q_scan


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
    detector: dict[str, Any],
    evaluation: dict[str, Any],
) -> list[Path]:
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
    return stale_detectors + stale_evaluations + stale_results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ATLAS_ROOT)
    parser.add_argument("--check", action="store_true", help="replay and compare without writing")
    args = parser.parse_args()
    root = args.root.resolve()
    specs, detector, evaluation, raw_result, _, _ = run(root)
    detector_path = root / "detectors" / f"{detector['semantic_id']}.json"
    evaluation_path = root / "evaluations" / f"{evaluation['semantic_id']}.json"
    result_path = root.parents[2] / evaluation["result"]["artifact"]["path"]
    expected = [
        (detector_path, detector),
        (evaluation_path, evaluation),
        (result_path, raw_result),
    ]
    stale = _stale_paths(root, detector, evaluation)
    if args.check:
        mismatches = [
            str(path) for path, value in expected if not path.is_file() or read_json(path) != value
        ]
        if stale:
            mismatches.extend(f"stale:{path}" for path in stale)
        if mismatches:
            raise SystemExit(f"USp(4) toy-minor atlas artifacts differ: {mismatches}")
        print("OK: exact USp(4) toy-minor atlas artifacts match; stale=0")
        return
    for path in stale:
        path.unlink()
    for path, value in expected:
        write_json(path, value)
    print(
        "PASS_USP4_TOY_MINOR_ATLAS "
        f"specs={','.join(spec['semantic_id'] for spec in specs)} "
        f"detector={detector['semantic_id']} evaluation={evaluation['semantic_id']} "
        f"stale_removed={len(stale)}"
    )


if __name__ == "__main__":
    main()
