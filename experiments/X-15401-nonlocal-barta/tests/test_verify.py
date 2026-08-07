from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("x154verify", ROOT / "verify.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
assert spec.loader is not None
spec.loader.exec_module(module)

CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class NonlocalBartaTests(unittest.TestCase):
    def test_committed_certificate(self):
        out = module.verify(copy.deepcopy(CERT))
        self.assertEqual(out["status"], "EXACT_SYNTHETIC_NONLOCAL_BARTA_POLAR_FLOOR")
        self.assertEqual(out["barta_floor"], {"numerator": "1", "denominator": "1"})
        self.assertEqual(out["target_floor"], {"numerator": "1", "denominator": "2"})
        self.assertEqual(out["edge_signs"], [1, -1])

    def test_negative_potential_still_positive(self):
        out = module.verify(copy.deepcopy(CERT))
        self.assertEqual(out["barta_values"][2], {"numerator": "1", "denominator": "1"})

    def test_false_barta_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["claimed"]["barta_floor"]["numerator"] = 2
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_false_resolvent_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["claimed"]["odd_resolvent"]["numerator"] = 405
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_rank_one_gate_fail_closed(self):
        bad = copy.deepcopy(CERT)
        bad["polar_a"] = {"numerator": 10, "denominator": 1}
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_nonpositive_psi_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["psi"][1] = {"numerator": 0, "denominator": 1}
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_duplicate_edge_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["jump_edges"].append(copy.deepcopy(bad["jump_edges"][0]))
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_invalid_edge_sign_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["jump_edges"][1]["sign"] = 0
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_boolean_integer_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["vertex_count"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_boundary_not_promoted(self):
        bad = copy.deepcopy(CERT)
        # Make tau*resolvent = 1 exactly by setting a=1961/808.
        bad["polar_a"] = {"numerator": 1961, "denominator": 808}
        with self.assertRaises(module.CertificateError):
            module.verify(bad)


if __name__ == "__main__":
    unittest.main()
