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
    / "ffps_tilt_endpoint_layer_phase_diagram.py"
)
SPEC = importlib.util.spec_from_file_location("tilt_endpoint_layer", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load tilt endpoint-layer producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class TiltEndpointLayerPhaseDiagramTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_phi_asymptotic_coefficients(self) -> None:
        self.assertEqual(subject.phi_leading_constant(1), Fraction(3, 2))
        self.assertEqual(subject.phi_first_relative_correction(1), -1)
        self.assertEqual(subject.phi_leading_constant(2), Fraction(15, 2))
        self.assertEqual(subject.phi_first_relative_correction(2), -3)

    def test_energy_asymptotic_coefficients(self) -> None:
        self.assertEqual(subject.energy_leading_constant(1), 2)
        self.assertEqual(subject.energy_first_relative_correction(1), Fraction(3, 2))
        self.assertEqual(subject.energy_leading_constant(3), 20)
        self.assertEqual(subject.energy_first_relative_correction(3), Fraction(21, 2))

    def test_laguerre_polynomials(self) -> None:
        self.assertEqual(subject.laguerre_polynomial(0), (Fraction(1),))
        self.assertEqual(
            subject.laguerre_polynomial(2),
            (Fraction(1), Fraction(-2), Fraction(1, 2)),
        )

    def test_gamma_layer_norm_identity(self) -> None:
        for rung in range(1, 7):
            self.assertEqual(
                subject.gamma_layer_norm(rung),
                subject.effective_width_energy_constant(rung),
            )

    def test_gamma_layer_first_correction(self) -> None:
        for rung in range(1, 7):
            self.assertEqual(
                subject.correction_from_gamma_layer(rung),
                subject.energy_first_relative_correction(rung),
            )

    def test_first_rung_algebraic_asymptotic(self) -> None:
        self.assertEqual(
            subject.first_rung_algebraic_asymptotic_coefficients(),
            (Fraction(2), Fraction(3), Fraction(9, 2), Fraction(6)),
        )

    def test_first_rung_bv_join(self) -> None:
        left = subject.first_rung_detector_variation(0.5)
        right = subject.first_rung_detector_variation(0.500000000001)
        self.assertAlmostEqual(left, right, places=9)
        self.assertEqual(subject.first_rung_phi(0), 1)
        self.assertEqual(subject.first_rung_sup_detector(0), 6)
        self.assertEqual(subject.first_rung_detector_variation(0), 24)

    def test_raw_power_phase_chart(self) -> None:
        self.assertEqual(
            subject.raw_power_exponents(1, Fraction(1), Fraction(1, 2)),
            (Fraction(-3, 2), Fraction(-2)),
        )
        self.assertTrue(subject.raw_power_schedule_certified(2, 1, 1))
        self.assertFalse(subject.raw_power_schedule_certified(2, 1, 2))

    def test_critical_power_chart(self) -> None:
        self.assertEqual(
            subject.critical_power_exponents(1, Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(-1)),
        )
        self.assertEqual(
            subject.critical_power_exponents(1, Fraction(1), Fraction(1, 4)),
            (Fraction(3, 4), Fraction(0)),
        )

    def test_safe_log_cost(self) -> None:
        self.assertEqual(
            subject.renormalized_safe_log_cost(2, Fraction(1, 100), Fraction(1, 200)),
            Fraction(11, 200),
        )

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(
            ledger["safe_critical_normalization_window"], "PROVED SUFFICIENT"
        )
        self.assertEqual(ledger["converse_failure_outside_safe_window"], "NOT PROVED")
        self.assertEqual(ledger["new_unconditional_beta_estimate"], "NOT PROVED")
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_resource_caps(self) -> None:
        caps = subject.run()["resource_caps"]
        self.assertEqual(caps["maximum_rung"], 6)
        self.assertEqual(caps["beta_terms"], 0)
        self.assertEqual(caps["quadratures"], 0)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.phi_leading_constant(0)
        with self.assertRaises(ValueError):
            subject.laguerre_polynomial(-1)
        with self.assertRaises(ValueError):
            subject.first_rung_phi(-1)
        with self.assertRaises(ValueError):
            subject.first_rung_sup_detector(1, 0)
        with self.assertRaises(ValueError):
            subject.renormalized_safe_log_cost(1, Fraction(-1), Fraction(0))
        with self.assertRaises(ValueError):
            subject.raw_power_exponents(1, Fraction(-1), Fraction(0))
        with self.assertRaises(ValueError):
            subject.critical_power_exponents(1, Fraction(0), Fraction(0))


if __name__ == "__main__":
    unittest.main()
