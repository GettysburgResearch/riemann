from __future__ import annotations

import importlib.util
import json
import math
import unittest
from fractions import Fraction
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_higher_derivative_carrier_hierarchy.py"
)
SPEC = importlib.util.spec_from_file_location("higher_derivative_hierarchy", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load higher-derivative carrier producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class HigherDerivativeCarrierHierarchyTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_carrier_mass_and_endpoint_notch(self) -> None:
        support = Fraction(3)
        for rung in range(1, 7):
            carrier = subject.carrier_polynomial(rung, support)
            self.assertEqual(subject.polynomial_integral(carrier, support), 1)
            for derivative_order in range(rung):
                derivative = subject.polynomial_derivative(carrier, derivative_order)
                self.assertEqual(subject.polynomial_value(derivative, Fraction(0)), 0)
                self.assertEqual(subject.polynomial_value(derivative, support), 0)

    def test_rodrigues_legendre_identity(self) -> None:
        support = Fraction(2)
        for rung in range(1, 7):
            detector = subject.detector_polynomial(rung, support)
            factor = subject.detector_legendre_factor(rung, support)
            expected = tuple(
                factor * value
                for value in subject.shifted_legendre_polynomial(rung, support)
            )
            self.assertEqual(detector, expected)

    def test_carrier_moment_formula(self) -> None:
        support = Fraction(2)
        for rung in range(1, 7):
            carrier = subject.carrier_polynomial(rung, support)
            for order in range(4):
                weighted = (Fraction(0),) * order + carrier
                self.assertEqual(
                    subject.polynomial_integral(weighted, support),
                    subject.carrier_moment(rung, order, support),
                )

    def test_detector_moment_notch(self) -> None:
        support = Fraction(2)
        for rung in range(1, 7):
            detector = subject.detector_polynomial(rung, support)
            for order in range(rung + 4):
                weighted = (Fraction(0),) * order + detector
                self.assertEqual(
                    subject.polynomial_integral(weighted, support),
                    subject.detector_moment(rung, order, support),
                )
            self.assertEqual(
                subject.detector_moment(rung, rung, support),
                Fraction((-1) ** rung * math.factorial(rung)),
            )

    def test_detector_norm_and_sharp_constant(self) -> None:
        support = Fraction(2)
        for rung in range(1, 7):
            detector = subject.detector_polynomial(rung, support)
            norm = subject.polynomial_integral(
                subject.polynomial_product(detector, detector), support
            )
            self.assertEqual(norm, subject.detector_norm_squared(rung, support))
            self.assertEqual(
                norm * support ** (2 * rung + 1),
                subject.sharp_energy_constant(rung),
            )

    def test_first_sharp_constants(self) -> None:
        self.assertEqual(
            [subject.sharp_energy_constant(rung) for rung in range(1, 4)],
            [12, 720, 100800],
        )
        for rung in range(1, 7):
            self.assertEqual(
                subject.higher_legendre_energy_constant(rung, 0),
                subject.sharp_energy_constant(rung),
            )
        self.assertEqual(subject.higher_legendre_energy_constant(1, 1), 720)

    def test_moment_transform_diagonal(self) -> None:
        support = Fraction(2)
        for rung in range(1, 7):
            for extra_order in range(4):
                coefficients = subject.moment_transform_coefficients(
                    rung, extra_order, support
                )
                expected = Fraction(
                    (-1) ** rung
                    * math.factorial(rung)
                    * math.comb(rung + extra_order, rung)
                )
                self.assertEqual(coefficients[-1], expected)

    def test_first_transform_rows(self) -> None:
        support = Fraction(2)
        self.assertEqual(
            subject.moment_transform_coefficients(1, 0, support),
            (Fraction(-1),),
        )
        self.assertEqual(
            subject.moment_transform_coefficients(1, 1, support),
            (Fraction(-2), Fraction(-2)),
        )
        self.assertEqual(
            subject.moment_transform_coefficients(2, 1, support),
            (Fraction(6), Fraction(6)),
        )

    def test_autocorrelation_and_spectral_sign(self) -> None:
        beta_prefix = Fraction(3)
        for rung in range(1, 7):
            autocorrelation = subject.autocorrelation_first_available_moment(
                rung, beta_prefix
            )
            spectral = subject.spectral_first_available_derivative(rung, beta_prefix)
            self.assertEqual(spectral, (-1) ** rung * autocorrelation)
            self.assertGreater(spectral, 0)

    def test_critical_width_phase(self) -> None:
        for rung in range(1, 7):
            critical = subject.critical_width_power(rung)
            self.assertTrue(subject.forward_paid(rung, Fraction(critical)))
            self.assertTrue(subject.reverse_paid(rung, Fraction(critical)))
            self.assertTrue(subject.forward_paid(rung, Fraction(critical - 1)))
            self.assertFalse(subject.reverse_paid(rung, Fraction(critical - 1)))
            self.assertFalse(subject.forward_paid(rung, Fraction(critical + 1)))
            self.assertTrue(subject.reverse_paid(rung, Fraction(critical + 1)))

    def test_trivial_dilution_meets_one_line(self) -> None:
        for rung in range(1, 7):
            escape = subject.trivial_dilution_exponent(rung, Fraction(0))
            self.assertEqual(escape, Fraction(1, subject.critical_width_power(rung)))
            self.assertEqual(subject.zero_exclusion_boundary(rung, escape), 1)

    def test_variation_constant_is_positive(self) -> None:
        values = [subject.variation_scale_constant_bound(rung) for rung in range(1, 7)]
        self.assertEqual(values[0], 30)
        self.assertTrue(all(left < right for left, right in pairwise(values)))

    def test_condition_number_and_growing_rung_factor(self) -> None:
        self.assertEqual(
            subject.support_condition_number(1, Fraction(4), Fraction(2)), 8
        )
        self.assertEqual(
            subject.support_condition_number(2, Fraction(4), Fraction(2)), 32
        )
        self.assertEqual(
            subject.normalized_forward_factor(1, Fraction(4), Fraction(2)),
            1200,
        )

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_payload_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(
            ledger["all_support_fixed_rung_renormalized_RH_equivalence"], "PROVED"
        )
        self.assertEqual(ledger["critical_width_power_within_current_bounds"], "PROVED")
        self.assertEqual(ledger["unique_signed_carrier_variational_optimum"], "PROVED")
        self.assertEqual(ledger["complete_higher_rung_Legendre_tower"], "PROVED")
        self.assertEqual(ledger["exact_support_condition_number"], "PROVED")
        self.assertEqual(
            ledger["normalized_safe_growing_rung_RH_equivalence"], "PROVED"
        )
        self.assertEqual(
            ledger["supercritical_adaptive_schedule_obstruction"], "PROVED"
        )
        self.assertEqual(
            ledger["new_unconditional_subpower_beta_energy_estimate"], "NOT PROVED"
        )
        self.assertEqual(
            ledger["unrestricted_growing_rung_forward_or_equivalence"],
            "NOT PROVED",
        )
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.carrier_normalization(0, Fraction(1))
        with self.assertRaises(ValueError):
            subject.carrier_normalization(1, Fraction(0))
        with self.assertRaises(ValueError):
            subject.polynomial_derivative((Fraction(1),), -1)
        with self.assertRaises(ValueError):
            subject.polynomial_integral((Fraction(1),), Fraction(-1))
        with self.assertRaises(ValueError):
            subject.carrier_moment(1, -1, Fraction(1))
        with self.assertRaises(ValueError):
            subject.detector_moment(1, -1, Fraction(1))
        with self.assertRaises(ValueError):
            subject.moment_transform_coefficients(1, -1, Fraction(1))
        with self.assertRaises(ValueError):
            subject.higher_legendre_energy_constant(1, -1)
        with self.assertRaises(ValueError):
            subject.forward_paid(1, Fraction(-1))
        with self.assertRaises(ValueError):
            subject.reverse_paid(1, Fraction(-1))
        with self.assertRaises(ValueError):
            subject.trivial_dilution_exponent(1, Fraction(3))
        with self.assertRaises(ValueError):
            subject.zero_exclusion_boundary(1, Fraction(-1))
        with self.assertRaises(ValueError):
            subject.support_condition_number(1, Fraction(1), Fraction(2))
        with self.assertRaises(ValueError):
            subject.normalized_forward_factor(1, Fraction(1), Fraction(0))


if __name__ == "__main__":
    unittest.main()
