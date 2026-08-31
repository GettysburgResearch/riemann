"""Same-Frobenius canonical products, cyclic norms and frame limitations."""

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
    / "research/l-families/atlas/generalized/graded-completion-lab/regularized_replay.py"
)
SPEC = importlib.util.spec_from_file_location("regularized_frobenius_tower", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class ActualFrobeniusTests(unittest.TestCase):
    def test_actual_multiplicities_match_frozen_pbw(self):
        _, frozen = R.source()
        for n in range(2, 65, 2):
            self.assertEqual(
                R.multiplicity(n), sum(frozen.source_row(n)["multiplicities"][1:])
            )
        self.assertEqual(
            [R.multiplicity(n) for n in (2, 4, 6, 8, 10, 12)], [1, 2, 5, 16, 51, 170]
        )

    def test_same_frobenius_matrix_square_is_minus_seven(self):
        self.assertEqual(R.frobenius_matrix(1), ((0, -7), (1, 0)))
        self.assertEqual(R.frobenius_matrix(2), ((-7, 0), (0, -7)))
        self.assertEqual(R.frobenius_matrix(4), ((49, 0), (0, 49)))

    def test_recurrence_traces_match_literal_powers(self):
        for e in range(17):
            matrix = R.frobenius_matrix(e)
            self.assertEqual(R.frobenius_trace(e), matrix[0][0] + matrix[1][1])
        self.assertEqual(
            [R.frobenius_trace(e) for e in range(7)], [2, 0, -14, 0, 98, 0, -686]
        )

    def test_frozen_actual_curve_is_counted_not_fitted(self):
        _, frozen = R.source()
        row = frozen.point_counts()
        self.assertEqual(row["proper_counts"], [8, 8])
        self.assertEqual(row["P7"], [1, 0, 7])
        self.assertEqual(row["P49"], [1, 14, 49])
        self.assertFalse(row["F49_enumerated"])

    def test_source_caps_and_types_precede_cached_product(self):
        for bad in (True, 1.0, 0, 9):
            with self.assertRaises(ValueError):
                R.proper_product(bad, 16, 64)
        with self.assertRaises(ValueError):
            R.multiplicity(3)
        with self.assertRaises(ValueError):
            R.regularized_direct(1, 1, 2)
        with self.assertRaises(ValueError):
            R.frobenius_trace(257)


class CanonicalProductTests(unittest.TestCase):
    def test_first_operator_grade_is_four_not_two(self):
        row = R.regularized_direct(1, 1, 4, 16)
        self.assertEqual(row[4], 0)
        self.assertEqual(row[8], 14)
        self.assertEqual(row[16], 49)

    def test_even_extension_proper_factor_uses_powered_frobenius(self):
        row = R.regularized_direct(2, 1, 4, 8)
        self.assertEqual(row[4], 28)
        self.assertEqual(row[8], 294)

    def test_finite_canonical_product_matches_formal_logarithm(self):
        for e, p in ((1, 1), (1, 3), (2, 2), (3, 5), (8, 8)):
            direct = R.regularized_direct(e, p)
            logarithmic = R.formal_exp(R.regularized_log(e, p), 64)
            self.assertEqual(direct, logarithmic)

    def test_regularization_can_change_coefficient_sign(self):
        original = R.regularized_direct(2, 1, 4, 8)
        second = R.regularized_direct(2, 2, 4, 8)
        self.assertEqual(original[4], 28)
        self.assertEqual(second[4], 0)
        self.assertEqual(second[8], -98)

    def test_odd_trace_cancellation_really_preserves_adjacent_orders(self):
        for e in (1, 3):
            for p in (1, 3, 5, 7):
                self.assertEqual(
                    R.regularized_direct(e, p, 8, 40),
                    R.regularized_direct(e, p + 1, 8, 40),
                )

    def test_counterterm_transition_without_division_at_zeros(self):
        result = R.transition_control(2, 1, 2, 32)
        self.assertEqual(result["first_changed_coefficient"]["degree"], 4)
        self.assertTrue(
            result["multiplicative_identity_verified_without_dividing_at_zeros"]
        )
        self.assertIsNone(
            R.transition_control(1, 1, 2, 32)["first_changed_coefficient"]
        )

    def test_transition_cocycle_as_actual_trace_sums(self):
        first = R.counterterm(2, 1, 3, 16, 32)
        second = R.counterterm(2, 3, 5, 16, 32)
        total = R.counterterm(2, 1, 5, 16, 32)
        self.assertEqual([a + b for a, b in zip(first, second, strict=True)], total)

    def test_regularization_limit_is_one_not_native_multiplier(self):
        self.assertEqual(R.regularized_direct(2, 8, 16, 28), [1] + [0] * 28)
        self.assertNotEqual(R.regularized_direct(2, 1, 16, 28), [1] + [0] * 28)


class DomainAndNormTests(unittest.TestCase):
    def test_branch_exponents_have_correct_sign_and_denominator(self):
        self.assertEqual(R.radius_control(1, 1)["branch_exponent"], Fraction(-7, 4))
        self.assertEqual(R.radius_control(1, 3)["branch_exponent"], Fraction(49, 8))
        self.assertEqual(R.radius_control(2, 1)["branch_exponent"], Fraction(-7, 2))
        self.assertEqual(R.radius_control(2, 2)["branch_exponent"], Fraction(49, 4))

    def test_all_preregistered_first_orders_are_nonintegral(self):
        for e in range(1, 9):
            for p in range(1, 9):
                row = R.radius_control(e, p)
                self.assertNotEqual(row["branch_exponent"].denominator, 1)
                self.assertEqual(
                    row["first_nonzero_trace_order"], p if e % 2 == 0 else p + p % 2
                )

    def test_scalar_and_ordinary_operator_domains_are_distinguished(self):
        row = R.radius_control(1, 1)
        self.assertEqual(row["scalar_radius"], "2^(-1/2)")
        self.assertEqual(row["ordinary_Sp_radius"], "2^(-1/1)")
        self.assertEqual(R.radius_control(2, 3)["scalar_radius"], "2^(-1/3)")

    def test_full_source_parity_and_before_branch(self):
        for e in range(1, 9):
            row = R.radius_control(e, 1)
            self.assertEqual(row["full_after_radius"], "1/sqrt(2)" if e % 2 else "1/2")
            self.assertEqual(row["full_before_radius"], "1/2")
            self.assertNotEqual(row["before_exponent_mod_integer"].denominator, 1)

    def test_cyclic_norms_degrees_two_three_four(self):
        for degree in (2, 3, 4):
            row = R.cyclic_norm_control(1, 2, degree, 48)
            self.assertEqual(row["right_order"], 2 * degree)
            self.assertTrue(
                row["root_of_unity_sieve_applied_to_Frobenius_power_not_total_grade"]
            )

    def test_quadratic_symmetric_spectrum_norm_is_square(self):
        left = R.substituted(R.regularized_direct(2, 2, 16, 24), 2, 48)
        right = R.polynomial_power(R.regularized_direct(1, 4, 16, 48), 2, 48)
        self.assertEqual(left, right)

    def test_unchanged_regularization_order_is_false(self):
        left = R.substituted(R.regularized_direct(2, 2, 16, 16), 2, 32)
        wrong = R.polynomial_power(R.regularized_direct(1, 2, 16, 32), 2, 32)
        self.assertEqual(
            R.first_difference(left, wrong), {"degree": 8, "left": 0, "right": 28}
        )

    def test_total_grade_sieve_is_not_frobenius_power_sieve(self):
        correct = R.regularized_log(2, 2, 16, 32, norm_degree=2)
        base = R.regularized_log(2, 2, 16, 32)
        wrong = [2 * value if n % 2 == 0 else 0 for n, value in enumerate(base)]
        self.assertEqual(R.first_difference(correct, wrong)["degree"], 12)

    def test_cyclic_norm_caps_reject_unregistered_power(self):
        with self.assertRaises(ValueError):
            R.cyclic_norm_control(3, 2, 4)
        with self.assertRaises(ValueError):
            R.cyclic_norm_control(1, 3, 4)


class AuthenticationTests(unittest.TestCase):
    def test_authentication_precedes_executable_import(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("blocked")),
            patch.object(R.importlib.util, "spec_from_file_location") as imported,
        ):
            with self.assertRaises(ValueError):
                R.source()
            imported.assert_not_called()

    def test_wrong_source_blob_is_rejected(self):
        with (
            patch.object(R.subprocess, "check_output", return_value="wrong\n"),
            self.assertRaises(ValueError),
        ):
            R.authenticate()

    def test_canonical_json_rejects_numeric_aliases(self):
        for value in (True, 1.0, "1"):
            self.assertFalse(R.strict_equal({"e": 1}, {"e": value}))
        self.assertFalse(R.strict_equal([1, 2], (1, 2)))
        self.assertFalse(R.strict_equal({1: "a"}, {"1": "a"}))

    def test_nonfinite_json_fails_closed(self):
        self.assertFalse(R.strict_equal([float("nan")], [float("nan")]))
        self.assertFalse(R.strict_equal([float("inf")], [float("inf")]))

    def test_payload_mutation_rejected_with_same_python_value(self):
        good = {"order": 1, "eta": [-7, 4], "same": True}
        for key, value in (("order", True), ("eta", [-7.0, 4]), ("same", 1)):
            bad = copy.deepcopy(good)
            bad[key] = value
            with (
                patch.object(R, "build_payload", return_value=good),
                self.assertRaises(ValueError),
            ):
                R.check_payload(bad)

    def test_bound_fixture_keeps_all_panels_and_wrong_order_witness(self):
        record = json.loads(R.FIXTURE.read_bytes())
        R.check_payload(record)
        self.assertEqual(len(record["regularizations"]), 64)
        self.assertEqual(len(record["cyclic_norms"]), 12)
        self.assertEqual(record["wrong_unchanged_order_base_change"]["degree"], 8)
        self.assertEqual(record["actual_F7_source"]["proper_counts"], [8, 8])


if __name__ == "__main__":
    unittest.main()
