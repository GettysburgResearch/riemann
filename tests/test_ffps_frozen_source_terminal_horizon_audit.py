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
    / "ffps_frozen_source_terminal_horizon_audit.py"
)
SPEC = importlib.util.spec_from_file_location("terminal_horizon_audit", MODULE_PATH)
assert SPEC and SPEC.loader
terminal_horizon_audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(terminal_horizon_audit)


class FfpsFrozenSourceTerminalHorizonAuditTest(unittest.TestCase):
    def test_exact_sixth_root_cutoffs(self) -> None:
        self.assertEqual(terminal_horizon_audit.integer_nth_root_floor(2**24, 6), 16)
        self.assertEqual(terminal_horizon_audit.integer_nth_root_floor(2**25, 6), 17)
        self.assertLess(17**6, 2**25)
        self.assertLess(2**25, 18**6)

    def test_boolean_cutoff_crossing(self) -> None:
        core = (17, 43)
        self.assertEqual(terminal_horizon_audit.f_coefficient((17,), 16), -1)
        self.assertEqual(terminal_horizon_audit.f_coefficient((17,), 17), 0)
        self.assertEqual(terminal_horizon_audit.f_coefficient((43,), 16), -1)
        self.assertEqual(terminal_horizon_audit.f_coefficient((43,), 17), -1)
        self.assertEqual(terminal_horizon_audit.b_coefficient(core, 16), 2)
        self.assertEqual(terminal_horizon_audit.b_coefficient(core, 17), 0)

    def test_live_physical_atom_and_fixed_terminal_dilation(self) -> None:
        result = terminal_horizon_audit.run()
        fixture = result["cutoff_crossing_counterfixture"]
        horizon = fixture["Y"]
        physical_product = fixture["physical_product"]
        self.assertLess(horizon // 8, physical_product)
        self.assertLess(physical_product, 2 * horizon)
        self.assertGreater(Fraction(horizon, physical_product), Fraction(9, 2))
        self.assertLess(Fraction(horizon, physical_product), 8)
        support = result["fixed_source_support_theorem"]
        self.assertEqual(support["terminal_horizon_dilation"], 32)
        self.assertEqual(support["maximum_future_inverse_depth_from_X_in_[Y,2Y]"], 5)
        self.assertGreater(fixture["extra_support_endpoint_for_atom"], 2 * horizon)
        self.assertLess(fixture["extra_support_endpoint_for_atom"], 4 * horizon)

    def test_negative_mass_is_not_projection_monotone(self) -> None:
        for magnitude in (1, 7, 101):
            witness = terminal_horizon_audit.projection_negative_mass_counterexample(
                magnitude
            )
            self.assertEqual(witness["complete"], 0)
            self.assertEqual(witness["complete_negative_mass"], 0)
            self.assertEqual(witness["selected_negative_mass"], magnitude)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            terminal_horizon_audit.integer_nth_root_floor(-1, 6)
        with self.assertRaises(ValueError):
            terminal_horizon_audit.integer_nth_root_floor(16, 0)
        with self.assertRaises(ValueError):
            terminal_horizon_audit.projection_negative_mass_counterexample(0)

    def test_scope_and_caps(self) -> None:
        result = terminal_horizon_audit.run()
        typed = result["typed_conclusion"]
        self.assertIn("same-U", typed["smallest_new_gate"])
        self.assertIn("not in the frozen claims", typed["type_I_repair_boundary"])
        caps = result["resource_caps"]
        self.assertEqual(caps["boolean_labels"], 4)
        self.assertEqual(caps["maximum_boolean_subsets_per_support"], 4)
        self.assertEqual(caps["conductors_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
