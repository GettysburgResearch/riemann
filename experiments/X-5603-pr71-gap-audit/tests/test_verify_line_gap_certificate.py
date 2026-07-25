from __future__ import annotations

import copy
import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "verify_line_gap_certificate",
    HERE.parent / "verify_line_gap_certificate.py",
)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


def binary_interval(lower: int, upper: int, exponent: int = 0):
    return {
        "lower": {"mantissa": str(lower), "exponent": str(exponent)},
        "upper": {"mantissa": str(upper), "exponent": str(exponent)},
    }


def base(discrepancy: int = 2):
    return {
        "schema": MOD.SCHEMA,
        "target": {"numerator": "2", "denominator": "1"},
        "lower_hardy_zero_ball": binary_interval(0, 0),
        "upper_hardy_zero_ball": binary_interval(4, 4),
        "interior_slab_lower_exact": binary_interval(1, 1),
        "interior_slab_upper_exact": binary_interval(3, 3),
        "lower_hardy_zero_index": "1000",
        "upper_hardy_zero_index": "1001",
        "N_lower_ball": binary_interval(2000, 2000),
        "N_upper_ball": binary_interval(2000 + discrepancy, 2000 + discrepancy),
        "N_lower": "2000",
        "N_upper": str(2000 + discrepancy),
        "total_zero_discrepancy_in_line_empty_slab": str(discrepancy),
        "classification": (
            "CERTIFIED_EMPTY_FULL_STRIP_INTERIOR_SLAB"
            if discrepancy == 0
            else "CERTIFIED_OFF_CRITICAL_ZERO_IN_LINE_EMPTY_SLAB"
        ),
    }


class LineGapCheckerTests(unittest.TestCase):
    def test_positive_even_discrepancy(self):
        result = MOD.verify(base(2))
        self.assertTrue(result["verified"])
        self.assertEqual(result["total_zero_discrepancy"], "2")
        self.assertIn("OFF_CRITICAL", result["status"])

    def test_zero_discrepancy(self):
        result = MOD.verify(base(0))
        self.assertEqual(result["status"], "CERTIFIED_EMPTY_FULL_STRIP_INTERIOR_SLAB")
        self.assertIsNone(result["counterexample_candidate"])

    def test_odd_discrepancy_rejected(self):
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(base(1))

    def test_nonconsecutive_hardy_indices_rejected(self):
        data = base(0)
        data["upper_hardy_zero_index"] = "1002"
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(data)

    def test_slab_touching_zero_ball_rejected(self):
        data = base(0)
        data["lower_hardy_zero_ball"] = binary_interval(0, 1)
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(data)

    def test_nonunique_count_ball_rejected(self):
        data = base(0)
        data["N_lower_ball"] = binary_interval(2000, 2001)
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(data)

    def test_false_classification_rejected(self):
        data = base(2)
        data["classification"] = "CERTIFIED_EMPTY_FULL_STRIP_INTERIOR_SLAB"
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(data)

    def test_mutated_claimed_count_rejected(self):
        data = copy.deepcopy(base(2))
        data["N_upper"] = "2003"
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(data)


if __name__ == "__main__":
    unittest.main()
