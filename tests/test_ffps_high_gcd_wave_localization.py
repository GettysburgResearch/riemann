from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE_DIR = ROOT / "research/l-families/atlas/function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import ffps_high_gcd_wave_localization as packet  # noqa: E402


class HighGcdWaveLocalizationTests(unittest.TestCase):
    def test_factor_64_window(self) -> None:
        panel = packet.ratio_localization_panel()
        self.assertEqual(panel["ratio_window"], "1/64 < a/b < 64")
        self.assertTrue(any(row["checked_squarefree_pairs"] for row in panel["rows"]))

    def test_eight_fold_harmonic_bound(self) -> None:
        for row in packet.divisor_harmonic_panel()["rows"]:
            self.assertLessEqual(packet.Fraction(row["left"]), packet.Fraction(row["right"]))

    def test_high_low_partition(self) -> None:
        panel = packet.high_low_partition_panel()
        self.assertTrue(panel["partition_exact"])
        for row in panel["rows"]:
            self.assertEqual(
                packet.Fraction(row["full"]),
                packet.Fraction(row["low"]) + packet.Fraction(row["high"]),
            )

    def test_scope(self) -> None:
        payload = packet.run(check_sources=False)
        self.assertFalse(payload["scope_firewall"]["highgcdwave_proved"])
        self.assertFalse(payload["scope_firewall"]["rh_or_grh_proved"])


if __name__ == "__main__":
    unittest.main()
