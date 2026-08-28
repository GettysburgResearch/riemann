from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE_DIR = ROOT / "research/l-families/atlas/function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import ffps_divisor_wave_witt_zeta_tower as packet  # noqa: E402


class DivisorWaveWittZetaTowerTests(unittest.TestCase):
    def test_witt_product_through_depth_eight(self) -> None:
        panel = packet.witt_factor_panel()
        self.assertEqual(panel["local_identity_verified_through_degree"], 8)
        self.assertEqual(panel["target"], "1-(z+z^-1)x")

    def test_first_packets_and_degree_two_factor(self) -> None:
        panel = packet.first_extractions_panel()
        self.assertEqual(panel["packets"]["2"], {0: 1})
        self.assertIn("zeta^(67)(2s)", panel["degree_two_factor"])
        self.assertIn("1/(R+1)", panel["normal_convergence"])

    def test_scope_firewall(self) -> None:
        rendered = packet.run(check_sources=False)
        self.assertFalse(rendered["scope_firewall"]["highgcdwave_proved"])
        self.assertFalse(rendered["scope_firewall"]["rh_or_grh_proved"])


if __name__ == "__main__":
    unittest.main()
