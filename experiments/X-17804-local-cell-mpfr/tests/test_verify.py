from __future__ import annotations
import copy, importlib.util, json, unittest
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("v",HERE/"verify.py");v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
BASE=json.loads((HERE/"results/summary.json").read_text())
class Test(unittest.TestCase):
 def test_valid(self): self.assertEqual(v.verify(copy.deepcopy(BASE),HERE/"directed_local_cell.c")["verdict"],"DIRECTED_COMPLETE_PRIME_CELL_CLOSED")
 def test_wrong_count(self):
  d=copy.deepcopy(BASE);d["prime_power_terms"]+=1
  with self.assertRaises(ValueError):v.verify(d)
 def test_ambiguity(self):
  d=copy.deepcopy(BASE);d["precision_ladder"][1]["ambiguous_knots"]=1
  with self.assertRaises(ValueError):v.verify(d)
 def test_nesting(self):
  d=copy.deepcopy(BASE);d["precision_ladder"][2]["lower"]="2e-9"
  with self.assertRaises(ValueError):v.verify(d)
 def test_midpoint(self):
  d=copy.deepcopy(BASE);d["independent_moment_sweep_midpoint"]="0"
  with self.assertRaises(ValueError):v.verify(d)
 def test_hash(self):
  d=copy.deepcopy(BASE);d["source_sha256"]="00"
  with self.assertRaises(ValueError):v.verify(d,HERE/"directed_local_cell.c")
if __name__=="__main__":unittest.main()
