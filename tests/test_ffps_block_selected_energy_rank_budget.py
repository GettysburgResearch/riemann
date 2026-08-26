from __future__ import annotations

import importlib.util
import math
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
    / "ffps_block_selected_energy_rank_budget.py"
)
SPEC = importlib.util.spec_from_file_location("rank_budget", MODULE_PATH)
assert SPEC and SPEC.loader
rank_budget = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rank_budget)


class BlockSelectedEnergyRankBudgetTest(unittest.TestCase):
    def test_closed_form_against_direct_binomial_sum(self) -> None:
        for blocks in range(1, 9):
            for place_degree in range(1, 5):
                row = rank_budget.rank_budget(blocks, place_degree)
                direct = sum(
                    math.comb(blocks, size) * (2 * place_degree * size - 2) ** 2
                    for size in range(1, blocks + 1)
                )
                self.assertEqual(row["total_selected_energy_rank"], direct)
                self.assertEqual(
                    row["average_selected_energy_rank"],
                    str(Fraction(direct, 2**blocks - 1)),
                )

    def test_quadratic_not_linear_budget(self) -> None:
        row = rank_budget.rank_budget(12, 2)
        average_square = Fraction(row["average_selected_energy_rank"])
        average_first = Fraction(row["average_first_moment_rank"])
        self.assertGreater(average_square, average_first)
        self.assertLess(average_square, 4 * 12 * 12 + 1)

    def test_exact_asymptotic_remainder(self) -> None:
        for blocks in range(1, 9):
            for place_degree in range(1, 5):
                row = rank_budget.rank_budget(blocks, place_degree)
                average = Fraction(row["average_selected_energy_rank"])
                polynomial = (
                    place_degree**2 * blocks**2
                    + (place_degree**2 - 4 * place_degree) * blocks
                    + 4
                )
                remainder = Fraction(
                    place_degree**2 * blocks * (blocks + 1) - 4 * place_degree * blocks,
                    2**blocks - 1,
                )
                self.assertEqual(average, polynomial + remainder)

    def test_invalid_and_resource_caps(self) -> None:
        for blocks in (True, 0, 13):
            with self.assertRaises(ValueError):
                rank_budget.rank_budget(blocks, 1)
        for degree in (True, 0, 6):
            with self.assertRaises(ValueError):
                rank_budget.rank_budget(2, degree)
        caps = rank_budget.run()["resource_caps"]
        self.assertEqual(caps["subsets_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
