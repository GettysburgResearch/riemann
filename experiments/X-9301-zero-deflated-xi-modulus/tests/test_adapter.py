from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "adapt_x7501_zero_deflation", ROOT / "adapt_x7501_zero_deflation.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def rat(n, d=1):
    return {"numerator": n, "denominator": d}


def point(identifier, x):
    return {
        "id": identifier,
        "x": rat(x),
        "xi_rectangle": {
            "real": {"lower": rat(x + 1), "upper": rat(x + 1)},
            "imag": {"lower": rat(0), "upper": rat(0)},
        },
        "point_sha256": "f" * 64,
    }


class AdapterTests(unittest.TestCase):
    def source(self):
        return {
            "schema": MODULE.SOURCE_SCHEMA,
            "classification": "SYNTHETIC_MODEL",
            "normalization_id": MODULE.NORMALIZATION,
            "ordinate": rat(10),
            "points": [point("p1", 1), point("p2", 2), point("p3", 3), point("p4", 4)],
            "certificate_sha256": "e" * 64,
        }

    def config(self):
        return {
            "schema": MODULE.CONFIG_SCHEMA,
            "normalization_id": MODULE.NORMALIZATION,
            "log_terms": 128,
            "zero_bins": [
                {
                    "id": "z",
                    "lower_ordinate": rat(9),
                    "upper_ordinate": rat(9),
                    "count_lower": 1,
                    "gate": {
                        "status": "CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND",
                        "sha256": "a" * 64,
                    },
                }
            ],
            "rows": [
                {
                    "id": "d",
                    "kind": "deflated-cross-loewner-determinant",
                    "rows": ["p1", "p3"],
                    "columns": ["p2", "p4"],
                }
            ],
        }

    def test_adapter_squares_horizontal_offsets(self):
        output = MODULE.adapt(self.source(), self.config())
        self.assertEqual(output["schema"], MODULE.OUTPUT_SCHEMA)
        by_id = {point["id"]: point for point in output["points"]}
        self.assertEqual(by_id["p3"]["u"], rat(9))
        self.assertEqual(len(output["points"]), 4)

    def test_missing_source_point_rejected(self):
        config = self.config()
        config["rows"][0]["columns"][1] = "missing"
        with self.assertRaises(MODULE.AdapterError):
            MODULE.adapt(self.source(), config)

    def test_boolean_log_terms_rejected(self):
        config = self.config()
        config["log_terms"] = True
        with self.assertRaises(MODULE.AdapterError):
            MODULE.adapt(self.source(), config)

    def test_production_source_is_not_promoted_without_artifact_binding(self):
        source = self.source()
        source["classification"] = "RIEMANN_XI_DIRECTED"
        with self.assertRaisesRegex(MODULE.AdapterError, "production.*disabled"):
            MODULE.adapt(source, self.config())


if __name__ == "__main__":
    unittest.main()
