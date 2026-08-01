from __future__ import annotations
import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from verify import verify
AL=json.load(open(ROOT/'certificates/aligned.json'));MI=json.load(open(ROOT/'certificates/misaligned.json'))
class T(unittest.TestCase):
 def test_aligned(self): self.assertEqual(verify(copy.deepcopy(AL))['verdict'],'CERTIFIED_SOURCE_EQUALS_DEFICIT_CANONICAL')
 def test_misaligned(self): self.assertEqual(verify(copy.deepcopy(MI))['verdict'],'CERTIFIED_DEFICIT_CANONICAL_SOURCE_NOT_IDENTIFIED')
 def test_cross(self):
  d=copy.deepcopy(AL);d['D'][2][3]=d['D'][3][2]=1
  with self.assertRaises(ValueError):verify(d)
 def test_high(self):
  d=copy.deepcopy(AL);d['D'][1][1]=1
  with self.assertRaises(ValueError):verify(d)
 def test_low(self):
  d=copy.deepcopy(AL);d['D'][3][3]=3
  with self.assertRaises(ValueError):verify(d)
 def test_metric_cross(self):
  d=copy.deepcopy(AL);d['Y_C']=[[1],[0],[1]]
  with self.assertRaises(ValueError):verify(d)
 def test_rank(self):
  d=copy.deepcopy(AL);d['source_Y']=[[1,1],[0,0],[0,0]]
  with self.assertRaises(ValueError):verify(d)
 def test_false_relation(self):
  d=copy.deepcopy(MI);d['expected_source_relation']='EQUAL'
  with self.assertRaises(ValueError):verify(d)
 def test_bool(self):
  d=copy.deepcopy(AL);d['theta']=True
  with self.assertRaises(ValueError):verify(d)
if __name__=='__main__':unittest.main()
