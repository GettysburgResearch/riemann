from __future__ import annotations

import argparse
import hashlib
import platform
from fractions import Fraction
from pathlib import Path
from typing import Any

from atlas_core import ATLAS_ROOT, fraction_json, read_json, semantic_identity, sha256_hex, write_json
from local_euler import elliptic_trace, normalized_even_moment_term, primes_up_to, quadratic_character


RAW_RESULT_SCHEMA = "research/l-families/atlas/detectors/raw-schemas/local-euler-result.schema.json"
DETECTOR_DEFINITION = (
    "For each declared unramified prime p, write the unitary reciprocal local factor with prime "
    "coefficient b_p=-a_p/p^(w/2), then form the exact finite averages "
    "M_2(P)=|P|^(-1) sum_p b_p^2 and M_4(P)=|P|^(-1) sum_p b_p^4."
)


def raw_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def programme_ref(number: int) -> dict[str, Any]:
    return {
        "repository": "gfreund123/riemann",
        "kind": "GITHUB_ISSUE",
        "number": number,
        "url": f"https://github.com/gfreund123/riemann/issues/{number}",
    }


def hash_object(value: str, binds: str, mode: str = "RAW_BYTES") -> dict[str, str]:
    return {"algorithm": "sha256", "value": value, "binds": binds, "hash_mode": mode}


def make_lfunction_spec(
    *,
    slug: str,
    title: str,
    programme_numbers: list[int],
    source_identifiers: list[str],
    construction: str,
    classification: dict[str, Any],
    base_field: dict[str, Any],
    conductor: dict[str, Any],
    completed_normalization: dict[str, Any],
    analytic_properties: dict[str, Any],
    functional_equation: dict[str, Any],
    central_data: dict[str, Any],
    euler_product: dict[str, Any],
    zero_data: dict[str, Any],
    data_sources: list[dict[str, Any]],
    software: list[dict[str, str]],
    assumptions: list[dict[str, str]],
    notes: str,
    twist_parameters: list[str] | None = None,
) -> dict[str, Any]:
    identity_kernel = {
        "version": 1,
        "slug": slug,
        "base_field_label": base_field["label"],
        "construction": construction,
        "source_identifiers": sorted(source_identifiers),
        "twist_parameters": sorted(twist_parameters or []),
    }
    semantic_id, identity_sha256 = semantic_identity("LFUNC", slug, identity_kernel)
    return {
        "schema_version": "riemann.atlas.l_function_spec.v1",
        "record_type": "L_FUNCTION_SPEC",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": title,
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(number) for number in programme_numbers],
        "scope_boundary": "Phase-0 metadata and declared finite adapters only; no zero-set or global conclusion is inherited.",
        "supersedes": [],
        "classification": classification,
        "base_field": base_field,
        "conductor": conductor,
        "completed_normalization": completed_normalization,
        "analytic_properties": analytic_properties,
        "functional_equation": functional_equation,
        "central_data": central_data,
        "euler_product": euler_product,
        "zero_data": zero_data,
        "source_identifiers": source_identifiers,
        "data_sources": data_sources,
        "software": software,
        "assumptions": assumptions,
        "notes": notes,
    }


def generated_source(identifier: str, locator: str, timestamp: str, coverage: str) -> dict[str, Any]:
    return {
        "role": "definition_source",
        "source_kind": "GENERATED_EXACT",
        "identifier": identifier,
        "locator": locator,
        "version_or_retrieved_utc": timestamp,
        "coverage": coverage,
        "rigor_level": "RIGOROUS_CERTIFIED",
        "hashes": [],
        "retention": "GENERATED",
        "notes": "The finite adapter is checked into the repository and separately content-bound by each evaluation.",
    }


def build_specs(config: dict[str, Any], source_manifest: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    timestamp = config["run_timestamp_utc"]
    software = config["software"]
    specs: list[dict[str, Any]] = []
    metadata_by_slug: dict[str, Any] = {}

    zeta = make_lfunction_spec(
        slug="ZETA.RIEMANN",
        title="Riemann zeta reference object",
        programme_numbers=[741],
        source_identifiers=["DLMF:25.2"],
        construction="Riemann zeta function over Q",
        classification={
            "domain": "NUMBER_FIELD", "degree": 1, "object_type": "RIEMANN_ZETA", "family_id": "GL1.ZETA",
            "automorphic_class": "GL1", "self_duality": "SELF_DUAL", "symmetry_type": "UNKNOWN", "motivic_weight": 0,
        },
        base_field={"label": "Q", "characteristic": 0},
        conductor={"kind": "INTEGER", "value": "1", "norm_decimal": "1", "status": "IMPORTED_THEOREM"},
        completed_normalization={
            "normalization_id": "ZETA.UNITARY.STANDARD", "critical_center": "1/2",
            "exact_formula": "Lambda(s)=pi^(-s/2) Gamma(s/2) zeta(s)",
            "analytic_variable": "s", "conductor_factor": "1",
            "gamma_factors": [{"kind": "GAMMA_R", "shift": "0", "multiplicity": 1, "scale": "pi^(-s/2)"}],
            "notes": "The pole-removing xi prefactor is not used by the local-Euler detector.",
        },
        analytic_properties={
            "analytic_continuation": "IMPORTED_THEOREM", "functional_equation": "IMPORTED_THEOREM",
            "euler_product": "IMPORTED_THEOREM", "source_ref": "DLMF:25.2",
        },
        functional_equation={
            "exact_formula": "Lambda(s)=Lambda(1-s)", "root_number": "+1",
            "root_number_status": "IMPORTED_THEOREM", "source_ref": "DLMF:25.2",
        },
        central_data={
            "assertion": "EXACT", "value": 0, "rigor_level": "RIGOROUS_GIVEN_IMPORTED_THEOREM",
            "source_ref": "DLMF:25.2", "parity_forced": False,
            "notes": "This does not assert anything about noncentral zeros.",
        },
        euler_product={
            "good_factor_formula": "L_p(s)^(-1)=1-p^(-s)", "bad_factor_policy": "There are no finite bad primes.",
            "reciprocal_coefficient_definition": "mu_zeta(p)=-1",
            "coverage": "All rational primes admitted by the finite prime_bound.", "source_refs": ["DLMF:25.2"],
            "rigor_level": "RIGOROUS_GIVEN_IMPORTED_THEOREM",
        },
        zero_data={
            "usage": "NOT_USED", "coverage_class": "NOT_APPLICABLE",
            "rigor_level": "RIGOROUS_GIVEN_IMPORTED_THEOREM", "source_refs": [], "window": None,
            "precision": None, "central_zero_policy": "NOT_APPLICABLE",
        },
        data_sources=[{
            "role": "analytic_normalization", "source_kind": "PUBLICATION", "identifier": "DLMF:25.2",
            "locator": "https://dlmf.nist.gov/25.2", "version_or_retrieved_utc": timestamp,
            "coverage": "Definition, Euler product, and classical functional equation only.",
            "rigor_level": "RIGOROUS_GIVEN_IMPORTED_THEOREM", "hashes": [], "retention": "DURABLE_EXTERNAL",
            "notes": "Stable section identifier; no external page bytes are claimed as checked-in.",
        }],
        software=software,
        assumptions=[{"code": "CLASSICAL_ZETA_THEORY", "statement": "The classical analytic continuation and functional equation are imported.", "status": "IMPORTED"}],
        notes="Reference GL(1) row. RH is neither assumed nor tested.",
    )
    specs.append(zeta)
    metadata_by_slug["ZETA.RIEMANN"] = {"kind": "zeta", "weight": 0, "bad_primes": []}

    chi5 = make_lfunction_spec(
        slug="DIRICHLET.QUADRATIC.MOD5",
        title="Primitive quadratic Dirichlet L-function modulo 5",
        programme_numbers=[741],
        source_identifiers=["DIRICHLET:KRONECKER:5"],
        construction="Primitive real even quadratic character modulo 5",
        classification={
            "domain": "NUMBER_FIELD", "degree": 1, "object_type": "DIRICHLET_L", "family_id": "GL1.QUADRATIC.MOD5",
            "automorphic_class": "GL1", "self_duality": "SELF_DUAL", "symmetry_type": "SYMPLECTIC", "motivic_weight": 0,
        },
        base_field={"label": "Q", "characteristic": 0},
        conductor={"kind": "INTEGER", "value": "5", "norm_decimal": "5", "status": "PROVED_NATIVE"},
        completed_normalization={
            "normalization_id": "DIRICHLET.EVEN.UNITARY", "critical_center": "1/2",
            "exact_formula": "Lambda(s)=(5/pi)^(s/2) Gamma(s/2) L(s,chi_5)", "analytic_variable": "s",
            "conductor_factor": "5^(s/2)",
            "gamma_factors": [{"kind": "GAMMA_R", "shift": "0", "multiplicity": 1, "scale": "pi^(-s/2)"}],
            "notes": "chi_5(-1)=+1.",
        },
        analytic_properties={
            "analytic_continuation": "IMPORTED_THEOREM", "functional_equation": "IMPORTED_THEOREM",
            "euler_product": "IMPORTED_THEOREM", "source_ref": "CLASSICAL_DIRICHLET_THEORY",
        },
        functional_equation={
            "exact_formula": "Lambda(s)=Lambda(1-s)", "root_number": "+1",
            "root_number_status": "IMPORTED_THEOREM", "source_ref": "CLASSICAL_DIRICHLET_THEORY",
        },
        central_data={
            "assertion": "UNKNOWN", "value": None, "rigor_level": "DISCOVERY_ONLY", "source_ref": "NONE",
            "parity_forced": False, "notes": "Central values are outside this coefficient-only pilot.",
        },
        euler_product={
            "good_factor_formula": "L_p(s)^(-1)=1-chi_5(p)p^(-s) for p != 5", "bad_factor_policy": "Omit p=5.",
            "reciprocal_coefficient_definition": "mu_chi(p)=-chi_5(p)",
            "coverage": "All rational primes p<=prime_bound except 5.", "source_refs": ["DIRICHLET:KRONECKER:5"],
            "rigor_level": "RIGOROUS_CERTIFIED",
        },
        zero_data={
            "usage": "NOT_USED", "coverage_class": "NOT_APPLICABLE", "rigor_level": "DISCOVERY_ONLY",
            "source_refs": [], "window": None, "precision": None, "central_zero_policy": "NOT_APPLICABLE",
        },
        data_sources=[generated_source(
            "Legendre symbol modulo 5", "research/l-families/atlas/core/local_euler.py", timestamp,
            "Every finite character value requested by the declared prime window.",
        )],
        software=software,
        assumptions=[{"code": "CLASSICAL_DIRICHLET_THEORY", "statement": "Analytic continuation and the completed functional equation are imported.", "status": "IMPORTED"}],
        notes="Finite character and coefficient rows are exact; zero data is absent.",
    )
    specs.append(chi5)
    metadata_by_slug["DIRICHLET.QUADRATIC.MOD5"] = {"kind": "quadratic_character", "modulus": 5, "weight": 0, "bad_primes": [5]}

    for record in source_manifest["records"]:
        rank = record["analytic_rank"]
        label = record["curve_label"]
        slug = f"EC.{label.split('.')[0].upper()}.R{rank}"
        root_number = record["root_number"]
        spec = make_lfunction_spec(
            slug=slug,
            title=f"Elliptic-curve L-function {label}, imported rank {rank}",
            programme_numbers=[738, 741],
            source_identifiers=[f"LMFDB:EC:{label}", f"LMFDB:LFUNCTION:{label.split('.')[0]}.a"],
            construction=f"L-function of the rational elliptic curve with LMFDB label {label}",
            classification={
                "domain": "NUMBER_FIELD", "degree": 2, "object_type": "ELLIPTIC_CURVE_L", "family_id": "GL2.ELLIPTIC.RANK_STRESS",
                "automorphic_class": "GL2", "self_duality": "SELF_DUAL",
                "symmetry_type": "ORTHOGONAL_ODD" if root_number == "-1" else "ORTHOGONAL_EVEN", "motivic_weight": 1,
            },
            base_field={"label": "Q", "characteristic": 0},
            conductor={
                "kind": "INTEGER", "value": str(record["conductor"]), "norm_decimal": str(record["conductor"]),
                "status": "IMPORTED_THEOREM",
            },
            completed_normalization={
                "normalization_id": "EC.WEIGHT2.UNITARY.SHIFT_HALF", "critical_center": "1/2",
                "exact_formula": "Lambda_u(s)=N^((s+1/2)/2)(2*pi)^(-(s+1/2)) Gamma(s+1/2) L(s+1/2,E)",
                "analytic_variable": "unitary s", "conductor_factor": "N^((s+1/2)/2)",
                "gamma_factors": [{
                    "kind": "EXPLICIT_OTHER", "shift": "1/2", "multiplicity": 1,
                    "scale": "(2*pi)^(-(s+1/2))", "notes": "A Gamma_C presentation differs by an s-independent factor.",
                }],
                "notes": "The standard weight-2 center s=1 is shifted to unitary center 1/2.",
            },
            analytic_properties={
                "analytic_continuation": "IMPORTED_THEOREM", "functional_equation": "IMPORTED_THEOREM",
                "euler_product": "IMPORTED_THEOREM", "source_ref": "ELLIPTIC_CURVE_MODULARITY_UNPINNED",
            },
            functional_equation={
                "exact_formula": "Lambda_u(s)=w_E Lambda_u(1-s)", "root_number": root_number,
                "root_number_status": "IMPORTED_THEOREM", "source_ref": f"LMFDB:LFUNCTION:{label.split('.')[0]}.a",
            },
            central_data={
                "assertion": "EXACT", "value": rank, "rigor_level": "DISCOVERY_ONLY",
                "source_ref": f"LMFDB:LFUNCTION:{label.split('.')[0]}.a", "parity_forced": root_number == "-1",
                "notes": "LMFDB display imported for stress-test classification; not independently certified here.",
            },
            euler_product={
                "good_factor_formula": "L_p^u(s)^(-1)=1-(a_p/sqrt(p))p^(-s)+p^(-2s)",
                "bad_factor_policy": (
                    f"At the semistable bad prime {record['bad_primes'][0]}, the classical reciprocal factor is "
                    f"1-({record['bad_local_trace']})T; the local-Euler moment detector explicitly omits this prime."
                ),
                "reciprocal_coefficient_definition": "mu_E(p)=-a_p and mu_E(p^2)=p in the classical variable at good p",
                "coverage": "Every good rational prime p<=prime_bound is independently point-counted from the imported model.",
                "source_refs": [f"LMFDB:EC:{label}"], "rigor_level": "DISCOVERY_ONLY",
            },
            zero_data={
                "usage": "NOT_USED", "coverage_class": "NOT_APPLICABLE", "rigor_level": "DISCOVERY_ONLY",
                "source_refs": [], "window": None, "precision": None, "central_zero_policy": "NOT_APPLICABLE",
            },
            data_sources=[
                {
                    "role": "curve_metadata", "source_kind": "DATABASE", "identifier": f"LMFDB:EC:{label}",
                    "locator": record["api_url"], "version_or_retrieved_utc": record["api_response_timestamp"],
                    "coverage": "Weierstrass coefficients, conductor, and bad-prime list.", "rigor_level": "DISCOVERY_ONLY",
                    "hashes": [hash_object(record["api_response_sha256"], "Observed UTF-8 API response; bytes are not retained in this compact release")],
                    "retention": "DYNAMIC_EXTERNAL", "notes": "The unretained response hash is an observation lock, not an independently replayable source certificate.",
                },
                {
                    "role": "rank_root_number", "source_kind": "DATABASE", "identifier": f"LMFDB:LFUNCTION:{label.split('.')[0]}.a",
                    "locator": record["lfunction_url"], "version_or_retrieved_utc": record["api_response_timestamp"],
                    "coverage": "Displayed functional-equation sign and analytic rank.", "rigor_level": "DISCOVERY_ONLY",
                    "hashes": [], "retention": "DYNAMIC_EXTERNAL", "notes": "Dynamic page identified but not archived.",
                },
            ],
            software=software,
            assumptions=[
                {"code": "CURVE_MODEL_IMPORTED", "statement": "The LMFDB Weierstrass model identifies the intended isogeny-class L-function.", "status": "IMPORTED"},
                {"code": "MODULARITY_IMPORTED", "statement": "Analytic continuation and the functional equation are imported from elliptic-curve modularity.", "status": "IMPORTED"},
            ],
            notes="Point counts are exact for the imported model; rank and sign remain discovery metadata.",
        )
        specs.append(spec)
        metadata_by_slug[slug] = {
            "kind": "elliptic_curve",
            "ainvs": record["ainvs"],
            "weight": 1,
            "bad_primes": record["bad_primes"],
            "bad_local_trace": record["bad_local_trace"],
        }
    return specs, metadata_by_slug


def build_detector(root: Path) -> dict[str, Any]:
    normalization_identity = [
        "Use the unitary local variable and stored motivic weight w.",
        "Omit, rather than guess, every declared bad Euler factor.",
    ]
    identity_kernel = {
        "version": 1,
        "slug": "LOCAL_EULER.EVEN_MOMENTS",
        "mathematical_definition": DETECTOR_DEFINITION,
        "kernel_convention": "COEFFICIENT_DISPERSION",
        "central_zero_policy": "NOT_APPLICABLE",
        "normalization_requirements": normalization_identity,
        "contract_revision": 1,
    }
    semantic_id, identity_sha256 = semantic_identity("DETECTOR", "LOCAL_EULER.EVEN_MOMENTS", identity_kernel)
    implementation_path = root / "core" / "run_pilot.py"
    return {
        "schema_version": "riemann.atlas.detector_contract.v1",
        "record_type": "DETECTOR_CONTRACT",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact normalized local-Euler even moments",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(741), programme_ref(738)],
        "scope_boundary": "Exact finite local-coefficient statistic only; it consumes no zero data and has no RH/GRH predicate.",
        "supersedes": [],
        "detector_kind": "COEFFICIENT_DISPERSION",
        "mathematical_definition": DETECTOR_DEFINITION,
        "kernel_convention": "COEFFICIENT_DISPERSION",
        "central_zero_policy": "NOT_APPLICABLE",
        "required_inputs": [
            {"name": "lfunction_spec", "input_type": "LFUNCTION_SPEC", "required": True, "coverage_requirement": "COMPLETE"},
            {"name": "local_euler_factors", "input_type": "LOCAL_EULER_FACTORS", "required": True, "coverage_requirement": "FINITE_COMPLETE"},
        ],
        "parameters": [
            {"name": "prime_bound", "value_type": "INTEGER", "required": True, "domain": "integer >= 2", "constraints": {"minimum": 2}},
            {"name": "moments", "value_type": "INTEGER_LIST", "required": True, "domain": "positive even integers", "constraints": {"nonempty": True, "element_minimum": 1, "element_multiple_of": 2}, "default": [2, 4]},
            {"name": "bad_prime_policy", "value_type": "ENUM", "required": True, "domain": "DECLARED_OMIT", "constraints": {"enum_values": ["DECLARED_OMIT"]}, "default": "DECLARED_OMIT"},
        ],
        "normalization_requirements": [
            {"field": "classification.motivic_weight", "requirement": normalization_identity[0], "comparison_role": "SCALING"},
            {"field": "euler_product.bad_factor_policy", "requirement": normalization_identity[1], "comparison_role": "FIREWALL"},
            {"field": "completed_normalization.normalization_id", "requirement": "Bind the exact LFunctionSpec record content in every evaluation.", "comparison_role": "IDENTITY"},
        ],
        "invariances": [
            {"code": "ISOGENY_GOOD_ROWS", "statement": "Good-prime rows are invariant within a rational elliptic-curve isogeny class.", "status": "PROVED"},
            {"code": "UNITARY_TOP_MODULUS", "statement": "The normalized top reciprocal local coefficient has modulus one for every included self-dual factor.", "status": "PROVED"},
        ],
        "family_adapters": [
            {"family": "GL1_ZETA_AND_REAL_DIRICHLET", "status": "REQUIRED_AVAILABLE", "adapter_path": "research/l-families/atlas/core/local_euler.py", "correction": "Omit conductor primes and use weight zero."},
            {"family": "GL2_ELLIPTIC", "status": "REQUIRED_AVAILABLE", "adapter_path": "research/l-families/atlas/core/local_euler.py", "correction": "Point-count a_p, divide even moments by p^(w*k/2), and omit bad primes."},
            {"family": "FUNCTION_FIELD", "status": "REQUIRED_AVAILABLE", "adapter_path": "research/l-families/atlas/function_field/pilot.py", "correction": "Use degree as scale; bespoke raw results are separately wrapped."},
        ],
        "theorem_links": [{"semantic_id": "NONE", "status": "NONE", "scope": "No canonical theorem is inferred from this Phase-0 statistic."}],
        "failure_modes": [
            {"code": "BAD_PRIME_AS_GOOD", "description": "Substituting a good factor at a conductor prime changes the object.", "hostile_control": "Validator requires the declared omit policy."},
            {"code": "MOTIVIC_SCALE_MIX", "description": "Raw a_p values are not comparable across weights.", "hostile_control": "Only exact even powers after p^(w/2) normalization are emitted."},
            {"code": "FINITE_TO_LIMIT", "description": "A short prime window is not a Sato-Tate or family-moment theorem.", "hostile_control": "Evaluation scope is SINGLE_OBJECT with FINITE_COMPLETE coverage."},
            {"code": "LOCAL_TO_GRH", "description": "Local coefficient rows contain no zero-completeness information.", "hostile_control": "global_claim_allowed is false and zero data is NOT_USED."},
        ],
        "output_contract": {
            "representations": ["EXACT_RATIONAL"], "arithmetic_classes": ["EXACT_RATIONAL"],
            "raw_schema_path": RAW_RESULT_SCHEMA, "global_claim_allowed": False,
        },
        "reference_implementation": {
            "path": "research/l-families/atlas/core/run_pilot.py", "entry_point": "evaluate_local_euler",
            "version": "1", "source_sha256": raw_sha256(implementation_path),
        },
        "formalization_refs": [{"state": "DEFINITION_READY", "target": "Finite rational aggregation after a typed local normalization.", "path": None}],
        "notes": "The function-field and GL(2) pilots remain raw adapters/results until wrapped by EvaluationRecord objects.",
    }


def trace_for_prime(metadata: dict[str, Any], prime: int) -> int:
    if metadata["kind"] == "zeta":
        return 1
    if metadata["kind"] == "quadratic_character":
        return quadratic_character(prime, metadata["modulus"])
    if metadata["kind"] == "elliptic_curve":
        return elliptic_trace(prime, metadata["ainvs"])
    raise ValueError(f"unsupported adapter kind {metadata['kind']!r}")


def evaluate_local_euler(spec: dict[str, Any], detector_id: str, metadata: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    included = [p for p in primes_up_to(config["prime_bound"]) if p not in metadata["bad_primes"]]
    rows: list[dict[str, Any]] = []
    second_terms: list[Fraction] = []
    fourth_terms: list[Fraction] = []
    sign_counts = {"negative": 0, "zero": 0, "positive": 0}
    all_unit_magnitude = True
    all_hasse = True
    for prime in included:
        trace = trace_for_prime(metadata, prime)
        inverse_sign = -trace
        sign_counts["zero" if inverse_sign == 0 else ("positive" if inverse_sign > 0 else "negative")] += 1
        square = normalized_even_moment_term(trace, prime, 2, metadata["weight"])
        fourth = normalized_even_moment_term(trace, prime, 4, metadata["weight"])
        second_terms.append(square)
        fourth_terms.append(fourth)
        unit_magnitude = square == 1
        all_unit_magnitude &= unit_magnitude
        hasse = metadata["kind"] != "elliptic_curve" or trace * trace <= 4 * prime
        all_hasse &= hasse
        coefficient = str(-trace) if metadata["weight"] == 0 else ("0" if trace == 0 else f"{-trace}/sqrt({prime})")
        rows.append({
            "p": prime, "a_p": trace, "inverse_prime_coefficient": coefficient,
            "coefficient_square": fraction_json(square.numerator, square.denominator),
            "coefficient_fourth": fraction_json(fourth.numerator, fourth.denominator),
            "unit_magnitude": unit_magnitude, "hasse_control": hasse,
        })
    mean_square = sum(second_terms, Fraction()) / len(second_terms)
    mean_fourth = sum(fourth_terms, Fraction()) / len(fourth_terms)
    return {
        "schema_version": "riemann.atlas.raw.local_euler_result.v1",
        "subject_semantic_id": spec["semantic_id"],
        "detector_semantic_id": detector_id,
        "per_prime": rows,
        "summary": {
            "prime_count": len(rows), "mean_square": fraction_json(mean_square.numerator, mean_square.denominator),
            "mean_fourth": fraction_json(mean_fourth.numerator, mean_fourth.denominator), "sign_counts": sign_counts,
            "unitary_top_coefficient_modulus_squared": "1", "unitary_top_coefficient_control": True,
            "naive_prime_coefficient_unit_magnitude": all_unit_magnitude, "hasse_control": all_hasse,
        },
    }


def artifact_binding(root: Path, relative_path: str, role: str, coverage: str, schema_path: str | None, mode: str = "CANONICAL_JSON_UTF8_NFC") -> dict[str, Any]:
    path = root.parents[2] / relative_path
    digest = sha256_hex(read_json(path)) if mode == "CANONICAL_JSON_UTF8_NFC" else raw_sha256(path)
    return {
        "role": role, "path": relative_path, "sha256": digest, "hash_mode": mode,
        "coverage_class": coverage, "media_type": "application/json" if relative_path.endswith(".json") else "text/x-python",
        "schema_path": schema_path, "notes": "Content checked by the offline atlas validator.",
    }


def make_evaluation(
    root: Path,
    spec: dict[str, Any],
    spec_path: str,
    detector: dict[str, Any],
    detector_path: str,
    raw_result: dict[str, Any],
    metadata: dict[str, Any],
    config: dict[str, Any],
) -> tuple[dict[str, Any], str]:
    spec_binding = {"semantic_id": spec["semantic_id"], "record_sha256": sha256_hex(spec)}
    detector_binding = {"semantic_id": detector["semantic_id"], "record_sha256": sha256_hex(detector)}
    adapter_relative = "research/l-families/atlas/core/local_euler.py"
    adapter = artifact_binding(root, adapter_relative, "family_adapter", "FINITE_COMPLETE", None, "RAW_BYTES")
    if metadata["kind"] == "elliptic_curve":
        input_relative = "research/l-families/atlas/sources/lmfdb-curves.json"
        input_binding = artifact_binding(root, input_relative, "primitive_source_manifest", "PARTIAL", None)
    else:
        input_relative = adapter_relative
        input_binding = artifact_binding(root, input_relative, "primitive_exact_definition", "FINITE_COMPLETE", None, "RAW_BYTES")
    config_values = {"prime_bound": config["prime_bound"], "moments": [2, 4], "bad_prime_policy": "DECLARED_OMIT"}
    configuration_sha256 = sha256_hex(config_values)
    input_fulfillments = [
        {"name": "lfunction_spec", "input_type": "LFUNCTION_SPEC", "coverage_class": "COMPLETE", "sources": [spec["semantic_id"]]},
        {"name": "local_euler_factors", "input_type": "LOCAL_EULER_FACTORS", "coverage_class": "FINITE_COMPLETE", "sources": sorted({adapter_relative, input_relative})},
    ]
    implementation_relative = "research/l-families/atlas/core/run_pilot.py"
    implementation_sha256 = raw_sha256(root.parents[2] / implementation_relative)
    slug = spec["identity_kernel"]["slug"] + ".LOCAL_EULER"
    identity_kernel = {
        "version": 1, "slug": slug, "lfunction_spec_bindings": [spec_binding],
        "detector_contract_binding": detector_binding, "adapter_bindings": [adapter],
        "configuration_sha256": configuration_sha256, "input_sha256s": sorted([input_binding["sha256"]]),
        "input_fulfillments_sha256": sha256_hex(input_fulfillments),
        "implementation_commit": config["code_commit"], "implementation_sha256": implementation_sha256, "seed": None,
    }
    semantic_id, identity_sha256 = semantic_identity("EVAL", slug, identity_kernel)
    result_relative = f"research/l-families/atlas/results/{semantic_id}.json"
    result_path = root.parents[2] / result_relative
    write_json(result_path, raw_result)
    result_binding = artifact_binding(root, result_relative, "detector_result", "FINITE_COMPLETE", RAW_RESULT_SCHEMA)
    rigor = "DISCOVERY_ONLY" if metadata["kind"] == "elliptic_curve" else "RIGOROUS_GIVEN_IMPORTED_THEOREM"
    evaluation = {
        "schema_version": "riemann.atlas.evaluation_record.v1", "record_type": "EVALUATION_RECORD",
        "semantic_id": semantic_id, "identity_sha256": identity_sha256, "identity_kernel": identity_kernel,
        "title": f"Local-Euler even moments for {spec['title']}", "revision": 1, "record_state": "DRAFT",
        "programme_refs": spec["programme_refs"],
        "scope_boundary": f"Every declared good prime p<={config['prime_bound']}; no bad factor, prime limit, family average, or zero conclusion.",
        "supersedes": [], "subject": {"kind": "L_FUNCTION", "description": spec["title"]},
        "lfunction_spec_bindings": [spec_binding], "detector_contract_binding": detector_binding,
        "adapter_bindings": [adapter], "configuration": {"values": config_values, "canonical_sha256": configuration_sha256},
        "evaluation_scope": "SINGLE_OBJECT", "input_bindings": [input_binding], "input_fulfillments": input_fulfillments,
        "arithmetic": {
            "class": "EXACT_RATIONAL", "directed": False,
            "rounding_contract": "No real-number rounding; point counts and even moments use integers/Fraction.",
            "serialization_contract": "Sorted-key JSON; hashes use canonical UTF-8 NFC JSON without whitespace.",
        },
        "coverage": {
            "class": "FINITE_COMPLETE", "statement": f"Every prime p<={config['prime_bound']} except declared bad primes {metadata['bad_primes']}.",
            "omissions": ["bad Euler factors", "primes above the bound", "zero ordinates"],
        },
        "rigor_level": rigor, "software": config["software"],
        "run": {
            "timestamp_utc": config["run_timestamp_utc"], "command": "python research/l-families/atlas/core/run_pilot.py",
            "code_commit": config["code_commit"], "implementation_path": implementation_relative,
            "implementation_sha256": implementation_sha256,
        },
        "central_zero_policy_applied": "NOT_APPLICABLE",
        "result": {
            "representation": "EXACT_RATIONAL", "predicate_outcome": "NOT_APPLICABLE", "artifact": result_binding,
            "summary": "Exact local trace rows and exact rational second/fourth moments on the declared finite window.",
        },
        "result_hashes": [hash_object(result_binding["sha256"], "Canonical JSON raw result", "CANONICAL_JSON_UTF8_NFC")],
        "interpretation": {
            "status": "EXACT_FINITE", "statement": "The displayed finite rows and even moments are exact given the bound source object.",
            "smallest_gap": "A proved prime or twist-family limiting theorem is required before nominating a universal moment law.",
            "theorem_claim_id": None,
        },
        "assumptions": spec["assumptions"],
        "firewalls": [
            {"code": "NO_RH_GRH", "statement": "No finite local-Euler table establishes RH or GRH."},
            {"code": "NO_RANK_CORRELATION", "statement": "One curve per displayed rank cannot support a rank-conditioned law."},
            {"code": "BAD_PRIMES_OMITTED", "statement": "Bad primes are omitted rather than assigned a guessed good factor."},
            {"code": "ZERO_DATA_ABSENT", "statement": "The result has no zero-completeness content."},
        ],
        "notes": f"Spec path {spec_path}; detector path {detector_path}. Records remain DRAFT until an exact PR/head provenance sidecar exists.",
    }
    return evaluation, result_relative


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the small exact Phase-0 atlas corpus and local-Euler rows.")
    parser.add_argument("--root", type=Path, default=ATLAS_ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    config = read_json(root / "config" / "pilot.json")
    manifest = read_json(root / "sources" / "lmfdb-curves.json")
    specs, metadata_by_slug = build_specs(config, manifest)
    detector = build_detector(root)
    detector_relative = f"research/l-families/atlas/detectors/{detector['semantic_id']}.json"
    write_json(root / "detectors" / f"{detector['semantic_id']}.json", detector)
    evaluation_count = 0
    for spec in specs:
        slug = spec["identity_kernel"]["slug"]
        spec_relative = f"research/l-families/atlas/specs/{spec['semantic_id']}.json"
        write_json(root / "specs" / f"{spec['semantic_id']}.json", spec)
        raw_result = evaluate_local_euler(spec, detector["semantic_id"], metadata_by_slug[slug], config)
        evaluation, _ = make_evaluation(
            root, spec, spec_relative, detector, detector_relative, raw_result, metadata_by_slug[slug], config
        )
        write_json(root / "evaluations" / f"{evaluation['semantic_id']}.json", evaluation)
        evaluation_count += 1
    print(
        f"PASS_ATLAS_LOCAL_EULER specs={len(specs)} evaluations={evaluation_count} "
        f"python={platform.python_version()} prime_bound={config['prime_bound']}"
    )


if __name__ == "__main__":
    main()
