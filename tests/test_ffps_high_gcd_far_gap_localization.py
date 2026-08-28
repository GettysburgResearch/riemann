from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE_DIR = ROOT / "research/l-families/atlas/function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import ffps_high_gcd_far_gap_localization as packet  # noqa: E402


class HighGcdFarGapLocalizationTests(unittest.TestCase):
    def test_tau_square_majorant(self) -> None:
        panel = packet.tau_square_panel()
        self.assertEqual(panel["checked"], 80)
        for row in panel["rows"]:
            self.assertLessEqual(row["tau_squared"], row["d4"])

    def test_divisor_harmonic_bounds(self) -> None:
        for row in packet.divisor_harmonic_panel()["rows"]:
            self.assertLessEqual(
                packet.Fraction(row["left"]), packet.Fraction(row["right"])
            )

    def test_shifted_cauchy_factors(self) -> None:
        panel = packet.shifted_cauchy_panel()
        bound = packet.Fraction(panel["common_bound"])
        self.assertEqual(panel["shifts_checked"], 15)
        self.assertLessEqual(packet.Fraction(panel["max_first_l2_factor"]), bound)
        self.assertLessEqual(packet.Fraction(panel["max_second_l2_factor"]), bound)

    def test_three_way_partition_and_scope(self) -> None:
        panel = packet.three_way_partition_panel()
        self.assertTrue(panel["partition_exact"])
        for row in panel["rows"]:
            self.assertEqual(
                packet.Fraction(row["full"]),
                packet.Fraction(row["low"])
                + packet.Fraction(row["high_near"])
                + packet.Fraction(row["high_far"]),
            )
        payload = packet.run(check_sources=False)
        self.assertTrue(
            payload["scope_firewall"]["gap_is_in_reduced_product_shell_variables"]
        )
        self.assertFalse(payload["scope_firewall"]["highfargcdwave_proved"])
        self.assertFalse(payload["scope_firewall"]["rh_or_grh_proved"])

    def test_shifted_coprimality(self) -> None:
        panel = packet.shifted_coprimality_panel()
        self.assertGreater(panel["checked"], 0)
        self.assertEqual(panel["identity"], "gcd(a,a+h)=gcd(a,h)")


if __name__ == "__main__":
    unittest.main()
