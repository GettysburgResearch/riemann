from decimal import Decimal
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from curvature_nominee_matched_scan import build_template as build_nominee_template
from wide_curvature_scan import (
    deterministic_centers,
    summarize_window,
    van_der_corput_base2,
)


class CurvatureNominationTests(unittest.TestCase):
    def test_van_der_corput_controls(self) -> None:
        self.assertEqual(van_der_corput_base2(1), Decimal("0.5"))
        self.assertEqual(van_der_corput_base2(2), Decimal("0.25"))
        self.assertEqual(van_der_corput_base2(3), Decimal("0.75"))
        self.assertEqual(van_der_corput_base2(4), Decimal("0.125"))
        with self.assertRaises(ValueError):
            van_der_corput_base2(0)

    def test_deterministic_centers(self) -> None:
        centers = deterministic_centers(96)
        self.assertEqual(len(centers), 96)
        self.assertEqual(len(set(centers)), 96)
        self.assertEqual(centers[0], "4000000000000.1234")
        self.assertEqual(centers[1], "3500000000000.1234")
        self.assertTrue(all(Decimal("3000000000000") < Decimal(x) < Decimal("5000000000001") for x in centers))

    def test_synthetic_window_summary(self) -> None:
        data = {
            "curvature": {
                "negative_samples": 0,
                "minimum_curvature": "12.5",
                "minimum_t": "4000000000000.25",
            }
        }
        row = summarize_window(data, index=7, center="4000000000000.1234")
        self.assertEqual(row["window_index"], 7)
        self.assertEqual(row["minimum_curvature"], 12.5)
        self.assertEqual(row["nominee_t"], "4000000000000.25")
        self.assertEqual(row["positive_negative_count_fields"], [])

    def test_nominee_template_size(self) -> None:
        nominees = {
            "schema": "riemann.xi-wide-curvature-nomination.v1",
            "parameters": {"window_count": 96},
            "top_nominees": [
                {"nominee_t": f"{3000000000000 + index}.125", "minimum_curvature": index + 1}
                for index in range(12)
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "nominees.json"
            path.write_text(json.dumps(nominees), encoding="utf-8")
            template, metadata = build_nominee_template(path, 8)
        self.assertEqual(len(template["points"]), 152)
        self.assertEqual(len(template["channels"]), 6048)
        self.assertEqual(len(metadata), 6048)
        self.assertEqual(template["metadata"]["experiment_id"], "X-3904")


if __name__ == "__main__":
    unittest.main()
