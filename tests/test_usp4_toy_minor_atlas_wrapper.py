"""Focused atlas tests for the exact USp(4) toy-minor moment comparator."""

from __future__ import annotations

import copy
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS_ROOT = ROOT / "research" / "l-families" / "atlas"
CORE = ATLAS_ROOT / "core"
sys.path.insert(0, str(CORE))

from atlas_core import read_json, sha256_hex  # noqa: E402
from run_pilot import raw_sha256  # noqa: E402
from validate_atlas import SchemaStore, validate_instance  # noqa: E402
import wrap_usp4_toy_minor_moments as wrapper  # noqa: E402


class USp4ToyMinorAtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        (
            cls.specs,
            cls.detector,
            cls.evaluation,
            cls.result,
            cls.comparator,
            cls.q_scan,
        ) = wrapper.run(ATLAS_ROOT)
        cls.specs_by_q = {
            int(spec["base_field"]["constant_field_order"]): spec for spec in cls.specs
        }

    def test_reuses_exactly_the_three_existing_genus_two_specs(self) -> None:
        self.assertEqual(set(self.specs_by_q), {3, 5, 7})
        self.assertEqual(len(self.specs), 3)
        for q, slug in wrapper.SPEC_SLUGS.items():
            spec = self.specs_by_q[q]
            self.assertEqual(spec["identity_kernel"]["slug"], slug)
            stored = ATLAS_ROOT / "specs" / f"{spec['semantic_id']}.json"
            self.assertEqual(read_json(stored), spec)

    def test_records_are_draft_content_addressed_and_programme_bound(self) -> None:
        for record in (self.detector, self.evaluation):
            self.assertEqual(record["record_state"], "DRAFT")
            self.assertEqual(record["identity_sha256"], sha256_hex(record["identity_kernel"]))
            self.assertTrue(record["semantic_id"].endswith(record["identity_sha256"][:32]))
            self.assertEqual([ref["number"] for ref in record["programme_refs"]], [737, 741])

    def test_binds_and_replays_both_sources_and_both_fixtures(self) -> None:
        adapter_paths = {binding["path"] for binding in self.evaluation["adapter_bindings"]}
        input_paths = {binding["path"] for binding in self.evaluation["input_bindings"]}
        self.assertEqual(adapter_paths, {wrapper.COMPARATOR_SOURCE, wrapper.Q_SCAN_SOURCE})
        self.assertEqual(input_paths, {wrapper.COMPARATOR_FIXTURE, wrapper.Q_SCAN_FIXTURE})

        locks = self.result["source_locks"]
        self.assertEqual(
            locks["comparator_source"]["raw_sha256"],
            raw_sha256(ROOT / wrapper.COMPARATOR_SOURCE),
        )
        self.assertEqual(
            locks["q_scan_source"]["raw_sha256"],
            raw_sha256(ROOT / wrapper.Q_SCAN_SOURCE),
        )
        self.assertEqual(
            locks["comparator_fixture"]["canonical_sha256"],
            sha256_hex(self.comparator),
        )
        self.assertEqual(
            locks["q_scan_fixture"]["canonical_sha256"], sha256_hex(self.q_scan)
        )
        self.assertEqual(
            self.comparator["finite_source"]["canonical_sha256"], sha256_hex(self.q_scan)
        )

    def test_exact_character_range_and_weyl_certificates(self) -> None:
        character = self.result["character_identity"]
        self.assertEqual(character["formula"], "F=-(1+chi_{omega_2}+chi_{2*omega_2})")
        self.assertEqual(
            character["dimensions_at_identity"],
            {"standard": 4, "omega_2": 5, "2*omega_2": 14, "F": -20},
        )
        exact_range = self.result["range_certificate"]
        self.assertEqual(
            Fraction(exact_range["minimum"]["numerator"], exact_range["minimum"]["denominator"]),
            -20,
        )
        self.assertEqual(
            Fraction(exact_range["maximum"]["numerator"], exact_range["maximum"]["denominator"]),
            Fraction(4, 3),
        )
        self.assertEqual(len(exact_range["minimum_witnesses"]), 2)
        self.assertEqual(len(exact_range["maximum_witnesses"]), 4)
        weyl = self.result["weyl_certificate"]
        self.assertEqual(weyl["density_constant_term"], 8)
        self.assertEqual(weyl["positive_roots_as_exponent_pairs"], [list(x) for x in wrapper.POSITIVE_ROOTS])
        self.assertEqual(weyl["haar_moments_orders_1_through_6"], list(wrapper.HAAR_MOMENTS))
        self.assertEqual(
            weyl["haar_centered_moments_orders_1_through_6"],
            list(wrapper.HAAR_CENTERED_MOMENTS),
        )
        self.assertEqual(
            weyl["haar_cumulants_orders_1_through_6"],
            list(wrapper.HAAR_CUMULANTS),
        )

    def test_all_finite_moments_remain_exactly_histogram_normalized(self) -> None:
        source_by_q = {int(item["q"]): item for item in self.comparator["finite_comparisons"]}
        for comparison in self.result["finite_comparisons"]:
            q = int(comparison["q"])
            self.assertEqual(
                comparison["spec_semantic_id"], self.specs_by_q[q]["semantic_id"]
            )
            source_moments = source_by_q[q]["moments"]
            self.assertEqual([row["order"] for row in comparison["moments"]], list(range(1, 7)))
            for actual, source in zip(comparison["moments"], source_moments, strict=True):
                finite = actual["finite_exact"]
                gap = actual["finite_minus_haar"]
                self.assertEqual(
                    Fraction(finite["numerator"], finite["denominator"]),
                    Fraction(*source["finite_exact"]),
                )
                self.assertEqual(
                    Fraction(gap["numerator"], gap["denominator"]),
                    Fraction(*source["finite_minus_haar"]),
                )
                self.assertEqual(actual["usp4_haar_exact"], source["usp4_haar_exact"])

    def test_frozen_directional_pattern_is_bound_and_not_extrapolated(self) -> None:
        pattern = self.result["frozen_moment_pattern"]
        self.assertEqual(pattern, self.comparator["frozen_moment_pattern"])
        self.assertEqual(pattern["status"], wrapper.FROZEN_PATTERN_STATUS)
        self.assertTrue(pattern["not_a_theorem_beyond_frozen_fields"])
        self.assertEqual([row["order"] for row in pattern["per_order"]], list(range(1, 7)))
        self.assertTrue(
            all(
                all(value is True for key, value in row.items() if key != "order")
                for row in pattern["per_order"]
            )
        )

    def test_degree_six_negative_sign_bound_is_exact_and_conditional(self) -> None:
        certificate = self.result["negative_sign_moment_certificate"]
        self.assertEqual(certificate["status"], wrapper.SIGN_MAJORANT_STATUS)
        haar = certificate["haar"]
        self.assertEqual(
            Fraction(
                haar["moment_majorant_nonnegative_upper_bound"]["numerator"],
                haar["moment_majorant_nonnegative_upper_bound"]["denominator"],
            ),
            Fraction(7663, 12023),
        )
        self.assertEqual(
            Fraction(
                haar["negative_probability_lower_bound"]["numerator"],
                haar["negative_probability_lower_bound"]["denominator"],
            ),
            Fraction(4360, 12023),
        )
        self.assertEqual(
            [row["q"] for row in certificate["finite_q_bounds"]], [3, 5, 7]
        )
        for row in certificate["finite_q_bounds"]:
            lower = row["negative_probability_lower_bound"]
            observed = row["observed_negative_fraction"]
            self.assertLessEqual(
                Fraction(lower["numerator"], lower["denominator"]),
                Fraction(observed["numerator"], observed["denominator"]),
            )
            self.assertTrue(row["verified_bound_holds"])
        stronger = certificate["support_adapted_majorant"]
        strong_haar = stronger["haar"]["negative_probability_lower_bound"]
        self.assertEqual(
            Fraction(strong_haar["numerator"], strong_haar["denominator"]),
            Fraction(2478693937, 6358302720),
        )
        self.assertTrue(stronger["strictly_improves_cubic_square_bound"])
        self.assertTrue(
            all(
                row["numerator"] > 0
                for row in stronger[
                    "positive_interval_quotient_bernstein_coefficients_degree_4"
                ]
            )
        )
        for stronger_row, baseline_row in zip(
            stronger["finite_q_bounds"], certificate["finite_q_bounds"], strict=True
        ):
            strong_lower = stronger_row["negative_probability_lower_bound"]
            baseline_lower = baseline_row["negative_probability_lower_bound"]
            self.assertGreater(
                Fraction(strong_lower["numerator"], strong_lower["denominator"]),
                Fraction(baseline_lower["numerator"], baseline_lower["denominator"]),
            )
        conditional = certificate["conditional_consequence"]
        self.assertEqual(
            conditional["status"], "CONDITIONAL_ON_FIRST_SIX_MOMENT_CONVERGENCE"
        )
        self.assertTrue(conditional["not_an_equidistribution_proof"])
        self.assertIn("2478693937/6358302720", conditional["statement"])
        self.assertIn("lower bound", certificate["scope"])

    def test_exact_arithmetic_is_firewalled_from_convergence(self) -> None:
        self.assertEqual(self.evaluation["rigor_level"], "RIGOROUS_CERTIFIED")
        target = self.result["convergence_target"]
        self.assertEqual(target["status"], wrapper.CONVERGENCE_STATUS)
        self.assertEqual(target["atlas_status"], "PROPOSED")
        self.assertTrue(target["not_a_theorem"])
        self.assertIsNone(self.evaluation["interpretation"]["theorem_claim_id"])
        text = " ".join(
            [
                *self.result["firewalls"],
                *(entry["statement"] for entry in self.evaluation["firewalls"]),
                self.detector["scope_boundary"],
            ]
        ).lower()
        for phrase in (
            "not a theorem",
            "another field",
            "pick/loewner",
            "xd",
            "hcnc",
            "number-field",
        ):
            self.assertIn(phrase, text)

    def test_strict_raw_result_schema_holds(self) -> None:
        schema_path = ROOT / wrapper.RAW_RESULT_SCHEMA
        errors = validate_instance(
            self.result,
            read_json(schema_path),
            schema_path,
            SchemaStore(),
        )
        self.assertEqual(errors, [])

    def test_strict_schema_rejects_q_and_moment_order_drift(self) -> None:
        schema_path = ROOT / wrapper.RAW_RESULT_SCHEMA
        schema = read_json(schema_path)
        hostile_cases = []

        duplicate_q = copy.deepcopy(self.result)
        duplicate_q["finite_comparisons"][1]["q"] = 3
        duplicate_q["finite_comparisons"][1]["member_count"] = 162
        hostile_cases.append(duplicate_q)

        reversed_q = copy.deepcopy(self.result)
        reversed_q["finite_comparisons"].reverse()
        hostile_cases.append(reversed_q)

        duplicate_order = copy.deepcopy(self.result)
        duplicate_order["finite_comparisons"][0]["moments"][1]["order"] = 1
        duplicate_order["finite_comparisons"][0]["moments"][1]["usp4_haar_exact"] = -1
        hostile_cases.append(duplicate_order)

        out_of_range_order = copy.deepcopy(self.result)
        out_of_range_order["finite_comparisons"][0]["moments"][0]["order"] = 7
        hostile_cases.append(out_of_range_order)

        altered_majorant = copy.deepcopy(self.result)
        altered_majorant["negative_sign_moment_certificate"]["majorant"][
            "coefficients_low_to_high"
        ][1]["numerator"] += 1
        hostile_cases.append(altered_majorant)

        altered_haar_bound = copy.deepcopy(self.result)
        altered_haar_bound["negative_sign_moment_certificate"]["haar"][
            "negative_probability_lower_bound"
        ]["numerator"] += 1
        hostile_cases.append(altered_haar_bound)

        reversed_sign_rows = copy.deepcopy(self.result)
        reversed_sign_rows["negative_sign_moment_certificate"]["finite_q_bounds"].reverse()
        hostile_cases.append(reversed_sign_rows)

        altered_support_coefficient = copy.deepcopy(self.result)
        altered_support_coefficient["negative_sign_moment_certificate"][
            "support_adapted_majorant"
        ]["coefficients_in_x_low_to_high"][1]["numerator"] += 1
        hostile_cases.append(altered_support_coefficient)

        altered_bernstein = copy.deepcopy(self.result)
        altered_bernstein["negative_sign_moment_certificate"][
            "support_adapted_majorant"
        ]["positive_interval_quotient_bernstein_coefficients_degree_4"][0][
            "numerator"
        ] += 1
        hostile_cases.append(altered_bernstein)

        reversed_support_rows = copy.deepcopy(self.result)
        reversed_support_rows["negative_sign_moment_certificate"][
            "support_adapted_majorant"
        ]["finite_q_bounds"].reverse()
        hostile_cases.append(reversed_support_rows)

        for hostile in hostile_cases:
            with self.subTest(hostile=hostile):
                self.assertTrue(
                    validate_instance(hostile, schema, schema_path, SchemaStore())
                )

    def test_written_artifacts_equal_dynamic_builder_output(self) -> None:
        detector_path = ATLAS_ROOT / "detectors" / f"{self.detector['semantic_id']}.json"
        evaluation_path = ATLAS_ROOT / "evaluations" / f"{self.evaluation['semantic_id']}.json"
        result_path = ROOT / self.evaluation["result"]["artifact"]["path"]
        self.assertEqual(read_json(detector_path), self.detector)
        self.assertEqual(read_json(evaluation_path), self.evaluation)
        self.assertEqual(read_json(result_path), self.result)


if __name__ == "__main__":
    unittest.main()
