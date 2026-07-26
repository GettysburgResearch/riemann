from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "rebind_pr71_zero_block", ROOT / "rebind_pr71_zero_block.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def value(mantissa: int) -> dict[str, str]:
    return {"mantissa": str(mantissa), "exponent": "0"}


class ZeroBlockRebindTests(unittest.TestCase):
    def block(self) -> dict:
        intervals = ((1, 2), (4, 5), (7, 8), (10, 11))
        return {
            "schema": MODULE.SCHEMA,
            "classification": MODULE.CLASSIFICATION,
            "precision_bits": 192,
            "requested_start_index": "100",
            "requested_length": 4,
            "returned_count": 4,
            "target": {"numerator": "6", "denominator": "1"},
            "target_below_local_index": 1,
            "target_above_local_index": 2,
            "target_below_zero_index": "101",
            "target_above_zero_index": "102",
            "zeros": [
                {
                    "local_index": index,
                    "zero_index": str(100 + index),
                    "ball": {
                        "lower": value(lower),
                        "upper": value(upper),
                    },
                }
                for index, (lower, upper) in enumerate(intervals)
            ],
            "proof_boundary": "synthetic fixture",
        }

    def test_rebinds_only_target_metadata(self) -> None:
        source = self.block()
        result = MODULE.rebind(source, 9, 1)
        self.assertEqual(result["target_below_zero_index"], "102")
        self.assertEqual(result["target_above_zero_index"], "103")
        self.assertEqual(result["zeros"], source["zeros"])
        self.assertEqual(
            result["derived_target_rebinding"]["source_zero_block_sha256"],
            MODULE.canonical_sha(source),
        )

    def test_target_overlapping_zero_is_rejected(self) -> None:
        with self.assertRaisesRegex(MODULE.RebindError, "overlaps"):
            MODULE.rebind(self.block(), 7, 1)

    def test_target_outside_block_is_rejected(self) -> None:
        with self.assertRaisesRegex(MODULE.RebindError, "strictly inside"):
            MODULE.rebind(self.block(), 12, 1)

    def test_nonconsecutive_index_is_rejected(self) -> None:
        source = self.block()
        source["zeros"][2]["zero_index"] = "999"
        with self.assertRaisesRegex(MODULE.RebindError, "not consecutive"):
            MODULE.rebind(source, 9, 1)


if __name__ == "__main__":
    unittest.main()
