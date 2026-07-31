from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x14307_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
mod = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mod
SPEC.loader.exec_module(mod)


class ExactProlateSourceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.data = json.loads((ROOT / "certificates" / "synthetic-exact.json").read_text())

    def test_passes_exact_control(self) -> None:
        result = mod.verify_certificate(copy.deepcopy(self.data))
        self.assertEqual(result["three_mode"]["normalized_leakage_squared"], "6/19")
        self.assertEqual(result["radical_tail"]["projective_residual_squared"], "4/11")
        self.assertEqual(result["verdict"], "CERTIFIED_EXACT_SOURCE_AND_PROJECTIVE_RADICAL_TAIL")

    def test_rejects_wrong_eigenvalue_order(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["three_mode"]["modes"][1]["concentration_eigenvalue"] = "19/20"
        with self.assertRaises(mod.VerificationError):
            mod.verify_certificate(bad)

    def test_rejects_zero_cross_product(self) -> None:
        bad = copy.deepcopy(self.data)
        for row in bad["three_mode"]["modes"]:
            row["concentration_eigenvalue"] = "1/2"
        with self.assertRaises(mod.VerificationError):
            mod.verify_certificate(bad)

    def test_rejects_false_claimed_leakage(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["three_mode"]["expected"]["normalized_leakage_squared"] = "1/3"
        with self.assertRaises(mod.VerificationError):
            mod.verify_certificate(bad)

    def test_rejects_nonradical_vector(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["radical_tail"]["radical_vector"][2] = "2"
        with self.assertRaises(mod.VerificationError):
            mod.verify_certificate(bad)

    def test_rejects_nonsymmetric_form(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["radical_tail"]["form_matrix"][0][1] = "-3"
        with self.assertRaises(mod.VerificationError):
            mod.verify_certificate(bad)

    def test_rejects_indefinite_weight(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["radical_tail"]["localized_weight"][1][1] = "-1"
        with self.assertRaises(mod.VerificationError):
            mod.verify_certificate(bad)

    def test_rejects_boolean_fraction(self) -> None:
        bad = copy.deepcopy(self.data)
        bad["three_mode"]["modes"][0]["value_at_zero"] = True
        with self.assertRaises(mod.VerificationError):
            mod.verify_certificate(bad)


if __name__ == "__main__":
    unittest.main()
