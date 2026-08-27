from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_spectral_zero_free_carrier_tilt.py"
)
SPEC = importlib.util.spec_from_file_location("spectral_zero_free_tilt", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load spectral-zero-free tilt producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class SpectralZeroFreeCarrierTiltTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_centered_beta_polynomials(self) -> None:
        self.assertEqual(
            subject.centered_beta_polynomial(1),
            (Fraction(1), Fraction(0), Fraction(-1)),
        )
        self.assertEqual(
            subject.centered_beta_polynomial(2),
            (Fraction(1), Fraction(0), Fraction(-2), Fraction(0), Fraction(1)),
        )

    def test_ordinary_legendre_polynomials(self) -> None:
        self.assertEqual(
            subject.ordinary_legendre_polynomial(1),
            (Fraction(0), Fraction(1)),
        )
        self.assertEqual(
            subject.ordinary_legendre_polynomial(2),
            (Fraction(-1, 2), Fraction(0), Fraction(3, 2)),
        )
        self.assertEqual(
            subject.ordinary_legendre_polynomial(3),
            (Fraction(0), Fraction(-3, 2), Fraction(0), Fraction(5, 2)),
        )

    def test_matched_rodrigues_identity(self) -> None:
        for rung in range(1, 7):
            derivative = subject.polynomial_derivative(
                subject.centered_beta_polynomial(rung), rung
            )
            expected = tuple(
                Fraction(subject.rodrigues_factor(rung)) * value
                for value in subject.ordinary_legendre_polynomial(rung)
            )
            self.assertEqual(derivative, expected)

    def test_tilt_first_variation_identity(self) -> None:
        for rung in range(1, 7):
            derivative = subject.polynomial_derivative(
                subject.multiply_by_x(subject.centered_beta_polynomial(rung)),
                rung,
            )
            expected = tuple(
                Fraction(subject.rodrigues_factor(rung)) * value
                for value in subject.ordinary_legendre_polynomial(rung + 1)
            )
            self.assertEqual(derivative, expected)

    def test_centered_beta_moments(self) -> None:
        self.assertEqual(subject.centered_beta_even_moment(1, 0), 1)
        self.assertEqual(subject.centered_beta_even_moment(1, 1), Fraction(1, 5))
        self.assertEqual(subject.centered_beta_even_moment(1, 2), Fraction(3, 35))
        self.assertEqual(subject.centered_beta_even_moment(2, 1), Fraction(1, 7))

    def test_phi_series(self) -> None:
        self.assertEqual(
            subject.phi_even_series_coefficients(1, 3),
            (Fraction(1), Fraction(1, 10), Fraction(1, 280), Fraction(1, 15120)),
        )

    def test_exact_energy_curvature_ratio(self) -> None:
        for rung in range(1, 7):
            detector = subject.polynomial_derivative(
                subject.centered_beta_polynomial(rung), rung
            )
            variation = subject.polynomial_derivative(
                subject.multiply_by_x(subject.centered_beta_polynomial(rung)),
                rung,
            )
            detector_norm = subject.symmetric_polynomial_integral(
                subject.polynomial_product(detector, detector)
            )
            variation_norm = subject.symmetric_polynomial_integral(
                subject.polynomial_product(variation, variation)
            )
            self.assertEqual(
                variation_norm / detector_norm, subject.curvature_ratio(rung)
            )

    def test_first_curvature_ratios(self) -> None:
        self.assertEqual(
            [subject.curvature_ratio(rung) for rung in range(1, 4)],
            [Fraction(3, 5), Fraction(5, 7), Fraction(7, 9)],
        )

    def test_first_rung_exact_energy_series(self) -> None:
        self.assertEqual(
            subject.first_rung_scaled_energy_series(8),
            (
                Fraction(12),
                Fraction(0),
                Fraction(36, 5),
                Fraction(0),
                Fraction(72, 175),
                Fraction(0),
                Fraction(-4, 315),
                Fraction(0),
                Fraction(204, 336875),
            ),
        )

    def test_sharp_support_two_energy(self) -> None:
        self.assertEqual(
            subject.optimal_energy_support_two_from_polynomial(1),
            Fraction(3, 2),
        )
        self.assertEqual(
            subject.optimal_energy_support_two_from_polynomial(2),
            Fraction(45, 2),
        )
        for rung in range(1, 7):
            self.assertEqual(
                subject.optimal_energy_support_two_from_polynomial(rung),
                Fraction(subject.sharp_energy_constant(rung), 2 ** (2 * rung + 1)),
            )

    def test_vertical_line_logic(self) -> None:
        self.assertFalse(
            subject.zero_free_vertical_line_from_imaginary_zero_locus(Fraction(0))
        )
        for tilt in (Fraction(-2), Fraction(-1, 10), Fraction(1, 10), Fraction(2)):
            self.assertTrue(
                subject.zero_free_vertical_line_from_imaginary_zero_locus(tilt)
            )

    def test_laplace_orientation(self) -> None:
        self.assertEqual(
            subject.laplace_zero_line_real_part(Fraction(3), Fraction(2)),
            Fraction(-3),
        )
        self.assertEqual(
            subject.laplace_zero_line_real_part(Fraction(-3), Fraction(2)),
            Fraction(3),
        )
        self.assertTrue(subject.closed_right_half_plane_zero_free(Fraction(1)))
        self.assertFalse(subject.closed_right_half_plane_zero_free(Fraction(0)))
        self.assertFalse(subject.closed_right_half_plane_zero_free(Fraction(-1)))

    def test_external_input_is_explicit(self) -> None:
        payload = subject.run()
        external = payload["classical_external_input"]
        self.assertEqual(external["url"], "https://dlmf.nist.gov/10.21#i")
        self.assertFalse(external["computational_reproof_claimed"])

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_payload_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(
            ledger["all_nonzero_Phi_zeros_purely_imaginary"],
            "CLASSICAL EXTERNAL THEOREM",
        )
        self.assertEqual(
            ledger["real_Fourier_zero_free_for_nonzero_tilt"],
            "PROVED FROM CLASSICAL INPUT",
        )
        self.assertEqual(ledger["zero_free_class_same_infimum_not_attained"], "PROVED")
        self.assertEqual(ledger["Laplace_zero_line_and_orientation"], "PROVED")
        self.assertEqual(ledger["new_beta_convolution_cancellation"], "NOT PROVED")
        self.assertEqual(
            ledger["uniform_condition_number_improvement_from_real_zero_freeness"],
            "DISPROVED IN THIS ENERGY CLASS",
        )
        self.assertEqual(ledger["subpower_detector_estimate_RH_or_GRH"], "NOT PROVED")

    def test_resource_caps(self) -> None:
        caps = subject.run()["resource_caps"]
        self.assertEqual(caps["beta_terms"], 0)
        self.assertEqual(caps["Bessel_root_searches"], 0)
        self.assertEqual(caps["quadratures"], 0)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.centered_beta_polynomial(0)
        with self.assertRaises(ValueError):
            subject.polynomial_derivative((Fraction(1),), -1)
        with self.assertRaises(ValueError):
            subject.ordinary_legendre_polynomial(-1)
        with self.assertRaises(ValueError):
            subject.centered_beta_even_moment(1, -1)
        with self.assertRaises(ValueError):
            subject.phi_even_series_coefficients(1, -1)
        with self.assertRaises(ValueError):
            subject.curvature_ratio(0)
        with self.assertRaises(ValueError):
            subject.first_rung_scaled_energy_series(-1)
        with self.assertRaises(ValueError):
            subject.divide_series_after_common_zero(
                (Fraction(0), Fraction(1)),
                (Fraction(1),),
                1,
            )
        with self.assertRaises(ValueError):
            subject.laplace_zero_line_real_part(Fraction(1), Fraction(0))


if __name__ == "__main__":
    unittest.main()
