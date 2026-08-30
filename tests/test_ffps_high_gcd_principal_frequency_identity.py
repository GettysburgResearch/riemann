from __future__ import annotations

import sys
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE_DIR = ROOT / "research/l-families/atlas/function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import ffps_high_gcd_principal_frequency_identity as packet  # noqa: E402


class HighGcdPrincipalFrequencyIdentityTests(unittest.TestCase):
    def test_kernel_mean_is_exactly_nonzero(self) -> None:
        panel = packet.kernel_mean_panel()
        self.assertTrue(panel["boundary_mean_nonzero"])
        self.assertTrue(panel["autocorrelation_zero_frequency_positive"])
        self.assertEqual(panel["boundary_positivity_margin"], "9")
        self.assertEqual(panel["autocorrelation_positivity_margin"], "81")

    def test_additive_principal_frequency(self) -> None:
        panel = packet.additive_autocorrelation_panel()
        self.assertEqual(panel["principal_frequency"], panel["z_squared"])
        self.assertGreater(panel["shifts"], 0)

    def test_coprimality_inversion(self) -> None:
        panel = packet.coprimality_inversion_panel()
        self.assertEqual(len(panel["rows"]), 5)
        for row in panel["rows"]:
            self.assertEqual(row["direct"], row["divisor_inversion"])

    def test_global_assembly_is_coreagg(self) -> None:
        panel = packet.global_coreagg_panel()
        self.assertEqual(
            panel["left_coprime_frequency_assembly"], panel["right_coreagg"]
        )
        for row in panel["local_rows"]:
            self.assertEqual(
                Fraction(row["kappa2_minus_one"]), Fraction(row["tau_over_prime"])
            )

    def test_scope_firewall(self) -> None:
        payload = packet.run(check_sources=False)
        firewall = payload["scope_firewall"]
        self.assertFalse(firewall["hidden_vanishing_moment_exists"])
        self.assertFalse(firewall["minor_arc_only_estimate_sufficient"])
        self.assertFalse(firewall["highfargcdwave_proved"])
        self.assertFalse(firewall["rh_or_grh_proved"])


if __name__ == "__main__":
    unittest.main()
