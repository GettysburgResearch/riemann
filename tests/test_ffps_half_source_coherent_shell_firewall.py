from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_half_source_coherent_shell_firewall.py"
)
SPEC = importlib.util.spec_from_file_location("coherent_shell", MODULE_PATH)
assert SPEC and SPEC.loader
coherent_shell = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(coherent_shell)


class FfpsHalfSourceCoherentShellFirewallTest(unittest.TestCase):
    def test_scale_ledger(self) -> None:
        ledger = coherent_shell.scale_ledger()
        self.assertEqual(ledger["cutoff"], Fraction(5, 3))
        self.assertEqual(ledger["half_product"], 5)
        self.assertEqual(ledger["two_half_product"], 10)
        self.assertEqual(ledger["source_diagonal"], -2)
        self.assertEqual(ledger["coherent_square"], 1)
        self.assertEqual(ledger["coherent_to_diagonal_gap"], 3)

    def test_rough_sign_and_ratio_window(self) -> None:
        result = coherent_shell.run()
        fixture = result["scale_fixture"]
        self.assertEqual(fixture["rough_half_source_coefficient"], "-1")
        self.assertTrue(fixture["inside_ratio_eight"])
        self.assertLess(Fraction(fixture["two_half_product_ratio_bound"]), 8)

    def test_wick_fraction_tends_to_one(self) -> None:
        small = coherent_shell.disjoint_ordered_fraction(5, 11)
        large = coherent_shell.disjoint_ordered_fraction(101, 1009)
        self.assertGreater(large, small)
        self.assertGreater(large, Fraction(98, 100))

    def test_guards_and_caps(self) -> None:
        with self.assertRaises(ValueError):
            coherent_shell.disjoint_ordered_fraction(1, 10)
        caps = coherent_shell.run()["resource_caps"]
        self.assertEqual(caps["prime_intervals_enumerated"], 0)
        self.assertEqual(caps["source_atoms_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
