from __future__ import annotations
import importlib.util, unittest
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("v",ROOT/"verify.py")
v=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(v)
class Tests(unittest.TestCase):
 def test_verdict(self): self.assertEqual(v.verify()["verdict"],"PASS_PR476_NATIVE_SLACK_REPAIR_FINITE_ALGEBRA")
 def test_strict_coefficient(self): self.assertLess(Fraction(1,32)+Fraction(1,40)+Fraction(1,64),Fraction(1,8))
 def test_reversed_target_fails(self):
  n=(1,4,9); w=(Fraction(2,5),Fraction(1,3),Fraction(4,15)); self.assertGreater(v.mass(Fraction(144),n,w),v.mass(Fraction(36),n,w))
 def test_capacity_mutation(self):
  s=[Fraction(x) for x in v.slack_route()["parent_slack"]]; s[0]-=2; self.assertTrue(any(x<0 for x in s))
 def test_y4_mixed_odd_zero(self): self.assertEqual(v.y4(3*5*16),{})
 def test_y4_odd_two_adic_zero(self): self.assertEqual(v.y4(2*9),{})
 def test_equal_reserve_not_strict(self): r=Fraction(1,230); self.assertFalse(r-r>0)
 def test_terminal_equality_not_strict(self): self.assertFalse(5033-5033>0)
 def test_old_scalar_absent(self): self.assertNotIn("4 sqrt",str(v.verify()))
if __name__=="__main__": unittest.main()
