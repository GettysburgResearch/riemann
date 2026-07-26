from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "summarize_pr71_ordinate_screen",
    ROOT / "summarize_pr71_ordinate_screen.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class OrdinateScreenSummaryTests(unittest.TestCase):
    def test_parse_directed_summary(self) -> None:
        summary = {
            "schema": MODULE.DENSE_SCHEMA,
            "all_high_intervals_nested": True,
            "counterexample_nomination": None,
            "point_count": 16,
            "order2_row_count": 5460,
            "target": {"numerator": 7, "denominator": 1 << 32},
            "status_counts": {
                "CERTIFIED_NEGATIVE": 0,
                "UNRESOLVED": 0,
                "CERTIFIED_NONNEGATIVE": 5460,
            },
            "top_geometry_adjusted_rows": [{"id": "tight"}],
        }
        parsed = MODULE.parse_directed_summary(summary, 7, 16, 5460)
        self.assertEqual(parsed["tightest_geometry_row"]["id"], "tight")

    def test_parse_ranking_requires_input_robustness(self) -> None:
        ranking = {
            "schema": MODULE.RANKING_SCHEMA,
            "precision_bits": 256,
            "target": {"numerator": 7, "denominator": 1 << 32},
            "counterexample_nomination": None,
            "robust_negative_midpoint_count": 0,
            "orders": [
                {
                    "order": 3,
                    "pattern_count": 17160,
                    "negative_midpoint_count": 0,
                    "negative_beyond_input_uncertainty_count": 0,
                },
                {
                    "order": 4,
                    "pattern_count": 45045,
                    "negative_midpoint_count": 700,
                    "negative_beyond_input_uncertainty_count": 0,
                },
            ],
        }
        parsed = MODULE.parse_ranking(ranking, 7, 256)
        self.assertEqual(parsed["order4_negative_midpoint_count"], 700)
        ranking["orders"][1]["negative_beyond_input_uncertainty_count"] = 1
        with self.assertRaisesRegex(MODULE.SummaryError, "coverage or robust"):
            MODULE.parse_ranking(ranking, 7, 256)

    def test_parse_replay_requires_positive_nested_high_interval(self) -> None:
        def verification(status: str) -> dict:
            return {
                "source_artifacts_verified": True,
                "certified_negative_rows": 0,
                "rows": [
                    {
                        "id": "candidate",
                        "status": status,
                        "interval": {
                            "lower": {"numerator": 1, "denominator": 3},
                            "upper": {"numerator": 1, "denominator": 2},
                        },
                    }
                ],
            }

        parsed = MODULE.parse_replay(
            verification("UNRESOLVED"),
            verification("CERTIFIED_NONNEGATIVE"),
            {"all_high_intervals_nested": True, "nested_row_intervals": 1},
            "UNRESOLVED",
        )
        self.assertEqual(parsed["high_status"], "CERTIFIED_NONNEGATIVE")
        self.assertTrue(parsed["all_high_intervals_nested"])


if __name__ == "__main__":
    unittest.main()
