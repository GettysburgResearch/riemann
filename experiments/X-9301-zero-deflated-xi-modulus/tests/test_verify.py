from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_zero_deflated_modulus", ROOT / "verify_zero_deflated_modulus.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

CERT = ROOT / "certificates" / "synthetic-hidden-offline-zero.json"


class ZeroDeflatedModulusTests(unittest.TestCase):
    def load(self):
        return json.loads(CERT.read_text(encoding="utf-8"))

    def test_hidden_offline_control(self):
        result = MODULE.verify(self.load())
        self.assertEqual(result["verdict"], "SYNTHETIC_ZERO_DEFLATION_SEPARATION")
        self.assertEqual(result["certified_negative_rows"], 2)
        self.assertEqual(result["unresolved_rows"], 0)
        statuses = {row["id"]: row["status"] for row in result["rows"]}
        self.assertEqual(statuses["raw-monotonicity-hidden"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(statuses["raw-loewner-hidden"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(statuses["deflated-monotonicity-exposes"], "CERTIFIED_NEGATIVE")
        self.assertEqual(statuses["deflated-loewner-exposes"], "CERTIFIED_NEGATIVE")

    def test_exact_algebraic_monotonicity_value(self):
        result = MODULE.verify(self.load())
        row = next(
            item for item in result["rows"] if item["id"] == "deflated-monotonicity-exposes"
        )
        lower = MODULE.rational(row["interval"]["lower"], "lower")
        upper = MODULE.rational(row["interval"]["upper"], "upper")
        self.assertEqual(lower, upper)
        self.assertEqual(lower, -314572800000000000000000000)

    def test_overlapping_zero_bins_rejected(self):
        data = self.load()
        data["zero_bins"].append(
            {
                "id": "overlap",
                "lower_ordinate": {"numerator": 1, "denominator": 1},
                "upper_ordinate": {"numerator": 2, "denominator": 1},
                "count_lower": 1,
                "gate": {
                    "status": MODULE.SYNTHETIC_GATE,
                    "sha256": "2" * 64,
                },
            }
        )
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_zero_count_rejected(self):
        data = self.load()
        data["zero_bins"][0]["count_lower"] = 0
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_production_gate_required(self):
        data = self.load()
        data["classification"] = "RIEMANN_XI_DIRECTED"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_point_digest_mutation_rejected(self):
        data = self.load()
        data["points"][0]["xi_rectangle"]["real"]["lower"]["numerator"] += 1
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_loewner_row_column_collision_rejected(self):
        data = self.load()
        row = next(
            item for item in data["rows"] if item["id"] == "deflated-loewner-exposes"
        )
        row["columns"][0] = row["rows"][0]
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_boolean_count_rejected(self):
        data = self.load()
        data["zero_bins"][0]["count_lower"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_widened_bin_remains_valid_but_weaker(self):
        data = self.load()
        data["zero_bins"][0]["upper_ordinate"] = {"numerator": 2, "denominator": 1}
        result = MODULE.verify(data)
        self.assertEqual(
            result["zero_bins"][0]["distance_square_upper"],
            {"numerator": 4, "denominator": 1},
        )


if __name__ == "__main__":
    unittest.main()
