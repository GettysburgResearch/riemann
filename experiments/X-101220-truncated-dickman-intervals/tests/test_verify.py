import importlib.util
from pathlib import Path
import unittest
HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('verify',HERE/'verify.py')
verify=importlib.util.module_from_spec(spec); spec.loader.exec_module(verify)
class TestT101220(unittest.TestCase):
    def test_verdict(self):
        self.assertEqual(verify.build_result()['verdict'],'PASS_T101220_TRUNCATED_DICKMAN_INTERVAL_LOCALIZATION')
    def test_continuum_positive(self):
        for a in (1.5,2.0,3.0,5.0):
            self.assertGreater(verify.continuum_grid(a)[0],0)
    def test_fail_closed(self):
        s=verify.build_result()['scope']
        self.assertFalse(s['remaining_small_owner_packing_proved'])
        self.assertFalse(s['rh_established'])
if __name__=='__main__': unittest.main()
