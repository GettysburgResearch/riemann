from __future__ import annotations
import copy, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
S=importlib.util.spec_from_file_location("v",ROOT/"verify.py");assert S and S.loader
V=importlib.util.module_from_spec(S);S.loader.exec_module(V)
class Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.c=json.loads((ROOT/"certificates/control.json").read_text())
 def test_control(self):
  r=V.verify(copy.deepcopy(self.c));self.assertEqual(r["verdict"],"PASS_Y4_SPARSE_FACTOR67_ROOT_COST_PACKET")
 def test_bad_range(self):
  b=copy.deepcopy(self.c);b["check_through"]=1
  with self.assertRaises(V.CertificateError):V.verify(b)
 def test_bad_log_bound(self):
  b=copy.deepcopy(self.c);b["log_2X_upper"]=1
  with self.assertRaises(V.CertificateError):V.verify(b)
 def test_formula_mutation_detected(self):
  original=V.y4_formula
  try:
   V.y4_formula=lambda q:{}
   with self.assertRaises(V.CertificateError):V.verify(copy.deepcopy(self.c))
  finally: V.y4_formula=original
if __name__=="__main__":unittest.main()
