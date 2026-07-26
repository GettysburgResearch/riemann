from __future__ import annotations

import importlib.util
import sys
import unittest
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "rank_dense_high_order_midpoints",
    ROOT / "rank_dense_high_order_midpoints.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class HighOrderMidpointRankingTests(unittest.TestCase):
    def test_broad_grid_pattern_counts(self) -> None:
        self.assertEqual(MODULE.partition_count(20, 3), 387600)
        self.assertEqual(MODULE.partition_count(20, 4), 4408950)

    def test_partitions_are_disjoint_and_transpose_unique(self) -> None:
        partitions = list(MODULE.disjoint_partitions(6, 3))
        self.assertEqual(len(partitions), 10)
        canonical = set()
        for rows, columns in partitions:
            self.assertFalse(set(rows) & set(columns))
            key = (rows, columns) if rows < columns else (columns, rows)
            self.assertNotIn(key, canonical)
            canonical.add(key)

    def test_determinant_sign(self) -> None:
        identity = [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
        determinant, scale = MODULE.determinant_and_permanent_scale(identity)
        self.assertEqual(determinant, 1.0)
        self.assertEqual(scale, 1.0)
        identity[0], identity[1] = identity[1], identity[0]
        determinant, scale = MODULE.determinant_and_permanent_scale(identity)
        self.assertEqual(determinant, -1.0)
        self.assertEqual(scale, 1.0)

    def test_relative_vandermonde_uses_selected_nodes(self) -> None:
        nodes = [Fraction(1), Fraction(2), Fraction(10), Fraction(20)]
        self.assertAlmostEqual(
            MODULE.relative_vandermonde((0, 2), nodes), 9 / 11
        )
        with localcontext() as context:
            context.prec = 50
            self.assertEqual(
                MODULE.decimal_relative_vandermonde((0, 2), nodes),
                Decimal(9) / Decimal(11),
            )

    def test_decimal_determinant_sign(self) -> None:
        matrix = [
            [Decimal(0), Decimal(1), Decimal(0)],
            [Decimal(1), Decimal(0), Decimal(0)],
            [Decimal(0), Decimal(0), Decimal(1)],
        ]
        determinant, scale = MODULE.decimal_determinant_and_permanent_scale(
            matrix, MODULE.signed_permutations(3)
        )
        self.assertEqual(determinant, Decimal(-1))
        self.assertEqual(scale, Decimal(1))


if __name__ == "__main__":
    unittest.main()
