from __future__ import annotations
import copy, importlib.util, json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('x16208_verify',ROOT/'verify.py'); assert SPEC and SPEC.loader
mod=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=mod; SPEC.loader.exec_module(mod)
BASE=json.loads((ROOT/'certificate.json').read_text())
class Tests(unittest.TestCase):
 def test_production_close(self):
  out=mod.verify(copy.deepcopy(BASE)); self.assertEqual(out['classification'],'PRODUCTION_COMPLETE_ALIAS_WRAPPER_CLOSED'); self.assertLess(mod.frac(out['cross_operator_upper'],'cross'),mod.Fraction(9999999,10000000))
 def test_cross_understatement(self):
  x=copy.deepcopy(BASE); x['alias']['cross_error_upper']='4/5'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_sigma_scope(self):
  x=copy.deepcopy(BASE); x['phase']['sigma_sq_upper']='1/64'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_endpoint_method(self):
  x=copy.deepcopy(BASE); x['endpoint']['method']='P4_SOURCE_DERIVATIVE'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_endpoint_l2(self):
  x=copy.deepcopy(BASE); x['endpoint']['l2_norm_upper']='1/64'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_full_gram(self):
  x=copy.deepcopy(BASE); x['alias']['full_upper']='17'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_source_digest(self):
  x=copy.deepcopy(BASE); x['source']['actual_primitive_sha256']='bad'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_support_measure(self):
  x=copy.deepcopy(BASE); x['cofinal_block']['exceptional_measure_upper']='1'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_scalarization(self):
  x=copy.deepcopy(BASE); x['scalarization']['claimed_epsilon_upper']='9/10'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_cofinal_decay(self):
  x=copy.deepcopy(BASE); x['cofinal_decay']['next_sqrt_floor']=180
  with self.assertRaises(mod.CertificateError): mod.verify(x)
if __name__=='__main__': unittest.main()
