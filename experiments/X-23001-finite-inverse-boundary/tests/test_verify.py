import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import verify  # noqa: E402

CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class VerifyTests(unittest.TestCase):
    def test_central(self):
        result = verify.verify(copy.deepcopy(CERT))
        self.assertTrue(result["verified"])

    def test_wrong_schema(self):
        c = copy.deepcopy(CERT)
        c["schema"] = "wrong"
        with self.assertRaises(ValueError):
            verify.verify(c)

    def test_extra_key(self):
        c = copy.deepcopy(CERT)
        c["extra"] = 1
        with self.assertRaises(ValueError):
            verify.verify(c)

    def test_boolean_integer(self):
        c = copy.deepcopy(CERT)
        c["arithmetic_cases"][0]["K"] = True
        with self.assertRaises(TypeError):
            verify.verify(c)

    def test_bad_range(self):
        c = copy.deepcopy(CERT)
        c["arithmetic_cases"][0]["N"] = 2
        with self.assertRaises(ValueError):
            verify.verify(c)

    def test_zero_germ_constant(self):
        c = copy.deepcopy(CERT)
        c["germ_cases"][0]["g"][0] = "0"
        with self.assertRaises(ValueError):
            verify.verify(c)

    def test_bad_multiplicity(self):
        c = copy.deepcopy(CERT)
        c["germ_cases"][0]["multiplicity"] = 0
        with self.assertRaises(ValueError):
            verify.verify(c)

    def test_bad_fraction_type(self):
        c = copy.deepcopy(CERT)
        c["germ_cases"][0]["M"][0] = 0.5
        with self.assertRaises(TypeError):
            verify.verify(c)


if __name__ == "__main__":
    unittest.main()
