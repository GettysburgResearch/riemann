from __future__ import annotations

import copy
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "summarize_pr71_exhaustive_grid",
    ROOT / "summarize_pr71_exhaustive_grid.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ExhaustiveGridTests(unittest.TestCase):
    def setUp(self) -> None:
        self.point_ids = tuple(f"p{index}" for index in range(9))
        self.rows = MODULE.generate_exhaustive_rows(self.point_ids)

    def test_nine_node_counts_match_closed_formula(self) -> None:
        counts = MODULE.validate_exhaustive_coverage(self.rows, self.point_ids)
        self.assertEqual(counts, {1: 36, 2: 378, 3: 840, 4: 315})
        self.assertEqual(len(self.rows), 1569)

    def test_transpose_duplicate_is_rejected(self) -> None:
        duplicate = copy.deepcopy(
            next(row for row in self.rows if row["kind"].endswith("determinant"))
        )
        duplicate["id"] += "-transpose"
        duplicate["rows"], duplicate["columns"] = (
            duplicate["columns"],
            duplicate["rows"],
        )
        with self.assertRaisesRegex(MODULE.ExhaustiveError, "duplicate mathematical"):
            MODULE.validate_exhaustive_coverage(
                self.rows + [duplicate], self.point_ids
            )

    def test_missing_pattern_is_rejected(self) -> None:
        with self.assertRaisesRegex(MODULE.ExhaustiveError, "exactly cover"):
            MODULE.validate_exhaustive_coverage(self.rows[:-1], self.point_ids)

    def test_five_nodes_stop_at_order_two(self) -> None:
        point_ids = self.point_ids[:5]
        rows = MODULE.generate_exhaustive_rows(point_ids)
        counts = MODULE.validate_exhaustive_coverage(rows, point_ids)
        self.assertEqual(counts, {1: 10, 2: 15})


if __name__ == "__main__":
    unittest.main()
