from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_full_rational_place_notch.py"
)
NOTE_PATH = MODULE_PATH.with_name("QUADRATIC_FAMILY_FULL_RATIONAL_PLACE_NOTCH.md")
SPEC = importlib.util.spec_from_file_location("full_place_notch", MODULE_PATH)
assert SPEC and SPEC.loader
full_place_notch = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(full_place_notch)


class QuadraticFamilyFullRationalPlaceNotchTest(unittest.TestCase):
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

    def test_zeta_numerator_has_only_even_coefficients(self) -> None:
        for q in full_place_notch.Q_PANELS:
            coefficients = full_place_notch.zeta_numerator_coefficients(q)
            self.assertEqual(len(coefficients), q)
            self.assertTrue(all(coefficients[index] == 0 for index in range(1, q, 2)))
            self.assertEqual(
                coefficients[-1],
                (full_place_notch.orientation_sign(q) * q) ** ((q - 1) // 2),
            )

    def test_every_odd_degree_correlation_vanishes(self) -> None:
        for q in full_place_notch.Q_PANELS:
            for degree in range(1, 18, 2):
                self.assertEqual(full_place_notch.full_place_correlation(q, degree), 0)

    def test_direct_prime_controls(self) -> None:
        for prime, lower, upper in full_place_notch.DIRECT_PANELS:
            for degree in range(lower, upper + 1):
                self.assertEqual(
                    full_place_notch.direct_prime_correlation(prime, degree),
                    full_place_notch.full_place_correlation(prime, degree),
                )

    def test_first_even_coefficients(self) -> None:
        for q in full_place_notch.Q_PANELS:
            sign = full_place_notch.orientation_sign(q)
            genus = (q - 1) // 2
            self.assertEqual(full_place_notch.full_place_correlation(q, 0), 1)
            expected_degree_two = genus * sign * q + q - q
            self.assertEqual(
                full_place_notch.full_place_correlation(q, 2),
                expected_degree_two,
            )

    def test_guards_and_caps(self) -> None:
        with self.assertRaises(ValueError):
            full_place_notch.orientation_sign(15)
        with self.assertRaises(ValueError):
            full_place_notch.full_place_correlation(3, -1)
        caps = full_place_notch.run()["resource_caps"]
        self.assertLessEqual(caps["candidate_polynomials"], 600)
        self.assertEqual(caps["extension_field_elements_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
