from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "function_field_basewave_curve_extension.py"
)
SPEC = importlib.util.spec_from_file_location(
    "function_field_basewave_curve_extension", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FunctionFieldBasewaveCurveExtensionTest(unittest.TestCase):
    def test_frozen_shadow_predecessor_is_pinned(self) -> None:
        subject.check_shadow_blobs()

    def test_local_cubic_identity(self) -> None:
        certificate = subject.local_cubic_certificate()
        self.assertEqual(certificate["checks"], 9)
        self.assertIn("ab(a+b-ab)", certificate["identity"])

    def test_p1_minus_infinity_recovers_affine_line(self) -> None:
        for field_size in subject.REPLAY_FIELD_SIZES:
            with self.subTest(field_size=field_size):
                value = Fraction(1, 4 * field_size)
                row = subject.p1_affine_specialization(field_size, value)
                self.assertEqual(
                    Fraction(row["outside_product"]), 1 - field_size * value
                )

    def test_deleted_support_tracks_places_not_distinct_degrees(self) -> None:
        panel = subject.deleted_modulus_panel((1, 2, 2, 5))
        self.assertEqual(panel["degrees"], [1, 2, 2, 5])
        self.assertEqual(panel["degree_multiplicities"], {"1": 1, "2": 2, "5": 1})
        self.assertTrue(panel["support_only"])
        self.assertTrue(panel["repeated_degrees_allowed"])
        expected = subject.deleted_factor_value(
            2, (1, 2, 2, 5), Fraction(1, 7), Fraction(2, 11)
        )
        self.assertEqual(
            Fraction(panel["exact_q4_replay_value_at_X_1_7_Y_2_11"]), expected
        )

    def test_residual_replay_radius_is_strictly_inside_domain(self) -> None:
        panel = subject.convergence_panel()
        for row in panel["rows"]:
            with self.subTest(field_size=row["field_size"]):
                self.assertLess(Fraction(row["r_to_the_sixth"]), row["field_size"])

    def test_repeated_unit_root_has_exact_polynomial_growth(self) -> None:
        for multiplicity in range(1, 5):
            with self.subTest(multiplicity=multiplicity):
                row = subject.polynomial_degree_certificate(multiplicity, 16)
                self.assertEqual(row["coefficient_polynomial_degree"], multiplicity - 1)
                expected = [
                    subject.repeated_unit_root_coefficient(multiplicity, degree)
                    for degree in range(17)
                ]
                self.assertEqual(row["coefficients"], expected)

    def test_scope_and_resource_firewalls(self) -> None:
        report = subject.run(check_sources=False)
        scope = report["scope"]
        self.assertTrue(scope["all_curve_factorization_proved"])
        self.assertTrue(scope["polynomial_coefficient_bound_proved"])
        self.assertTrue(scope["fixed_offset_unit_circle_expansion_proved"])
        self.assertFalse(scope["exponential_decay_in_positive_genus_claimed"])
        self.assertFalse(scope["shell_l2_summability_claimed"])
        self.assertFalse(scope["waveprimcar_proved"])
        self.assertFalse(scope["rh_proved"])
        resources = report["resource_caps"]
        self.assertEqual(resources["point_counts"], 0)
        self.assertEqual(resources["closed_points_enumerated"], 0)
        self.assertEqual(resources["curves_enumerated"], 0)
        self.assertEqual(resources["floating_point_operations"], 0)

    def test_input_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.deleted_modulus_panel((1, 0))
        with self.assertRaises(ValueError):
            subject.p1_affine_specialization(0, Fraction(1, 2))
        with self.assertRaises(ValueError):
            subject.reciprocal_series((Fraction(2),), 3)
        with self.assertRaises(ValueError):
            subject.repeated_unit_root_coefficient(2, -1)


if __name__ == "__main__":
    unittest.main()
