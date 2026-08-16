import importlib.util, pathlib, unittest
P=pathlib.Path(__file__).parents[1]/'native_arithmetic.py'
s=importlib.util.spec_from_file_location('native_arithmetic',P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class Tests(unittest.TestCase):
    def test_counterexample_split(self):
        d=m.pr503_and_finite_q_witness();self.assertTrue(d['finite_Q_lower_gt_1_over_5'])
    def test_live_fibres(self):
        self.assertEqual(m.live_anchored_leaf_fixture()['cutoff'],133)
        self.assertEqual(m.live_bulk_fixture()['x'],16)
    def test_mutations(self):
        self.assertGreaterEqual(len(m.mutation_checks()),14)
if __name__=='__main__':unittest.main()
