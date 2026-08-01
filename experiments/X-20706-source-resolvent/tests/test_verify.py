import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))
from verify import VerifyError, verify

BASE = json.loads(
    (Path(__file__).parents[1] / "certificates/synthetic.json").read_text()
)


class Tests(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(verify(copy.deepcopy(BASE))["verified"])

    def test_bad_metric(self):
        value = copy.deepcopy(BASE)
        value["metric_diagonal"][1] = 0
        with self.assertRaises(VerifyError):
            verify(value)

    def test_bad_kernel(self):
        value = copy.deepcopy(BASE)
        value["complement_basis"][0][0] = -1
        with self.assertRaises(VerifyError):
            verify(value)

    def test_bad_matrix(self):
        value = copy.deepcopy(BASE)
        value["A"][0][0] = -10
        with self.assertRaises(VerifyError):
            verify(value)

    def test_nonsymmetric_matrix(self):
        value = copy.deepcopy(BASE)
        value["A"][0][1] = 0
        with self.assertRaises(VerifyError):
            verify(value)


if __name__ == "__main__":
    unittest.main()
