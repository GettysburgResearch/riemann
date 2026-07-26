from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "summarize_pr71_nearest_ladder", ROOT / "summarize_pr71_nearest_ladder.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


class LadderSummaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.block = {
            "schema": MODULE.BLOCK_SCHEMA,
            "classification": "CERTIFIED_CRITICAL_LINE_ZERO_BLOCK",
            "precision_bits": 256,
            "target": fj(Fraction(10)),
            "zeros": [
                {"zero_index": str(index), "ball": {}} for index in range(130)
            ],
        }
        block_sha = MODULE.canonical_sha(self.block)
        for count in MODULE.COUNTS:
            selected = list(range(1, count + 1))
            interval = {
                "lower": fj(Fraction(1, count + 1)),
                "upper": fj(Fraction(1, count + 1)),
            }
            row = {
                "id": "d2",
                "kind": "deflated-cross-loewner-determinant",
                "interval": interval,
                "status": "CERTIFIED_NONNEGATIVE",
            }
            certificates = {}
            for precision in (384, 512):
                certificate = {
                    "schema": "test",
                    "source": {
                        "zero_block_sha256": block_sha,
                        "nearest_count": count,
                        "selected_zero_indices": selected,
                        "selection_scope": MODULE.GLOBAL_NEAREST_SCOPE,
                    },
                }
                certificate["certificate_sha256"] = MODULE.canonical_sha(certificate)
                certificates[precision] = certificate
                verification = {
                    "source_artifacts_verified": True,
                    "certificate_sha256": certificate["certificate_sha256"],
                    "certified_negative_rows": 0,
                    "unresolved_rows": 0,
                    "verdict": "NO_NEGATIVE_IN_DECLARED_ROWS",
                    "rows": [row],
                }
                self.write(
                    f"nearest-{count}-certificate-p{precision}.json", certificate
                )
                self.write(
                    f"nearest-{count}-verification-p{precision}.json", verification
                )
            comparison = {
                "all_high_intervals_nested": True,
                "low_artifact_sha256": MODULE.canonical_sha(certificates[384]),
                "high_artifact_sha256": MODULE.canonical_sha(certificates[512]),
            }
            self.write(
                f"nearest-{count}-precision-comparison-p384-p512.json",
                comparison,
            )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, name: str, value: dict) -> None:
        (self.root / name).write_text(json.dumps(value), encoding="utf-8")

    def test_summarizes_strict_complete_ladder(self) -> None:
        result = MODULE.summarize(self.root, self.block, 384, 512)
        self.assertEqual(result["finite_table_status"], "CERTIFIED_POSITIVE_FIXED_PR71_TABLE")
        self.assertEqual(result["closed_cell_count"], 8)
        self.assertTrue(result["final_rung_uses_requested_nearest_prefix"])
        self.assertEqual(result["guard_zero_ball_count"], 2)

    def test_comparison_digest_drift_is_rejected(self) -> None:
        path = self.root / "nearest-64-precision-comparison-p384-p512.json"
        comparison = json.loads(path.read_text(encoding="utf-8"))
        comparison["high_artifact_sha256"] = "0" * 64
        self.write(path.name, comparison)
        with self.assertRaisesRegex(MODULE.SummaryError, "precision nesting"):
            MODULE.summarize(self.root, self.block, 384, 512)

    def test_custom_increasing_rungs_are_supported(self) -> None:
        result = MODULE.summarize(
            self.root, self.block, 384, 512, counts=(64, 128)
        )
        self.assertEqual(result["closed_cell_count"], 2)
        self.assertEqual(
            [rung["nearest_count"] for rung in result["ladder_rungs"]],
            [64, 128],
        )


if __name__ == "__main__":
    unittest.main()
