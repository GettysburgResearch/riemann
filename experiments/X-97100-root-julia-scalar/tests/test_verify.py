import copy,json,subprocess,sys,tempfile,unittest
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE))
import verify as V
class T(unittest.TestCase):
 def base(self):return json.loads((HERE/'certificates/control.json').read_text())
 def test_pass(self):self.assertEqual(V.validate(self.base())['verdict'],'PASS_T97100_PARITY_SAFE_SINGLE_SCALAR_ROOT_JULIA')
 def bad(self,mut):
  x=self.base();mut(x)
  with self.assertRaises(Exception):V.validate(x)
 def test_schema(self):self.bad(lambda x:x.__setitem__('schema','bad'))
 def test_cutoff(self):self.bad(lambda x:x.__setitem__('cutoff',16))
 def test_rh(self):self.bad(lambda x:x['firewalls'].__setitem__('rh_established',True))
 def test_rjte(self):self.bad(lambda x:x['firewalls'].__setitem__('rjte_proved',True))
 def test_pr559(self):self.bad(lambda x:x['firewalls'].__setitem__('imports_pr559_terminal',True))
 def test_pr556(self):self.bad(lambda x:x['firewalls'].__setitem__('imports_pr556_global',True))
 def test_parity(self):self.bad(lambda x:x['firewalls'].__setitem__('parity_blind_terminal',True))
 def test_history(self):self.bad(lambda x:x['odd_history_terminal'].__setitem__('parity',1))
 def test_genealogy(self):self.bad(lambda x:x['genealogy'].__setitem__('pr561_sha','deadbeef'))
if __name__=='__main__':unittest.main()
