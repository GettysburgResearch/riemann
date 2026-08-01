from __future__ import annotations
import copy, json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from verify import Reject, verify
BASE=json.loads((ROOT/'certificates/synthetic.json').read_text())

def q(a,b=1): return {'numerator':a,'denominator':b}

class TestFullComplement(unittest.TestCase):
    def test_control(self):
        out=verify(copy.deepcopy(BASE))
        self.assertEqual(out['status'],'CERTIFIED_FULL_COMPLEMENT_AND_SHARP_COUNT')
        self.assertEqual(out['count_upper'],2)
        self.assertEqual(out['count_lower'],2)
        self.assertEqual(out['angle_squared_upper'],q(1,100))

    def test_nonorthogonal_split_rejected(self):
        d=copy.deepcopy(BASE); d['complement_basis'][0][0]=q(1)
        with self.assertRaises(Reject): verify(d)

    def test_incomplete_packet_rejected(self):
        d=copy.deepcopy(BASE); d['complement_basis'][3][1]=q(0)
        with self.assertRaises(Reject): verify(d)

    def test_frame_failure_rejected(self):
        d=copy.deepcopy(BASE); d['threshold']=q(8)
        with self.assertRaises(Reject): verify(d)

    def test_radical_moat_failure_rejected(self):
        d=copy.deepcopy(BASE); d['evaluation_gram'][0][0]=q(1)
        with self.assertRaises(Reject): verify(d)

    def test_threshold_order_rejected(self):
        d=copy.deepcopy(BASE); d['radical_evaluation_upper']=q(2)
        with self.assertRaises(Reject): verify(d)

    def test_boolean_rejected(self):
        d=copy.deepcopy(BASE); d['threshold']['numerator']=True
        with self.assertRaises(Reject): verify(d)

    def test_expected_tamper_rejected(self):
        d=copy.deepcopy(BASE); d['expected']['count_upper']=1
        with self.assertRaises(Reject): verify(d)

    def test_metric_failure_rejected(self):
        d=copy.deepcopy(BASE); d['metric'][3][3]=q(0)
        with self.assertRaises(Reject): verify(d)

if __name__=='__main__': unittest.main()
