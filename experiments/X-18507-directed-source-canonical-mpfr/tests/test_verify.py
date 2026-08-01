from __future__ import annotations
import copy, json, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify import verify

PRIMITIVE = json.loads((ROOT / 'primitives/c10-N2-p384.json').read_text())
TRIAL = json.loads((ROOT / 'trials/c10-N2.json').read_text())
PRIMITIVE_PATH = ROOT / 'primitives/c10-N2-p384.json'

class TestDirectedConsumer(unittest.TestCase):
    def test_base(self):
        out = verify(copy.deepcopy(PRIMITIVE), copy.deepcopy(TRIAL), PRIMITIVE_PATH)
        self.assertEqual(out['verdict'], 'CERTIFIED_DELTA_ZERO_SOURCE_CANONICAL_DIRECT_BLOCK')
        self.assertEqual(out['delta_operator_norm_upper'], '0')

    def test_source_column_mutation(self):
        d = copy.deepcopy(PRIMITIVE); d['Q_W'][0] = 0
        with self.assertRaises(ValueError): verify(d, copy.deepcopy(TRIAL), PRIMITIVE_PATH)

    def test_kernel_basis_mutation(self):
        d = copy.deepcopy(PRIMITIVE); d['Q_E'][0][0] = -1
        with self.assertRaises(ValueError): verify(d, copy.deepcopy(TRIAL), PRIMITIVE_PATH)

    def test_metric_mutation(self):
        d = copy.deepcopy(PRIMITIVE); d['metric_diagonal'][1] = 3
        with self.assertRaises(ValueError): verify(d, copy.deepcopy(TRIAL), PRIMITIVE_PATH)

    def test_support_mutation(self):
        t = copy.deepcopy(TRIAL); t['support']['N'] = 3
        with self.assertRaises(ValueError): verify(copy.deepcopy(PRIMITIVE), t, PRIMITIVE_PATH)

    def test_coercivity_mutation(self):
        t = copy.deepcopy(TRIAL); t['h'] = '1'
        with self.assertRaises(ValueError): verify(copy.deepcopy(PRIMITIVE), t, PRIMITIVE_PATH)

    def test_pivot_mutation(self):
        t = copy.deepcopy(TRIAL); t['m'] = '1'
        with self.assertRaises(ValueError): verify(copy.deepcopy(PRIMITIVE), t, PRIMITIVE_PATH)

    def test_preconditioner_shape_mutation(self):
        t = copy.deepcopy(TRIAL); t['coercivity_preconditioner_Y'][1][0] = '1'
        with self.assertRaises(ValueError): verify(copy.deepcopy(PRIMITIVE), t, PRIMITIVE_PATH)

    def test_interval_matrix_mutation(self):
        d = copy.deepcopy(PRIMITIVE); d['P_even'][0][0]['lower'] = {'mantissa': '1', 'exponent': 100}
        with self.assertRaises((ValueError, ZeroDivisionError)): verify(d, copy.deepcopy(TRIAL), PRIMITIVE_PATH)

if __name__ == '__main__': unittest.main()
