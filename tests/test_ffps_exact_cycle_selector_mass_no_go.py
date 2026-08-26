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
    / "ffps_exact_cycle_selector_mass_no_go.py"
)
SPEC = importlib.util.spec_from_file_location("cycle_selector_mass", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class ExactCycleSelectorMassNoGoTest(unittest.TestCase):
    def test_frozen_source_blobs(self) -> None:
        subject.check_source_blobs()

    def test_determinant_selector_on_every_small_cycle_type(self) -> None:
        for degree in range(1, subject.MAX_CYCLE_DEGREE + 1):
            for cycle_type in subject.partitions(degree):
                self.assertEqual(
                    subject.cycle_selector_trace(cycle_type),
                    Fraction(int(cycle_type == (degree,))),
                )

    def test_unique_hook_coefficients_and_dimensions(self) -> None:
        for degree in range(1, subject.MAX_HOOK_DEGREE + 1):
            rows = subject.hook_rows(degree)
            self.assertEqual(len(rows), degree)
            for k, row in enumerate(rows):
                self.assertEqual(row["cycle_character"], (-1) ** k)
                self.assertEqual(
                    row["selector_coefficient"], str(Fraction((-1) ** k, degree))
                )
                self.assertEqual(row["dimension"], math.comb(degree - 1, k))

    def test_forced_rank_masses(self) -> None:
        for degree in range(2, subject.MAX_HOOK_DEGREE + 1):
            masses = subject.selector_rank_masses(degree)
            self.assertEqual(masses["absolute"], Fraction(2 ** (degree - 1), degree))
            self.assertEqual(masses["positive"], Fraction(2 ** (degree - 2), degree))
            self.assertEqual(masses["negative"], Fraction(2 ** (degree - 2), degree))
            self.assertEqual(masses["integral_numerator_even"], 2 ** (degree - 2))
            self.assertEqual(masses["integral_numerator_odd"], 2 ** (degree - 2))

    def test_product_mass_is_multiplicative(self) -> None:
        self.assertEqual(subject.product_selector_mass((2, 3)), Fraction(4, 3))
        self.assertEqual(subject.product_selector_mass((2, 3, 5)), Fraction(64, 15))

    def test_guards_and_scope(self) -> None:
        with self.assertRaises(ValueError):
            subject.hook_rows(0)
        with self.assertRaises(ValueError):
            subject.cycle_selector_trace(())
        with self.assertRaises(ValueError):
            subject.product_selector_mass(())
        result = subject.run(check_sources=False)
        self.assertFalse(result["ffps_consequence"]["rh_proved"])
        self.assertEqual(result["resource_caps"]["finite_field_points"], 0)
        self.assertEqual(result["resource_caps"]["maximum_cycle_degree"], 10)


if __name__ == "__main__":
    unittest.main()
