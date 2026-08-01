import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from verify import verify,VerificationError
BASE=json.loads((ROOT/'certificates/c5-N1-p256.json').read_text())
class T(unittest.TestCase):
 def ok(self,d): self.assertEqual(verify(d)['verdict'],'CERTIFIED_POSITIVE_REAL_D0001_DIRECT_BLOCK')
 def bad(self,d):
  with self.assertRaises(VerificationError): verify(d)
 def test_base(self): self.ok(copy.deepcopy(BASE))
 def test_support_mutation(self): d=copy.deepcopy(BASE);d['support']['c']=10;self.bad(d)
 def test_basis_mutation(self): d=copy.deepcopy(BASE);d['declared_metric']['Q_W']['integer_column'][0]='1';self.bad(d)
 def test_boolean_rational(self): d=copy.deepcopy(BASE);d['compressed']['m']['numerator']=True;self.bad(d)
 def test_nonzero_trial(self): d=copy.deepcopy(BASE);d['compressed']['X_N']['upper']['mantissa']='1';self.bad(d)
 def test_false_verdict(self): d=copy.deepcopy(BASE);d['verdict']='PASS';self.bad(d)
 def test_matrix_mutation(self): d=copy.deepcopy(BASE);d['primitive_matrices']['Q_even'][0][0]['lower']['mantissa']=str(10**80);self.bad(d)
 def test_pivot_touch(self): d=copy.deepcopy(BASE);d['compressed']['m']={'numerator':1,'denominator':2};self.bad(d)
if __name__=='__main__':unittest.main()
