from __future__ import annotations

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
    / "ffps_critical_moving_order_phase_boundary.py"
)
SPEC = importlib.util.spec_from_file_location("moving_order_boundary", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load moving-order boundary producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class CriticalMovingOrderPhaseBoundaryTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_log_modulus_matches_direct_formula(self) -> None:
        for frequency in (0.01, 0.25, 1.0, 3.0):
            self.assertAlmostEqual(
                math.exp(subject.log_p_fourier_modulus_squared(frequency)),
                subject.p_fourier_modulus_squared(frequency),
                places=13,
            )

    def test_variance_is_the_quadratic_decay(self) -> None:
        _, variance = subject.mean_and_variance()
        for frequency in (1.0e-3, 5.0e-4):
            ratio = -subject.log_p_fourier_modulus_squared(frequency) / frequency**2
            self.assertAlmostEqual(ratio, variance, places=6)

    def test_boundary_endpoint_decay(self) -> None:
        rows = subject.endpoint_rows()
        self.assertLess(abs(rows[-1]["decay_ratio"] - 1.0), 1.0e-10)
        self.assertAlmostEqual(
            subject.predicted_endpoint_decay(400.0, 1.0, 1.0),
            400.0,
        )

    def test_integer_order_is_the_declared_ceiling(self) -> None:
        for log_x in subject.LOG_X_ROWS:
            order_90 = subject._decimal_integer_order(log_x, 1.0, 1.0, precision=90)
            order_130 = subject._decimal_integer_order(log_x, 1.0, 1.0, precision=130)
            self.assertEqual(subject.integer_order(log_x, 1.0, 1.0), order_130)
            self.assertEqual(order_90, order_130)

        float_proxy = math.ceil(subject.continuous_order(1600.0, 1.0, 1.0))
        self.assertNotEqual(subject.integer_order(1600.0, 1.0, 1.0), float_proxy)

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_order_is_subpower(self) -> None:
        rows = subject.endpoint_rows()
        self.assertLess(
            rows[-1]["order_is_subpower_ratio"],
            rows[0]["order_is_subpower_ratio"],
        )

    def test_smoother_stair_has_unit_log_exponent(self) -> None:
        rows = subject.endpoint_rows()
        self.assertLess(
            abs(rows[-1]["stair_decay_over_log_X"] - 1.0),
            abs(rows[0]["stair_decay_over_log_X"] - 1.0),
        )

    def test_phase_rows_distinguish_the_certified_boundary(self) -> None:
        rows = subject.phase_rows()
        below = next(
            row
            for row in rows
            if row["alpha"] == 1.0 and row["constant_over_variance"] == 0.5
        )
        above = next(
            row
            for row in rows
            if row["alpha"] == 1.0 and row["constant_over_variance"] == 2.0
        )
        self.assertLess(below["certified_margin_over_log_X"], 0.0)
        self.assertGreater(above["certified_margin_over_log_X"], 0.0)

    def test_payload_firewalls(self) -> None:
        payload = subject.run()
        ledger = payload["proof_ledger"]
        self.assertEqual(ledger["phase_region_RH_equivalence"], "PROVED")
        self.assertEqual(ledger["criterion_failure_below_boundary"], "NOT PROVED")
        self.assertEqual(ledger["beta_energy_estimate"], "NOT PROVED")
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.critical_log_frequency(0.0)
        with self.assertRaises(ValueError):
            subject.continuous_order(100.0, 1.5, 1.0)
        with self.assertRaises(ValueError):
            subject.continuous_order(100.0, 0.5, 0.0)
        with self.assertRaises(ValueError):
            subject.smoother_stair_decay(100.0, 0.0)


if __name__ == "__main__":
    unittest.main()
