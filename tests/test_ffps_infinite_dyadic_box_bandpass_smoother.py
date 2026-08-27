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
    / "ffps_infinite_dyadic_box_bandpass_smoother.py"
)
SPEC = importlib.util.spec_from_file_location("infinite_dyadic_smoother", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class InfiniteDyadicBoxBandpassSmootherTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_contract()

    def test_partial_width_and_probability_mass(self) -> None:
        for levels in range(1, subject.PARTIAL_LEVEL_CAP + 1):
            expected_width = Fraction(1) - Fraction(1, 2**levels)
            self.assertEqual(subject.partial_total_width(levels), expected_width)
            self.assertEqual(sum(subject.discrete_dyadic_smoother(levels)), 1)

    def test_partial_laplace_linear_coefficient(self) -> None:
        for levels in range(1, subject.PARTIAL_LEVEL_CAP + 1):
            series = subject.partial_laplace_series(levels, 2)
            self.assertEqual(series[0], 1)
            self.assertEqual(series[1], -subject.partial_total_width(levels) / 2)

    def test_dyadic_smoothing_preserves_exact_notch(self) -> None:
        smoother = subject.discrete_dyadic_smoother(subject.PARTIAL_LEVEL_CAP)
        for order in range(1, subject.REPLAY_ORDER_CAP + 1):
            bandpass = subject.convolve(
                subject.finite_difference(subject.TOY_BOUNDARY_KERNEL, order),
                smoother,
            )
            kernel_moments = subject.moments(bandpass, order)
            self.assertEqual(kernel_moments[:order], (Fraction(0),) * order)
            self.assertNotEqual(kernel_moments[order], 0)
            correlation_moments = subject.correlation_moments(
                subject.autocorrelation(bandpass), 2 * order
            )
            self.assertEqual(
                correlation_moments[: 2 * order], (Fraction(0),) * (2 * order)
            )
            self.assertNotEqual(correlation_moments[2 * order], 0)

    def test_exact_binary_envelope_exponent(self) -> None:
        for binary_scale in range(3, subject.ENVELOPE_EXPONENT_CAP + 1):
            self.assertEqual(
                subject.envelope_binary_exponent(binary_scale),
                -((binary_scale - 1) * (binary_scale - 2) // 2),
            )

    def test_scope_fences(self) -> None:
        result = subject.run(check_sources=False)
        self.assertTrue(result["infinite_smoother"]["probability_density"])
        self.assertTrue(result["infinite_smoother"]["right_half_plane_zero_free"])
        self.assertTrue(result["fixed_bandpass"]["rh_equivalent_energy"])
        self.assertFalse(result["fixed_bandpass"]["estimate_proved"])
        self.assertTrue(result["scope"]["fixed_parameters"])
        self.assertFalse(result["scope"]["horizon_dependent_filter"])
        self.assertFalse(result["scope"]["low_frequency_estimate"])
        self.assertFalse(result["scope"]["rh_or_grh_proved"])
        self.assertTrue(result["scope"]["theta_fixed_in_open_interval_zero_one_half"])
        self.assertIn(
            "exp((log X)^(1/2+theta))", result["spectral_tail"]["subpower_cutoff"]
        )
        self.assertIn("X^(-A)", result["spectral_tail"]["superpower_tail"])
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.dyadic_width(0)
        with self.assertRaises(ValueError):
            subject.discrete_dyadic_smoother(subject.PARTIAL_LEVEL_CAP + 1)
        with self.assertRaises(ValueError):
            subject.finite_difference((Fraction(1),), 0)
        with self.assertRaises(ValueError):
            subject.envelope_binary_exponent(2)


if __name__ == "__main__":
    unittest.main()
