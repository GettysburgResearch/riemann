import importlib.util
from pathlib import Path
import unittest
HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('verify',HERE/'verify.py')
verify=importlib.util.module_from_spec(spec); spec.loader.exec_module(verify)
class TestT101210(unittest.TestCase):
    def test_verdict(self):
        self.assertEqual(verify.build_result()['verdict'],'PASS_T101210_FIXED_SHELL_CELL_AND_DEEP_EXCURSION_REDUCTION')
    def test_fail_closed(self):
        s=verify.build_result()['scope']
        self.assertFalse(s['sampled_deep_tail_estimate_proved'])
        self.assertFalse(s['rh_established'])
    def test_support(self):
        self.assertLess(abs(verify.K(536.0)),1e-9)
        self.assertGreater(abs(verify.K(10.0)),1e-3)
if __name__=='__main__': unittest.main()
