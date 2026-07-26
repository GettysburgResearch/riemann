from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SPEC = importlib.util.spec_from_file_location("verify_x9704", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)


class PositiveNodeGeronimusTests(unittest.TestCase):
    def setUp(self) -> None:
        self.certificate = json.loads(
            (ROOT / "certificates" / "synthetic-positive.json").read_text()
        )

    def test_positive_full_cone(self) -> None:
        result = VERIFY.verify(copy.deepcopy(self.certificate))
        self.assertEqual(
            result["verdict"],
            "CERTIFIED_POSITIVE_FULL_NEXT_DEGREE_HALF_LINE_CONE",
        )
        self.assertTrue(result["g0_robust_positive"])
        self.assertTrue(result["g1_robust_positive"])
        self.assertEqual(result["negative_rows"], [])

    def test_lower_square_witness(self) -> None:
        certificate = copy.deepcopy(self.certificate)
        certificate["b0_interval"] = {
            "lower": {"numerator": 0, "denominator": 1},
            "upper": {"numerator": 0, "denominator": 1},
        }
        result = VERIFY.verify(certificate)
        self.assertEqual(result["negative_rows"][0]["kind"], "square")
        upper = VERIFY.rat(
            result["negative_rows"][0]["interval"]["upper"], "upper"
        )
        self.assertLess(upper, 0)

    def test_upper_y_square_witness(self) -> None:
        certificate = copy.deepcopy(self.certificate)
        certificate["b0_interval"] = {
            "lower": {"numerator": 10, "denominator": 1},
            "upper": {"numerator": 10, "denominator": 1},
        }
        result = VERIFY.verify(certificate)
        self.assertEqual(result["negative_rows"][0]["kind"], "y-square")

    def test_reject_even_old_moment_count(self) -> None:
        certificate = copy.deepcopy(self.certificate)
        certificate["old_moments"].pop()
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(certificate)

    def test_reject_nonpositive_new_node(self) -> None:
        certificate = copy.deepcopy(self.certificate)
        certificate["w"] = {"numerator": 0, "denominator": 1}
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(certificate)

    def test_production_requires_bound_sources(self) -> None:
        certificate = copy.deepcopy(self.certificate)
        certificate["classification"] = VERIFY.PRODUCTION
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(certificate)

    def test_wide_b0_interval_is_unresolved_not_midpoint_positive(self) -> None:
        certificate = copy.deepcopy(self.certificate)
        certificate["b0_interval"] = {
            "lower": {"numerator": 0, "denominator": 1},
            "upper": {"numerator": 10, "denominator": 1},
        }
        result = VERIFY.verify(certificate)
        self.assertEqual(result["verdict"], "UNRESOLVED")
        self.assertFalse(result["g0_robust_positive"])
        self.assertFalse(result["g1_robust_positive"])


if __name__ == "__main__":
    unittest.main()
