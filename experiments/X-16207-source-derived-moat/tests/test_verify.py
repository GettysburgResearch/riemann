from __future__ import annotations
import copy,importlib.util,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SPEC=importlib.util.spec_from_file_location('x16207_verify',ROOT/'verify.py'); assert SPEC and SPEC.loader
mod=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=mod; SPEC.loader.exec_module(mod); BASE=json.loads((ROOT/'certificate.json').read_text())
class Tests(unittest.TestCase):
 def test_radial_derivative_close_but_endpoint_stays_open(self):
  out=mod.verify(copy.deepcopy(BASE)); self.assertEqual(out['classification'],'RADIAL_DERIVATIVE_CLOSED_NORMALIZED_ENDPOINT_OPEN')
 def test_absolute_f4_cannot_close_relative_endpoint(self):
  x=copy.deepcopy(BASE); x['repaired_columns'][0]['source_fourth_derivative_l1_upper_unscaled']='1'
  out=mod.verify(x); self.assertEqual(out['classification'],'RADIAL_DERIVATIVE_CLOSED_NORMALIZED_ENDPOINT_OPEN')
 def test_endpoint_close_still_leaves_alias_open(self):
  x=copy.deepcopy(BASE); x['endpoint_relative_ledger'].update({'classification':'DIRECTED','normalized_fourth_derivative_l1_upper':'10','poisson_endpoint_point_upper':'1/100','poisson_endpoint_l2_sq_upper':'1/10000','poisson_endpoint_l2_norm_upper':'1/100'})
  out=mod.verify(x); self.assertEqual(out['classification'],'SOURCE_FIELDS_CLOSED_COMPLETE_ALIAS_GRAM_OPEN')
 def test_full_close_requires_both_alias_bounds(self):
  x=copy.deepcopy(BASE); x['endpoint_relative_ledger'].update({'classification':'DIRECTED','normalized_fourth_derivative_l1_upper':'10','poisson_endpoint_point_upper':'1/100','poisson_endpoint_l2_sq_upper':'1/10000','poisson_endpoint_l2_norm_upper':'1/100'}); x['complete_arithmetic_alias'].update({'cross_error_upper':'1/10','full_upper':'3'})
  out=mod.verify(x); self.assertEqual(out['classification'],'PRODUCTION_PROFILE_GRAM_CLOSED')
 def test_partial_alias_rejected(self):
  x=copy.deepcopy(BASE); x['complete_arithmetic_alias']['cross_error_upper']='1/10'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_radial_understatement_rejected(self):
  x=copy.deepcopy(BASE); x['source_derived_replacements']['tail_l2_sq_upper']='0'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_derivative_understatement_rejected(self):
  x=copy.deepcopy(BASE); x['source_derived_replacements']['derivative_tail_l2_sq_upper']='0'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
 def test_digest_mutation_rejected(self):
  x=copy.deepcopy(BASE); x['source']['actual_primitive_sha256']='bad'
  with self.assertRaises(mod.CertificateError): mod.verify(x)
if __name__=='__main__': unittest.main()
