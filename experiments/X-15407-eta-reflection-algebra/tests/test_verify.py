from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("x15407verify", ROOT / "verify.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
assert spec.loader is not None
spec.loader.exec_module(module)

CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class EtaReflectionTests(unittest.TestCase):
    def test_committed_certificate(self):
        out = module.verify(copy.deepcopy(CERT))
        self.assertEqual(out["status"], "EXACT_ETA_REFLECTION_ALGEBRA")
        self.assertEqual(out["reflected_product"], {"numerator": "-10", "denominator": "1"})

    def test_eta_constant_and_linear_moments(self):
        out = module.verify(copy.deepcopy(CERT))
        zero = {
            "rational": {"numerator": "0", "denominator": "1"},
            "sqrt2": {"numerator": "0", "denominator": "1"},
        }
        self.assertEqual(out["constant_moment"], zero)
        self.assertEqual(out["linear_moment"], zero)
        self.assertEqual(out["pole_polynomial_value"], zero)

    def test_false_energy_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["claimed"]["h_times_window_energy"]["sqrt2"]["numerator"] = -2
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_false_reflection_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["reflection_control"]["Fref"]["numerator"] = -4
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_false_second_ratio_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["reflection_control"]["zeta_second_ratio"]["numerator"] = -2
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_negative_selberg_input_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["selberg_control"]["lambda"][3]["numerator"] = -1
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_boolean_integer_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["reflection_control"]["F"]["numerator"] = True
        with self.assertRaises(module.CertificateError):
            module.verify(bad)

    def test_bad_schema_rejected(self):
        bad = copy.deepcopy(CERT)
        bad["schema"] = "riemann.invalid"
        with self.assertRaises(module.CertificateError):
            module.verify(bad)


if __name__ == "__main__":
    unittest.main()
