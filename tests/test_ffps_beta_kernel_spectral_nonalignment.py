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
    / "ffps_beta_kernel_spectral_nonalignment.py"
)
SPEC = importlib.util.spec_from_file_location("beta_kernel_nonalignment", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class BetaKernelSpectralNonalignmentTest(unittest.TestCase):
    def test_source_blobs(self) -> None:
        subject.check_source_blobs()

    def test_boundary_shift_coefficients(self) -> None:
        self.assertEqual(
            subject.boundary_shift_coefficients(),
            (
                (Fraction(1), Fraction(0)),
                (Fraction(-2), Fraction(-2)),
                (Fraction(3), Fraction(4)),
                (Fraction(-4), Fraction(-2)),
                (Fraction(2), Fraction(0)),
            ),
        )

    def test_tail_transform_factorization(self) -> None:
        self.assertEqual(
            subject.tail_common_numerator(), subject.factored_tail_numerator()
        )
        self.assertEqual(
            subject.tail_common_numerator(),
            (Fraction(-3), Fraction(-7), Fraction(10)),
        )

    def test_frozen_and_scaled_zero_orders(self) -> None:
        self.assertEqual(subject.frozen_boundary_amplitude_order(0), 0)
        self.assertEqual(subject.frozen_boundary_amplitude_order(7), 2)
        self.assertEqual(subject.scaled_channel_amplitude_order(0), 1)
        self.assertEqual(subject.scaled_channel_amplitude_order(-7), 3)
        with self.assertRaises(TypeError):
            subject.frozen_boundary_amplitude_order(Fraction(1, 2))

    def test_window_scale_certificates(self) -> None:
        for height in subject.WINDOW_REPLAY_HEIGHTS:
            certificate = subject.window_certificate(height)
            self.assertTrue(certificate["scaled_height_below_one"])
            self.assertTrue(certificate["carrier_zero_free_open_rh_strip"])
            self.assertLess(subject.window_scale(height) * height, 1)
        self.assertEqual(subject.window_scale(Fraction(10)), Fraction(1, 11))
        with self.assertRaises(ValueError):
            subject.window_scale(Fraction(0))
        with self.assertRaises(ValueError):
            subject.window_scale(1)  # type: ignore[arg-type]

    def test_two_channel_lattices_have_no_bounded_nonzero_collision(self) -> None:
        self.assertEqual(subject.bounded_nonzero_lattice_intersections(), 0)
        for left in range(-32, 33):
            for right in range(-32, 33):
                if left or right:
                    self.assertFalse(subject.sqrt_two_integer_relation(left, right))
        self.assertTrue(subject.sqrt_two_integer_relation(0, 0))
        with self.assertRaises(ValueError):
            subject.bounded_nonzero_lattice_intersections(0)

    def test_universal_kernel_has_zero_mass(self) -> None:
        left, right = subject.universal_piece_integrals()
        self.assertEqual(left, 1)
        self.assertEqual(right, -1)
        self.assertEqual(left + right, 0)

    def test_universal_weight_has_only_the_forced_sampled_zero(self) -> None:
        self.assertEqual(subject.universal_weight(0.0), 0.0)
        for sample in subject.UNIVERSAL_WEIGHT_SAMPLES:
            self.assertGreater(subject.universal_weight(float(sample)), 0.0)
        with self.assertRaises(ValueError):
            subject.universal_weight(float("inf"))

    def test_canonical_scope(self) -> None:
        result = subject.run(check_sources=False)
        self.assertTrue(result["scope"]["exact_transform_and_zero_classification"])
        self.assertFalse(result["scope"]["zero_dependent_kernel_choice"])
        self.assertFalse(result["scope"]["zeta_zero_computation"])
        self.assertFalse(result["scope"]["perron_bound_proved"])
        self.assertFalse(result["scope"]["simplicity_proved"])
        self.assertFalse(result["scope"]["rh_proved"])
        self.assertFalse(result["scope"]["grh_proved"])
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)
        self.assertIn(
            "vector/direct-sum",
            result["global_direct_sum_repair"]["scope"],
        )


if __name__ == "__main__":
    unittest.main()
