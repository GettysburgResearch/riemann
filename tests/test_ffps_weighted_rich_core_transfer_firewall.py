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
    / "ffps_weighted_rich_core_transfer_firewall.py"
)
SPEC = importlib.util.spec_from_file_location("weighted_rich_firewall", MODULE_PATH)
assert SPEC and SPEC.loader
weighted_rich_firewall = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(weighted_rich_firewall)


class FfpsWeightedRichCoreTransferFirewallTest(unittest.TestCase):
    def test_rough_support_formula(self) -> None:
        primes = (103, 107, 127, 131, 139, 151, 163, 167)
        for size in range(1, len(primes) + 1):
            self.assertEqual(
                weighted_rich_firewall.boolean_b(primes[:size], 39),
                1 + (-1) ** size,
            )

    def test_exact_shell_is_clean_poor_and_nonzero(self) -> None:
        panel = weighted_rich_firewall.exact_shell_panel()
        self.assertEqual(panel["eligible_counts"], [0, 0])
        self.assertEqual(panel["boolean_coefficients"], [2, 2])
        for multiplier in panel["ratio_eight_shell_multipliers"]:
            self.assertGreaterEqual(float(multiplier), 1)
            self.assertLessEqual(float(multiplier), 8)
        supports = panel["core_supports"]
        self.assertEqual(len({prime for support in supports for prime in support}), 4)

    def test_weighted_majorant_still_has_a_log_saving(self) -> None:
        for alpha in (0.1, 0.274064461784, 0.49):
            self.assertGreater(weighted_rich_firewall.l1_majorant_saving(alpha), 0)
            self.assertLess(
                weighted_rich_firewall.l1_majorant_bad_exponent(alpha), 5
            )

    def test_guards_and_caps(self) -> None:
        with self.assertRaises(ValueError):
            weighted_rich_firewall.l1_majorant_saving(3)
        caps = weighted_rich_firewall.run()["resource_caps"]
        self.assertEqual(caps["maximum_labelled_partitions"], 6561)
        self.assertEqual(caps["source_atoms_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
