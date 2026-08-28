from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE_DIR = ROOT / "research/l-families/atlas/function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import ffps_divisor_wave_shifted_zeta_factorization as packet  # noqa: E402


class DivisorWaveShiftedZetaTests(unittest.TestCase):
    def test_hyperbola_interval(self) -> None:
        for row in packet.hyperbola_interval_panel()["rows"]:
            self.assertTrue(row["interval_equal"])

    def test_squarefree_orientation_product(self) -> None:
        panel = packet.orientation_laurent_panel()
        self.assertTrue(panel["product_equal"])
        self.assertEqual(panel["orientation_count"], 16)

    def test_local_shifted_zeta_factor(self) -> None:
        panel = packet.local_euler_panel()
        for row in panel["rows"]:
            self.assertTrue(row["product_recovers_1_minus_t_x"])
            self.assertEqual(row["correction_coefficients"][1], "0")

    def test_scope(self) -> None:
        payload = packet.run(check_sources=False)
        self.assertFalse(payload["scope_firewall"]["fourier_mode_bound_proved"])
        self.assertFalse(payload["scope_firewall"]["rh_or_grh_proved"])


if __name__ == "__main__":
    unittest.main()
