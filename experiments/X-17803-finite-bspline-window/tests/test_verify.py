import copy,importlib.util,json,sys,unittest
from pathlib import Path
H=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('x',H/'verify.py');m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
B=json.loads((H/'certificates/synthetic.json').read_text())
class T(unittest.TestCase):
 def test_ok(self):self.assertTrue(m.verify(copy.deepcopy(B))['tail_below_1e_minus_20'])
 def test_schema(self):
  d=copy.deepcopy(B);d['schema']='x'
  with self.assertRaises(ValueError):m.verify(d)
 def test_small_J(self):
  d=copy.deepcopy(B);d['J']=0
  with self.assertRaises(ValueError):m.verify(d)
 def test_low_T(self):
  d=copy.deepcopy(B);d['tail_height']=10
  with self.assertRaises(ValueError):m.verify(d)
 def test_probe(self):
  d=copy.deepcopy(B);d['symmetry_probes'][0]={'numerator':3,'denominator':1}
  with self.assertRaises(ValueError):m.verify(d)
 def test_boolean(self):
  d=copy.deepcopy(B);d['J']=True
  with self.assertRaises(ValueError):m.verify(d)
if __name__=='__main__':unittest.main()
