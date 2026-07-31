from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x15409_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
VERIFY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)


class BlaschkePairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(
            (ROOT / "certificates" / "synthetic.json").read_text(encoding="utf-8")
        )

    def test_committed_certificate(self) -> None:
        result = VERIFY.verify(copy.deepcopy(self.data))
        self.assertEqual(result["status"], "EXACT_BLASCHKE_PAIR_HANKEL_PRESSURE")
        self.assertEqual(
            result["cases"][1]["toeplitz_floor"],
            {"numerator": "59", "denominator": "900"},
        )

    def test_false_norm_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["cases"][0]["claimed"]["hankel_norm"]["numerator"] = "2"
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_false_floor_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["cases"][1]["claimed"]["toeplitz_floor"]["numerator"] = "60"
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_crossing_or_beyond_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["cases"][0]["omega"] = copy.deepcopy(data["cases"][0]["delta"])
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_duplicate_case_name_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["cases"][1]["name"] = data["cases"][0]["name"]
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_boolean_integer_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["cases"][0]["delta"]["numerator"] = True
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_nonmonotone_claim_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["cases"][1]["claimed"]["hankel_norm"] = copy.deepcopy(
            data["cases"][0]["claimed"]["hankel_norm"]
        )
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)


if __name__ == "__main__":
    unittest.main()
