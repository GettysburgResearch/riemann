from __future__ import annotations

import importlib.util
import json
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
    / "function_field_beta_boolean_evaluation_bandpass.py"
)
SPEC = importlib.util.spec_from_file_location(
    "function_field_beta_boolean_evaluation_bandpass", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FunctionFieldBetaBooleanEvaluationBandpassTest(unittest.TestCase):
    def test_frozen_sources_are_pinned(self) -> None:
        subject.check_source_blobs()

    def test_literal_beta_local_factor_is_squared(self) -> None:
        self.assertEqual(subject.beta_local_coefficients(1), (1, -2, 1))
        self.assertEqual(subject.beta_local_coefficients(-1), (1, 2, 1))
        panel = subject.beta_local_panel()
        self.assertEqual(len(panel["rows"]), 2)

    def test_degree_bandpass_has_declared_notch(self) -> None:
        polynomial = subject.bandpass_polynomial(
            (Fraction(1), Fraction(2), Fraction(1)),
            step=1,
            order=2,
            box_length=3,
            box_order=1,
        )
        self.assertEqual(len(polynomial) - 1, 6)
        self.assertEqual(subject.vanishing_order_at_one(polynomial), 2)

    def test_boolean_projector_is_exact_coefficientwise(self) -> None:
        polynomial = subject.bandpass_polynomial((Fraction(1),), step=1, order=1)
        series = subject.a1_boolean_series(
            square_root_q=3,
            exceptional_degree=1,
            conductor_degree=3,
            character_at_exceptional=-1,
            boolean_sign=-1,
            filter_polynomial=polynomial,
            completed_l_polynomial=(Fraction(1), Fraction(0), Fraction(1)),
            coefficient_cap=20,
        )
        for degree in range(21):
            self.assertEqual(
                series["boolean"][degree],
                (series["trivial"][degree] - series["character"][degree]) / 2,
            )

    def test_complete_field_is_finite_and_deletion_only_decays(self) -> None:
        polynomial = subject.bandpass_polynomial((Fraction(1),), step=1, order=1)
        series = subject.a1_boolean_series(
            square_root_q=3,
            exceptional_degree=1,
            conductor_degree=3,
            character_at_exceptional=-1,
            boolean_sign=1,
            filter_polynomial=polynomial,
            completed_l_polynomial=(Fraction(1), Fraction(0), Fraction(1)),
            coefficient_cap=24,
        )
        complete = series["trivial_numerator"]
        deleted = series["trivial"]
        self.assertEqual(len(complete) - 1, 3)
        for degree in range(len(complete), len(deleted)):
            self.assertEqual(deleted[degree], deleted[degree - 3] / 27)

    def test_quadratic_completed_degree_has_parity_correction(self) -> None:
        self.assertEqual(subject.quadratic_completed_degree(9), 8)
        self.assertEqual(subject.quadratic_completed_degree(10), 8)
        self.assertEqual(subject.quadratic_completed_degree(3), 2)
        self.assertEqual(subject.quadratic_completed_degree(4), 2)

    def test_irreducible_degree_counts_are_exact_and_positive(self) -> None:
        self.assertEqual(subject.irreducible_count(3, 1), 3)
        self.assertEqual(subject.irreducible_count(3, 2), 3)
        self.assertEqual(subject.irreducible_count(5, 3), 40)
        for field_size in subject.REPLAY_FIELD_SIZES:
            for degree in subject.REPLAY_CONDUCTOR_DEGREES:
                self.assertGreater(subject.irreducible_count(field_size, degree), 0)

    def test_degree_obstruction_forces_a_surviving_mode(self) -> None:
        polynomial = subject.bandpass_polynomial(
            (Fraction(1), Fraction(2), Fraction(1)),
            step=1,
            order=2,
            box_length=3,
            box_order=1,
        )
        panel = subject.degree_obstruction_panel(polynomial)
        for row in panel["rows"]:
            self.assertGreater(
                row["quadratic_completed_l_degree"], row["filter_degree"]
            )
            self.assertFalse(row["all_frobenius_modes_can_be_cancelled"])

    def test_formal_periodic_control_has_exact_linear_energy_coefficient(self) -> None:
        panel = subject.periodic_control_panel()
        self.assertEqual(Fraction(panel["character_mean_square"]), Fraction(10, 9))
        self.assertEqual(
            Fraction(panel["boolean_energy_leading_coefficient"]), Fraction(5, 18)
        )
        self.assertFalse(panel["arithmetic_modulus_realization_claimed"])

    def test_positive_boolean_average_retains_character_energy(self) -> None:
        panel = subject.boolean_parallelogram_panel()
        self.assertEqual(panel["coefficient_checks"], 21)
        self.assertIn("retains half", panel["verdict"])
        self.assertIn("coherent amplitude", panel["verdict"])

    def test_rational_series_reconstructs_product(self) -> None:
        numerator = (Fraction(1), Fraction(-2), Fraction(1))
        denominator = (Fraction(1), Fraction(0), Fraction(1))
        coefficients = subject.rational_series(numerator, denominator, 20)
        for degree in range(21):
            reconstructed = coefficients[degree]
            if degree >= 2:
                reconstructed += coefficients[degree - 2]
            expected = numerator[degree] if degree < len(numerator) else 0
            self.assertEqual(reconstructed, expected)

    def test_scope_and_resource_firewalls(self) -> None:
        report = subject.run(check_sources=False)
        scope = report["scope_firewalls"]
        self.assertTrue(scope["genuine_incomplete_boolean_restriction"])
        self.assertTrue(scope["all_curve_euler_identity"])
        self.assertTrue(scope["a1_uniform_nonannihilation_for_large_conductor"])
        self.assertFalse(scope["complete_family_result"])
        self.assertFalse(scope["owner_restriction_included"])
        self.assertFalse(scope["incomplete_waveprimcar_proved"])
        self.assertFalse(scope["number_field_inference"])
        self.assertFalse(scope["rh_proved"])
        resources = report["resource_caps"]
        self.assertEqual(resources["polynomials_enumerated"], 0)
        self.assertEqual(resources["curves_enumerated"], 0)
        self.assertEqual(resources["points_enumerated"], 0)
        self.assertEqual(resources["floating_point_operations"], 0)

    def test_canonical_json_fixture(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(json.loads(json.dumps(result)), fixture)

    def test_input_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.beta_local_coefficients(0)
        with self.assertRaises(ValueError):
            subject.bandpass_polynomial((Fraction(0),), step=1, order=1)
        with self.assertRaises(ValueError):
            subject.a1_boolean_series(
                3,
                1,
                3,
                1,
                0,
                (Fraction(1),),
                (Fraction(1),),
                4,
            )
        with self.assertRaises(ValueError):
            subject.rational_series((Fraction(1),), (Fraction(0),), 4)


if __name__ == "__main__":
    unittest.main()
