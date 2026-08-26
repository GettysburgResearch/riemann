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
    / "ffps_four_phase_rich_core_source.py"
)
SPEC = importlib.util.spec_from_file_location("four_phase_source", MODULE_PATH)
assert SPEC and SPEC.loader
four_phase_source = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(four_phase_source)


class FourPhaseRichCoreSourceTest(unittest.TestCase):
    def test_two_prime_blocks_always_contract_in_replay_range(self) -> None:
        primes = [
            prime for prime in range(2, 100) if four_phase_source.eligible_prime(prime)
        ]
        for left in primes:
            for right in primes:
                self.assertLess(four_phase_source.block_leverage(left, right), 1)

    def test_closed_leverage_formula(self) -> None:
        self.assertEqual(four_phase_source.block_leverage(5, 13), Fraction(24, 43))
        panel = four_phase_source.four_phase_panel((5, 13, 17, 29))
        self.assertEqual(panel["joint_leverage"], "2688/6751")
        self.assertTrue(panel["strict_contraction"])

    def test_every_selected_mode_is_bilateral(self) -> None:
        quotient = four_phase_source.run()["quotient"]
        self.assertTrue(quotient["every_mode_is_bilateral"])
        self.assertEqual(len(quotient["nonprincipal_modes"]), 3)

    def test_source_and_input_guards(self) -> None:
        with self.assertRaises(ValueError):
            four_phase_source.block_leverage(7, 13)
        with self.assertRaises(ValueError):
            four_phase_source.four_phase_panel((5, 13, 17, 17))
        caps = four_phase_source.run()["resource_caps"]
        self.assertEqual(caps["source_atoms_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
