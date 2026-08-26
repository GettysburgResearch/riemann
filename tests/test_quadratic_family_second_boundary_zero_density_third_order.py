from __future__ import annotations

import importlib.util
import math
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
    / "quadratic_family_second_boundary_zero_density_third_order.py"
)
SPEC = importlib.util.spec_from_file_location("second_density_third_order", MODULE_PATH)
assert SPEC and SPEC.loader
third_order = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(third_order)


class SecondBoundaryThirdOrderTest(unittest.TestCase):
    def test_one_pinned_harmonic_identity(self) -> None:
        for h_value in range(7, 41):
            self.assertEqual(
                third_order.one_pinned_direct_weight(h_value),
                third_order.one_pinned_harmonic_weight(h_value),
            )

    def test_degree_profile_exhaustion(self) -> None:
        for h_value in (7, 8, 15, 25, 40):
            self.assertEqual(
                set(third_order.degree_profiles(h_value)),
                set(third_order.claimed_profiles(h_value)),
            )
            self.assertEqual(
                third_order.enumerated_profile_weight(h_value),
                third_order.all_profile_principal_weight(h_value),
            )

    def test_exact_affine_log2_coefficients(self) -> None:
        self.assertEqual(
            third_order.H_MINUS_3_ONE_PINNED,
            (Fraction(7, 36), Fraction(1, 9)),
        )
        self.assertEqual(
            third_order.H_MINUS_3_TWO_PINNED,
            (Fraction(1, 4), Fraction(0)),
        )
        self.assertEqual(
            third_order.H_MINUS_3_TOTAL,
            (Fraction(4, 9), Fraction(1, 9)),
        )
        self.assertEqual(
            third_order.M_MINUS_3,
            (Fraction(352, 9), Fraction(160, 9)),
        )

    def test_bounded_asymptotic_panels(self) -> None:
        c2 = third_order.affine_float(third_order.H_MINUS_2)
        c3 = third_order.affine_float(third_order.H_MINUS_3_TOTAL)
        estimates = []
        for h_value in (25, 50, 100, 200):
            weight = float(third_order.all_profile_principal_weight(h_value))
            estimates.append(h_value**3 * (weight - c2 / h_value**2))
        self.assertLess(abs(estimates[-1] - c3), 0.01)
        self.assertLess(abs(estimates[-1] - c3), abs(estimates[0] - c3))

    def test_invalid_inputs_and_resource_caps(self) -> None:
        for h_value in (True, 6, 201):
            with self.assertRaises(ValueError):
                third_order.one_pinned_direct_weight(h_value)
        with self.assertRaises(ValueError):
            third_order.degree_profiles(41)
        report = third_order.run()
        self.assertIn("same_local_probability", report["fixed_q_count"])
        caps = report["resource_caps"]
        self.assertEqual(caps["polynomials_enumerated"], 0)
        self.assertEqual(caps["residue_classes_enumerated"], 0)
        self.assertTrue(
            math.isfinite(
                report["convergence_panels"][-1]["M_cubed_next_coefficient_estimate"]
            )
        )


if __name__ == "__main__":
    unittest.main()
