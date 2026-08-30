from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE_DIR = ROOT / "research/l-families/atlas/function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import ffps_gcd_wave_mode_decoupling as packet  # noqa: E402


class GcdWaveModeDecouplingTests(unittest.TestCase):
    def test_local_decoupling(self) -> None:
        panel = packet.local_decoupling_panel()
        self.assertEqual(len(panel["rows"]), 6)
        self.assertIn("(2/p)", panel["identity"])

    def test_critical_coupling_is_summable(self) -> None:
        panel = packet.convergence_panel()
        self.assertTrue(panel["normal_convergence"])
        self.assertTrue(panel["nonzero_after_deleting_primes_at_most_13"])

    def test_scope_firewall(self) -> None:
        rendered = packet.run(check_sources=False)
        self.assertFalse(rendered["scope_firewall"]["highgcdwave_proved"])
        self.assertFalse(rendered["scope_firewall"]["rh_or_grh_proved"])


if __name__ == "__main__":
    unittest.main()
