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
CHARACTER_DECOMPOSITION_SOURCE = (
    "research/l-families/atlas/function_field/"
    "usp4_toy_minor_character_decomposition.py"
)
CHARACTER_DECOMPOSITION_FIXTURE = (
    "research/l-families/atlas/function_field/"
    "usp4_toy_minor_character_decomposition.json"
)
TWELVE_MOMENT_SOURCE = (
    "research/l-families/atlas/function_field/usp4_twelve_moment_sign_bound.py"
)
TWELVE_MOMENT_FIXTURE = (
    "research/l-families/atlas/function_field/usp4_twelve_moment_sign_bound.json"
)
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
CHARACTER_DECOMPOSITION_STATUS = "PROVED_EXACT_C2_CHARACTER_DECOMPOSITION"
TWELVE_MOMENT_STATUS = "RIGOROUS_EXACT_FINITE_MOMENT_MAJORANT"
HAAR_MOMENTS = (-1, 3, -11, 56, -374, 3117)
HAAR_MOMENTS_12 = (
    -1,
    3,
    -11,
    56,
    -374,
    3117,
    -30321,
    327688,
    -3815668,
    46998100,
    -605231862,
    8084025096,
)
HAAR_CENTERED_MOMENTS = (0, 2, -4, 27, -178, 1533)
HAAR_CUMULANTS = (-1, 2, -4, 15, -98, 803)
CHARACTER_IRREDUCIBLE_COUNTS = (3, 9, 16, 25, 36, 49)
TENSOR_DIMENSIONS = tuple(20**order for order in range(1, 7))
POSITIVE_ROOTS = ((2, 0), (0, 2), (1, 1), (1, -1))
DETECTOR_DEFINITION = (
    "For U in USp(4), set F(U)=(Tr U)^2-e_2(U)^2. Prove the exact Laurent-character "
    "identity F=-(1+chi_{omega_2}+chi_{2*omega_2}), certify the exact range [-20,4/3], "
    "decompose F^m for m=1,...,6 into irreducible C_2 characters, evaluate the first twelve "
    "Haar moments by the normalized C_2 Weyl constant-term formula, "
    "and compare them exactly with the complete q=3,5,7 histogram moments of K_D/q^2, "
    "where K_D=q*a_D^2-b_D^2. Use exact degree-six and degree-twelve polynomial "
    "majorants to certify successively stronger lower bounds for the negative-sign probability."
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


def load_and_replay_fixtures(
    root: Path,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
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

    support_majorant = sign_certificate.get("support_adapted_majorant", {})
    generated_support = comparator_module.support_adapted_sign_majorant()
    stored_support_coefficients = [
        _fraction(pair, f"support-majorant coefficient {index}")
        for index, pair in enumerate(
            support_majorant.get("coefficients_in_x_low_to_high", [])
        )
    ]
    if stored_support_coefficients != generated_support["polynomial_x"]:
        raise ValueError("support-adapted majorant coefficients drifted")
    stored_bernstein = [
        _fraction(pair, f"support-majorant Bernstein coefficient {index}")
        for index, pair in enumerate(
            support_majorant.get(
                "positive_interval_quotient_bernstein_coefficients_degree_4", []
            )
        )
    ]
    if stored_bernstein != generated_support["quotient_bernstein"] or not all(
        coefficient > 0 for coefficient in stored_bernstein
    ):
        raise ValueError("support-adapted majorant Bernstein certificate drifted")
    support_haar = support_majorant.get("haar", {})
    if _fraction(
        support_haar.get("moment_majorant_nonnegative_upper_bound", []),
        "support-adapted Haar nonnegative upper bound",
    ) != Fraction(3879608783, 6358302720):
        raise ValueError("support-adapted Haar nonnegative upper bound drifted")
    if _fraction(
        support_haar.get("negative_probability_lower_bound", []),
        "support-adapted Haar negative lower bound",
    ) != Fraction(2478693937, 6358302720):
        raise ValueError("support-adapted Haar negative lower bound drifted")
    support_rows = support_majorant.get("finite_q_bounds", [])
    if [row.get("q") for row in support_rows] != list(Q_VALUES):
        raise ValueError("support-adapted finite sign rows drifted")
    for row, baseline_row in zip(support_rows, finite_sign_rows, strict=True):
        q = int(row["q"])
        moments = [
            _fraction(entry["finite_exact"], f"q={q} support sign moment")
            for entry in comparisons[q]["moments"]
        ]
        expected_upper = comparator_module.polynomial_moment(
            generated_support["polynomial_x"], moments
        )
        stored_upper = _fraction(
            row["moment_majorant_nonnegative_upper_bound"],
            f"q={q} support nonnegative upper bound",
        )
        stored_lower = _fraction(
            row["negative_probability_lower_bound"],
            f"q={q} support negative lower bound",
        )
        observed = _fraction(
            row["observed_negative_fraction"], f"q={q} support observed sign"
        )
        if (
            stored_upper != expected_upper
            or stored_lower != 1 - expected_upper
            or stored_lower
            <= _fraction(
                baseline_row["negative_probability_lower_bound"],
                f"q={q} baseline negative lower bound",
            )
            or stored_lower > observed
            or row.get("verified_bound_holds") is not True
        ):
            raise ValueError(f"q={q} support-adapted sign certificate mismatch")
    if support_majorant.get("strictly_improves_cubic_square_bound") is not True:
        raise ValueError("support-adapted majorant lost its strict-improvement check")
    conditional = sign_certificate.get("conditional_consequence", {})
    if conditional.get("status") != "CONDITIONAL_ON_FIRST_SIX_MOMENT_CONVERGENCE":
        raise ValueError("negative-sign liminf consequence lost its conditional status")
    if conditional.get("not_an_equidistribution_proof") is not True:
        raise ValueError("negative-sign conditional consequence lost its theorem firewall")
    if "2478693937/6358302720" not in conditional.get("statement", ""):
        raise ValueError("negative-sign conditional consequence uses the wrong exact bound")
    character_decomposition = read_json(repo_root / CHARACTER_DECOMPOSITION_FIXTURE)
    character_module = _load_module(
        repo_root,
        CHARACTER_DECOMPOSITION_SOURCE,
        "_riemann_atlas_usp4_toy_minor_character_decomposition",
    )
    if character_module.build_fixture() != character_decomposition:
        raise ValueError(
            "USp(4) character-decomposition fixture differs from its exact guarded replay"
        )
    producer = character_decomposition.get("producer", {})
    character_text = (
        (repo_root / CHARACTER_DECOMPOSITION_SOURCE)
        .read_text(encoding="utf-8")
        .replace("\r\n", "\n")
    )
    if producer.get("script") != Path(CHARACTER_DECOMPOSITION_SOURCE).name or producer.get(
        "source_sha256_lf_normalized"
    ) != hashlib.sha256(character_text.encode("utf-8")).hexdigest():
        raise ValueError("USp(4) character-decomposition producer source lock mismatch")
    if character_decomposition.get("status") != CHARACTER_DECOMPOSITION_STATUS:
        raise ValueError("USp(4) character decomposition lost its exact status")
    group = character_decomposition.get("group", {})
    if group.get("root_system") != "C2" or group.get("weyl_order") != 8:
        raise ValueError("USp(4) character decomposition uses the wrong C2 convention")
    if group.get("highest_weight_convention") != (
        "a*omega1+b*omega2 corresponds to e-basis coordinates "
        "(lambda1,lambda2)=(a+b,b)"
    ):
        raise ValueError("USp(4) highest-weight convention drifted")
    character_identity = character_decomposition.get("character_identity", {})
    if (
        character_identity.get("defining_formula") != "F=(Tr U)^2-e_2(U)^2"
        or character_identity.get("F_equals_minus_G") is not True
        or character_identity.get("laurent_identity_verified_exactly") is not True
        or character_identity.get("G_dimension") != 20
        or character_identity.get("constituent_dimensions") != [1, 5, 14]
    ):
        raise ValueError("USp(4) character-decomposition identity drifted")
    powers = character_decomposition.get("powers", [])
    if [row.get("power") for row in powers] != list(range(1, 7)):
        raise ValueError("USp(4) character-decomposition powers drifted")
    for order, row in enumerate(powers, start=1):
        sign = -1 if order % 2 else 1
        decomposition = row.get("decomposition", [])
        if (
            row.get("global_sign_from_F_equals_minus_G") != sign
            or row.get("irreducible_count") != CHARACTER_IRREDUCIBLE_COUNTS[order - 1]
            or len(decomposition) != CHARACTER_IRREDUCIBLE_COUNTS[order - 1]
            or row.get("tensor_dimension") != TENSOR_DIMENSIONS[order - 1]
            or row.get("dimension_sum_from_decomposition") != TENSOR_DIMENSIONS[order - 1]
            or row.get("trivial_coefficient_in_F_power") != HAAR_MOMENTS[order - 1]
            or row.get("independent_weyl_constant_term_haar_moment")
            != HAAR_MOMENTS[order - 1]
            or row.get("reconstruction_exact") is not True
        ):
            raise ValueError(f"USp(4) character-decomposition summary drifted at m={order}")
        for entry in decomposition:
            highest = entry.get("highest_weight", {})
            a = highest.get("omega1_coefficient")
            b = highest.get("omega2_coefficient")
            multiplicity = entry.get("tensor_multiplicity_in_G_power")
            if (
                isinstance(a, bool)
                or not isinstance(a, int)
                or isinstance(b, bool)
                or not isinstance(b, int)
                or isinstance(multiplicity, bool)
                or not isinstance(multiplicity, int)
                or a < 0
                or b < 0
                or multiplicity <= 0
                or highest.get("notation") != f"{a}*omega1+{b}*omega2"
                or highest.get("e_basis_coordinates") != [a + b, b]
                or entry.get("coefficient_in_F_power") != sign * multiplicity
                or entry.get("dimension") != character_module.weyl_dimension(a, b)
                or entry.get("dimension_contribution_to_G_power")
                != multiplicity * entry["dimension"]
            ):
                raise ValueError(
                    f"USp(4) irreducible-character record drifted at m={order}"
                )
    verification = character_decomposition.get("verification", {})
    if not all(
        verification.get(key) is True
        for key in (
            "all_kostant_character_dimensions_match_weyl_formula",
            "all_generated_characters_are_weyl_invariant",
            "all_power_reconstructions_exact",
            "all_tensor_multiplicities_positive",
            "all_F_power_coefficients_have_uniform_sign_minus_one_to_m",
            "all_dimension_sums_equal_20_to_m",
            "all_trivial_multiplicities_match_independent_haar_constant_terms",
        )
    ):
        raise ValueError("USp(4) character-decomposition verification failed")
    if verification.get("signed_trivial_multiplicities") != list(HAAR_MOMENTS):
        raise ValueError("USp(4) signed trivial multiplicities drifted")
    all_power = character_decomposition.get("all_power_corollary", {})
    if (
        all_power.get("integrality") is not True
        or all_power.get("strict_sign_rule")
        != "(-1)^m*Haar(F^m)>0 for every m>=0"
        or all_power.get("scope")
        != "compact-group Haar moments only; no finite-family convergence"
    ):
        raise ValueError("USp(4) all-power Haar-moment corollary drifted")
    resource = character_decomposition.get("resource_contract", {})
    if (
        resource.get("maximum_power") != 6
        or resource.get("random_sampling") is not False
        or resource.get("numerical_integration") is not False
        or resource.get("external_cas") is not False
    ):
        raise ValueError("USp(4) character-decomposition resource contract drifted")
    operation_caps = resource.get("operation_caps", {})
    observed_operations = resource.get("observed_operations", {})
    if set(operation_caps) != set(observed_operations) or any(
        not isinstance(observed_operations[name], int)
        or observed_operations[name] < 0
        or observed_operations[name] > operation_caps[name]
        for name in operation_caps
    ):
        raise ValueError("USp(4) character-decomposition operation guard failed")

    twelve_moment = read_json(repo_root / TWELVE_MOMENT_FIXTURE)
    _verify_payload_hash(twelve_moment, "USp(4) twelve-moment fixture")
    twelve_module = _load_module(
        repo_root,
        TWELVE_MOMENT_SOURCE,
        "_riemann_atlas_usp4_twelve_moment_sign_bound",
    )
    if twelve_module.build_fixture() != twelve_moment:
        raise ValueError("USp(4) twelve-moment fixture differs from its exact replay")
    twelve_producer = twelve_moment.get("producer", {})
    twelve_text = (
        (repo_root / TWELVE_MOMENT_SOURCE)
        .read_text(encoding="utf-8")
        .replace("\r\n", "\n")
    )
    finite_histogram_source = twelve_producer.get("finite_histogram_source", {})
    if (
        twelve_producer.get("source") != TWELVE_MOMENT_SOURCE
        or twelve_producer.get("source_sha256_lf_normalized")
        != hashlib.sha256(twelve_text.encode("utf-8")).hexdigest()
        or finite_histogram_source.get("path") != Q_SCAN_FIXTURE
        or finite_histogram_source.get("canonical_sha256") != sha256_hex(q_scan)
        or finite_histogram_source.get("payload_sha256")
        != q_scan.get("payload_sha256")
    ):
        raise ValueError("USp(4) twelve-moment producer source lock mismatch")
    if (
        twelve_moment.get("status") != TWELVE_MOMENT_STATUS
        or twelve_moment.get("event") != "F>=0"
        or twelve_moment.get("statistic") != "F=(Tr U)^2-e_2(U)^2"
    ):
        raise ValueError("USp(4) twelve-moment status or statistic drifted")
    twelve_scope = twelve_moment.get("scope", {})
    if (
        twelve_scope.get("not_an_optimality_claim") is not True
        or twelve_scope.get("not_an_equidistribution_theorem") is not True
        or twelve_scope.get("not_a_number_field_transfer") is not True
        or "exact rational algebra" not in twelve_scope.get("discovery_firewall", "")
    ):
        raise ValueError("USp(4) twelve-moment theorem firewall drifted")
    twelve_weyl = twelve_moment.get("weyl_constant_term", {})
    if (
        twelve_weyl.get("root_system") != "C2"
        or twelve_weyl.get("density_constant_term") != 8
        or twelve_weyl.get("positive_roots_as_exponent_pairs")
        != [list(root) for root in POSITIVE_ROOTS]
        or twelve_weyl.get("raw_moments_orders_1_through_12")
        != list(HAAR_MOMENTS_12)
    ):
        raise ValueError("USp(4) twelve-moment Weyl certificate drifted")
    t_moments = twelve_weyl.get("t_moments_orders_0_through_12", [])
    if len(t_moments) != 13 or any(
        _fraction(pair, f"t-moment {order}")
        != twelve_module.t_moments(HAAR_MOMENTS_12)[order]
        for order, pair in enumerate(t_moments)
    ):
        raise ValueError("USp(4) transformed twelve-moment sequence drifted")
    twelve_majorant = twelve_moment.get("majorant", {})
    if (
        twelve_majorant.get("degree") != 12
        or twelve_majorant.get("definition") != "P(x)=p((3*x+28)/32)"
        or twelve_majorant.get("pointwise_statement")
        != "P(x)>=0 on [-20,0], and P(x)>=1 on [0,4/3]."
        or len(twelve_majorant.get("polynomial_x_coefficients_low_to_high", []))
        != 13
    ):
        raise ValueError("USp(4) degree-twelve majorant definition drifted")
    bernstein = [
        _fraction(pair, f"degree-twelve Bernstein coefficient {index}")
        for index, pair in enumerate(
            twelve_majorant.get(
                "positive_side_quotient_bernstein_coefficients_degree_9", []
            )
        )
    ]
    if len(bernstein) != 10 or not all(coefficient > 0 for coefficient in bernstein):
        raise ValueError("USp(4) degree-twelve Bernstein positivity proof failed")
    twelve_bound = twelve_moment.get("haar_bound", {})
    expected_upper = twelve_module.EXPECTED_UPPER
    degree_six_upper = twelve_module.SUPPORT_DEGREE_SIX_UPPER
    if (
        _fraction(
            twelve_bound.get("moment_majorant_nonnegative_upper_bound", []),
            "degree-twelve Haar nonnegative upper bound",
        )
        != expected_upper
        or _fraction(
            twelve_bound.get("negative_probability_lower_bound", []),
            "degree-twelve Haar negative lower bound",
        )
        != 1 - expected_upper
        or _fraction(
            twelve_bound.get("support_adapted_degree_six_upper_bound", []),
            "degree-six comparison upper bound",
        )
        != degree_six_upper
        or _fraction(
            twelve_bound.get("strict_improvement", []),
            "degree-twelve strict improvement",
        )
        != degree_six_upper - expected_upper
        or not expected_upper < degree_six_upper
    ):
        raise ValueError("USp(4) degree-twelve Haar sign bound drifted")
    twelve_rows = twelve_moment.get("finite_q_bounds", [])
    if [row.get("q") for row in twelve_rows] != list(Q_VALUES):
        raise ValueError("USp(4) twelve-moment finite rows drifted")
    q_families_by_q = {int(family["q"]): family for family in q_scan["families"]}
    polynomial_x = twelve_module.majorant_certificate()["polynomial_x"]
    for row in twelve_rows:
        q = int(row["q"])
        raw = twelve_module.finite_raw_moments(q_families_by_q[q])
        expected_finite_upper = twelve_module.polynomial_moment(polynomial_x, raw)
        observed_negative = Fraction(
            int(q_families_by_q[q]["sign_counts"]["negative"]),
            int(q_families_by_q[q]["member_count"]),
        )
        if (
            _fraction(
                row.get("moment_majorant_nonnegative_upper_bound", []),
                f"q={q} twelve-moment upper bound",
            )
            != expected_finite_upper
            or _fraction(
                row.get("negative_probability_lower_bound", []),
                f"q={q} twelve-moment lower bound",
            )
            != 1 - expected_finite_upper
            or _fraction(
                row.get("observed_negative_fraction", []),
                f"q={q} twelve-moment observed sign",
            )
            != observed_negative
            or row.get("verified_bound_holds") is not True
            or 1 - expected_finite_upper > observed_negative
        ):
            raise ValueError(f"q={q} twelve-moment finite sign bound drifted")
    twelve_resource = twelve_moment.get("resource_contract", {})
    if (
        twelve_resource.get("maximum_moment") != 12
        or twelve_resource.get("actual_laurent_pair_products") != 238743
        or twelve_resource.get("maximum_laurent_pair_products") != 300000
        or twelve_resource.get("actual_laurent_pair_products")
        > twelve_resource.get("maximum_laurent_pair_products")
        or twelve_resource.get("random_sampling") is not False
        or twelve_resource.get("numerical_integration") is not False
        or twelve_resource.get("field_enumeration") is not False
        or twelve_resource.get("external_dependencies") is not False
    ):
        raise ValueError("USp(4) twelve-moment resource contract drifted")
    return comparator, q_scan, character_decomposition, twelve_moment


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
        "Compare F(U) only with K_D/q^2; freeze Haar and sign-majorant moments 1 through 12, explicit finite comparison rows 1 through 6, and q values 3,5,7.",
        "Keep exact Laurent and finite-histogram arithmetic separate from the proposed q-to-infinity convergence statement.",
        "Treat F as a toy reciprocal-coefficient statistic, not Pick/Loewner, XD, or HCNC.",
        "Use only exactly certified nonnegative-event majorants on [-20,4/3], and keep every finite-family liminf consequence conditional on the required moment convergence.",
        "For F^m through m=6, use exact C2 Kostant characters and retain the full irreducible decomposition fixture as a content-bound input.",
        "For the degree-twelve sign majorant, replay exact factorization and Bernstein positivity, bind the full fixture, and make no optimality claim.",
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
            "Exact character identity, irreducible decompositions through power six, Weyl "
            "constant terms through moment twelve, and q=3,5,7 histogram calculations only. "
            "Convergence is proposed, with no optimality, analytic-kernel, or number-field claim."
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
                "domain": "orders 1 through 12",
                "constraints": {"minimum": 1, "maximum": 12, "frozen_value": 12},
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
            {
                "field": "result.character_decomposition_certificate",
                "requirement": normalization[6],
                "comparison_role": "IDENTITY",
            },
            {
                "field": "result.twelve_moment_sign_certificate",
                "requirement": normalization[7],
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
                "code": "C2_IRREDUCIBLE_POWER_DECOMPOSITION",
                "statement": (
                    "For m=1,...,6, F^m has an exact irreducible C2-character "
                    "decomposition with sign-adjusted nonnegative tensor multiplicities, "
                    "dimension sum 20^m, and trivial coefficient equal to the Haar moment."
                ),
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
                    "Exact degree-six majorants give 1_{F>=0}<=p(F) and therefore the "
                    "support-adapted bound Pr_Haar(F<0)>=2478693937/6358302720."
                ),
                "status": "PROVED",
            },
            {
                "code": "DEGREE_TWELVE_SIGN_MAJORANT",
                "statement": (
                    "An exact degree-twelve majorant gives 1_{F>=0}<=P(F) and "
                    "Pr_Haar(F<0)>=153081644970674178368978470022738347661743507912075314789490808683/"
                    "318454738700269877013669525120657835305950388794994707229994647552, "
                    "strictly improving the stored degree-six moment bound."
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
                "family": "USP4_C2_CHARACTER_RING",
                "status": "REQUIRED_AVAILABLE",
                "adapter_path": CHARACTER_DECOMPOSITION_SOURCE,
                "correction": (
                    "Use exact integer Kostant multiplicities, dominance subtraction, and "
                    "the independently checked Weyl dimension formula."
                ),
            },
            {
                "family": "USP4_DEGREE_TWELVE_SIGN_MAJORANT",
                "status": "REQUIRED_AVAILABLE",
                "adapter_path": TWELVE_MOMENT_SOURCE,
                "correction": (
                    "Replay twelve exact C2 moments, rational factorization, and Bernstein "
                    "positivity under the explicit small operation cap."
                ),
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
                    "liminf Pr(K_D/q^2<0)>=2478693937/6358302720."
                ),
            },
            {
                "semantic_id": (
                    "CONDITIONAL.FUNCTION_FIELD.GENUS2.NEGATIVE_SIGN."
                    "TWELVE_MOMENT_LIMINF"
                ),
                "status": "CONDITIONAL_EXACT",
                "scope": (
                    "Convergence of the first twelve raw moments implies liminf "
                    "Pr(K_D/q^2<0)>=153081644970674178368978470022738347661743507912075314789490808683/"
                    "318454738700269877013669525120657835305950388794994707229994647552."
                ),
            },
        ],
        "failure_modes": [
            {
                "code": "WEYL_NORMALIZATION_LOSS",
                "description": "The C2 constant term is used without division by the Weyl order 8.",
                "hostile_control": "The replay requires density constant term 8 and the frozen exact twelve moments.",
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
                    "The raw certificates label polynomial values as lower bounds, make no "
                    "optimality claim, and keep q-to-infinity consequences conditional."
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
                "target": (
                    "C2 Weyl constant term, USp(4) Laurent-character identity, and the "
                    "power-one-through-six irreducible decompositions and degree-twelve "
                    "sign majorant."
                ),
                "path": None,
            }
        ],
        "notes": (
            "Certified claims are the exact identity, irreducible decompositions through power "
            "six, constant terms, twelve Haar moments, finite histogram bounds, and exact "
            "degree-six and degree-twelve sign lower bounds. The limiting moment comparison "
            "remains proposed, and no majorant optimality is claimed."
        ),
    }


def _fraction_record(pair: Sequence[int]) -> dict[str, int | str]:
    value = _fraction(pair, "raw-result fraction")
    return fraction_json(value.numerator, value.denominator)


def _witness_record(witness: Mapping[str, Sequence[int]]) -> dict[str, Any]:
    return {"X": _fraction_record(witness["X"]), "Y": _fraction_record(witness["Y"])}


def _sign_moment_certificate_record(source: Mapping[str, Any]) -> dict[str, Any]:
    majorant = source["majorant"]
    support_majorant = source["support_adapted_majorant"]
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
        "support_adapted_majorant": {
            "coordinate": support_majorant["coordinate"],
            "polynomial_factorization": support_majorant["polynomial_factorization"],
            "coefficients_in_x_low_to_high": [
                _fraction_record(pair)
                for pair in support_majorant["coefficients_in_x_low_to_high"]
            ],
            "pointwise_statement": support_majorant["pointwise_statement"],
            "nonnegative_support_proof": support_majorant[
                "nonnegative_support_proof"
            ],
            "positive_interval_factorization": support_majorant[
                "positive_interval_factorization"
            ],
            "positive_interval_bernstein_coordinate": support_majorant[
                "positive_interval_bernstein_coordinate"
            ],
            "positive_interval_quotient_bernstein_coefficients_degree_4": [
                _fraction_record(pair)
                for pair in support_majorant[
                    "positive_interval_quotient_bernstein_coefficients_degree_4"
                ]
            ],
            "positive_interval_proof": support_majorant["positive_interval_proof"],
            "haar": {
                "moment_majorant_nonnegative_upper_bound": _fraction_record(
                    support_majorant["haar"][
                        "moment_majorant_nonnegative_upper_bound"
                    ]
                ),
                "negative_probability_lower_bound": _fraction_record(
                    support_majorant["haar"]["negative_probability_lower_bound"]
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
                for row in support_majorant["finite_q_bounds"]
            ],
            "strictly_improves_cubic_square_bound": support_majorant[
                "strictly_improves_cubic_square_bound"
            ],
            "construction_scope": support_majorant["construction_scope"],
        },
        "conditional_consequence": dict(source["conditional_consequence"]),
        "scope": source["scope"],
    }


def _character_decomposition_certificate_record(
    source: Mapping[str, Any],
) -> dict[str, Any]:
    """Keep proof-critical character data compact; bind the full fixture separately."""

    return {
        "status": source["status"],
        "highest_weight_convention": source["group"]["highest_weight_convention"],
        "defining_identity": source["character_identity"]["defining_formula"],
        "irreducible_identity": source["character_identity"]["F"],
        "maximum_power": source["resource_contract"]["maximum_power"],
        "powers": [
            {
                "power": int(row["power"]),
                "irreducible_count": int(row["irreducible_count"]),
                "tensor_dimension": int(row["tensor_dimension"]),
                "trivial_coefficient_in_F_power": int(
                    row["trivial_coefficient_in_F_power"]
                ),
                "independent_weyl_constant_term_haar_moment": int(
                    row["independent_weyl_constant_term_haar_moment"]
                ),
                "all_sign_adjusted_tensor_multiplicities_positive": all(
                    entry["tensor_multiplicity_in_G_power"] > 0
                    and entry["coefficient_in_F_power"]
                    == row["global_sign_from_F_equals_minus_G"]
                    * entry["tensor_multiplicity_in_G_power"]
                    for entry in row["decomposition"]
                ),
                "dimension_reconstruction_exact": (
                    row["dimension_sum_from_decomposition"]
                    == row["tensor_dimension"]
                ),
                "laurent_reconstruction_exact": row["reconstruction_exact"],
            }
            for row in source["powers"]
        ],
        "all_power_corollary": dict(source["all_power_corollary"]),
        "verification": {
            key: source["verification"][key]
            for key in (
                "all_kostant_character_dimensions_match_weyl_formula",
                "all_generated_characters_are_weyl_invariant",
                "all_power_reconstructions_exact",
                "all_tensor_multiplicities_positive",
                "all_F_power_coefficients_have_uniform_sign_minus_one_to_m",
                "all_dimension_sums_equal_20_to_m",
                "all_trivial_multiplicities_match_independent_haar_constant_terms",
            )
        },
        "scope": source["scope_firewall"]["this_proves"],
        "does_not_prove": list(source["scope_firewall"]["this_does_not_prove"]),
    }


def _twelve_moment_certificate_record(source: Mapping[str, Any]) -> dict[str, Any]:
    majorant = source["majorant"]
    haar_bound = source["haar_bound"]
    resource = source["resource_contract"]
    return {
        "status": source["status"],
        "event": source["event"],
        "maximum_moment": resource["maximum_moment"],
        "haar_moments_orders_1_through_12": source["weyl_constant_term"][
            "raw_moments_orders_1_through_12"
        ],
        "majorant": {
            "degree": majorant["degree"],
            "definition": majorant["definition"],
            "pointwise_statement": majorant["pointwise_statement"],
            "nonnegative_side_proof": majorant["nonnegative_side_proof"],
            "positive_side_factorization": majorant["positive_side_factorization"],
            "positive_side_bernstein_coordinate": majorant[
                "positive_side_bernstein_coordinate"
            ],
            "positive_side_bernstein_coefficient_count": len(
                majorant[
                    "positive_side_quotient_bernstein_coefficients_degree_9"
                ]
            ),
            "all_positive_side_bernstein_coefficients_strictly_positive": all(
                _fraction(pair, "compact degree-twelve Bernstein coefficient") > 0
                for pair in majorant[
                    "positive_side_quotient_bernstein_coefficients_degree_9"
                ]
            ),
            "exact_factorization_and_positivity_replayed": True,
        },
        "haar_bound": {
            "moment_majorant_nonnegative_upper_bound": _fraction_record(
                haar_bound["moment_majorant_nonnegative_upper_bound"]
            ),
            "negative_probability_lower_bound": _fraction_record(
                haar_bound["negative_probability_lower_bound"]
            ),
            "support_adapted_degree_six_upper_bound": _fraction_record(
                haar_bound["support_adapted_degree_six_upper_bound"]
            ),
            "strict_improvement": _fraction_record(
                haar_bound["strict_improvement"]
            ),
            "strictly_improves_support_adapted_degree_six_bound": True,
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
        "resource_contract": {
            "maximum_laurent_pair_products": resource[
                "maximum_laurent_pair_products"
            ],
            "actual_laurent_pair_products": resource[
                "actual_laurent_pair_products"
            ],
            "maximum_wall_seconds": resource["maximum_wall_seconds"],
            "random_sampling": resource["random_sampling"],
            "numerical_integration": resource["numerical_integration"],
            "field_enumeration": resource["field_enumeration"],
            "external_dependencies": resource["external_dependencies"],
        },
        "scope": dict(source["scope"]),
    }


def build_raw_result(
    root: Path,
    specs: Sequence[dict[str, Any]],
    detector: dict[str, Any],
    comparator: dict[str, Any],
    q_scan: dict[str, Any],
    character_decomposition: dict[str, Any],
    twelve_moment: dict[str, Any],
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
            "character_decomposition_source": {
                "path": CHARACTER_DECOMPOSITION_SOURCE,
                "raw_sha256": raw_sha256(repo_root / CHARACTER_DECOMPOSITION_SOURCE),
            },
            "character_decomposition_fixture": {
                "path": CHARACTER_DECOMPOSITION_FIXTURE,
                "canonical_sha256": sha256_hex(character_decomposition),
                "producer_source_sha256_lf_normalized": character_decomposition[
                    "producer"
                ]["source_sha256_lf_normalized"],
            },
            "twelve_moment_source": {
                "path": TWELVE_MOMENT_SOURCE,
                "raw_sha256": raw_sha256(repo_root / TWELVE_MOMENT_SOURCE),
            },
            "twelve_moment_fixture": {
                "path": TWELVE_MOMENT_FIXTURE,
                "canonical_sha256": sha256_hex(twelve_moment),
                "payload_sha256": twelve_moment["payload_sha256"],
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
        "character_decomposition_certificate": (
            _character_decomposition_certificate_record(character_decomposition)
        ),
        "twelve_moment_sign_certificate": _twelve_moment_certificate_record(
            twelve_moment
        ),
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
            "The all-power alternating Haar-moment sign theorem is a compact-group character statement and does not imply finite-family moment convergence.",
            "The directional finite-moment pattern is exact only for q=3,5,7 and does not assert monotonicity or a rate at another field.",
            "The degree-six polynomial gives a lower bound for the negative-sign probability, not its exact Haar value; its liminf consequence is conditional on six-moment convergence.",
            "The degree-twelve polynomial gives a strictly stronger exact lower bound, not the exact probability or an optimality claim; numerical discovery is excluded from acceptance, and any finite-family liminf requires twelve-moment convergence.",
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
    character_decomposition: dict[str, Any],
    twelve_moment: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    repo_root = root.parents[2]
    comparator_adapter = artifact_binding(
        root, COMPARATOR_SOURCE, "exact_usp4_laurent_adapter", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    character_adapter = artifact_binding(
        root,
        CHARACTER_DECOMPOSITION_SOURCE,
        "exact_usp4_character_ring_adapter",
        "FINITE_COMPLETE",
        None,
        "RAW_BYTES",
    )
    twelve_moment_adapter = artifact_binding(
        root,
        TWELVE_MOMENT_SOURCE,
        "exact_usp4_twelve_moment_sign_adapter",
        "FINITE_COMPLETE",
        None,
        "RAW_BYTES",
    )
    qscan_adapter = artifact_binding(
        root, Q_SCAN_SOURCE, "exact_genus2_histogram_adapter", "FINITE_COMPLETE", None, "RAW_BYTES"
    )
    comparator_input = artifact_binding(
        root, COMPARATOR_FIXTURE, "exact_usp4_moment_certificate", "FINITE_COMPLETE", None
    )
    character_input = artifact_binding(
        root,
        CHARACTER_DECOMPOSITION_FIXTURE,
        "exact_usp4_character_decomposition_certificate",
        "FINITE_COMPLETE",
        None,
    )
    twelve_moment_input = artifact_binding(
        root,
        TWELVE_MOMENT_FIXTURE,
        "exact_usp4_twelve_moment_sign_certificate",
        "FINITE_COMPLETE",
        None,
    )
    qscan_input = artifact_binding(
        root, Q_SCAN_FIXTURE, "complete_q3_q5_q7_histograms", "FINITE_COMPLETE", None
    )
    spec_bindings = [content_binding(spec) for spec in sorted(specs, key=lambda row: row["semantic_id"])]
    detector_binding = content_binding(detector)
    values = {
        "q_values": list(Q_VALUES),
        "maximum_moment": 12,
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
            "sources": [
                COMPARATOR_SOURCE,
                COMPARATOR_FIXTURE,
                CHARACTER_DECOMPOSITION_SOURCE,
                CHARACTER_DECOMPOSITION_FIXTURE,
                TWELVE_MOMENT_SOURCE,
                TWELVE_MOMENT_FIXTURE,
            ],
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
    adapters = [
        comparator_adapter,
        character_adapter,
        twelve_moment_adapter,
        qscan_adapter,
    ]
    inputs = [comparator_input, character_input, twelve_moment_input, qscan_input]
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
    raw_result = build_raw_result(
        root,
        specs,
        detector,
        comparator,
        q_scan,
        character_decomposition,
        twelve_moment,
    )
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
            "Compact exact certificate; the four source implementations and four full "
            "fixtures are separately content-bound."
        ),
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
            "Exact irreducible character decompositions through power six, Haar moments and "
            "sign-majorant arithmetic through moment twelve, plus the complete q=3,5,7 "
            "quintic families only; no optimality, convergence, or transfer claim."
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
                "All irreducible C2-character decompositions through power 6, all Haar moments "
                "and sign-majorant arithmetic through moment 12, and all 162, 2500, and 14406 "
                "finite-family members at q=3,5,7 respectively."
            ),
            "omissions": [
                "explicit irreducible decompositions above power 6 and moments above order 12",
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
                "The exact decompositions of F^m have 3, 9, 16, 25, 36, and 49 irreducible "
                "terms for m=1,...,6; their signed trivial multiplicities give Haar moments "
                "-1, 3, -11, 56, -374, 3117. F has exact USp(4) range [-20,4/3], and a "
                "degree-twelve moment majorant proves Pr_Haar(F<0)>="
                "153081644970674178368978470022738347661743507912075314789490808683/"
                "318454738700269877013669525120657835305950388794994707229994647552, "
                "strictly improving the degree-six bound. All six frozen moment gaps shrink directionally "
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
                "The character identity, six irreducible power decompositions, range certificate, "
                "Weyl normalization and twelve Haar moments, three finite histogram moment "
                "sequences through order six, and six frozen directional gap checks are exact. "
                "The character packet also "
                "proves the alternating strict sign and integrality of every compact-group Haar "
                "moment. The six- and twelve-moment negative-sign lower bounds are exact; their "
                "finite-family liminf consequences and the proposed q-to-infinity moment relation "
                "remain conditional and unproved, respectively. The degree-twelve majorant is "
                "not claimed optimal."
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
                "code": "CHARACTER_RING_NOT_FINITE_FAMILY",
                "statement": (
                    "The all-power alternating sign theorem concerns compact-group Haar "
                    "moments only and does not establish finite-family convergence."
                ),
            },
            {
                "code": "SIGN_BOUND_NOT_SIGN_PROBABILITY",
                "statement": (
                    "The degree-six and degree-twelve values are Haar lower bounds, not the "
                    "exact negative-sign probability or claimed optimal moment bounds; each "
                    "finite-family liminf remains conditional."
                ),
            },
            {
                "code": "DEGREE_TWELVE_DISCOVERY_FIREWALL",
                "statement": (
                    "Numerical optimization only nominated the rational factor pattern; atlas "
                    "acceptance replays exact rational factorization and Bernstein positivity."
                ),
            },
            {
                "code": "TOY_NOT_ANALYTIC_KERNEL",
                "statement": "F and K_D are toy coefficient statistics, not Pick/Loewner, XD, or HCNC.",
            },
            {
                "code": "FINITE_Q_SCOPE",
                "statement": (
                    "The finite evidence contains exactly q=3,5,7, explicit comparison rows "
                    "through order 6, and sign-majorant arithmetic through order 12."
                ),
            },
            {
                "code": "NO_NUMBER_FIELD_TRANSFER",
                "statement": "No result transfers from these function fields to number-field L-functions.",
            },
        ],
        "notes": (
            "RIGOROUS_CERTIFIED applies to exact Laurent, C2 character-ring, twelve-moment Weyl, "
            "finite histogram, and polynomial-majorant arithmetic. The raw result separately marks "
            "moment convergence CONJECTURAL and PROPOSED, and the negative-sign liminf as "
            "conditional."
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
    dict[str, Any],
    dict[str, Any],
]:
    root = root.resolve()
    config = read_json(root / "config" / "pilot.json")
    comparator, q_scan, character_decomposition, twelve_moment = (
        load_and_replay_fixtures(root)
    )
    specs = load_family_specs(root)
    detector = build_detector(root)
    evaluation, raw_result = make_evaluation(
        root,
        config,
        specs,
        detector,
        comparator,
        q_scan,
        character_decomposition,
        twelve_moment,
    )
    return (
        specs,
        detector,
        evaluation,
        raw_result,
        comparator,
        q_scan,
        character_decomposition,
        twelve_moment,
    )


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
    specs, detector, evaluation, raw_result, _, _, _, _ = run(root)
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
