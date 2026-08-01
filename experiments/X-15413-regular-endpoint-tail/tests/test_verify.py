from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify import CertificateError, verify  # noqa: E402


class VerifyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads((ROOT / "certificates" / "synthetic.json").read_text())

    def test_committed_certificate(self) -> None:
        result = verify(copy.deepcopy(self.data))
        self.assertEqual(result["status"], "EXACT_REGULAR_ENDPOINT_TAIL_CORRECTION")

    def test_false_raw_determinant_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["claimed"]["raw_determinant"]["numerator"] = "1"
        with self.assertRaises(CertificateError):
            verify(data)

    def test_false_endpoint_determinant_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["claimed"]["endpoint_determinant"]["denominator"] = "2"
        with self.assertRaises(CertificateError):
            verify(data)

    def test_false_cross_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["claimed"]["anchored_cross_entries"][1]["numerator"] = "-100"
        with self.assertRaises(CertificateError):
            verify(data)

    def test_false_total_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["claimed"]["total_entries"][0]["numerator"] = "2"
        with self.assertRaises(CertificateError):
            verify(data)

    def test_unsorted_nodes_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["nodes"]["x"], data["nodes"]["y"] = data["nodes"]["y"], data["nodes"]["x"]
        with self.assertRaises(CertificateError):
            verify(data)

    def test_boolean_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["nodes"]["x"]["numerator"] = True
        with self.assertRaises(CertificateError):
            verify(data)


if __name__ == "__main__":
    unittest.main()
