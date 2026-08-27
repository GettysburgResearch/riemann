from __future__ import annotations

import importlib.util
import json
import math
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
    / "ffps_sharp_bv_safe_factor_phase_diagram.py"
)
SPEC = importlib.util.spec_from_file_location("sharp_bv_phase", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load sharp BV phase producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class SharpBVSafeFactorPhaseDiagramTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_shape_constants(self) -> None:
        self.assertEqual(
            [subject.sharp_bv_shape_constant(r) for r in range(4)],
            [3, 20, 224, 3456],
        )

    def test_order_constants(self) -> None:
        self.assertEqual(subject.order_constant(0), 9)
        self.assertEqual(subject.order_constant(1), Fraction(100, 3))
        self.assertEqual(subject.order_constant(2), Fraction(3136, 45))

    def test_consecutive_ratio_identity(self) -> None:
        for order in range(12):
            self.assertEqual(
                subject.order_constant(order + 1) / subject.order_constant(order),
                subject.consecutive_ratio(order),
            )

    def test_strict_monotonicity_certificate(self) -> None:
        self.assertEqual(subject.monotonicity_gap_numerator(0), 73)
        for order in range(100):
            self.assertGreater(subject.consecutive_ratio(order), 1)
            self.assertGreater(subject.monotonicity_gap_numerator(order), 0)

    def test_ratio_drop_and_log_concavity(self) -> None:
        for order in range(99):
            self.assertGreater(
                subject.consecutive_ratio(order),
                subject.consecutive_ratio(order + 1),
            )
            self.assertGreater(subject.ratio_drop_numerator(order), 0)

    def test_asymptotic(self) -> None:
        for order in (100, 500):
            ratio = float(subject.order_constant(order)) / (2 * math.pi * order**2)
            self.assertAlmostEqual(ratio, 1, delta=0.03)

    def test_width_penalty(self) -> None:
        self.assertEqual(subject.width_penalty(0, Fraction(4), Fraction(2)), 9)
        self.assertEqual(subject.width_penalty(1, Fraction(4), Fraction(2)), 81)

    def test_exact_minimum_safe_factor(self) -> None:
        self.assertEqual(
            subject.exact_minimum_safe_factor(0, Fraction(4), Fraction(2)), 81
        )
        self.assertEqual(
            subject.exact_minimum_safe_factor(1, Fraction(4), Fraction(2)), 2700
        )

    def test_width_monotonicity_and_order_zero_winner(self) -> None:
        for order in range(1, 8):
            self.assertGreater(
                subject.exact_minimum_safe_factor(order, Fraction(5), Fraction(3)),
                subject.exact_minimum_safe_factor(0, Fraction(5), Fraction(3)),
            )
        for order in range(5):
            self.assertGreater(
                subject.exact_minimum_safe_factor(order, Fraction(5), Fraction(2)),
                subject.exact_minimum_safe_factor(order, Fraction(5), Fraction(3)),
            )

    def test_power_law_phase(self) -> None:
        self.assertTrue(
            subject.power_law_safe(order_exponent=Fraction(1, 2), width_exponent=0)
        )
        self.assertFalse(
            subject.power_law_safe(order_exponent=1, width_exponent=Fraction(1, 2))
        )
        self.assertTrue(subject.power_law_safe(order_exponent=2, width_exponent=3))
        self.assertFalse(subject.power_law_safe(order_exponent=3, width_exponent=3))

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(ledger["universal_BV_route_prefers_low_pass"], "PROVED")
        self.assertEqual(
            ledger["higher_order_never_improves_actual_beta_energy"], "NOT PROVED"
        )
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_resource_caps(self) -> None:
        caps = subject.run()["resource_caps"]
        self.assertEqual(caps["maximum_information_order"], 12)
        self.assertEqual(caps["beta_terms"], 0)
        self.assertEqual(caps["root_searches"], 0)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.order_constant(-1)
        with self.assertRaises(ValueError):
            subject.width_penalty(0, Fraction(-1), Fraction(1))
        with self.assertRaises(ValueError):
            subject.width_penalty(0, Fraction(1), Fraction(0))


if __name__ == "__main__":
    unittest.main()
