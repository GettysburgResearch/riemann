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
    / "ffps_bilateral_block_source_rank_gate.py"
)
SPEC = importlib.util.spec_from_file_location("source_rank", MODULE_PATH)
assert SPEC and SPEC.loader
source_rank = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(source_rank)


class BilateralBlockSourceRankGateTest(unittest.TestCase):
    def test_singleton_formula(self) -> None:
        self.assertEqual(source_rank.single_block_leverage(5), 1)
        self.assertEqual(source_rank.single_block_leverage(13), Fraction(6, 5))
        self.assertGreater(source_rank.single_block_leverage(17), 1)

    def test_clean_kernel_coarsens_to_product_parity(self) -> None:
        clean = source_rank.quotient_kernel((3,))
        for left in range(4):
            for right in range(4):
                same_product_parity = (left.bit_count() - right.bit_count()) % 2 == 0
                self.assertEqual(clean[left][right], 0 if same_product_parity else 2)

    def test_full_kernel_separates_all_four_cosets(self) -> None:
        full = source_rank.quotient_kernel((1, 2, 3))
        for left in range(4):
            for right in range(4):
                self.assertEqual(
                    full[left][right], 0 if left == right else Fraction(4, 3)
                )

    def test_resource_and_input_firewalls(self) -> None:
        for prime in (True, 3, 7, 37):
            with self.assertRaises(ValueError):
                source_rank.single_block_leverage(prime)
        with self.assertRaises(ValueError):
            source_rank.quotient_kernel(())
        with self.assertRaises(ValueError):
            source_rank.quotient_kernel((1, 1))
        payload = source_rank.run()
        self.assertEqual(
            payload["source_arity_gate"][
                "minimum_coordinates_for_two_strictly_improving_blocks"
            ],
            4,
        )
        self.assertEqual(payload["resource_caps"]["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
