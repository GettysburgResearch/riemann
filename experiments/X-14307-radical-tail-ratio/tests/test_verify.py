from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x14307", ROOT / "verify.py")
assert SPEC and SPEC.loader
M = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = M
SPEC.loader.exec_module(M)


class RatioTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base = json.loads((ROOT / "certificates" / "synthetic.json").read_text())

    def run_data(self, data):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "c.json"
            path.write_text(json.dumps(data))
            return M.verify(path)

    def test_positive_control(self):
        result = self.run_data(self.base)
        self.assertEqual(result["verdict"], "CERTIFIED_BOTH_RATIO_TARGETS")

    def test_source_fourier_mutation_fails(self):
        data = copy.deepcopy(self.base)
        data["source"]["polynomial_in_z"][1] = {"numerator": -1, "denominator": 1}
        with self.assertRaises(M.CertificateError):
            self.run_data(data)

    def test_zero_source_fails(self):
        data = copy.deepcopy(self.base)
        data["source"]["polynomial_in_z"] = [
            {"numerator": 0, "denominator": 1} for _ in range(3)
        ]
        with self.assertRaises(M.CertificateError):
            self.run_data(data)

    def test_nonpositive_coercivity_fails(self):
        data = copy.deepcopy(self.base)
        data["coercivity_lower"] = {"numerator": 0, "denominator": 1}
        with self.assertRaises(M.CertificateError):
            self.run_data(data)

    def test_false_declared_bound_fails(self):
        data = copy.deepcopy(self.base)
        data["declared_linear_ratio_upper"] = {"numerator": 1, "denominator": 1000000}
        with self.assertRaises(M.CertificateError):
            self.run_data(data)

    def test_boolean_integer_fails(self):
        data = copy.deepcopy(self.base)
        data["tail_residual_upper"]["numerator"] = True
        with self.assertRaises(M.CertificateError):
            self.run_data(data)


if __name__ == "__main__":
    unittest.main()
