"""Independent exact checks for the frozen genus-two function-field pilot."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOT_DIR = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(PILOT_DIR))

import genus2_pilot  # noqa: E402
import pilot  # noqa: E402


class ExactF9AndPointCountTests(unittest.TestCase):
    def test_f9_model_is_a_field_with_expected_square_multiplicities(self) -> None:
        elements = genus2_pilot.f9_elements()
        self.assertEqual(len(elements), 9)
        self.assertEqual(genus2_pilot.f9_multiply((0, 1), (0, 1)), (2, 0))
        for value in elements:
            self.assertEqual(genus2_pilot.f9_add(value, (0, 0)), value)
        for value in elements[1:]:
            powers = (1, 0)
            for _ in range(8):
                powers = genus2_pilot.f9_multiply(powers, value)
            self.assertEqual(powers, (1, 0))

        multiplicities = {
            value: sum(
                genus2_pilot.f9_multiply(root, root) == value for root in elements
            )
            for value in elements
        }
        self.assertEqual(sorted(multiplicities.values()), [0, 0, 0, 0, 1, 2, 2, 2, 2])

    def test_three_point_count_reconstructions(self) -> None:
        examples = {
            (0, 2, 0, 0, 0, 1): ((4, 6), (1, 0, -2, 0, 9)),
            (1, 0, 0, 0, 0, 1): ((4, 10), (1, 0, 0, 0, 9)),
            (1, 0, 2, 0, 0, 1): ((5, 9), (1, 1, 0, 3, 9)),
        }
        for conductor, (counts, expected_l) in examples.items():
            n1 = genus2_pilot.point_count_f3(conductor)
            n2 = genus2_pilot.point_count_f9(conductor)
            self.assertEqual((n1, n2), counts)
            self.assertEqual(genus2_pilot.l_polynomial_from_point_counts(n1, n2), expected_l)
            self.assertEqual(pilot.l_coefficients(conductor, 3), expected_l)


class AlgebraAndCertificateTests(unittest.TestCase):
    def test_hankel_minor_has_genus_two_closed_form(self) -> None:
        q, a, b = 3, 2, 4
        l_coefficients = (1, a, b, q * a, q * q)
        reciprocal = pilot.reciprocal_coefficients_formal(l_coefficients, 4)
        self.assertEqual(
            genus2_pilot.reciprocal_hankel_numerator(reciprocal),
            q * a * a - b * b,
        )

    def test_integer_purity_certificate_needs_no_approximated_roots(self) -> None:
        certificate = genus2_pilot.purity_certificate((1, 1, 0, 3, 9))
        self.assertEqual(certificate["pair_trace_polynomial_low_to_high"], [-6, 1, 1])
        self.assertEqual(certificate["pair_trace_discriminant"], 25)
        self.assertTrue(certificate["reciprocal_roots_have_modulus_sqrt_q"])
        self.assertTrue(certificate["L_zeros_have_modulus_q_to_minus_one_half"])

        for coefficients in (
            (1, 1, 0, 2, 9),
            (1, 0, -7, 0, 9),
            (1, 0, 7, 0, 9),
        ):
            with self.subTest(coefficients=coefficients):
                hostile = genus2_pilot.purity_certificate(coefficients)
                self.assertFalse(hostile["reciprocal_roots_have_modulus_sqrt_q"])
        for invalid_q in (0, -3, 3.0, True):
            with self.subTest(invalid_q=invalid_q):
                with self.assertRaisesRegex(ValueError, "positive integer"):
                    genus2_pilot.purity_certificate((1, 1, 0, 3, 9), invalid_q)

    def test_twist_involution_is_exact_and_changes_odd_coefficients(self) -> None:
        conductor = (0, 2, 0, 0, 0, 1)
        partner = genus2_pilot.conductor_involution(conductor)
        self.assertEqual(genus2_pilot.conductor_involution(partner), conductor)
        coefficients = pilot.l_coefficients(conductor, 3)
        partner_coefficients = pilot.l_coefficients(partner, 3)
        self.assertEqual(
            partner_coefficients,
            tuple((-1) ** degree * value for degree, value in enumerate(coefficients)),
        )


class FrozenGenusTwoFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = genus2_pilot.build_fixture()

    def test_family_is_the_complete_squarefree_quintic_family(self) -> None:
        family = self.fixture["family"]
        self.assertEqual(family["candidate_count"], 243)
        self.assertEqual(family["member_count"], 162)
        self.assertEqual(family["member_count"], family["expected_squarefree_count"])

    def test_exact_checks_cover_points_euler_reciprocal_purity_and_twist(self) -> None:
        self.assertTrue(all(self.fixture["exact_checks"].values()))

    def test_toy_minor_has_all_three_signs_and_exact_mean(self) -> None:
        statistics = self.fixture["family_statistics"]
        self.assertEqual(
            (
                statistics["negative_member_count"],
                statistics["zero_member_count"],
                statistics["positive_member_count"],
            ),
            (102, 12, 48),
        )
        self.assertEqual(statistics["toy_minor_numerator_mean"], [-104, 27])
        self.assertEqual(statistics["normalized_toy_minor_mean"], [-104, 243])
        self.assertEqual(
            statistics["toy_minor_numerator_histogram"],
            {
                "-24": 6,
                "-22": 12,
                "-16": 6,
                "-13": 6,
                "-9": 6,
                "-6": 12,
                "-4": 24,
                "-1": 30,
                "0": 12,
                "2": 24,
                "3": 6,
                "8": 18,
            },
        )

    def test_witnesses_and_parity_control_are_exact(self) -> None:
        witnesses = self.fixture["witnesses"]
        self.assertEqual(
            witnesses["negative"]["toy_coefficient_hankel_minor_numerator"], -4
        )
        self.assertEqual(witnesses["zero"]["toy_coefficient_hankel_minor_numerator"], 0)
        self.assertEqual(witnesses["positive"]["toy_coefficient_hankel_minor_numerator"], 3)
        statistics = self.fixture["family_statistics"]
        self.assertEqual(statistics["parity_odd_B1_B2_mean"], [0, 1])
        self.assertEqual(
            statistics["parity_odd_B1_B2_sign_counts"],
            {"negative": 54, "zero": 54, "positive": 54},
        )
        self.assertEqual(statistics["twist_involution_fixed_member_count"], 4)

    def test_asymptotic_statement_is_explicitly_only_a_target(self) -> None:
        self.assertEqual(
            self.fixture["asymptotic_target"]["status"],
            "CONJECTURAL_TARGET_NOT_A_THEOREM",
        )
        self.assertIn("not as a theorem", self.fixture["firewall"])

    def test_fixture_builder_rejects_nonfrozen_scans(self) -> None:
        with self.assertRaisesRegex(ValueError, "requires exactly"):
            genus2_pilot.build_fixture(q=5)

    def test_checked_in_fixture_is_exact_generator_output(self) -> None:
        stored = json.loads(
            (PILOT_DIR / "genus2_f3_quintics.json").read_text(encoding="utf-8")
        )
        self.assertEqual(stored, self.fixture)


if __name__ == "__main__":
    unittest.main()
