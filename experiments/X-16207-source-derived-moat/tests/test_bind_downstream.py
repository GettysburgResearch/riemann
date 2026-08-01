from __future__ import annotations
import copy,importlib.util,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SPEC=importlib.util.spec_from_file_location('binder',ROOT/'bind_downstream.py'); assert SPEC and SPEC.loader
mod=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=mod; SPEC.loader.exec_module(mod)
SOURCE=json.loads((ROOT/'certificate.json').read_text()); WRAPPER={'radial_replay':{},'poisson_endpoint':{},'profile_gram':{},'scalarization':{}}
class Tests(unittest.TestCase):
 def test_open_endpoint_refuses_wrapper(self):
  with self.assertRaises(mod.vmod.CertificateError): mod.bind(copy.deepcopy(SOURCE),copy.deepcopy(WRAPPER))
 def test_closed_endpoint_open_alias_refuses_wrapper(self):
  x=copy.deepcopy(SOURCE); x['endpoint_relative_ledger'].update({'normalized_fourth_derivative_l1_upper':'10','poisson_endpoint_point_upper':'1/100','poisson_endpoint_l2_sq_upper':'1/10000','poisson_endpoint_l2_norm_upper':'1/100'})
  with self.assertRaises(mod.vmod.CertificateError): mod.bind(x,copy.deepcopy(WRAPPER))
 def test_both_closed_bind_downstream(self):
  x=copy.deepcopy(SOURCE); x['endpoint_relative_ledger'].update({'normalized_fourth_derivative_l1_upper':'10','poisson_endpoint_point_upper':'1/100','poisson_endpoint_l2_sq_upper':'1/10000','poisson_endpoint_l2_norm_upper':'1/100'}); x['complete_arithmetic_alias'].update({'cross_error_upper':'1/10','full_upper':'3'})
  out=mod.bind(x,copy.deepcopy(WRAPPER)); self.assertEqual(out['profile_gram']['lower'],'8999999/10000000'); self.assertEqual(out['profile_gram']['upper'],'3'); self.assertEqual(out['poisson_endpoint']['derivative_l1_upper'],'10')
if __name__=='__main__': unittest.main()
