from __future__ import annotations
import copy, importlib.util, json, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('verify_mpfr',ROOT/'verify_mpfr.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
BASE=json.loads((ROOT/'results/mpfr-replay.json').read_text())
class TestMPFR(unittest.TestCase):
 def run_data(self,d):
  with tempfile.NamedTemporaryFile('w',delete=False,suffix='.json') as f: json.dump(d,f); p=f.name
  return v.main(p)
 def test_replay(self): self.assertEqual(self.run_data(BASE),0)
 def test_bad_terms(self):
  d=copy.deepcopy(BASE);d['prime_power_terms']-=1
  with self.assertRaises(ValueError):self.run_data(d)
 def test_non_nested(self):
  d=copy.deepcopy(BASE);d['runs'][2]['prime_upper']='7e-11'
  with self.assertRaises(ValueError):self.run_data(d)
 def test_no_backend_overlap(self):
  d=copy.deepcopy(BASE);d['binary128_grid20_lower']='1e-9';d['binary128_grid20_upper']='2e-9'
  with self.assertRaises(ValueError):self.run_data(d)
 def test_old_inside(self):
  d=copy.deepcopy(BASE);d['old_linear_midpoint']=d['runs'][1]['prime_center']
  with self.assertRaises(ValueError):self.run_data(d)
 def test_model_outside(self):
  d=copy.deepcopy(BASE);d['ordinary_zero_plus_trivial_model']='1e-8'
  with self.assertRaises(ValueError):self.run_data(d)
 def test_boolean(self):
  with self.assertRaises(TypeError):v.D(True)
if __name__=='__main__':unittest.main()
