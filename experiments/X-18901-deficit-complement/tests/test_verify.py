from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x18901_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class DeficitComplementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads((ROOT / "certificates" / "synthetic.json").read_text(encoding="utf-8"))

    def test_valid_certificate(self) -> None:
        result = MODULE.verify(copy.deepcopy(self.base))
        self.assertTrue(result["verified"])
        self.assertEqual(result["augmentation_rank"], 2)
        self.assertEqual(
            result["verdict"],
            "CERTIFIED_CANONICAL_AUGMENTED_COMPLEMENT_FLOOR",
        )

    def test_missing_dangerous_mode_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["augmentation_basis"] = [[0], [1], [0], [0]]
        data["complement_basis"] = [[0, 0], [0, 0], [1, 0], [0, 1]]
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_nonorthogonal_decomposition_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["complement_basis"] = [[1], [0], [0], [1]]
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_false_lower_model_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["operator"][3][3] = 0
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_negative_deficit_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["deficit"][3][3] = -1
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_wrong_spectral_cross_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["deficit"][2][3] = {"numerator": 1, "denominator": 10}
        data["deficit"][3][2] = {"numerator": 1, "denominator": 10}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_nonpositive_target_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["target_floor"] = 0
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_boolean_rational_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["target_floor"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_incomplete_basis_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["augmentation_basis"] = [[0], [1], [0], [0]]
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()
