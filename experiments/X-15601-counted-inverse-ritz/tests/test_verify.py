from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SPEC = importlib.util.spec_from_file_location("x15601_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class CountedInverseRitzTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads((ROOT / "certificates" / "synthetic-counted-floor.json").read_text())

    def test_synthetic_certificate(self) -> None:
        result = MOD.verify(self.data)
        self.assertEqual(result["verdict"], "CERTIFIED_COUNTED_INVERSE_RITZ_AMBIENT_FLOOR")
        self.assertEqual(result["certified_floor"], {"numerator": -3, "denominator": 4996})

    def test_count_cap_is_load_bearing(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["count_subspace"] = [
            [{"numerator": 0, "denominator": 1}],
            [{"numerator": 1, "denominator": 1}],
        ]
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_nonnegative_q_rejected(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["q_upper"] = {"numerator": 1, "denominator": 1}
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_optimistic_q_rejected(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["q_upper"] = {"numerator": -3, "denominator": 1}
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_shifted_form_must_be_negative(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["t"] = {"numerator": -1, "denominator": 1}
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_claimed_floor_cannot_exceed_formula(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["claimed_floor"] = {"numerator": 0, "denominator": 1}
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_boolean_integer_rejected(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["dimension"] = True
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_production_requires_typed_count_gate(self) -> None:
        bad = {
            "schema": MOD.SCHEMA,
            "classification": MOD.PRODUCTION,
            "dimension": 1,
            "gamma": {"numerator": 1, "denominator": 2},
            "t": {"numerator": 1, "denominator": 4},
            "q_upper": {"numerator": -4, "denominator": 1},
            "claimed_floor": {"numerator": 0, "denominator": 1},
            "H_upper": [[{"numerator": -1, "denominator": 4}]],
            "K_lower": [[{"numerator": 1, "denominator": 16}]],
            "K_upper": [[{"numerator": 1, "denominator": 16}]],
        }
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(bad)

    def test_valid_production_packet(self) -> None:
        data = {
            "schema": MOD.SCHEMA,
            "classification": MOD.PRODUCTION,
            "dimension": 1,
            "gamma": {"numerator": 1, "denominator": 2},
            "t": {"numerator": 1, "denominator": 4},
            "q_upper": {"numerator": -1249, "denominator": 313},
            "claimed_floor": {"numerator": -3, "denominator": 4996},
            "count_gate": {
                "status": MOD.COUNT_STATUS,
                "cap": 1,
                "gamma": {"numerator": 1, "denominator": 2},
                "source_sha256": "a" * 64,
                "analytic_claim": "L-14311"
            },
            "H_upper": [[{"numerator": -1, "denominator": 4}]],
            "K_lower": [[{"numerator": 313, "denominator": 5000}]],
            "K_upper": [[{"numerator": 313, "denominator": 5000}]],
        }
        result = MOD.verify(data)
        self.assertEqual(result["certified_floor"], {"numerator": -3, "denominator": 4996})


if __name__ == "__main__":
    unittest.main()
