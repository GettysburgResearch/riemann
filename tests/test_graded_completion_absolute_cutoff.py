"""Same-family Frobenius norms, literal cutoffs and actual source ambiguity."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/graded-completion-lab/absolute_cutoff_replay.py"
)
SPEC = importlib.util.spec_from_file_location("absolute_frobenius_cutoff", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class CutoffArithmetic(unittest.TestCase):
    def test_literal_ceilings_compose_before_trace_identities(self):
        for cutoff in range(1, 65):
            for e in range(1, 7):
                for d in range(1, 7):
                    self.assertEqual(
                        R.relative_order(R.relative_order(cutoff, e), d),
                        R.relative_order(cutoff, e * d),
                    )

    def test_absolute_and_relative_thresholds_are_distinct(self):
        self.assertEqual(
            [R.absolute_order(n) for n in range(4, 17, 2)], [4, 6, 8, 10, 12, 14, 16]
        )
        self.assertEqual(
            [R.relative_order(R.absolute_order(n), 2) for n in range(4, 17, 2)],
            [2, 3, 4, 5, 6, 7, 8],
        )
        self.assertEqual(R.relative_order(4, 3), 2)

    def test_nonmonotone_cutoff_remains_the_declared_source_rule(self):
        self.assertEqual(
            [R.absolute_order(n, "nonmonotone") for n in range(4, 17, 2)],
            [4, 3, 8, 5, 12, 7, 16],
        )
        self.assertEqual(R.relative_order(R.absolute_order(6, "nonmonotone"), 2), 2)

    def test_actual_surviving_order_retains_odd_trace_ambiguity(self):
        rows = R.threshold_controls()
        self.assertEqual(len(rows), 96)
        self.assertEqual(R.surviving_order(1, 3), 4)
        self.assertEqual(R.surviving_order(1, 4), 4)
        self.assertEqual(R.surviving_order(2, 3), 3)
        self.assertEqual(R.surviving_order(3, 1), 2)

    def test_all_cutoff_types_and_caps_fail_closed(self):
        for bad in (True, 4.0, 3, 66):
            with self.assertRaises(ValueError):
                R.absolute_order(bad)
        for bad in (True, 0, 385, 1.0):
            with self.assertRaises(ValueError):
                R.relative_order(bad, 2)
        for bad in (True, 0, 37, 2.0):
            with self.assertRaises(ValueError):
                R.relative_order(4, bad)
        with self.assertRaises(ValueError):
            R.absolute_order(4, "nonmonotone", 2)
        with self.assertRaises(ValueError):
            R.absolute_order(4, "unknown")

    def test_phase_zero_is_admissible_but_not_a_natural_boundary_claim(self):
        self.assertEqual(R.phase(0), 0)
        self.assertEqual(R.phase(Fraction(1, 2)), Fraction(1, 2))
        for bad in (True, 0.5, 9, Fraction(1, 65)):
            with self.assertRaises(ValueError):
                R.phase(bad)


class ActualCanonicalBlocks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.provenance, cls.g, cls.original = R.source()

    def test_frozen_source_stays_the_same_actual_f7_family(self):
        self.assertEqual(self.original.point_counts()["P7"], [1, 0, 7])
        self.assertEqual(self.original.point_counts()["P49"], [1, 14, 49])
        self.assertEqual([self.g.multiplicity(n) for n in (4, 6, 8)], [2, 5, 16])
        self.assertIn("genus_producer", self.provenance)

    def test_all_primary_products_match_absolute_trace_inequality(self):
        for e in range(1, 5):
            for policy, slope in (("linear", 1), ("linear", 2), ("nonmonotone", 1)):
                direct = R.canonical_product(self.g, e, policy, slope)
                self.assertEqual(
                    direct,
                    self.g.formal_exp(R.absolute_log(self.g, e, policy, slope), 64),
                )

    def test_original_reference_field_matches_frozen_genus_policy(self):
        for policy, slope in (("linear", 1), ("linear", 2), ("nonmonotone", 1)):
            self.assertEqual(
                R.canonical_product(self.g, 1, policy, slope),
                self.g.canonical_product(1, policy, slope),
            )

    def test_e2_coherent_coefficients_and_fixed_slope_counterfeit(self):
        row = R.normalization_controls(self.g)
        self.assertEqual(row["e2_degree8"], -98)
        self.assertEqual(row["e2_degree12"], Fraction(1372, 3))
        self.assertEqual(
            row["wrong_fixed_relative_slope_first_difference"],
            {"degree": 8, "left": -98, "right": 0},
        )
        self.assertFalse(row["native_normalization_recovered"])

    def test_nonzero_trace_sign_after_cubic_field_extension(self):
        product = R.canonical_product(self.g, 3)
        self.assertEqual(product[8], 686)
        self.assertTrue(all(value == 0 for value in product[1:8]))

    def test_crossing_only_an_odd_zero_trace_changes_no_actual_block(self):
        self.assertEqual(
            R.block_product(self.g, 1, 4, 3), R.block_product(self.g, 1, 4, 4)
        )
        self.assertNotEqual(
            R.block_product(self.g, 2, 4, 3), R.block_product(self.g, 2, 4, 4)
        )
        self.assertNotEqual(
            R.block_product(self.g, 1, 4, 4), R.block_product(self.g, 1, 4, 6)
        )

    def test_effective_absolute_cutoff_classification_is_blockwise(self):
        for e in range(1, 7):
            for p1 in (1, 3, 5):
                even = p1 + 1
                self.assertEqual(
                    R.block_product(self.g, e, 4, R.relative_order(p1, e)),
                    R.block_product(self.g, e, 4, R.relative_order(even, e)),
                )

    def test_zero_phase_is_exactly_one_for_every_policy(self):
        for e in range(1, 5):
            self.assertEqual(R.canonical_product(self.g, e, xi=0), [1] + [0] * 64)
            self.assertEqual(R.absolute_log(self.g, e, xi=0), [0] * 65)

    def test_invalid_field_grade_and_cutoff_rejected_before_arithmetic(self):
        for args in (
            (True, "linear", 1, 16, 64),
            (7, "linear", 1, 16, 64),
            (1, "linear", 1, 18, 64),
            (1, "linear", 1, 16, 65),
        ):
            with self.assertRaises(ValueError):
                R.canonical_product(self.g, *args)


class CoherentNormsAndFrameChanges(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _, cls.g, _ = R.source()

    def test_all_twelve_same_sequence_norm_panels(self):
        for e in (1, 2):
            for d in (2, 3):
                for policy, slope in (("linear", 1), ("linear", 2), ("nonmonotone", 1)):
                    row = R.norm_control(self.g, e, d, policy, slope)
                    self.assertTrue(row["absolute_cutoff_sequence_unchanged"])

    def test_phase_is_raised_on_left_of_norm(self):
        for d in (2, 3):
            for xi in (-1, 0, 2):
                R.norm_control(self.g, 1, d, xi=xi)
        correct = self.g.substituted(
            R.canonical_product(self.g, 3, cut=21, xi=8), 3, 64
        )
        wrong = self.g.substituted(R.canonical_product(self.g, 3, cut=21, xi=2), 3, 64)
        self.assertNotEqual(correct, wrong)

    def test_quadratic_norm_for_odd_frobenius_is_a_square(self):
        left = self.g.substituted(R.canonical_product(self.g, 2, cut=32), 2, 64)
        right = R.canonical_product(self.g, 1)
        self.assertEqual(left, self.g.multiply(right, right, 64))

    def test_phase_sieve_is_on_trace_order_not_total_grade(self):
        correct = R.absolute_log(self.g, 2, "nonmonotone", cut=32, norm_degree=3)
        wrong = [Fraction(0)] * 33
        for n in range(4, 17, 2):
            for h in range(1, 32 // n + 1):
                if 2 * h >= R.absolute_order(n, "nonmonotone") and (n * h) % 3 == 0:
                    wrong[n * h] -= Fraction(
                        3 * self.g.multiplicity(n) * self.g.trace(2 * h), h
                    )
        self.assertNotEqual(correct[12], wrong[12])

    def test_oriented_frame_change_matches_product_ratio_without_dividing_zeros(self):
        first, second = ("linear", 1), ("linear", 2)
        for e in (1, 2):
            forward = R.frame_log(self.g, e, first, second)
            backward = R.frame_log(self.g, e, second, first)
            self.assertEqual(forward, [-x for x in backward])
            self.assertEqual(
                R.canonical_product(self.g, e, *second),
                self.g.multiply(
                    R.canonical_product(self.g, e, *first),
                    self.g.formal_exp(forward, 64),
                    64,
                ),
            )

    def test_frame_change_obeys_additive_same_family_norm(self):
        first, second = ("linear", 1), ("linear", 2)
        for e in (1, 2):
            for d in (2, 3):
                left = self.g.substituted(
                    R.frame_log(self.g, e * d, first, second, cut=64 // d), d, 64
                )
                right = R.frame_log(self.g, e, first, second, norm_degree=d)
                self.assertEqual(left, right)

    def test_coherence_does_not_choose_a_unique_absolute_cutoff(self):
        first = R.canonical_product(self.g, 1, slope=1)
        second = R.canonical_product(self.g, 1, slope=2)
        self.assertEqual(
            self.g.first_difference(first, second),
            {"degree": 16, "left": -49, "right": 0},
        )
        self.assertEqual(R.frame_log(self.g, 1, ("linear", 1), ("linear", 2))[16], 49)


class StrictSourceAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = R.build_payload()

    def test_payload_retains_phase_and_classification_scope(self):
        self.assertEqual(len(self.payload["absolute_cutoff_panels"]), 12)
        self.assertEqual(len(self.payload["same_family_norms"]), 12)
        self.assertEqual(len(self.payload["rational_phase_norms"]), 6)
        self.assertFalse(
            self.payload["scope"]["arbitrary_phase_natural_boundary_claimed"]
        )
        self.assertFalse(
            self.payload["scope"][
                "all_grade_scalar_identity_classified_without_block_hypothesis"
            ]
        )
        self.assertTrue(self.payload["scope"]["zero_phase_product_is_one"])
        with patch.object(R, "build_payload", return_value=self.payload):
            R.check_payload(json.loads(json.dumps(self.payload)))

    def test_authentication_precedes_any_predecessor_import(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("changed source")),
            patch.object(R.importlib.util, "spec_from_file_location") as loader,
        ):
            with self.assertRaises(ValueError):
                R.source()
            loader.assert_not_called()

    def test_numeric_aliases_cannot_keep_old_record_accepted(self):
        for replacement in (True, 1.0, float("nan"), float("inf")):
            candidate = copy.deepcopy(self.payload)
            candidate["absolute_cutoff_panels"][0]["e"] = replacement
            with (
                patch.object(R, "build_payload", return_value=self.payload),
                self.assertRaises(ValueError),
            ):
                R.check_payload(candidate)

    def test_changed_fraction_with_unchanged_digest_is_rejected(self):
        candidate = copy.deepcopy(self.payload)
        candidate["normalization_control"]["e2_degree12"][0] += 1
        with (
            patch.object(R, "build_payload", return_value=self.payload),
            self.assertRaises(ValueError),
        ):
            R.check_payload(candidate)

    def test_missing_scope_and_non_json_types_are_rejected(self):
        candidate = copy.deepcopy(self.payload)
        del candidate["scope"]["native_integral_normalization_recovered"]
        with (
            patch.object(R, "build_payload", return_value=self.payload),
            self.assertRaises(ValueError),
        ):
            R.check_payload(candidate)
        self.assertFalse(R.strict_equal({"x": (1, 2)}, {"x": [1, 2]}))


if __name__ == "__main__":
    unittest.main()
