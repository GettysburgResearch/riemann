from __future__ import annotations
import copy, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("verify", ROOT/"verify.py")
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
BASE=json.loads((ROOT/"certificates"/"control.json").read_text())

class Tests(unittest.TestCase):
    def test_control(self):
        r=MOD.verify(copy.deepcopy(BASE))
        self.assertEqual(r["verdict"],"PASS_CPNR_SIDA_AND_PISSI_SCOPE_AUDIT")
        self.assertEqual(r["thinning_bound"],"12012")
    def test_reject_overallocated_child_mass(self):
        x=copy.deepcopy(BASE); x["alphas"]=["1/8","0"]
        with self.assertRaises(MOD.CertificateError): MOD.verify(x)
    def test_reject_negative_residual(self):
        x=copy.deepcopy(BASE); x["current"][0]="10"
        with self.assertRaises(MOD.CertificateError): MOD.verify(x)
    def test_reject_zero_diffuse_branch(self):
        x=copy.deepcopy(BASE); x["pissi_native_branch_mass"]="0"
        with self.assertRaises(MOD.CertificateError): MOD.verify(x)
    def test_reject_wrong_measure_type(self):
        x=copy.deepcopy(BASE); x["pissi_lhs_measure_type"]="diffuse"
        with self.assertRaises(MOD.CertificateError): MOD.verify(x)
    def test_reject_nonshrinking_sida(self):
        x=copy.deepcopy(BASE); x["interval_lengths"]=["1/2","1/2"]
        with self.assertRaises(MOD.CertificateError): MOD.verify(x)
    def test_reject_boolean_rational(self):
        x=copy.deepcopy(BASE); x["log2_lower"]=True
        with self.assertRaises(MOD.CertificateError): MOD.verify(x)

if __name__=="__main__": unittest.main()
