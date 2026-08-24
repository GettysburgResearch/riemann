#!/usr/bin/env python3
from pathlib import Path
import importlib.util, sys, unittest
P=Path(__file__).resolve().parents[1]/"verify.py"
spec=importlib.util.spec_from_file_location("v",P); v=importlib.util.module_from_spec(spec); sys.modules["v"]=v; spec.loader.exec_module(v)
class Tests(unittest.TestCase):
 def test_scalar(self): self.assertEqual(v.scalar_checks(),1601)
 def test_sum_free(self): self.assertGreater(v.sum_free_checks(),2500)
 def test_record(self): self.assertTrue(v.record_checks()["explicit_lower_bound_gt_673_over_1000"])
 def test_payload(self):
  q=v.payload(); self.assertFalse(q["independent_second_replay"]["completed"]); self.assertFalse(q["ninety_percent_established"]); self.assertFalse(q["rh_established"])
if __name__=="__main__": unittest.main()
