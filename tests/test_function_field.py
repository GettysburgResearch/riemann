"""Independent exact checks for the small function-field pilot."""

from __future__ import annotations

import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOT_DIR = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(PILOT_DIR))

import pilot  # noqa: E402


class PolynomialArithmeticTests(unittest.TestCase):
    def test_exact_division_and_gcd(self) -> None:
        q = 5
        a = (1, 1)
        b = (2, 0, 1)
        c = (3, 1)
        product = pilot.multiply(a, b, q)
        quotient, remainder = pilot.divmod_poly(product, a, q)
        self.assertEqual((quotient, remainder), (b, ()))
        self.assertEqual(
            pilot.gcd_poly(product, pilot.multiply(a, c, q), q),
            a,
        )

    def test_factorization_moebius_and_squarefree(self) -> None:
        q = 5
        linear_a = (1, 1)
        linear_b = (2, 1)
        squarefree = pilot.multiply(linear_a, linear_b, q)
        square = pilot.multiply(linear_a, linear_a, q)
        self.assertEqual(pilot.factor_monic(squarefree, q), (linear_a, linear_b))
        self.assertEqual(pilot.moebius_polynomial(squarefree, q), 1)
        self.assertTrue(pilot.is_squarefree(squarefree, q))
        self.assertEqual(pilot.moebius_polynomial(square, q), 0)
        self.assertFalse(pilot.is_squarefree(square, q))

    def test_enumeration_guard(self) -> None:
        with self.assertRaisesRegex(ValueError, "refusing to enumerate"):
            list(pilot.monic_polynomials(5, 8))


class CharacterAndDetectorTests(unittest.TestCase):
    conductor = (0, 4, 2, 1)  # T^3 + 2*T^2 + 4*T
    q = 5

    def test_character_is_multiplicative_and_zero_on_conductor_factor(self) -> None:
        f = (1, 1)
        g = (2, 1)
        self.assertEqual(
            pilot.quadratic_character(self.conductor, pilot.multiply(f, g, self.q), self.q),
            pilot.quadratic_character(self.conductor, f, self.q)
            * pilot.quadratic_character(self.conductor, g, self.q),
        )
        self.assertEqual(pilot.quadratic_character(self.conductor, (0, 1), self.q), 0)

    def test_q5_geometric_character_is_periodic_mod_conductor(self) -> None:
        for f in pilot.monic_polynomials(self.q, 2):
            lifted = pilot.add(f, self.conductor, self.q)
            self.assertEqual(
                pilot.quadratic_character(self.conductor, f, self.q),
                pilot.quadratic_character(self.conductor, lifted, self.q),
            )

    def test_direct_euler_reciprocal_identity(self) -> None:
        l_coeffs = pilot.l_coefficients(self.conductor, self.q)
        direct = pilot.reciprocal_coefficients_direct(self.conductor, self.q, 3)
        formal = pilot.reciprocal_coefficients_formal(l_coeffs, 3)
        self.assertEqual(l_coeffs, (1, -2, 5))
        self.assertEqual(direct, (1, 2, -1, -12))
        self.assertEqual(direct, formal)
        self.assertEqual(pilot.convolution_identity(l_coeffs, direct), (1, 0, 0, 0))

    def test_critical_normalization_is_exact(self) -> None:
        h1 = pilot.normalized_reciprocal(2, 1, self.q)
        h2 = pilot.normalized_reciprocal(-1, 2, self.q)
        self.assertEqual(h1.rational, 0)
        self.assertEqual(h1.sqrt_coefficient, Fraction(2, 5))
        self.assertEqual(h2.rational, Fraction(-1, 5))
        self.assertEqual((h1 * h2).sqrt_coefficient, Fraction(-2, 25))

    def test_invalid_conductors_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "odd degree"):
            pilot.validate_conductor((1, 0, 1), self.q)
        with self.assertRaisesRegex(ValueError, "squarefree"):
            pilot.validate_conductor((1, 3, 3, 1), self.q)  # (T+1)^3


class FrozenFamilyFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = pilot.build_fixture()

    def test_exhaustive_family_separates_average_from_members(self) -> None:
        statistics = self.fixture["family_statistics"]
        self.assertEqual(self.fixture["family"]["member_count"], 100)
        self.assertEqual(statistics["mean_B1_times_B2"], [0, 1])
        self.assertEqual(
            (
                statistics["negative_member_count"],
                statistics["zero_member_count"],
                statistics["positive_member_count"],
            ),
            (40, 20, 40),
        )
        self.assertLess(self.fixture["witnesses"]["negative"]["signed_lag_one_numerator_B1_B2"], 0)
        self.assertGreater(self.fixture["witnesses"]["positive"]["signed_lag_one_numerator_B1_B2"], 0)

    def test_fixture_builder_rejects_nonfrozen_scans(self) -> None:
        with self.assertRaisesRegex(ValueError, "requires exactly"):
            pilot.build_fixture(q=7)

    def test_every_cubic_member_has_exact_root_modulus_certificate(self) -> None:
        self.assertTrue(
            self.fixture["exact_checks"]["genus_one_root_modulus_certificates_for_every_member"]
        )

    def test_checked_in_fixture_is_exact_generator_output(self) -> None:
        stored = json.loads((PILOT_DIR / "fixtures.json").read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)


if __name__ == "__main__":
    unittest.main()
