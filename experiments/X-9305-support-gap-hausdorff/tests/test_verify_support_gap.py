from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "verify_support_gap", HERE / "verify_support_gap.py"
)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class SupportGapTests(unittest.TestCase):
    def load_control(self):
        return json.loads(
            (HERE / "certificates" / "synthetic-inside-gap-factor.json").read_text()
        )

    def test_synthetic_strict_separation(self):
        result = module.verify(self.load_control())
        statuses = {row["id"]: row["status"] for row in result["rows"]}
        self.assertEqual(result["verdict"], "SYNTHETIC_SUPPORT_GAP_SEPARATION")
        self.assertEqual(statuses["chord-inside-gap"], "CERTIFIED_NEGATIVE")
        self.assertEqual(statuses["first-difference"], "CERTIFIED_NEGATIVE")
        self.assertEqual(
            statuses["ordinary-hankel-control"], "CERTIFIED_NONNEGATIVE"
        )
        self.assertEqual(statuses["support-localizer"], "CERTIFIED_NEGATIVE")

    def test_boundary_factor_has_zero_support_rows(self):
        data = self.load_control()
        data["synthetic_factors"][0]["y"] = {"numerator": 1, "denominator": 1}
        data["derivative_base"]["derivatives"] = [
            {
                "order": 1,
                "interval": {
                    "lower": {"numerator": 1, "denominator": 1},
                    "upper": {"numerator": 1, "denominator": 1},
                },
            },
            {
                "order": 2,
                "interval": {
                    "lower": {"numerator": -1, "denominator": 1},
                    "upper": {"numerator": -1, "denominator": 1},
                },
            },
            {
                "order": 3,
                "interval": {
                    "lower": {"numerator": 2, "denominator": 1},
                    "upper": {"numerator": 2, "denominator": 1},
                },
            },
            {
                "order": 4,
                "interval": {
                    "lower": {"numerator": -6, "denominator": 1},
                    "upper": {"numerator": -6, "denominator": 1},
                },
            },
            {
                "order": 5,
                "interval": {
                    "lower": {"numerator": 24, "denominator": 1},
                    "upper": {"numerator": 24, "denominator": 1},
                },
            },
        ]
        result = module.verify(data)
        rows = {row["id"]: row for row in result["rows"]}
        self.assertEqual(
            rows["first-difference"]["interval"]["lower"]["numerator"], 0
        )
        self.assertEqual(
            rows["support-localizer"]["interval"]["lower"]["numerator"], 0
        )
        self.assertEqual(result["certified_negative_rows"], 0)

    def test_production_requires_support_gate(self):
        data = self.load_control()
        data["classification"] = module.PRODUCTION
        data.pop("synthetic_factors")
        for row in data["values"]:
            row["residual_log"] = {
                "lower": {"numerator": 0, "denominator": 1},
                "upper": {"numerator": 0, "denominator": 1},
            }
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_missing_derivative_rejected(self):
        data = self.load_control()
        data["derivative_base"]["derivatives"] = data["derivative_base"][
            "derivatives"
        ][:1]
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_nonpositive_support_rejected(self):
        data = self.load_control()
        data["support_gap"] = {"numerator": 0, "denominator": 1}
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_duplicate_row_rejected(self):
        data = self.load_control()
        data["rows"].append(copy.deepcopy(data["rows"][0]))
        with self.assertRaises(module.CertificateError):
            module.verify(data)


if __name__ == "__main__":
    unittest.main()
