import copy, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from verify_ladder import verify
BASE={"schema":"riemann.quartic-target-ladder.v1","tau4":["0.00007434","0.00007436"],"rows":[]}
class Test(unittest.TestCase):
 def test_target_only(self): self.assertEqual(verify(copy.deepcopy(BASE))["status"],"QUARTIC_TARGET_ONLY")
 def test_overlap(self):
  d=copy.deepcopy(BASE);d["rows"]=[{"M":1,"N":2,"a4_linear":[".00007434",".00007435"],"trA4":[".00007435",".00007436"],"trK4":[".00007434",".00007436"],"jet_body_norm":["0",".1"],"readout_tail_s4":["0",".01"]}]
  self.assertEqual(verify(d)["row_verdicts"][0]["status"],"QUARTIC_ROW_OVERLAPS_TARGET")
 def test_persistent_jet(self):
  d=copy.deepcopy(BASE);d["rows"]=[{"M":1,"N":2,"a4_linear":["0","1"],"trA4":["0","1"],"trK4":["0","1"],"jet_body_norm":[".01",".02"],"readout_tail_s4":["0",".01"]}]
  self.assertEqual(verify(d)["row_verdicts"][0]["status"],"JET_BODY_PERSISTENCE_CERTIFIED")
 def test_reversed_rejected(self):
  d=copy.deepcopy(BASE);d["tau4"]=["2","1"]
  with self.assertRaises(ValueError): verify(d)
 def test_negative_norm_rejected(self):
  d=copy.deepcopy(BASE);d["rows"]=[{"M":1,"N":2,"a4_linear":["0","1"],"trA4":["0","1"],"trK4":["0","1"],"jet_body_norm":["-.1",".2"],"readout_tail_s4":["0",".01"]}]
  with self.assertRaises(ValueError): verify(d)
if __name__=="__main__": unittest.main()
