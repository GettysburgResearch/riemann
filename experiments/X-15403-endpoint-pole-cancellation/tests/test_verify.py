from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("x15403verify", ROOT / "verify.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
assert spec.loader is not None
spec.loader.exec_module(module)

CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class EndpointPoleCancellationTests(unittest.TestCase):
    def test_committed_certificate(self):
        out = module.verify(copy.deepcopy(CERT))
        self.assertEqual(out["status"], "EXACT_ENDPOINT_POLE_CANCELLATION")
        self.assertEqual(out["cancelled_main"], {"numerator": "0", "denominator": "1"})
        self.assertEqual(out["discrepancy_value"], {"numerator": "-288", "denominator": "35"})

    def test_false_pole_hankel_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["claimed"]["pole_hankel"]["numerator"] = 10
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_false_discrepancy_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["claimed"]["discrepancy_value"]["numerator"] = -287
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_bad_discrepancy_length_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["discrepancy_weights"].pop()
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_nonpositive_scale_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["pole_scale"] = {"numerator": 0, "denominator": 1}
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_bad_laplace_ratio_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["laplace_ratio"] = {"numerator": 1, "denominator": 1}
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_boolean_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["profile"][0]["numerator"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_profile_mutation_requires_new_claims(self):
        bad = copy.deepcopy(CERT)
        bad["profile"][1]["numerator"] = -1
        with self.assertRaises(module.CertificateError):
            module.verify(bad)


if __name__ == "__main__":
    unittest.main()
