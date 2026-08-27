from __future__ import annotations

import importlib.util
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
    / "ffps_fixed_support_beta_mesoscopic_microscope.py"
)
SPEC = importlib.util.spec_from_file_location("mesoscopic_microscope", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load mesoscopic microscope producer")
microscope = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(microscope)


class FixedSupportBetaMesoscopicMicroscopeTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        microscope.check_source_blobs()

    def test_variance(self) -> None:
        mean, variance = microscope.mean_and_variance()
        self.assertAlmostEqual(mean, 2.0 / (math.e - 1.0))
        self.assertGreater(variance, 0.0)
        self.assertLess(variance, 1.0)

    def test_weight_scaling_identity(self) -> None:
        _, variance = microscope.mean_and_variance()
        for order in (1, 4, 16):
            for tau in (0.25, 1.0, 2.0):
                frequency = math.sqrt(order) * tau / math.sqrt(variance)
                scaled = (
                    variance / order * microscope.compressed_weight(order, frequency)
                )
                self.assertAlmostEqual(
                    scaled,
                    microscope.scaled_weight(order, tau),
                    places=13,
                )

    def test_scaled_weight_converges_on_control_grid(self) -> None:
        early = max(
            abs(
                microscope.scaled_weight(4, tau)
                - microscope.gaussian_derivative_weight(tau)
            )
            for tau in microscope.TAUS
        )
        late = max(
            abs(
                microscope.scaled_weight(64, tau)
                - microscope.gaussian_derivative_weight(tau)
            )
            for tau in microscope.TAUS
        )
        self.assertLess(late, early)

    def test_global_compressed_weight_lower_bound(self) -> None:
        for order in (1, 2, 8, 32):
            for frequency in (0.25, 1.0, 4.0, 4.0 * math.pi):
                self.assertGreaterEqual(
                    microscope.compressed_weight(order, frequency),
                    microscope.compressed_weight_lower_bound(order, frequency),
                )

    def test_normalized_energy_constant(self) -> None:
        target = 1.0 / (4.0 * math.sqrt(math.pi))
        self.assertLess(
            abs(microscope.normalized_energy_constant(64) - target),
            4.0e-4,
        )

    def test_gaussian_autocorrelation_node_and_sign(self) -> None:
        node = math.sqrt(2.0)
        self.assertAlmostEqual(
            microscope.gaussian_derivative_autocorrelation(node),
            0.0,
            places=14,
        )
        self.assertGreater(microscope.gaussian_derivative_autocorrelation(1.0), 0.0)
        self.assertLess(microscope.gaussian_derivative_autocorrelation(2.0), 0.0)

    def test_weight_order_is_not_monotone(self) -> None:
        row = microscope.nonmonotonicity_control()
        self.assertLess(row["weight_order_2"], row["weight_order_1"])
        self.assertLess(row["weight_order_1"], row["weight_order_128"])
        self.assertLess(row["weight_order_128"], row["pointwise_limit"])

    def test_critical_order_is_subpower(self) -> None:
        rows = microscope.critical_scale_rows()
        self.assertLess(rows[-1]["log_m_over_log_X"], rows[0]["log_m_over_log_X"])

    def test_payload_firewalls(self) -> None:
        payload = microscope.run()
        ledger = payload["proof_ledger"]
        self.assertEqual(ledger["exact_scaling_bridge"], "PROVED EXACT")
        self.assertEqual(ledger["pointwise_order_monotonicity"], "FALSE")
        self.assertEqual(ledger["critical_growing_order_RH_equivalence"], "PROVED")
        self.assertEqual(ledger["critical_growing_order_beta_estimate"], "NOT PROVED")
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            microscope.compressed_weight(0, 1.0)
        with self.assertRaises(ValueError):
            microscope.scaled_weight(True, 1.0)
        with self.assertRaises(ValueError):
            microscope.scaled_weight(2, math.inf)


if __name__ == "__main__":
    unittest.main()
