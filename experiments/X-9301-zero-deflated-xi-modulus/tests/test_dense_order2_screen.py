from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "summarize_dense_order2_screen",
    ROOT / "summarize_dense_order2_screen.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class DenseOrder2ScreenTests(unittest.TestCase):
    def test_sixteen_node_coverage(self) -> None:
        point_ids = tuple(f"p{index}" for index in range(16))
        rows = MODULE.generate_order2_rows(point_ids)
        self.assertEqual(len(rows), 5460)
        self.assertEqual(len({row["id"] for row in rows}), 5460)

    def test_each_partition_occurs_once_up_to_transpose(self) -> None:
        point_ids = tuple(f"p{index}" for index in range(5))
        rows = MODULE.generate_order2_rows(point_ids)
        patterns = set()
        for row in rows:
            left = tuple(row["rows"])
            right = tuple(row["columns"])
            pattern = (left, right) if left < right else (right, left)
            self.assertNotIn(pattern, patterns)
            patterns.add(pattern)
        self.assertEqual(len(patterns), 15)


if __name__ == "__main__":
    unittest.main()
