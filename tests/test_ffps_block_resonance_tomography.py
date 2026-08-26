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
    / "ffps_block_resonance_tomography.py"
)
SPEC = importlib.util.spec_from_file_location("block_tomography", MODULE_PATH)
assert SPEC and SPEC.loader
block_tomography = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(block_tomography)


class BlockResonanceTomographyTest(unittest.TestCase):
    def test_fixed_visible_codimension(self) -> None:
        for blocks in range(1, 9):
            block_rows = block_tomography.bilateral_block_rows(blocks)
            for codimension in range(blocks + 1):
                row = block_tomography.tomography(
                    block_rows,
                    block_tomography.aligned_relations(blocks, codimension),
                )
                self.assertEqual(row["invariant_dimension"], codimension)
                self.assertEqual(
                    row["invariant_selected_mode_count"], 2**codimension - 1
                )
                self.assertEqual(
                    Fraction(row["normalized_selected_invariant_coefficient"]),
                    Fraction(2**codimension - 1, 2**blocks - 1),
                )

    def test_double_collision_and_one_sided_firewall(self) -> None:
        blocks = 7
        block_rows = block_tomography.bilateral_block_rows(blocks)
        full = block_tomography.tomography(
            block_rows,
            block_tomography.double_collision_relations(blocks, blocks),
        )
        self.assertEqual(full["invariant_dimension"], blocks)
        self.assertEqual(full["normalized_selected_invariant_coefficient"], "1")
        self.assertEqual(full["hard_invariant_coefficient"], 2**blocks)
        self.assertEqual(full["off_coset_interferometer_invariant_coefficient"], "0")

        left_only = block_tomography.tomography(block_rows, (1,))
        self.assertEqual(left_only["invariant_dimension"], 0)

    def test_arithmetic_character_sum_dichotomy(self) -> None:
        for blocks in range(2, 8):
            block_rows = block_tomography.bilateral_block_rows(blocks)
            for codimension in range(1, blocks + 1):
                relations = block_tomography.aligned_relations(blocks, codimension)
                row = block_tomography.tomography(
                    block_rows, relations, arithmetic_twist=1
                )
                self.assertFalse(row["arithmetic_twist_trivial_on_invariants"])
                self.assertEqual(row["selected_invariant_coefficient"], -1)
                self.assertEqual(row["hard_invariant_coefficient"], 0)
                self.assertEqual(
                    Fraction(row["normalized_selected_invariant_coefficient"]),
                    Fraction(-1, 2**blocks - 1),
                )

    def test_rank_defect_is_a_generic_invariant(self) -> None:
        row = block_tomography.tomography((0b11, 0b11, 0b1100), ())
        self.assertEqual(row["block_rank"], 2)
        self.assertEqual(row["block_kernel_dimension"], 1)
        self.assertEqual(row["invariant_dimension"], 1)
        self.assertEqual(row["invariant_selected_mode_count"], 1)

    def test_relative_projector_is_principal_everywhere(self) -> None:
        for blocks in range(1, 6):
            panel = block_tomography.quotient_projector_check(blocks)
            for row in panel["rows"]:
                self.assertEqual(row["relative_kernel"], 1)
                if row["quotient"] == 0:
                    self.assertEqual(row["hard_kernel"], 2**blocks)
                    self.assertEqual(row["selected_kernel"], 2**blocks - 1)
                else:
                    self.assertEqual(row["hard_kernel"], 0)
                    self.assertEqual(row["selected_kernel"], -1)

    def test_invalid_inputs_and_caps(self) -> None:
        with self.assertRaises(ValueError):
            block_tomography.tomography((), ())
        with self.assertRaises(ValueError):
            block_tomography.tomography((1,) * 11, ())
        with self.assertRaises(ValueError):
            block_tomography.tomography((1, 2), (), arithmetic_twist=4)
        caps = block_tomography.run()["resource_caps"]
        self.assertEqual(caps["finite_field_points"], 0)
        self.assertEqual(caps["curves_or_conductors"], 0)


if __name__ == "__main__":
    unittest.main()
