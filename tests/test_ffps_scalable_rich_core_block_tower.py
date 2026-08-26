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
    / "ffps_scalable_rich_core_block_tower.py"
)
SPEC = importlib.util.spec_from_file_location("rich_core_tower", MODULE_PATH)
assert SPEC and SPEC.loader
rich_core_tower = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rich_core_tower)


class ScalableRichCoreBlockTowerTest(unittest.TestCase):
    def test_each_block_beats_four_fifths(self) -> None:
        for blocks in range(1, rich_core_tower.MAX_BLOCKS + 1):
            panel = rich_core_tower.tower_panel(blocks)
            self.assertTrue(panel["all_blocks_contract"])
            self.assertLess(Fraction(panel["joint_leverage"]), Fraction(4, 5) ** blocks)

    def test_mode_and_coordinate_counts(self) -> None:
        panel = rich_core_tower.tower_panel(8)
        self.assertEqual(panel["phase_coordinates"], 16)
        self.assertEqual(panel["selected_modes"], 255)
        self.assertLess(Fraction(panel["principal_local_weight_product"]), 5)

    def test_density_leverage_balance(self) -> None:
        alpha = rich_core_tower.balanced_alpha()
        self.assertGreater(alpha, 0.25)
        self.assertLess(alpha, 0.30)
        self.assertAlmostEqual(
            rich_core_tower.density_exponent(alpha),
            rich_core_tower.leverage_exponent(alpha),
            places=12,
        )

    def test_path_complexity_scope_is_fixed_degree(self) -> None:
        ledger = rich_core_tower.run()["complexity_ledger"]
        self.assertIn("fixed equal place degree", ledger["growing_rank_consequence"])
        self.assertIn("not a native varying-place", ledger["status"])

    def test_guards_and_caps(self) -> None:
        for alpha in (0, 0.5, 1):
            with self.assertRaises(ValueError):
                rich_core_tower.density_exponent(alpha)
        with self.assertRaises(ValueError):
            rich_core_tower.tower_panel(0)
        caps = rich_core_tower.run()["resource_caps"]
        self.assertEqual(caps["source_atoms_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
