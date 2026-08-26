from __future__ import annotations

import importlib.util
import json
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
    / "ffps_anticausal_outer_inversion_gate.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_ANTICAUSAL_OUTER_INVERSION_GATE.md")
JSON_PATH = MODULE_PATH.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("anticausal_gate", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load anti-causal inversion replay")
anticausal_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(anticausal_gate)


class FfpsAnticausalOuterInversionGateTest(unittest.TestCase):
    def test_display_math_and_canonical_json(self) -> None:
        depth = 0
        for line in NOTE_PATH.read_text(encoding="utf-8").splitlines():
            if line == r"\[":
                depth += 1
                self.assertEqual(depth, 1)
            elif line == r"\]":
                depth -= 1
                self.assertGreaterEqual(depth, 0)
        self.assertEqual(depth, 0)
        self.assertEqual(
            json.loads(JSON_PATH.read_text(encoding="utf-8")), anticausal_gate.run()
        )

    def test_frozen_source_blobs(self) -> None:
        anticausal_gate.check_source_blobs()
        self.assertEqual(sum(map(len, anticausal_gate.FROZEN_SOURCES.values())), 8)

    def test_geometric_partial_sums(self) -> None:
        self.assertEqual(
            anticausal_gate.geometric_partial_sum(0), (Fraction(0), Fraction(0))
        )
        self.assertEqual(
            anticausal_gate.geometric_partial_sum(1), (Fraction(0), Fraction(1, 2))
        )
        self.assertEqual(
            anticausal_gate.geometric_partial_sum(2), (Fraction(1, 2), Fraction(1, 2))
        )
        with self.assertRaises(ValueError):
            anticausal_gate.geometric_partial_sum(-1)
        with self.assertRaises(ValueError):
            anticausal_gate.geometric_partial_sum(True)

    def test_exact_combined_constant(self) -> None:
        self.assertTrue(anticausal_gate.multiplier_polynomial_check())
        result = anticausal_gate.run()
        self.assertEqual(result["stable_inverse"]["L1_norm"], "8/3")
        self.assertEqual(result["combined_global_bound"]["C_inv"], "8/3+8/3*sqrt(2)")
        self.assertIn(
            "||g_-||_TV", result["anti_causal_inverse"]["zero_mass_one_sided_bound"]
        )

    def test_terminal_gate_and_caps(self) -> None:
        result = anticausal_gate.run()
        self.assertEqual(result["terminal_gate"]["name"], "TERMFUT106150")
        self.assertEqual(result["conclusion_scope"]["parent_binding_status"], "open")
        self.assertIn("NATBIND106150", result["conclusion_scope"]["parent_binding"])
        self.assertIn("refuted", result["conclusion_scope"]["raw_complete_beta_status"])
        self.assertIn(
            "RH-equivalent",
            result["conclusion_scope"]["viable_complete_replacement"],
        )
        multipliers = result["three_kernel_multipliers"]
        self.assertNotEqual(
            multipliers["explicit_native_K_L"],
            multipliers["common_mother_self_convolution"],
        )
        self.assertEqual(result["resource_caps"]["source_atoms_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
