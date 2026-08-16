from __future__ import annotations
import importlib.util,sys,unittest
from pathlib import Path
HERE=Path(__file__).resolve(); VERIFY=HERE.parents[1]/'verify.py'
SPEC=importlib.util.spec_from_file_location('x91880_verify',VERIFY); assert SPEC and SPEC.loader
M=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=M; SPEC.loader.exec_module(M)
class TestT91880(unittest.TestCase):
    def test_baseline(self):
        p=M.validate(); self.assertEqual(p['capacity']['native_total'],60989); self.assertTrue(p['identity']['same_row_identity'])
    def test_q2_obstruction(self):
        p=M.q2_score_obstruction(); self.assertTrue(p['numerator_negative']); self.assertTrue(p['denominator_positive'])
    def test_three_firewalls(self):
        self.assertEqual(M.rough_lift_separator()['lower'],'1/9'); self.assertEqual(M.volterra_causal_firewall()['witness']['p'],67)
    def test_all_mutations(self): self.assertEqual(len(M.run_mutations()),len(M.MUTATIONS))
if __name__=='__main__': unittest.main()
