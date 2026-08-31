"""Actual source multiplicities, Euler residues and bounded continuation witnesses."""

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
    / "research/l-families/atlas/generalized/graded-completion-lab/natural_boundary_replay.py"
)
SPEC = importlib.util.spec_from_file_location("frobenius_ladder_natural_boundary", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class ActualSourceTests(unittest.TestCase):
    def test_odd_divisor_dimensions_match_actual_pbw(self):
        _, frozen = R.source()
        for j in range(1, 33):
            self.assertEqual(
                R.multiplicity(j), sum(frozen.source_row(2 * j)["multiplicities"][1:])
            )
        self.assertEqual(
            [R.multiplicity(j) for j in range(1, 7)], [1, 2, 5, 16, 51, 170]
        )

    def test_actual_curve_source_and_power_not_new_field_fit(self):
        _, frozen = R.source()
        row = frozen.point_counts()
        self.assertEqual(row["proper_counts"], [8, 8])
        self.assertEqual(row["P7"], [1, 0, 7])
        self.assertEqual(row["P49"], [1, 14, 49])
        self.assertFalse(row["F49_enumerated"])

    def test_mobius_square_factors_and_source_bound(self):
        self.assertEqual(
            [R.mobius(n) for n in (1, 3, 9, 15, 25, 30)], [1, -1, 0, 1, 0, -1]
        )
        for j in range(1, 65):
            self.assertGreater(R.multiplicity(j), 0)
            self.assertLessEqual(j * R.multiplicity(j), 4**j)

    def test_parameter_and_source_type_caps(self):
        for bad in (True, 2.0, 0, 257):
            with self.assertRaises(ValueError):
                R.multiplicity(bad)
        for bad in (True, -7.0, 0, 1, -1, 2, 344):
            with self.assertRaises(ValueError):
                R.residue(bad, 1)
        with self.assertRaises(ValueError):
            R.canonical_product(-7, 65)


class EulerTransformTests(unittest.TestCase):
    def test_literal_factor_coefficients_have_correct_signs(self):
        self.assertEqual(R.canonical_product(-7, 4), [1, 0, 14, 35, 161])
        self.assertEqual(R.canonical_product(7, 4), [1, 0, -14, -35, -63])

    def test_product_division_matches_both_logarithmic_routes(self):
        for b in (-7, 7, -49, 49):
            actual = R.polynomial_log_derivative(R.canonical_product(b, 32))
            self.assertEqual(actual, R.direct_log_derivative(b, 32))
            self.assertEqual(actual, R.residue_log_derivative(b, 32))

    def test_omitted_grade_one_is_actual_factor_not_an_ignored_constant(self):
        for b in (-7, 7):
            omitted = R.canonical_product(b, 16)
            complete = R.canonical_product(b, 16, first_grade=1)
            self.assertEqual(complete, R.multiply([1, -b], omitted, 16))
            self.assertNotEqual(complete, omitted)
            self.assertEqual(R.residue_log_derivative(b, 1, False)[1], -b)
            self.assertEqual(R.residue_log_derivative(b, 1)[1], 0)

    def test_wrong_all_divisor_mobius_transform_changes_even_residue(self):
        b, m = -7, 2
        wrong = Fraction(sum(R.mobius(d) * b ** (m // d) for d in (1, 2)), 4 * m)
        self.assertEqual(R.residue(b, m), Fraction(49, 8))
        self.assertNotEqual(wrong, R.residue(b, m))

    def test_log_derivative_requires_literal_unit_integer_polynomial(self):
        for bad in ([True, 0], [1.0, 0], [2, 0], [1, Fraction(1, 2)], []):
            with self.assertRaises(ValueError):
                R.polynomial_log_derivative(bad)


class ResidueAndMonodromyTests(unittest.TestCase):
    def test_first_f7_residues(self):
        self.assertEqual(
            [R.residue(-7, m) for m in (1, 2, 4)],
            [Fraction(-7, 4), Fraction(49, 8), Fraction(2401, 16)],
        )

    def test_dyadic_denominators_through_v8(self):
        for b in (-7, 7, -49, 49):
            for v in range(9):
                self.assertEqual(R.residue(b, 2**v).denominator, 2 ** (v + 2))

    def test_odd_and_composite_residues_need_not_be_fractional(self):
        self.assertEqual(R.residue(-7, 3), -28)
        self.assertEqual(R.residue(-7, 5), -840)
        self.assertEqual(R.residue(-7, 6), 4900)
        self.assertEqual(R.residue(7, 3), 28)

    def test_even_extension_doubles_but_does_not_bound_denominators(self):
        for v in range(9):
            value = 2 * R.residue(-7, 2**v)
            self.assertEqual(value.denominator, 2 ** (v + 1))

    def test_integer_meromorphic_orders_cannot_cancel_fractional_parts(self):
        for v in range(9):
            value = R.residue(-7, 2**v)
            for order in (-17, -1, 0, 1, 29):
                self.assertEqual((value + order).denominator, value.denominator)

    def test_a_fixed_cover_degree_does_not_clear_larger_dyadic_order(self):
        for cover_degree in (1, 2, 3, 4, 8, 16):
            value = R.residue(-7, 32)
            self.assertTrue(
                all((e * value).denominator > 1 for e in range(1, cover_degree + 1))
            )

    def test_finite_head_norm_collisions_are_excluded_in_declared_controls(self):
        for b in (-7, 7, -49, 49):
            for m in (1, 2, 3, 4, 6, 8, 16):
                for j in range(2, 33):
                    self.assertNotEqual(abs(b) ** m, 4**j)


class ContinuationWitnessTests(unittest.TestCase):
    def test_both_cutoffs_and_original_positive_partial_sums(self):
        for b in (-7, -49):
            for radius in (Fraction(1, 2), Fraction(3, 4), Fraction(7, 8)):
                row = R.tail_witness(b, radius)
                self.assertLess(row["4_r_to_H_plus_one"], 1)
                self.assertLess(row["abs_b_r_to_J_plus_one"], Fraction(1, 2))
                self.assertLess(
                    row["original_positive_majorant_partial_sum"],
                    row["geometric_derivative_tail_bound"],
                )
                self.assertGreater(row["original_positive_majorant_partial_sum"], 0)

    def test_cutoffs_are_independent_and_strict_at_half_radius(self):
        row = R.tail_witness(-7, Fraction(1, 2))
        self.assertEqual((row["H"], row["J"]), (2, 3))
        self.assertEqual(4 * Fraction(1, 2) ** row["H"], 1)
        self.assertGreaterEqual(7 * Fraction(1, 2) ** row["J"], Fraction(1, 2))

    def test_radius_validation_and_search_cap(self):
        for bad in (0.5, True, Fraction(0), Fraction(1), Fraction(2)):
            with self.assertRaises(ValueError):
                R.tail_witness(-7, bad)
        with self.assertRaises(ValueError):
            R.tail_witness(-7, Fraction(9999, 10000))


class ActualCoordinateTests(unittest.TestCase):
    def test_same_frobenius_powers(self):
        self.assertEqual(R.matrix_power(1), ((0, -7), (1, 0)))
        self.assertEqual(R.matrix_power(2), ((-7, 0), (0, -7)))
        self.assertEqual(R.matrix_power(4), ((49, 0), (0, 49)))

    def test_all_four_constant_field_controls(self):
        rows = [R.coordinate_control(e) for e in range(1, 5)]
        self.assertEqual([row["auxiliary_b"] for row in rows], [-7, -7, -343, 49])
        self.assertEqual(
            [row["auxiliary_x_equals_z_power"] for row in rows], [4, 2, 4, 2]
        )
        self.assertEqual([row["copies"] for row in rows], [1, 2, 1, 2])
        self.assertEqual([row["first_nonzero_degree"] for row in rows], [8, 4, 8, 4])

    def test_f7_wrong_z_squared_substitution_fails(self):
        direct = R.proper_frobenius_product(1, 16)
        wrong = R.substitute(R.canonical_product(-7, 8), 2, 16)
        self.assertEqual(direct[4], 0)
        self.assertEqual(wrong[4], 14)
        self.assertEqual(direct[8], 14)

    def test_even_extension_repeated_eigenvalue_has_two_copies(self):
        direct = R.proper_frobenius_product(2, 16)
        one_copy = R.substitute(R.canonical_product(-7, 8), 2, 16)
        self.assertEqual(direct[4], 28)
        self.assertEqual(one_copy[4], 14)
        self.assertEqual(R.proper_frobenius_product(4, 8)[4], -196)


class AcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = R.build_payload()

    def test_full_payload_roundtrip_and_meromorphy_proof_pins(self):
        candidate = json.loads(json.dumps(self.payload))
        with patch.object(R, "build_payload", return_value=self.payload):
            R.check_payload(candidate)
        self.assertEqual(len(candidate["two_cutoff_tail_witnesses"]), 6)
        self.assertEqual(len(candidate["euler_transform_panels"]), 4)
        self.assertIn("coherent_meromorphy", candidate["source"])
        self.assertIn("finite_ladder_source", candidate["source"])

    def test_changed_residue_rejected_even_with_old_hash(self):
        candidate = copy.deepcopy(self.payload)
        candidate["euler_transform_panels"][0]["dyadic_residues"][0]["residue"][0] += 1
        with (
            patch.object(R, "build_payload", return_value=self.payload),
            self.assertRaises(ValueError),
        ):
            R.check_payload(candidate)

    def test_integer_boolean_float_and_nonfinite_counterfeits(self):
        for replacement in (True, 1.0, float("nan"), float("inf")):
            candidate = copy.deepcopy(self.payload)
            candidate["source_multiplicities"][0]["j"] = replacement
            with (
                patch.object(R, "build_payload", return_value=self.payload),
                self.assertRaises(ValueError),
            ):
                R.check_payload(candidate)

    def test_coverage_and_scope_fields_cannot_disappear_or_be_added(self):
        for extra in (False, True):
            candidate = copy.deepcopy(self.payload)
            if extra:
                candidate["extra"] = 1
            else:
                del candidate["scope"]["full_before_unit_natural_boundary_claimed"]
            with (
                patch.object(R, "build_payload", return_value=self.payload),
                self.assertRaises(ValueError),
            ):
                R.check_payload(candidate)

    def test_bad_authentication_precedes_import(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("changed source")),
            patch.object(R.importlib.util, "spec_from_file_location") as loader,
        ):
            with self.assertRaises(ValueError):
                R.source()
            loader.assert_not_called()

    def test_non_json_objects_and_changed_source_binding_rejected(self):
        self.assertFalse(R.strict_equal({"x": (1, 2)}, {"x": [1, 2]}))
        candidate = copy.deepcopy(self.payload)
        candidate["source"]["coherent_meromorphy"]["blob"] = "0" * 40
        with (
            patch.object(R, "build_payload", return_value=self.payload),
            self.assertRaises(ValueError),
        ):
            R.check_payload(candidate)


if __name__ == "__main__":
    unittest.main()
