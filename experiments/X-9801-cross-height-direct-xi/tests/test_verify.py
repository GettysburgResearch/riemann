from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x9801_verify", HERE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)


class VerifyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads(
            (HERE / "certificates" / "synthetic-negative.json").read_text()
        )

    def test_synthetic_negative(self) -> None:
        result = VERIFY.verify(copy.deepcopy(self.base))
        self.assertEqual(result["verdict"], "SYNTHETIC_STRICT_SEPARATION")
        self.assertEqual(result["difference_interval"]["upper"]["numerator"], -7)
        self.assertEqual(result["polynomial"]["distinct_real_roots"], 0)

    def test_height_sum_mutation_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["terms"][0]["exponent"] -= 1
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_duplicate_term_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["terms"].append(copy.deepcopy(data["terms"][0]))
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_reversed_response_polynomial_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        for term in data["terms"]:
            term["exponent"] = -term["exponent"]
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_missing_production_digest_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["classification"] = VERIFY.PRODUCTION
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_negative_h_interval_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["heights"][0]["points"][0]["h_interval"]["lower"]["numerator"] = -1
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_per_height_common_scaling_preserves_sign(self) -> None:
        baseline = VERIFY.verify(copy.deepcopy(self.base))
        data = copy.deepcopy(self.base)
        scales = {"minus": 3, "center": 5, "plus": 7}
        for height in data["heights"]:
            factor = 2 ** scales[height["id"]]
            height["common_xi_scale_power_of_two"] = scales[height["id"]]
            for point in height["points"]:
                point["h_interval"]["lower"]["numerator"] *= factor
                point["h_interval"]["upper"]["numerator"] *= factor
        result = VERIFY.verify(data)
        self.assertEqual(result["status"], baseline["status"])
        self.assertEqual(result["polynomial"], baseline["polynomial"])

    def test_bad_polynomial_gate_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["polynomial_gate"]["status"] = "MIDPOINT_ONLY"
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)


if __name__ == "__main__":
    unittest.main()
