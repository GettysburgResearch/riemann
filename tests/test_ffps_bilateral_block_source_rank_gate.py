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

    def test_product_only_comparison_coarsens_to_product_parity(self) -> None:
        product_only = source_rank.quotient_kernel((3,))
        for left in range(4):
            for right in range(4):
                same_product_parity = (left.bit_count() - right.bit_count()) % 2 == 0
                self.assertEqual(
                    product_only[left][right], 0 if same_product_parity else 2
                )

    def test_full_kernel_separates_all_four_cosets(self) -> None:
        full = source_rank.quotient_kernel((1, 2, 3))
        for left in range(4):
            for right in range(4):
                self.assertEqual(
                    full[left][right], 0 if left == right else Fraction(4, 3)
                )

    def test_frozen_source_retains_both_mixed_channels(self) -> None:
        payload = source_rank.run()
        ledger = payload["bilateral_fourier_ledger"]
        self.assertTrue(ledger["mixed_channels_retained"])
        self.assertEqual(ledger["native_quotient_rank"], 2)
        self.assertEqual(ledger["native_nonprincipal_character_count"], 3)
        self.assertFalse(
            ledger["product_only_comparison"]["native_source_forces_this_truncation"]
        )
        self.assertEqual(
            set(payload["frozen_source"]["claims"]),
            {"L-106120", "T-106121", "L-106131", "T-106140"},
        )

    def test_partition_not_fourier_rank_is_the_live_gate(self) -> None:
        self.assertEqual(
            source_rank.bilateral_checkerboard_leverage(5, 13), Fraction(24, 43)
        )
        payload = source_rank.run()
        first = payload["two_singleton_panels"][0]
        self.assertEqual(first["two_singleton_block_leverage"], "6/5")
        self.assertFalse(first["rank_two_contracts"])
        self.assertTrue(first["rank_one_contracts"])

    def test_resource_and_input_firewalls(self) -> None:
        for prime in (True, 3, 7, 37):
            with self.assertRaises(ValueError):
                source_rank.single_block_leverage(prime)
        with self.assertRaises(ValueError):
            source_rank.quotient_kernel(())
        with self.assertRaises(ValueError):
            source_rank.quotient_kernel((1, 1))
        with self.assertRaises(ValueError):
            source_rank.bilateral_checkerboard_leverage(5, 5)
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
