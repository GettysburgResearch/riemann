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

import ffps_relative_trace_tensor_closure as packet  # noqa: E402


class RelativeTraceTensorClosureTests(unittest.TestCase):
    def test_centered_identity_and_common_restriction(self) -> None:
        panel = packet.centered_identity_panel()
        self.assertTrue(panel["common_restriction_preserved"])
        self.assertTrue(panel["signed_outer_recombination_preserved"])
        for row in panel["rows"]:
            self.assertEqual(row["principal_centered"], row["hard_minus_selected"])

    def test_coprime_square_and_diagonal_externalize(self) -> None:
        panel = packet.coprime_wick_panel()
        self.assertEqual(len(panel["rows"]), 3)
        self.assertIn("zeta(2)^2", panel["square_outer_mass"])
        self.assertIn("zeta(4)", panel["diagonal_outer_mass"])
        self.assertLess(Fraction(panel["partial_mass_4_through_200"]), Fraction(11, 10))

    def test_exact_gate_and_scope(self) -> None:
        rendered = packet.run(check_sources=False)
        self.assertIn("TRACE-NATREL", rendered["updated_gate"]["proved"])
        self.assertIn("COPRIME-WICK-EXT", rendered["updated_gate"]["proved"])
        self.assertFalse(rendered["scope_firewall"]["full_reltrace_proved"])
        self.assertFalse(rendered["scope_firewall"]["rh_or_grh_proved"])


if __name__ == "__main__":
    unittest.main()
