from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "anchor_line_mass_verify", ROOT / "verify.py"
)
assert SPEC is not None and SPEC.loader is not None
verify = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = verify
SPEC.loader.exec_module(verify)


def load(name: str) -> dict:
    return json.loads(
        (ROOT / "certificates" / name).read_text(encoding="utf-8")
    )


def fraction(numerator: int, denominator: int = 1) -> dict[str, str]:
    return {
        "numerator": str(numerator),
        "denominator": str(denominator),
    }


class AnchorLineMassTests(unittest.TestCase):
    def test_strict_contradiction(self) -> None:
        result = verify.verify(load("synthetic-contradiction.json"))
        self.assertEqual(
            result["status"],
            "CERTIFIED_LINE_MASS_BUDGET_CONTRADICTION",
        )
        self.assertEqual(
            result["verification_sha256"],
            "19a9978824d8bdfb9f6dc6287439e097fe6c7529ab7e39e5ed37cb607d543f60",
        )

    def test_consistent_control(self) -> None:
        result = verify.verify(load("synthetic-consistent.json"))
        self.assertEqual(
            result["status"], "NO_STRICT_LINE_MASS_CONTRADICTION"
        )
        self.assertFalse(result["strict_reversal"])

    def test_removed_bin_is_rejected(self) -> None:
        data = load("synthetic-contradiction.json")
        data["zero_bins"][0]["survives_source_measure"] = False
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_overlapping_bins_are_rejected(self) -> None:
        data = load("synthetic-contradiction.json")
        second = copy.deepcopy(data["zero_bins"][0])
        second["id"] = "bin-two"
        data["zero_bins"].append(second)
        data["declared_bin_ids"] = ["bin-one", "bin-two"]
        data.pop("claimed_leverage_sum")
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_claimed_leverage_mutation_is_rejected(self) -> None:
        data = load("synthetic-contradiction.json")
        data["zero_bins"][0]["claimed_leverage_lower"] = fraction(1, 5)
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_polynomial_root_crossing_fails_closed(self) -> None:
        data = load("synthetic-contradiction.json")
        data["polynomial"] = [fraction(-1), fraction(1)]
        data["zero_bins"][0]["gamma_interval"] = {
            "lower": fraction(1, 2),
            "upper": fraction(3, 2),
        }
        data["zero_bins"][0].pop("claimed_leverage_lower")
        data.pop("claimed_leverage_sum")
        data["total_interval"] = {
            "lower": fraction(0),
            "upper": fraction(0),
        }
        result = verify.verify(data)
        self.assertEqual(
            result["line_mass_leverage_lower"], fraction(0)
        )
        self.assertFalse(result["strict_reversal"])

    def test_y_square_channel(self) -> None:
        data = load("synthetic-contradiction.json")
        data["channel"] = "y-square"
        data["zero_bins"][0]["gamma_interval"] = {
            "lower": fraction(2),
            "upper": fraction(2),
        }
        data["zero_bins"][0]["claimed_leverage_lower"] = fraction(2, 15)
        data["claimed_leverage_sum"] = fraction(2, 15)
        result = verify.verify(data)
        self.assertTrue(result["strict_reversal"])
        self.assertEqual(
            result["line_mass_leverage_lower"], fraction(2, 15)
        )

    def test_boolean_multiplicity_is_rejected(self) -> None:
        data = load("synthetic-contradiction.json")
        data["zero_bins"][0]["multiplicity_lower"] = True
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)

    def test_decorative_declared_bin_is_rejected(self) -> None:
        data = load("synthetic-contradiction.json")
        data["declared_bin_ids"].append("decorative")
        with self.assertRaises(verify.CertificateError):
            verify.verify(data)


if __name__ == "__main__":
    unittest.main()
