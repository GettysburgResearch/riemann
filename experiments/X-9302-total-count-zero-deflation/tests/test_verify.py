from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE_PATH = ROOT / "verify_total_count_deflation.py"
CERT_PATH = ROOT / "certificates" / "synthetic-total-count-hidden-offline.json"

spec = importlib.util.spec_from_file_location("verify_total_count_deflation", MODULE_PATH)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class TotalCountDeflationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads(CERT_PATH.read_text())

    def test_synthetic_hidden_offline_zero_is_exposed(self) -> None:
        result = module.verify(copy.deepcopy(self.data))
        by_id = {row["id"]: row for row in result["rows"]}
        self.assertEqual(result["certified_negative_rows"], 2)
        self.assertEqual(result["unresolved_rows"], 0)
        self.assertEqual(by_id["raw-monotonicity-hidden"]["status"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(by_id["deflated-monotonicity-exposes"]["status"], "CERTIFIED_NEGATIVE")
        self.assertEqual(by_id["raw-loewner-hidden"]["status"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(by_id["deflated-loewner-exposes"]["status"], "CERTIFIED_NEGATIVE")

    def test_shell_increments_are_exact(self) -> None:
        data = copy.deepcopy(self.data)
        data["count_windows"] = [
            {
                "id": "r-half",
                "radius": {"numerator": 1, "denominator": 2},
                "count_lower": 8,
                "gate": {"status": module.SYNTHETIC_GATE, "sha256": "2" * 64},
            },
            {
                "id": "r-one",
                "radius": {"numerator": 1, "denominator": 1},
                "count_lower": 20,
                "gate": {"status": module.SYNTHETIC_GATE, "sha256": "3" * 64},
            },
        ]
        result = module.verify(data)
        self.assertEqual(
            [shell["count_increment"] for shell in result["deflation_shells"]],
            [8, 12],
        )
        self.assertEqual(
            [shell["distance_square_upper"] for shell in result["deflation_shells"]],
            [
                {"numerator": 1, "denominator": 4},
                {"numerator": 1, "denominator": 1},
            ],
        )

    def assert_rejected(self, data: dict, message: str) -> None:
        with self.assertRaisesRegex(module.CertificateError, message):
            module.verify(data)

    def test_decreasing_count_is_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        first = copy.deepcopy(data["count_windows"][0])
        first["id"] = "small"
        first["radius"] = {"numerator": 1, "denominator": 2}
        first["count_lower"] = 21
        data["count_windows"].insert(0, first)
        self.assert_rejected(data, "nondecreasing")

    def test_nonincreasing_radius_is_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        other = copy.deepcopy(data["count_windows"][0])
        other["id"] = "same-radius"
        data["count_windows"].append(other)
        self.assert_rejected(data, "strictly increasing")

    def test_wrong_gate_is_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["count_windows"][0]["gate"]["status"] = module.PRODUCTION_GATE
        self.assert_rejected(data, "gate status")

    def test_boolean_count_is_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["count_windows"][0]["count_lower"] = True
        self.assert_rejected(data, "must be an integer")

    def test_zero_final_count_is_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["count_windows"][0]["count_lower"] = 0
        self.assert_rejected(data, "final total-zero lower count")

    def test_false_point_digest_is_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["points"][0]["point_sha256"] = "0" * 64
        self.assert_rejected(data, "point digest mismatch")


if __name__ == "__main__":
    unittest.main()
