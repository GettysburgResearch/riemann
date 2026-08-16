from __future__ import annotations
import copy, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("verify",ROOT/"verify.py")
V=importlib.util.module_from_spec(SPEC); assert SPEC.loader; SPEC.loader.exec_module(V)
BASE=json.loads((ROOT/"certificates"/"control.json").read_text())

class HardeningTests(unittest.TestCase):
    def test_control(self):
        self.assertEqual(V.validate(copy.deepcopy(BASE))["verdict"],
          "PASS_T96200_AFFINE_VOLTERRA_HARDENING_AND_FAIL_CLOSED_FRONTIER")
    def test_reject_schema(self):
        d=copy.deepcopy(BASE); d["schema"]="bad"
        with self.assertRaises(ValueError): V.validate(d)
    def test_reject_J_P_confusion(self):
        d=copy.deepcopy(BASE); d["normalization"]["y4_slack"]="10"
        with self.assertRaises(ValueError): V.validate(d)
    def test_reject_hidden_arithmetic_gap(self):
        d=copy.deepcopy(BASE); d["normalization"]["J"]="93"
        with self.assertRaises(ValueError): V.validate(d)
    def test_reject_old_consumer(self):
        d=copy.deepcopy(BASE); d["firewalls"]["old_t94000_endpoint_consumer"]=True
        with self.assertRaises(ValueError): V.validate(d)
    def test_reject_pr508_acceptance(self):
        d=copy.deepcopy(BASE); d["firewalls"]["pr508_directed_certificate_accepted"]=True
        with self.assertRaises(ValueError): V.validate(d)
    def test_reject_pr537_acceptance(self):
        d=copy.deepcopy(BASE); d["firewalls"]["pr537_frontier_chain_accepted"]=True
        with self.assertRaises(ValueError): V.validate(d)
    def test_reject_mpfr_waiver(self):
        d=copy.deepcopy(BASE); d["firewalls"]["mpfr_full_artifact_required"]=False
        with self.assertRaises(ValueError): V.validate(d)
    def test_reject_affine_drift(self):
        d=copy.deepcopy(BASE); d["affine"]["u_bar"]="3/4"
        with self.assertRaises(ValueError): V.validate(d)
    def test_reject_cost_K_drift(self):
        d=copy.deepcopy(BASE); d["cost"]["K"]+=1
        with self.assertRaises(ValueError): V.validate(d)
    def test_reject_witness_sign(self):
        d=copy.deepcopy(BASE); d["review503_witness"]["upper"]="1/100"
        with self.assertRaises(ValueError): V.validate(d)
    def test_reject_rh_claim(self):
        d=copy.deepcopy(BASE); d["firewalls"]["rh_established"]=True
        with self.assertRaises(ValueError): V.validate(d)

if __name__=="__main__": unittest.main()
