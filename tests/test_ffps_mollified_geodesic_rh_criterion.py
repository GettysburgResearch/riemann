from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from math import prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_mollified_geodesic_rh_criterion.py"
)
SPEC = importlib.util.spec_from_file_location("geodesic_criterion", MODULE_PATH)
assert SPEC and SPEC.loader
geodesic_criterion = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(geodesic_criterion)


class FfpsMollifiedGeodesicRhCriterionTest(unittest.TestCase):
    def test_squared_source_support(self) -> None:
        self.assertEqual(geodesic_criterion.squared_source_coefficient(4), -1)
        self.assertEqual(geodesic_criterion.squared_source_coefficient(9), -1)
        self.assertEqual(geodesic_criterion.squared_source_coefficient(36), 1)
        self.assertEqual(geodesic_criterion.squared_source_coefficient(12), 0)
        self.assertEqual(
            geodesic_criterion.normalized_squared_shift_coefficient(2),
            Fraction(-1, 2),
        )
        large_squarefree_root = prod(
            (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
        )
        self.assertEqual(
            geodesic_criterion.squared_source_coefficient(
                large_squarefree_root**2
            ),
            geodesic_criterion.beta(large_squarefree_root),
        )

    def test_duplicate_67_coefficient(self) -> None:
        self.assertEqual(geodesic_criterion.beta(67), -2)
        self.assertEqual(geodesic_criterion.beta(67 * 2), 2)
        self.assertEqual(geodesic_criterion.beta(67 * 67), 1)

    def test_differential_identity(self) -> None:
        self.assertEqual(
            geodesic_criterion.d_out_coefficients(),
            (
                Fraction(0),
                Fraction(3, 4),
                Fraction(1, 4),
                Fraction(-6),
                Fraction(5),
            ),
        )
        for integer in (2, 3, 5, 7):
            left, right = geodesic_criterion.differential_identity(
                Fraction(integer)
            )
            self.assertEqual(left, right)

    def test_endpoint_source_orientation(self) -> None:
        ledger = geodesic_criterion.endpoint_source_ledger()
        self.assertIn("beta^square", ledger["tau_0"])
        self.assertIn("Lambda_1*Lambda_1=beta", ledger["tau_1"])
        self.assertTrue(ledger["orientation"].startswith("I_1-I_0="))

    def test_causal_reflection_identity(self) -> None:
        even, odd = geodesic_criterion.reflection_energies(
            Fraction(5), Fraction(3)
        )
        self.assertEqual((even, odd), (Fraction(4), Fraction(1)))
        with self.assertRaises(ValueError):
            geodesic_criterion.reflection_energies(Fraction(1), Fraction(2))
        self.assertEqual(
            geodesic_criterion.reflected_negative_part(Fraction(-3)), 0
        )
        self.assertEqual(
            geodesic_criterion.reflected_negative_part(Fraction(2)), 4
        )
        self.assertTrue(
            geodesic_criterion.causal_cutoff_valid(Fraction(10), Fraction(11))
        )
        self.assertFalse(
            geodesic_criterion.causal_cutoff_valid(Fraction(10), Fraction(10))
        )

    def test_harmonic_majorant(self) -> None:
        self.assertEqual(
            geodesic_criterion.harmonic_l1_majorant(3), Fraction(11, 3)
        )
        with self.assertRaises(ValueError):
            geodesic_criterion.harmonic_l1_majorant(0)

    def test_equivalence_boundary(self) -> None:
        result = geodesic_criterion.run()
        self.assertEqual(
            result["open_gates"]["native"]["name"], "NATREF-MOLL106150"
        )
        self.assertEqual(
            result["open_gates"]["geodesic"]["name"], "GEO-WKSFSC106150"
        )
        self.assertFalse(
            result["equivalence"]["native_reflection_estimate_proved"]
        )
        self.assertFalse(result["equivalence"]["geodesic_estimate_proved"])
        self.assertFalse(result["equivalence"]["rh_proved"])
        self.assertEqual(result["resource_caps"]["conductors_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
