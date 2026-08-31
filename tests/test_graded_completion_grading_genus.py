"""Actual canonical factors, changed normalization and declared genus policies."""

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
    / "research/l-families/atlas/generalized/graded-completion-lab/grading_genus_replay.py"
)
SPEC = importlib.util.spec_from_file_location("grading_genus_completion", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class ActualSourceAndPolicies(unittest.TestCase):
    def test_source_multiplicity_is_actual_antiinvariant_pbw(self):
        _, frozen, original = R.source()
        for n in range(2, 65, 2):
            self.assertEqual(R.multiplicity(n), frozen.multiplicity(n))
            self.assertEqual(
                R.multiplicity(n), sum(original.source_row(n)["multiplicities"][1:])
            )
        self.assertEqual(
            [R.multiplicity(n) for n in (2, 4, 6, 8, 10, 12)], [1, 2, 5, 16, 51, 170]
        )

    def test_same_frobenius_matrix_and_trace_recurrence(self):
        self.assertEqual(R.frobenius_matrix(1), ((0, -7), (1, 0)))
        self.assertEqual(R.frobenius_matrix(2), ((-7, 0), (0, -7)))
        for e in range(1, 7):
            matrix = R.frobenius_matrix(e)
            self.assertEqual(matrix[0][0] + matrix[1][1], R.trace(e))
            self.assertEqual(
                matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0], 7**e
            )

    def test_nonmonotone_policy_is_not_replaced_by_monotone_hull(self):
        orders = [R.policy_order(n, "nonmonotone") for n in range(4, 17, 2)]
        self.assertEqual(orders, [4, 3, 8, 5, 12, 7, 16])
        self.assertLess(orders[1], orders[0])
        self.assertTrue(
            all(R.policy_order(n, "nonmonotone") >= n // 2 for n in range(4, 65, 2))
        )

    def test_slow_policy_uses_integer_logarithm_without_float(self):
        self.assertEqual(
            [R.policy_order(n, "slow") for n in (4, 6, 8, 14, 16, 32, 64)],
            [3, 3, 4, 4, 5, 6, 7],
        )
        self.assertEqual(R.policy_order(16, "linear", 6), 96)

    def test_genus_and_source_caps_reject_coercion(self):
        for bad in (True, 4.0, 3, 66):
            with self.assertRaises(ValueError):
                R.policy_order(bad)
        for bad in (True, 1.0, 0, 7):
            with self.assertRaises(ValueError):
                R.policy_order(4, "linear", bad)
        for bad in (None, True, "unknown"):
            with self.assertRaises(ValueError):
                R.policy_order(4, bad)
        with self.assertRaises(ValueError):
            R.policy_order(4, "slow", 2)

    def test_polynomial_caps_are_enforced_before_work(self):
        for args in (
            (True, "linear", 1, 16, 64),
            (7, "linear", 1, 16, 64),
            (1, "linear", 1, 18, 64),
            (1, "linear", 1, 16, 65),
        ):
            with self.assertRaises(ValueError):
                R.canonical_product(*args)
        with self.assertRaises(ValueError):
            R.bit_guard(1 << 20000)


class CanonicalProductControls(unittest.TestCase):
    def test_literal_proper_factor_keeps_omitted_grade_two(self):
        native = R.proper_product(1, cut=16)
        self.assertEqual(native[4], 0)
        self.assertEqual(native[8], 14)
        self.assertEqual(R.proper_product(2, cut=8)[4], 28)

    def test_all_twenty_direct_products_match_independent_trace_logs(self):
        for e in range(1, 5):
            for policy, slope in (
                ("linear", 1),
                ("linear", 2),
                ("linear", 3),
                ("slow", 1),
                ("nonmonotone", 1),
            ):
                self.assertEqual(
                    R.canonical_product(e, policy, slope),
                    R.formal_exp(R.policy_log(e, policy, slope), 64),
                )

    def test_first_source_block_has_exact_counterterm(self):
        proper = [Fraction(1)] + [Fraction(0)] * 31
        proper[8], proper[16] = 14, 49
        logarithm = [Fraction(0)] * 32
        logarithm[8] = -14
        expected = R.multiply(proper, R.formal_exp(logarithm, 31), 31)
        self.assertEqual(R.canonical_product(1, grade_cap=4, cut=31), expected)
        self.assertEqual(R.canonical_product(1, cut=31), expected)

    def test_exact_first_nonintegral_coefficient_changes_native_germ(self):
        row = R.normalization_control()
        self.assertEqual(row["native_coefficient_degree8"], 14)
        self.assertEqual(row["new_coefficient_degree8"], 0)
        self.assertEqual(row["new_coefficient_degree16"], -49)
        self.assertEqual(row["new_coefficient_degree24"], Fraction(686, 3))
        self.assertEqual(
            row["fractional_part_for_every_integral_H2_with_constant_one"],
            Fraction(2, 3),
        )
        self.assertFalse(row["uncomputed_H2_coefficients_invented"])

    def test_integral_H2_symbolic_coefficient_obstruction(self):
        for h8, h24 in ((0, 0), (1, 7), (-19, 103), (123, -321)):
            value = h24 - 49 * h8 + Fraction(686, 3)
            self.assertEqual(value.denominator, 3)
            self.assertEqual(value % 1, Fraction(2, 3))

    def test_linear_policy_first_degree_and_sign_all_declared_cases(self):
        for e in range(1, 5):
            for slope in (1, 2, 3):
                product = R.canonical_product(e, slope=slope)
                first = next(n for n in range(1, 65) if product[n])
                self.assertEqual(first, 16 * slope)
                self.assertEqual(
                    product[first], Fraction(-(7 ** (2 * e * slope)), slope)
                )

    def test_odd_trace_vanishing_can_identify_two_local_genus_orders(self):
        self.assertEqual(
            R.canonical_product(1, "slow", grade_cap=4),
            R.canonical_product(1, grade_cap=4),
        )
        self.assertNotEqual(
            R.canonical_product(2, "slow", grade_cap=4),
            R.canonical_product(2, grade_cap=4),
        )
        self.assertNotEqual(R.canonical_product(2, "slow", grade_cap=4)[12], 0)

    def test_zero_cutoff_stays_normalized(self):
        self.assertEqual(R.canonical_product(1, cut=0), [1])
        self.assertEqual(R.policy_log(1, cut=0), [0])
        with self.assertRaises(ValueError):
            R.formal_exp([1], 0)


class PolicyQuotientAndNorm(unittest.TestCase):
    def test_oriented_counterterm_reverses_sign(self):
        first, second = ("slow", 1), ("nonmonotone", 1)
        forward = R.policy_counterterm(1, first, second)
        backward = R.policy_counterterm(1, second, first)
        self.assertEqual(forward, [-value for value in backward])
        self.assertEqual(R.policy_counterterm(1, first, first), [0] * 65)

    def test_exact_policy_quotient_multiplies_across_zero_divisors(self):
        for e in (1, 2):
            first, second = ("linear", 1), ("linear", 2)
            quotient = R.formal_exp(R.policy_counterterm(e, first, second), 64)
            self.assertEqual(
                R.canonical_product(e, *second),
                R.multiply(R.canonical_product(e, *first), quotient, 64),
            )
        self.assertEqual(R.policy_counterterm(1, ("linear", 1), ("linear", 2))[16], 49)

    def test_all_eight_changed_slope_frobenius_norms(self):
        for e in (1, 2):
            for slope in (1, 2):
                for degree in (2, 3):
                    row = R.norm_control(e, slope, degree)
                    self.assertEqual(row["right_slope"], degree * slope)

    def test_unchanged_slope_counterfeit_is_visible_at_degree_sixteen(self):
        row = R.norm_control(1, 1, 2)["unchanged_slope_first_difference"]
        self.assertEqual(row, {"degree": 16, "left": 0, "right": -98})

    def test_phase_sieve_acts_on_frobenius_power_not_total_grade(self):
        correct = R.policy_log(1, "slow", cut=32, norm_degree=3)
        wrong = [Fraction(0)] * 33
        for n in range(4, 17, 2):
            for h in range(R.policy_order(n, "slow"), 32 // n + 1):
                if (n * h) % 3 == 0:
                    wrong[n * h] -= Fraction(3 * R.multiplicity(n) * R.trace(h), h)
        self.assertNotEqual(correct[24], wrong[24])

    def test_odd_extension_quadratic_norm_is_a_square(self):
        left = R.substituted(R.canonical_product(2, cut=32), 2, 64)
        right = R.canonical_product(1, slope=2)
        self.assertEqual(left, R.multiply(right, right, 64))


class AnalyticScopeControls(unittest.TestCase):
    def test_bounded_order_subsequence_has_nonzero_growing_log_term(self):
        rows = R.bounded_policy_controls()
        self.assertEqual(len(rows), 16)
        self.assertTrue(all(row["exponential_base"] > 1 for row in rows))
        self.assertTrue(all(row["leading_real_log_coefficient"] != 0 for row in rows))
        self.assertEqual(rows[0]["first_surviving_trace_order"], 2)

    def test_actual_zero_multiplicity_changes_when_frobenius_eigenvalues_coincide(self):
        rows = R.source_zero_controls()
        one = next(row for row in rows if (row["e"], row["grade"]) == (1, 4))
        two = next(row for row in rows if (row["e"], row["grade"]) == (2, 4))
        self.assertEqual(one["distinct_eigenvalue_count"], 2)
        self.assertEqual(one["multiplicity_per_distinct_Frobenius_eigenvalue"], 2)
        self.assertEqual(two["distinct_eigenvalue_count"], 1)
        self.assertEqual(two["multiplicity_per_distinct_Frobenius_eigenvalue"], 4)

    def test_good_place_zero_norms_are_separate_from_weight_zeros(self):
        for row in R.source_zero_controls():
            self.assertTrue(all(row["good_degree_1_through_16_noncollision"]))
            self.assertEqual(row["radius_power_2n"], Fraction(1, 7 ** row["e"]))
            self.assertTrue(row["infinite_density_is_proved_not_sampled"])


class StrictAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = R.build_payload()

    def test_payload_binds_all_source_and_analytic_scope(self):
        self.assertEqual(len(self.payload["policies"]), 20)
        self.assertEqual(len(self.payload["policy_quotients"]), 6)
        self.assertEqual(len(self.payload["frobenius_norms"]), 8)
        self.assertIn("geometric_joint_cover", self.payload["source"])
        self.assertFalse(
            self.payload["scope"]["global_scalar_frame_equals_native_germ"]
        )
        self.assertFalse(self.payload["scope"]["policy_uniqueness_claimed"])
        with patch.object(R, "build_payload", return_value=self.payload):
            R.check_payload(json.loads(json.dumps(self.payload)))

    def test_authentication_precedes_import(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("source changed")),
            patch.object(R.importlib.util, "spec_from_file_location") as loader,
        ):
            with self.assertRaises(ValueError):
                R.source()
            loader.assert_not_called()

    def test_numeric_type_counterfeits_cannot_reuse_the_digest(self):
        for replacement in (True, 1.0, float("nan"), float("inf")):
            candidate = copy.deepcopy(self.payload)
            candidate["policies"][0]["e"] = replacement
            with (
                patch.object(R, "build_payload", return_value=self.payload),
                self.assertRaises(ValueError),
            ):
                R.check_payload(candidate)

    def test_changed_coefficient_with_same_digest_is_rejected(self):
        candidate = copy.deepcopy(self.payload)
        candidate["normalization_change"]["new_coefficient_degree24"][0] += 1
        with (
            patch.object(R, "build_payload", return_value=self.payload),
            self.assertRaises(ValueError),
        ):
            R.check_payload(candidate)

    def test_source_coverage_and_scope_are_part_of_acceptance(self):
        candidate = copy.deepcopy(self.payload)
        del candidate["source"]["coherent_good_place_zeros"]
        with (
            patch.object(R, "build_payload", return_value=self.payload),
            self.assertRaises(ValueError),
        ):
            R.check_payload(candidate)
        self.assertFalse(R.strict_equal({"x": (1, 2)}, {"x": [1, 2]}))


if __name__ == "__main__":
    unittest.main()
