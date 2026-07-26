from __future__ import annotations
import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_sign_chain", ROOT / "verify_sign_chain.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
BASE = json.loads(
    (ROOT / "certificates" / "synthetic-saturated-chain.json").read_text()
)


class TestSignChain(unittest.TestCase):
    def test_valid_chain_and_refinement(self) -> None:
        output = MODULE.verify(copy.deepcopy(BASE))
        self.assertEqual(
            output["verdict"], "SATURATED_SIGN_CHAIN_ISOLATES_ALL_ZEROS"
        )
        self.assertEqual(len(output["bins"]), 3)
        self.assertEqual(
            output["bins"][0]["lower"], {"numerator": 2, "denominator": 1}
        )
        self.assertEqual(
            output["bins"][0]["upper"], {"numerator": 5, "denominator": 2}
        )
        self.assertTrue(all(row["simple"] for row in output["bins"]))

    def test_total_count_must_isolate_one_integer(self) -> None:
        data = copy.deepcopy(BASE)
        data["total_count_interval"]["upper"] = {
            "numerator": 401,
            "denominator": 100,
        }
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_unresolved_sign_rejected(self) -> None:
        data = copy.deepcopy(BASE)
        data["samples"][1]["z_interval"] = {
            "lower": {"numerator": -1, "denominator": 1},
            "upper": {"numerator": 1, "denominator": 1},
        }
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_missing_alternation_rejected(self) -> None:
        data = copy.deepcopy(BASE)
        data["samples"][1]["z_interval"] = {
            "lower": {"numerator": 1, "denominator": 1},
            "upper": {"numerator": 2, "denominator": 1},
        }
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_refinement_point_must_lie_in_current_bin(self) -> None:
        data = copy.deepcopy(BASE)
        data["refinements"][0]["steps"][1]["t"] = {
            "numerator": 4,
            "denominator": 1,
        }
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_production_requires_semantic_gates(self) -> None:
        data = copy.deepcopy(BASE)
        data["classification"] = MODULE.PRODUCTION
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()
