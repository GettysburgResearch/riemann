from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from verify_correction_budget import (  # noqa: E402
    CertificateError,
    SCHEMA,
    correction_budget,
    verify,
)


def rat(x: int, y: int = 1):
    return {"numerator": x, "denominator": y}


def base():
    return {
        "schema": SCHEMA,
        "cutoff_power10": 11,
        "cells": 1024,
        "carrier": rat(94184072727073, 20),
    }


class CorrectionBudgetTests(unittest.TestCase):
    def test_target_budget_is_below_one_over_750000(self):
        budget = correction_budget(
            cutoff_power10=11,
            cells=1024,
            carrier=Fraction(94184072727073, 20),
        )
        self.assertLess(budget["total"], Fraction(1, 750000))

    def test_safe_positive_margin_is_certified(self):
        data = base()
        data["leading_margin_interval"] = {
            "lower": rat(1, 4096),
            "upper": rat(1, 4096),
        }
        result = verify(data)
        self.assertTrue(result["certified_positive"])
        self.assertFalse(result["certified_negative"])

    def test_safe_negative_margin_is_certified(self):
        data = base()
        data["leading_margin_interval"] = {
            "lower": rat(-1, 4096),
            "upper": rat(-1, 4096),
        }
        result = verify(data)
        self.assertTrue(result["certified_negative"])
        self.assertFalse(result["certified_positive"])

    def test_zero_touch_is_unresolved(self):
        data = base()
        data["leading_margin_interval"] = {
            "lower": rat(-1, 10000000),
            "upper": rat(1, 10000000),
        }
        result = verify(data)
        self.assertEqual(result["verdict"], "UNRESOLVED")

    def test_bad_schema_is_rejected(self):
        data = base()
        data["schema"] = "wrong"
        with self.assertRaises(CertificateError):
            verify(data)

    def test_boolean_integer_is_rejected(self):
        data = base()
        data["cells"] = True
        with self.assertRaises(CertificateError):
            verify(data)

    def test_small_carrier_is_rejected(self):
        data = base()
        data["carrier"] = rat(8)
        with self.assertRaises(CertificateError):
            verify(data)


if __name__ == "__main__":
    unittest.main()
