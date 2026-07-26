from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "build_exhaustive_interlaced_config",
    ROOT / "build_exhaustive_interlaced_config.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ExhaustiveConfigTests(unittest.TestCase):
    def test_nine_points_produce_all_interlaced_rows(self) -> None:
        identifiers = [f"p{index}" for index in range(9)]
        result = MODULE.build(identifiers)
        self.assertEqual(
            result["row_counts"],
            {
                "monotonicity": 36,
                "order_2": 126,
                "order_3": 84,
                "order_4": 9,
            },
        )
        self.assertEqual(len(result["rows"]), 255)
        final = result["rows"][-1]
        self.assertEqual(final["rows"], ["p1", "p3", "p5", "p7"])
        self.assertEqual(final["columns"], ["p2", "p4", "p6", "p8"])

    def test_duplicate_points_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "unique"):
            MODULE.build(["a", "b", "c", "a"])


if __name__ == "__main__":
    unittest.main()
