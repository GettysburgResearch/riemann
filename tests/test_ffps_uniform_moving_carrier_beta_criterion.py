from __future__ import annotations

import cmath
import importlib.util
import json
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_uniform_moving_carrier_beta_criterion.py"
)
SPEC = importlib.util.spec_from_file_location("uniform_moving_carrier", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load uniform moving-carrier producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class UniformMovingCarrierBetaCriterionTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_atom_laplace_matches_direct_quadrature_formula(self) -> None:
        for tilt in (1.0, 2.0, 8.0):
            for value in (0.1 + 0.2j, 0.49 + 3.0j):
                direct = (
                    tilt
                    * (cmath.exp(tilt - value) - 1.0)
                    / ((math.exp(tilt) - 1.0) * (tilt - value))
                )
                self.assertAlmostEqual(subject.atom_laplace(tilt, value), direct)

    def test_atom_laplace_fills_removable_value(self) -> None:
        for tilt in (1.0, 2.0, 8.0):
            decay = math.exp(-tilt)
            expected = tilt * decay / (1.0 - decay)
            self.assertAlmostEqual(subject.atom_laplace(tilt, complex(tilt)), expected)

    def test_fourier_modulus_formula(self) -> None:
        for tilt in (1.0, 3.0, 10.0):
            for frequency in (0.0, 0.3, 2.0, 7.0):
                direct = abs(subject.atom_laplace(tilt, 1j * frequency)) ** 2
                exact = subject.atom_fourier_modulus_squared(tilt, frequency)
                self.assertAlmostEqual(direct, exact, places=13)
                self.assertLessEqual(exact, 1.0 + 1.0e-14)
                self.assertGreaterEqual(
                    exact + 1.0e-14,
                    1.0 / (1.0 + (frequency / tilt) ** 2),
                )

    def test_carrier_order_limit(self) -> None:
        value = 0.31 + 1.1j
        for tilt in (1.0, 4.0, 32.0):
            limit = subject.limiting_carrier(tilt, value)
            error_16 = abs(subject.carrier(tilt, 16, value) / limit - 1.0)
            error_512 = abs(subject.carrier(tilt, 512, value) / limit - 1.0)
            self.assertLess(error_512, error_16)

    def test_tilt_limit(self) -> None:
        value = 0.4 + 0.7j
        expected = value * cmath.exp(-2.0 * value)
        self.assertLess(
            abs(subject.carrier(64.0, 3, value) / expected - 1.0),
            0.04,
        )

    def test_variation_scale_is_polynomial(self) -> None:
        self.assertLess(subject.regularity_scale(64.0, 8), 1030.0)
        self.assertGreater(subject.regularity_scale(1.0, 1), 3.0)

    def test_universal_real_probability_floor(self) -> None:
        for row in subject.real_floor_rows():
            self.assertGreaterEqual(row["minimum_over_floor"], 1.0 - 1.0e-13)

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_payload_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(
            ledger["universal_probability_derivative_reverse_gate"], "PROVED"
        )
        self.assertEqual(ledger["arbitrary_schedule_reverse_RH_implication"], "PROVED")
        self.assertEqual(ledger["moving_energy_estimate"], "NOT PROVED")
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.atom_laplace(0.5, 0.2 + 0.0j)
        with self.assertRaises(ValueError):
            subject.carrier(1.0, 0, 0.2 + 0.0j)
        with self.assertRaises(ValueError):
            subject.atom_fourier_modulus_squared(1.0, math.inf)


if __name__ == "__main__":
    unittest.main()
