from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify_count_only", HERE / "verify.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class CountOnlySupportChordTests(unittest.TestCase):
    def control(self):
        return json.loads(
            (
                HERE
                / "certificates"
                / "synthetic-empty-slab-hidden-factor.json"
            ).read_text()
        )

    def test_exact_synthetic_negative(self):
        result = module.verify(self.control())
        self.assertEqual(result["verdict"], "SYNTHETIC_COUNT_ONLY_SEPARATION")
        self.assertEqual(result["certified_negative_rows"], 1)
        self.assertEqual(result["rows"][0]["status"], "CERTIFIED_NEGATIVE")

    def test_counted_factor_at_zero_is_nonnegative(self):
        data = self.control()
        data["synthetic_factors"][0]["y"] = {
            "numerator": 0,
            "denominator": 1,
        }
        data["total_count_interval"] = {
            "lower": {"numerator": 1, "denominator": 1},
            "upper": {"numerator": 1, "denominator": 1},
        }
        result = module.verify(data)
        self.assertEqual(result["certified_negative_rows"], 0)
        interval = result["rows"][0]["interval"]
        self.assertLessEqual(
            interval["lower"]["numerator"] / interval["lower"]["denominator"],
            0,
        )
        self.assertGreaterEqual(
            interval["upper"]["numerator"] / interval["upper"]["denominator"],
            0,
        )

    def test_outside_factor_passes_with_zero_count(self):
        data = self.control()
        data["synthetic_factors"][0]["y"] = {
            "numerator": 2,
            "denominator": 1,
        }
        result = module.verify(data)
        self.assertEqual(result["certified_negative_rows"], 0)
        self.assertEqual(result["rows"][0]["status"], "CERTIFIED_NONNEGATIVE")

    def test_production_requires_count_gate(self):
        data = self.control()
        data["classification"] = module.PRODUCTION
        data.pop("synthetic_factors")
        for point in data["points"]:
            point["xi_rectangle"] = {
                "real": {
                    "lower": {"numerator": 1, "denominator": 1},
                    "upper": {"numerator": 1, "denominator": 1},
                },
                "imag": {
                    "lower": {"numerator": 0, "denominator": 1},
                    "upper": {"numerator": 0, "denominator": 1},
                },
            }
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_ambiguous_count_rejected(self):
        data = self.control()
        data["total_count_interval"]["upper"] = {
            "numerator": 1,
            "denominator": 1,
        }
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_zero_base_node_rejected(self):
        data = self.control()
        data["points"][0]["u"] = {"numerator": 0, "denominator": 1}
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_target_outside_slab_rejected(self):
        data = self.control()
        data["target"] = {"numerator": 2, "denominator": 1}
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_duplicate_row_rejected(self):
        data = self.control()
        data["rows"].append(copy.deepcopy(data["rows"][0]))
        with self.assertRaises(module.CertificateError):
            module.verify(data)


if __name__ == "__main__":
    unittest.main()
