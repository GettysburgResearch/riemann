import importlib.util
from pathlib import Path
import unittest
HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('verify',HERE/'verify.py')
verify=importlib.util.module_from_spec(spec); spec.loader.exec_module(verify)
class TestT101200(unittest.TestCase):
    def test_verdict(self):
        self.assertEqual(verify.build_result()['verdict'],'PASS_T101200_AUDITED_CLOSURE_IMPLICATION_HYPERMATRIX')
    def test_fail_closed(self):
        s=verify.build_result()['scope']
        self.assertFalse(s['typed_cell_certificates_proved'])
        self.assertFalse(s['exceptional_cell_sparsity_proved'])
        self.assertFalse(s['rh_established'])
    def test_separator(self):
        self.assertEqual(verify.h(1)*verify.h(3)-verify.h(2)**2,-10680)
if __name__=='__main__': unittest.main()
