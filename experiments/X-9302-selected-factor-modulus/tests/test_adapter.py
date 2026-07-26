from __future__ import annotations
import importlib.util,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('adapt_x9301_selected_factor',ROOT/'adapt_x9301_selected_factor.py')
MOD=importlib.util.module_from_spec(SPEC);sys.modules[SPEC.name]=MOD;SPEC.loader.exec_module(MOD)

def R(n,d=1):return {'numerator':n,'denominator':d}
def I(a,b):return {'lower':R(a),'upper':R(b)}
def sample():
 return {
  'schema':'riemann.xi-modulus-zero-deflation.v1','classification':'RIEMANN_XI_DIRECTED','normalization_id':'riemann-xi-standard-half-s-sminus1-v1','ordinate':R(0),'log_terms':64,
  'points':[{'id':'a','u':R(1),'xi_rectangle':{'real':I(3,3),'imag':I(4,4)}},{'id':'b','u':R(2),'xi_rectangle':{'real':I(-1,2),'imag':I(0,0)}}],
  'zero_bins':[{'id':'z','lower_ordinate':R(1),'upper_ordinate':R(1),'count_lower':1,'gate':{'status':'CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND','sha256':'1'*64}}],
  'rows':[{'id':'m','kind':'deflated-monotonicity','left':'a','right':'b'}]
 }
class Tests(unittest.TestCase):
 def test_modulus_square_and_row_translation(self):
  o=MOD.adapt(sample());p={x['id']:x for x in o['points']}
  self.assertEqual(p['a']['modulus_square_interval'],I(25,25));self.assertEqual(p['b']['modulus_square_interval'],I(0,4))
  self.assertEqual(o['rows'][0]['kind'],'selected-factor-monotonicity')
 def test_boolean_count_rejected(self):
  d=sample();d['zero_bins'][0]['count_lower']=True
  with self.assertRaises(MOD.AdapterError):MOD.adapt(d)
 def test_unknown_row_rejected(self):
  d=sample();d['rows'][0]['kind']='wrong'
  with self.assertRaises(MOD.AdapterError):MOD.adapt(d)
if __name__=='__main__':unittest.main()
