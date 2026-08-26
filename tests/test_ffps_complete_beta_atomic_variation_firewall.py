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
    / "ffps_complete_beta_atomic_variation_firewall.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_COMPLETE_BETA_ATOMIC_VARIATION_FIREWALL.md")
SPEC = importlib.util.spec_from_file_location("complete_beta_atomic", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load complete-beta atomic replay")
complete_beta_atomic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(complete_beta_atomic)


class FfpsCompleteBetaAtomicVariationFirewallTest(unittest.TestCase):
    def test_frozen_source_blobs(self) -> None:
        complete_beta_atomic.check_source_blobs()

    def test_effective_atomic_coefficients(self) -> None:
        coefficients = complete_beta_atomic.complete_beta_atomic_coefficients()
        self.assertEqual(coefficients[0], (Fraction(5), Fraction(0)))
        self.assertEqual(coefficients[1], (Fraction(-10), Fraction(-25, 2)))
        self.assertEqual(coefficients[2], (Fraction(25), Fraction(25)))
        self.assertEqual(coefficients[3], (Fraction(-40), Fraction(-35, 2)))
        self.assertEqual(coefficients[4], (Fraction(20), Fraction(10)))
        self.assertEqual(coefficients[5], (Fraction(0), Fraction(-5)))

    def test_balanced_positive_negative_mass(self) -> None:
        positive, negative = complete_beta_atomic.positive_and_negative_mass()
        self.assertEqual(positive, (Fraction(50), Fraction(35)))
        self.assertEqual(negative, positive)
        self.assertEqual(
            complete_beta_atomic.total_atomic_variation(),
            (Fraction(100), Fraction(70)),
        )

    def test_exact_quadratic_sign(self) -> None:
        self.assertEqual(
            complete_beta_atomic.qsign((Fraction(3), Fraction(-2))), 1
        )
        self.assertEqual(
            complete_beta_atomic.qsign((Fraction(1), Fraction(-1))), -1
        )
        self.assertEqual(
            complete_beta_atomic.qsign((Fraction(-1), Fraction(1))), 1
        )
        self.assertEqual(
            complete_beta_atomic.qsign((Fraction(-3), Fraction(2))), -1
        )

    def test_complete_group_horizon_and_uniqueness(self) -> None:
        self.assertEqual(
            complete_beta_atomic.complete_group_positions(31),
            (31, 62, 124, 248, 496, 992),
        )
        self.assertTrue(complete_beta_atomic.complete_group_fits_horizon(31, 992))
        self.assertFalse(complete_beta_atomic.complete_group_fits_horizon(31, 991))
        positions = {
            position
            for odd_part in range(1, 64, 2)
            for position in complete_beta_atomic.complete_group_positions(odd_part)
        }
        self.assertEqual(len(positions), 32 * 6)
        with self.assertRaises(ValueError):
            complete_beta_atomic.complete_group_positions(2)
        with self.assertRaises(ValueError):
            complete_beta_atomic.complete_group_fits_horizon(1, True)

    def test_two_adic_beta_relation(self) -> None:
        self.assertTrue(complete_beta_atomic.check_two_adic_source_relation(1500))
        with self.assertRaises(ValueError):
            complete_beta_atomic.check_two_adic_source_relation(True)
        with self.assertRaises(ValueError):
            complete_beta_atomic.mobius(0)

    def test_scope(self) -> None:
        result = complete_beta_atomic.run()
        disposition = result["disposition"]
        self.assertEqual(disposition["raw_complete_jordan_premise"], "refuted")
        self.assertIn("vacuous", disposition["raw_landau_implication"])
        self.assertIn("sufficient", disposition["fixed_mollified_density_premise"])
        self.assertFalse(disposition["rh_proved"])
        self.assertEqual(result["lower_bound"]["growth"], "Omega(sqrt(Y))")
        self.assertEqual(
            result["lower_bound"]["squarefree_subsum_lead_at_x=Y/32"],
            "(70+50*sqrt(2))/pi^2*sqrt(Y)",
        )

    def test_display_math_delimiters_are_balanced(self) -> None:
        depth = 0
        for line in NOTE_PATH.read_text(encoding="utf-8").splitlines():
            if line == r"\[":
                depth += 1
                self.assertEqual(depth, 1)
            elif line == r"\]":
                depth -= 1
                self.assertGreaterEqual(depth, 0)
        self.assertEqual(depth, 0)

    def test_resource_caps(self) -> None:
        caps = complete_beta_atomic.run()["resource_caps"]
        self.assertEqual(caps["source_families_enumerated"], 0)
        self.assertEqual(caps["conductors_enumerated"], 0)
        self.assertEqual(caps["curves_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
