from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_boolean_depth_recombination_carleson.py"
)
SPEC = importlib.util.spec_from_file_location("boolean_carleson", MODULE_PATH)
assert SPEC and SPEC.loader
boolean_carleson = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(boolean_carleson)


class FfpsBooleanDepthRecombinationCarlesonTest(unittest.TestCase):
    def test_exact_depth_recombination(self) -> None:
        for panel in boolean_carleson.identity_panels():
            self.assertLessEqual(
                panel["maximum_absolute_coefficient"],
                panel["three_box_majorant"],
            )

    def test_direct_identity_on_mixed_cutoff_cells(self) -> None:
        support = (2, 3, 5, 7, 11)
        for cutoff in (1, 2, 6, 10, 21, 50, 100, 500):
            self.assertEqual(
                boolean_carleson.weighted_rich_firewall.boolean_b(support, cutoff),
                boolean_carleson.recombined_boolean_b(support, cutoff),
            )

    def test_shell_envelopes_save_log_powers(self) -> None:
        alpha = 0.274064461784
        self.assertGreater(boolean_carleson.shell_saving(alpha, 3), 0)
        self.assertGreater(boolean_carleson.shell_saving(alpha, 9), 0)
        self.assertLess(
            boolean_carleson.shell_bad_exponent(alpha, 3),
            boolean_carleson.shell_full_exponent(3),
        )

    def test_guards_and_caps(self) -> None:
        with self.assertRaises(ValueError):
            boolean_carleson.shell_bad_exponent(2, 3)
        caps = boolean_carleson.run()["resource_caps"]
        self.assertEqual(caps["maximum_three_box_assignments"], 729)
        self.assertEqual(caps["source_atoms_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
