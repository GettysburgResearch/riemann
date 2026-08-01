from __future__ import annotations
import copy, importlib.util, json, sys, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("wrapper_verify",ROOT/"verify.py")
assert SPEC and SPEC.loader
mod=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=mod; SPEC.loader.exec_module(mod)
BASE=json.loads((ROOT/"certificate.json").read_text())

class Tests(unittest.TestCase):
    def test_valid(self):
        out=mod.verify(copy.deepcopy(BASE))
        self.assertEqual(out["classification"],"EXACT_COFINAL_CCM_WRAPPER_BLOCK")
        self.assertEqual(out["cofinal_block"]["good_measure_lower"],"97/100")
    def test_alias_gap_rejected(self):
        p=copy.deepcopy(BASE); p["phase_partition"]["higher_alias_gap"]="1/10"
        with self.assertRaises(mod.CertificateError): mod.verify(p)
    def test_second_derivative_overstatement(self):
        p=copy.deepcopy(BASE); p["phase_partition"]["stationary_second_derivative_lower"]="1"
        with self.assertRaises(mod.CertificateError): mod.verify(p)
    def test_bad_cube_root(self):
        p=copy.deepcopy(BASE); p["phase_partition"]["cube_root_q"]=99
        with self.assertRaises(mod.CertificateError): mod.verify(p)
    def test_radial_understatement(self):
        p=copy.deepcopy(BASE); p["radial_replay"]["claimed_l2_sq_upper"]="1/1000000000"
        with self.assertRaises(mod.CertificateError): mod.verify(p)
    def test_zeta_understatement(self):
        p=copy.deepcopy(BASE); p["poisson_endpoint"]["zeta4_minus_one_upper"]="1/100"
        with self.assertRaises(mod.CertificateError): mod.verify(p)
    def test_no_good_support(self):
        p=copy.deepcopy(BASE); p["cofinal_block"]["mean_square_families"][0]["mean_square_upper"]="1"
        with self.assertRaises(mod.CertificateError): mod.verify(p)
    def test_scalarization_understatement(self):
        p=copy.deepcopy(BASE); p["scalarization"]["claimed_relative_epsilon_upper"]="1/100"
        with self.assertRaises(mod.CertificateError): mod.verify(p)
    def test_gap_failure(self):
        p=copy.deepcopy(BASE); p["tail_hierarchy"]["d8_lower"]="1/1000000"
        with self.assertRaises(mod.CertificateError): mod.verify(p)
    def test_digest_mismatch(self):
        p=copy.deepcopy(BASE); p["claimed_result_sha256"]="f"*64
        with self.assertRaises(mod.CertificateError): mod.verify(p)

if __name__=="__main__": unittest.main()
