from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from verify_variation_budget import (  # noqa: E402
    CertificateError,
    SCHEMA,
    variation_budget,
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


class VariationBudgetTests(unittest.TestCase):
    def test_target_budget_is_below_one_over_two_billion(self):
        value = variation_budget(
            cutoff_power10=11,
            cells=1024,
            carrier=Fraction(94184072727073, 20),
        )
        self.assertLess(value["total"], Fraction(1, 2_000_000_000))

    def test_exact_target_components(self):
        value = variation_budget(
            cutoff_power10=11,
            cells=1024,
            carrier=Fraction(94184072727073, 20),
        )
        self.assertEqual(
            value["archimedean"], Fraction(481650, 1036024799997803)
        )
        self.assertEqual(
            value["pole"],
            Fraction(24115570278400, 26611918666375728273441441987),
        )

    def test_safe_positive_margin_is_certified(self):
        data = base()
        data["leading_margin_interval"] = {
            "lower": rat(1, 1_000_000),
            "upper": rat(1, 1_000_000),
        }
        result = verify(data)
        self.assertTrue(result["certified_positive"])

    def test_safe_negative_margin_is_certified(self):
        data = base()
        data["leading_margin_interval"] = {
            "lower": rat(-1, 1_000_000),
            "upper": rat(-1, 1_000_000),
        }
        result = verify(data)
        self.assertTrue(result["certified_negative"])

    def test_zero_touch_is_unresolved(self):
        data = base()
        data["leading_margin_interval"] = {
            "lower": rat(-1, 10_000_000_000),
            "upper": rat(1, 10_000_000_000),
        }
        result = verify(data)
        self.assertEqual(result["verdict"], "UNRESOLVED")

    def test_non_power_two_cells_are_supported(self):
        value = variation_budget(
            cutoff_power10=3,
            cells=3,
            carrier=Fraction(100),
        )
        self.assertEqual(value["log2_cells_ceiling"], 2)

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


if __name__ == "__main__":
    unittest.main()
