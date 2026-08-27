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
    / "function_field_basewave_shadow.py"
)
SPEC = importlib.util.spec_from_file_location("function_field_basewave", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FunctionFieldBasewaveShadowTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_prime_power_and_irreducible_counts(self) -> None:
        self.assertTrue(subject.is_prime_power(4))
        self.assertTrue(subject.is_prime_power(7))
        self.assertFalse(subject.is_prime_power(6))
        self.assertEqual(
            [subject.irreducible_count(3, degree) for degree in range(1, 6)],
            [3, 3, 8, 18, 48],
        )
        self.assertEqual(subject.available_irreducible_count(3, 1, 1), 2)
        with self.assertRaises(ValueError):
            subject.irreducible_count(6, 2)

    def test_log_recurrence_matches_independent_product(self) -> None:
        for field_size in (3, 5, 7):
            with self.subTest(field_size=field_size):
                recurrence = subject.coefficient_table(field_size, 1, 8)
                direct = subject.truncated_euler_product_table(field_size, 1, 8)
                self.assertEqual(recurrence, direct)

    def test_axis_zeta_specialization(self) -> None:
        for field_size, exceptional_degree in ((3, 1), (5, 2), (7, 3)):
            coefficients = subject.coefficient_table(field_size, exceptional_degree, 12)
            for degree in range(13):
                with self.subTest(
                    field_size=field_size,
                    exceptional_degree=exceptional_degree,
                    degree=degree,
                ):
                    expected = subject.axis_coefficient(
                        field_size, exceptional_degree, degree
                    )
                    self.assertEqual(coefficients[degree][0], expected)
                    self.assertEqual(coefficients[0][degree], expected)

    def test_known_diagonal_coefficients(self) -> None:
        coefficients = subject.coefficient_table(3, 1, 12)
        self.assertEqual(
            [coefficients[degree][degree] for degree in range(13)],
            [1, 2, 0, -28, -68, -132, 240, 672, 2532, 3380, -2288, -22368, -81800],
        )

    def test_local_cubic_defect(self) -> None:
        certificate = subject.local_factorization_certificate()
        self.assertEqual(certificate["exact_checks"], 9)
        self.assertEqual(certificate["residual_starts_in_mixed_total_degree"], 3)
        self.assertIn("ab(a+b-ab)", certificate["identity"])

    def test_shell_coordinates_and_exact_quadratic_field_value(self) -> None:
        self.assertEqual(subject.shell_pair(1, 0, 6, -2), (4, 6))
        self.assertEqual(subject.shell_pair(1, 0, 6, 2), (6, 4))
        self.assertEqual(subject.shell_pair(1, 2, 6, 0), (4, 6))
        coefficients = subject.coefficient_table(3, 1, 8)
        shell = subject.complete_shell_amplitude(
            coefficients,
            3,
            1,
            0,
            6,
            subject.CONTROL_WEIGHTS,
        )
        self.assertEqual(
            shell["q_to_height_times_amplitude"],
            {"rational_part": 504, "sqrt_q_part": 48},
        )
        self.assertEqual(len(shell["channels"]), 5)

    def test_full_certificate_scope(self) -> None:
        certificate = subject.run(check_sources=False)
        self.assertEqual(
            certificate["theorem"]["proof_grade"],
            "PROVED BY EXACT EULER FACTORIZATION AND CAUCHY",
        )
        self.assertIn("1-XY", certificate["factorization"]["formula"])
        self.assertEqual(
            certificate["finite_replay"]["recurrence_product_match_degree"], 8
        )
        self.assertEqual(certificate["resource_caps"]["polynomial_enumeration"], 0)
        self.assertFalse(certificate["scope_firewall"]["rh_proved"])
        self.assertFalse(certificate["scope_firewall"]["waveprimcar_proved"])


if __name__ == "__main__":
    unittest.main()
