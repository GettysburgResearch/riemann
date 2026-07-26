from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "compare_total_deflation_precision",
    ROOT / "compare_total_deflation_precision.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

FIXTURE = (
    ROOT / "certificates" / "synthetic-total-count-hidden-offline.json"
)


class PrecisionComparisonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.low = json.loads(FIXTURE.read_text())
        self.high = copy.deepcopy(self.low)

    def test_distinct_proof_digests_preserve_count_semantics(self) -> None:
        self.high["count_windows"][0]["gate"]["sha256"] = "2" * 64
        result = MODULE.compare(self.low, self.high)
        self.assertTrue(result["all_high_intervals_nested"])
        self.assertEqual(result["count_window_count"], 1)

    def test_count_semantic_drift_is_rejected(self) -> None:
        self.high["count_windows"][0]["count_lower"] += 1
        with self.assertRaisesRegex(
            MODULE.ComparisonError, "count-window semantics"
        ):
            MODULE.compare(self.low, self.high)


if __name__ == "__main__":
    unittest.main()
