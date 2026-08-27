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
    / "ffps_spectral_near_notch_conditioning.py"
)
SPEC = importlib.util.spec_from_file_location("spectral_near_notch", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load spectral near-notch producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class SpectralNearNotchConditioningTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_curvature_and_moment(self) -> None:
        self.assertEqual(subject.energy_curvature(1), Fraction(3, 5))
        self.assertEqual(subject.energy_curvature(4), Fraction(9, 11))
        self.assertEqual(subject.centered_second_moment(1), Fraction(1, 5))

    def test_exact_even_notch_jet(self) -> None:
        self.assertEqual(
            subject.normalized_notch_modulus_jet(
                1, Fraction(2), Fraction(3), Fraction(5)
            ),
            (Fraction(4), Fraction(0), Fraction(-113, 60)),
        )

    def test_local_profile(self) -> None:
        self.assertEqual(subject.local_rescaled_profile(Fraction(3), 0), 9)
        self.assertEqual(subject.local_rescaled_profile(Fraction(3), 1), 18)
        self.assertEqual(subject.local_rescaled_profile(Fraction(3), -2), 45)

    def test_pointwise_tradeoff(self) -> None:
        self.assertEqual(subject.notch_floor_per_energy(1, Fraction(9)), 15)
        self.assertEqual(
            subject.energy_per_notch_floor(1, Fraction(9)), Fraction(1, 15)
        )

    def test_compact_band_tradeoff(self) -> None:
        squares = (Fraction(9), Fraction(4), Fraction(25, 4))
        self.assertEqual(subject.compact_band_floor_coefficient(squares), 4)
        self.assertEqual(
            subject.compact_band_condition_product(2, squares), Fraction(5, 28)
        )

    def test_high_notch_powers(self) -> None:
        self.assertEqual(
            [subject.high_notch_derivative_power(m) for m in range(1, 5)],
            [2, 3, 4, 5],
        )
        self.assertEqual(
            [subject.high_notch_squared_condition_power(m) for m in range(1, 5)],
            [4, 6, 8, 10],
        )

    def test_shift_and_quartic_floor_coefficients(self) -> None:
        self.assertEqual(subject.local_minimum_shift_times_root(1), 2)
        inverse_square = Fraction(1, 49)
        self.assertEqual(
            subject.minimum_floor_quartic_ratio(1, inverse_square),
            Fraction(2, 15) - Fraction(20, 3) * inverse_square,
        )
        self.assertEqual(
            subject.old_frequency_quartic_ratio(1, inverse_square),
            Fraction(2, 15) - Fraction(8, 3) * inverse_square,
        )
        self.assertEqual(
            subject.minimum_floor_quartic_ratio(2, inverse_square),
            Fraction(4, 21) - 14 * inverse_square,
        )
        self.assertEqual(
            subject.old_frequency_quartic_ratio(2, inverse_square),
            Fraction(4, 21) - 5 * inverse_square,
        )

    def test_odd_double_factorial(self) -> None:
        self.assertEqual(subject.odd_double_factorial(1), 1)
        self.assertEqual(subject.odd_double_factorial(7), 105)

    def test_first_spherical_roots(self) -> None:
        expected = {
            1: (4.493409457909, 7.725251836938),
            2: (5.763459196895, 9.095011330476),
            3: (6.987932000501, 10.417118547379),
        }
        for rung, wanted in expected.items():
            actual = subject.first_positive_spherical_roots(rung, 2)
            for observed, target in zip(actual, wanted, strict=True):
                self.assertAlmostEqual(observed, target, places=10)

    def test_root_residuals(self) -> None:
        for rung in range(1, 4):
            for root in subject.first_positive_spherical_roots(rung, 2):
                self.assertLess(abs(subject.spherical_bessel_j(rung, root)), 1e-14)
                self.assertGreater(subject.notch_derivative_magnitude(rung, root), 0)

    def test_payload_external_inputs(self) -> None:
        external = subject.run()["classical_external_inputs"]
        self.assertEqual(external[0]["url"], "https://dlmf.nist.gov/10.21#i")
        self.assertEqual(external[1]["url"], "https://dlmf.nist.gov/10.52#ii")

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(ledger["uniform_coercivity_from_zero_freeness"], "DISPROVED")
        self.assertEqual(
            ledger["new_beta_cancellation_or_subpower_estimate"], "NOT PROVED"
        )
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_resource_caps(self) -> None:
        caps = subject.run()["resource_caps"]
        self.assertEqual(caps["numerical_root_rungs"], 3)
        self.assertEqual(caps["numerical_roots_per_rung"], 2)
        self.assertEqual(caps["beta_terms"], 0)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.energy_curvature(0)
        with self.assertRaises(ValueError):
            subject.odd_double_factorial(2)
        with self.assertRaises(ValueError):
            subject.notch_floor_per_energy(1, Fraction(0))
        with self.assertRaises(ValueError):
            subject.compact_band_floor_coefficient(())
        with self.assertRaises(ValueError):
            subject.compact_band_floor_coefficient((Fraction(-1),))
        with self.assertRaises(ValueError):
            subject.first_positive_spherical_roots(1, 0)
        with self.assertRaises(ValueError):
            subject.spherical_bessel_j(1, 0)
        with self.assertRaises(ValueError):
            subject.spherical_bessel_j(-1, 1)
        with self.assertRaises(ValueError):
            subject.minimum_floor_quartic_ratio(1, Fraction(0))


if __name__ == "__main__":
    unittest.main()
