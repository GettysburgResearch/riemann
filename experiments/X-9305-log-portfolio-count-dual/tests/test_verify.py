from __future__ import annotations
import importlib.util, json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("x9305",ROOT/"verify.py")
MOD=importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name]=MOD
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)
CERT=ROOT/"certificates"/"synthetic.json"

class Tests(unittest.TestCase):
    def load(self): return json.loads(CERT.read_text())
    def test_separation_and_controls(self):
        r=MOD.verify(self.load())
        self.assertEqual(r["verdict"],"SYNTHETIC_PORTFOLIO_SEPARATION")
        self.assertEqual(r["adapted_status"],"CERTIFIED_NEGATIVE")
        self.assertTrue(all(x["status"]=="CERTIFIED_NONNEGATIVE" for x in r["two_point_controls"]))
        self.assertEqual(r["negative_derivative_numerator_coefficients"],[{"numerator":2,"denominator":1}])
    def test_beta_sum_rejected(self):
        d=self.load(); d["beta"][0]={"numerator":0,"denominator":1}
        with self.assertRaises(MOD.CertificateError): MOD.verify(d)
    def test_polynomial_identity_rejected(self):
        d=self.load(); d["response_certificate"]["negative_derivative_numerator_coefficients"][0]={"numerator":3,"denominator":1}
        with self.assertRaises(MOD.CertificateError): MOD.verify(d)
    def test_negative_polynomial_rejected(self):
        d=self.load(); d["beta"]=[{"numerator":1,"denominator":1},{"numerator":-2,"denominator":1},{"numerator":1,"denominator":1}]; d["response_certificate"]["negative_derivative_numerator_coefficients"][0]={"numerator":-2,"denominator":1}
        with self.assertRaises(MOD.CertificateError): MOD.verify(d)
    def test_unsafe_cost_rejected(self):
        d=self.load(); d["cell_cost_lower_bounds"][0]={"numerator":1,"denominator":8}
        with self.assertRaises(MOD.CertificateError): MOD.verify(d)
    def test_bad_dual_rejected(self):
        d=self.load(); d["dual"]["lambdas"][0]={"numerator":1,"denominator":5}
        with self.assertRaises(MOD.CertificateError): MOD.verify(d)
    def test_two_point_control_remains_positive(self):
        r=MOD.verify(self.load())
        self.assertEqual([x["status"] for x in r["two_point_controls"]],["CERTIFIED_NONNEGATIVE","CERTIFIED_NONNEGATIVE"])

if __name__=="__main__": unittest.main()
