from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("leverage_checker", ROOT / "verify_leverage_budget.py")
checker = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["leverage_checker"] = checker
SPEC.loader.exec_module(checker)


def rat(n: int, d: int = 1) -> dict[str, int]:
    return {"numerator": n, "denominator": d}


def iv(lo_n: int, lo_d: int, hi_n: int | None = None, hi_d: int | None = None):
    if hi_n is None:
        hi_n, hi_d = lo_n, lo_d
    return {"lower": rat(lo_n, lo_d), "upper": rat(hi_n, hi_d or 1)}


def base_payload() -> dict:
    return {
        "schema": checker.SCHEMA,
        "classification": "SYNTHETIC",
        "side": "lower",
        "w": rat(1),
        "support_lower": rat(0),
        "nodes": [],
        "q": [rat(1)],
        "gap": iv(3, 4),
        "zero_bins": [
            {
                "id": "z1",
                "y": iv(1, 1),
                "multiplicity": 1,
                "gate": {"status": checker.ZERO_GATE, "sha256": "synthetic"},
            }
        ],
    }


def verify_payload(payload: dict) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "certificate.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return checker.verify(path)


class LeverageBudgetTests(unittest.TestCase):
    def test_consistent_lower_budget(self) -> None:
        result = verify_payload(base_payload())
        self.assertEqual(result["verdict"], "CERTIFIED_CONSISTENT_PADE_LINE_MASS_BUDGET")
        contribution = result["certified_line_mass_contribution"]["lower"]
        self.assertEqual(contribution, rat(1, 2))

    def test_negative_lower_budget(self) -> None:
        payload = base_payload()
        payload["gap"] = iv(2, 5)
        result = verify_payload(payload)
        self.assertEqual(result["verdict"], "CERTIFIED_NEGATIVE_PADE_LINE_MASS_BUDGET")

    def test_negative_upper_budget(self) -> None:
        payload = base_payload()
        payload["side"] = "upper"
        payload["gap"] = iv(7, 10)
        payload["zero_bins"][0]["y"] = iv(3, 1)
        result = verify_payload(payload)
        self.assertEqual(result["verdict"], "CERTIFIED_NEGATIVE_PADE_LINE_MASS_BUDGET")
        self.assertEqual(result["certified_line_mass_contribution"]["lower"], rat(3, 4))

    def test_rejects_overlapping_bins(self) -> None:
        payload = base_payload()
        payload["zero_bins"].append(
            {
                "id": "z2",
                "y": iv(1, 1, 2, 1),
                "multiplicity": 1,
                "gate": {"status": checker.ZERO_GATE},
            }
        )
        with self.assertRaises(checker.CertificateError):
            verify_payload(payload)

    def test_rejects_bad_endpoint_normalization(self) -> None:
        payload = base_payload()
        payload["q"] = [rat(2)]
        with self.assertRaises(checker.CertificateError):
            verify_payload(payload)

    def test_rejects_bin_below_support(self) -> None:
        payload = base_payload()
        payload["support_lower"] = rat(2)
        with self.assertRaises(checker.CertificateError):
            verify_payload(payload)

    def test_rejects_bad_gate(self) -> None:
        payload = base_payload()
        payload["zero_bins"][0]["gate"]["status"] = "EMPIRICAL_ZERO"
        with self.assertRaises(checker.CertificateError):
            verify_payload(payload)


if __name__ == "__main__":
    unittest.main()
