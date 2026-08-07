from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("x15402verify", ROOT / "verify.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
assert spec.loader is not None
spec.loader.exec_module(module)
CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class ScalarBartaObstructionTests(unittest.TestCase):
    def test_committed_certificate(self):
        result = module.verify(copy.deepcopy(CERT))
        self.assertEqual(result["status"], "EXACT_SCALAR_BARTA_MEAN_OBSTRUCTION")
        self.assertEqual(
            result["edge_defect_sum"],
            {"numerator": "-20", "denominator": "3"},
        )

    def test_edge_sign_is_irrelevant_to_local_residual(self):
        changed = copy.deepcopy(CERT)
        changed["jump_edges"][1]["sign"] = 1
        result = module.verify(changed)
        baseline = module.verify(copy.deepcopy(CERT))
        self.assertEqual(result["barta_values"], baseline["barta_values"])

    def test_false_mean_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["claimed"]["barta_mean"]["numerator"] = 2
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_false_defect_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["claimed"]["edge_defect_sum"]["numerator"] = -19
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_nonpositive_psi_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["psi"][0]["numerator"] = 0
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_duplicate_edge_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["jump_edges"].append(copy.deepcopy(bad["jump_edges"][0]))
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_invalid_sign_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["jump_edges"][0]["sign"] = 0
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_boolean_dimension_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["vertex_count"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(bad)


if __name__ == "__main__":
    unittest.main()
