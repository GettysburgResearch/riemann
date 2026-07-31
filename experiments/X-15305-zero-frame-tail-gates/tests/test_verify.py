from __future__ import annotations
import copy, importlib.util, json, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(verify)

BASE = json.loads((ROOT / "certificates" / "synthetic.json").read_text())

class GateTests(unittest.TestCase):
    def test_positive(self):
        out = verify.verify(copy.deepcopy(BASE))
        self.assertEqual(out["visible_schur_floor"], {"numerator":"87","denominator":"40"})
        self.assertEqual(out["global_floor"], {"numerator":"-2","denominator":"125"})

    def test_zero_margin_rejected(self):
        x = copy.deepcopy(BASE)
        x["sigma2"] = {"numerator":13,"denominator":40}
        with self.assertRaises(verify.CertificateError):
            verify.verify(x)

    def test_negative_component_rejected(self):
        x = copy.deepcopy(BASE)
        x["assembly_radius"] = -1
        with self.assertRaises(verify.CertificateError):
            verify.verify(x)

    def test_zero_h_rejected(self):
        x = copy.deepcopy(BASE)
        x["ambient_coercivity"] = 0
        with self.assertRaises(verify.CertificateError):
            verify.verify(x)

    def test_false_beta_rejected(self):
        x = copy.deepcopy(BASE)
        x["claimed_beta"] = 1
        with self.assertRaises(verify.CertificateError):
            verify.verify(x)

    def test_false_epsilon_rejected(self):
        x = copy.deepcopy(BASE)
        x["claimed_epsilon"] = 1
        with self.assertRaises(verify.CertificateError):
            verify.verify(x)

    def test_boolean_rejected(self):
        x = copy.deepcopy(BASE)
        x["sigma2"] = True
        with self.assertRaises(verify.CertificateError):
            verify.verify(x)

    def test_wrong_schema_rejected(self):
        x = copy.deepcopy(BASE)
        x["schema"] = "bad"
        with self.assertRaises(verify.CertificateError):
            verify.verify(x)

if __name__ == "__main__":
    unittest.main()
