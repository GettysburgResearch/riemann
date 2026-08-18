from __future__ import annotations
import copy,json,sys,unittest
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE))
import verify
BASE=json.loads((HERE/'certificates/control.json').read_text())
class TestRJTEAudit(unittest.TestCase):
    def reject(self,mut):
        d=copy.deepcopy(BASE);mut(d)
        with self.assertRaises(Exception):verify.validate(d)
    def test_00_baseline(self):
        out=verify.validate(copy.deepcopy(BASE));self.assertEqual(out['verdict'],'PASS_T97200_RJTE_STATE_AUDIT_AND_COMPLETION_PORT');self.assertFalse(out['rh_established'])
    def test_01_schema(self):self.reject(lambda d:d.__setitem__('schema','bad'))
    def test_02_freeze(self):self.reject(lambda d:d['frozen'].__setitem__('pr570','0'*40))
    def test_03_pr564_metadata(self):self.reject(lambda d:d['firewalls'].__setitem__('pr564_metadata_is_theorem',True))
    def test_04_promote_rjte(self):self.reject(lambda d:d['firewalls'].__setitem__('rjte_proved',True))
    def test_05_promote_tfpe(self):self.reject(lambda d:d['firewalls'].__setitem__('tfpe_proved',True))
    def test_06_promote_rh(self):self.reject(lambda d:d['firewalls'].__setitem__('rh_established',True))
    def test_07_false_cm_scope(self):self.reject(lambda d:d['firewalls'].__setitem__('eventual_rjte_equals_unmodified_complete_monotonicity',True))
    def test_08_local_compiler_promotion(self):self.reject(lambda d:d['firewalls'].__setitem__('compiler_alone_implies_boundary',True))
    def test_09_trace_promotion(self):self.reject(lambda d:d['firewalls'].__setitem__('trace_alone_implies_tfpe',True))
    def test_10_overshoot_fixture(self):self.reject(lambda d:d['finite_overshoot'].__setitem__('odd_primes',[3,5,7,11]))
    def test_11_completion_order(self):self.reject(lambda d:d['completion_diagnostic'].__setitem__('prime_order','ascending'))
    def test_12_mutation_contract(self):self.reject(lambda d:d.__setitem__('expected_mutations',11))
if __name__=='__main__':unittest.main()
