from __future__ import annotations
import copy
import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify import VerificationError, verify  # noqa: E402


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = json.loads((ROOT / "certificates" / "synthetic.json").read_text())

    def test_pass(self):
        result = verify(copy.deepcopy(self.doc))
        self.assertEqual(result["verdict"], "EXACT_DYADIC_WEIGHTED_CHEBYSHEV_IDENTITY_VERIFIED")

    def test_energy_mutation(self):
        d = copy.deepcopy(self.doc)
        d["declared_energy"]["numerator"] += 1
        with self.assertRaises(VerificationError):
            verify(d)

    def test_negative_weight(self):
        d = copy.deepcopy(self.doc)
        d["weighted_atoms"][0]["weight"]["numerator"] = -1
        with self.assertRaises(VerificationError):
            verify(d)

    def test_duplicate_atom(self):
        d = copy.deepcopy(self.doc)
        d["weighted_atoms"][1]["n"] = 2
        with self.assertRaises(VerificationError):
            verify(d)

    def test_bad_bounds(self):
        d = copy.deepcopy(self.doc)
        d["upper_Y"] = {"numerator": 1, "denominator": 2}
        with self.assertRaises(VerificationError):
            verify(d)


if __name__ == "__main__":
    unittest.main()
