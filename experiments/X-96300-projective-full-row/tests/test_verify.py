import importlib.util, pathlib, unittest
P=pathlib.Path(__file__).parents[1]/'verify.py'
spec=importlib.util.spec_from_file_location('v',P);v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
class T(unittest.TestCase):
 def test_run(self):
  d=v.run();self.assertTrue(d['classification'].startswith('PASS_'));self.assertFalse(d['rh_established_by_replay'])
 def test_registry(self): self.assertEqual(v.verify_registry()['native_atoms'],327)
 def test_tail(self): self.assertEqual(v.verify_tail()['events'],51118080)
 def test_noncancel(self): self.assertIn('(x-1)(x-2)',v.verify_two_row_noncancellation()['resultant_factor'])
if __name__=='__main__': unittest.main()
