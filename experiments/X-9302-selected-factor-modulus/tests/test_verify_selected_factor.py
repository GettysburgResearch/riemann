from __future__ import annotations
import importlib.util,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('verify_selected_factor',ROOT/'verify_selected_factor.py')
MOD=importlib.util.module_from_spec(SPEC);sys.modules[SPEC.name]=MOD;SPEC.loader.exec_module(MOD)
CERT=ROOT/'certificates'/'synthetic-selected-factor.json'
class Tests(unittest.TestCase):
 def load(self):return json.loads(CERT.read_text())
 def test_strict_synthetic_separation(self):
  r=MOD.verify(self.load());self.assertEqual(r['certified_negative_rows'],2);self.assertEqual(r['verdict'],'SYNTHETIC_SELECTED_FACTOR_SEPARATION')
 def test_normalized_and_raw_have_same_negative_sign(self):
  r=MOD.verify(self.load());row=r['rows'][1]
  self.assertLess(row['raw_interval']['upper']['numerator'],0);self.assertLess(row['vandermonde_normalized_interval']['upper']['numerator'],0)
 def test_widening_zero_ball_increases_interval_width(self):
  a=self.load(); base=MOD.verify(a)['rows'][1]['vandermonde_normalized_interval']
  a['selected_zero_bins'][0]['lower_ordinate']={'numerator':999,'denominator':1000}
  a['selected_zero_bins'][0]['upper_ordinate']={'numerator':1001,'denominator':1000}
  wide=MOD.verify(a)['rows'][1]['vandermonde_normalized_interval']
  def width(x):return MOD.rat(x['upper'],'u')-MOD.rat(x['lower'],'l')
  self.assertGreater(width(wide),width(base))
 def test_bad_gate_rejected(self):
  a=self.load();a['selected_zero_bins'][0]['gate']['status']='wrong'
  with self.assertRaises(MOD.CertificateError):MOD.verify(a)
 def test_boolean_count_rejected(self):
  a=self.load();a['selected_zero_bins'][0]['count_lower']=True
  with self.assertRaises(MOD.CertificateError):MOD.verify(a)
 def test_touching_bins_rejected(self):
  a=self.load();z=dict(a['selected_zero_bins'][0]);z['id']='two';z['gate']=dict(z['gate']);z['gate']['sha256']='2'*64;a['selected_zero_bins'].append(z)
  with self.assertRaises(MOD.CertificateError):MOD.verify(a)
 def test_row_column_collision_rejected(self):
  a=self.load();a['rows'][1]['columns'][0]='u3'
  with self.assertRaises(MOD.CertificateError):MOD.verify(a)
if __name__=='__main__':unittest.main()
