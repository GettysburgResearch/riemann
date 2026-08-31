"""Source-level and hostile controls for the infinite variational certificates."""
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'research/riemann-structures/native-five-hour-pass/infinite-source'


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


base=load('tested_infinite_variational',HERE/'variational_certificate.py')
negative=load('tested_ordered_refutation',HERE/'variational_ordered_dual_refutation.py')


class InfiniteVariationalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=negative.build()

    def test_typed_json_aliases_refused(self):
        self.assertFalse(base.typed_equal({'x':True},{'x':1}))
        self.assertFalse(base.typed_equal({'x':1},{'x':1.0}))

    def test_duplicate_json_key_refused(self):
        with self.assertRaises(ValueError):base.json.loads('{"x":1,"x":2}',object_pairs_hook=base.unique_object)

    def test_all_twenty_terminal_moments_and_all_sixty_four_currents(self):
        L,Q,_,_=base.terminal_vectors(F)
        record=base.literal_terminal_control([base.HEIGHT*l+base.HEIGHT**2*q for l,q in zip(L,Q)])
        self.assertEqual(len(record['direct_moment_difference21']),21)
        self.assertEqual(len(record['all64_current_differences']),64)

    def test_corrupted_terminal_vector_refused(self):
        L,Q,_,_=base.terminal_vectors(F);delta=[base.HEIGHT*l+base.HEIGHT**2*q for l,q in zip(L,Q)]
        delta[2]+=F(1,10**6)
        with self.assertRaisesRegex(ValueError,'all20'):base.literal_terminal_control(delta)

    def test_literal_ordered_arc_moments_match_seven_column_formula(self):
        y=(F(-1,10),F(6,5),F(-1,2),F(3,5),F(19,20));a,b,c,d,t=y
        z=-a/b;fv=a+b*t;gw=c+d*t
        points=[(F(0),F(0),F(0)),(z,F(0),F(0)),(t,fv,F(0)),
                (t,F(1),F(0)),(t,F(1),gw),(F(1),F(1),c+d),(F(1),F(1),F(1))]
        measured=[base.monomial_path(points,e,i) for e,i in base.MOMENT_FORMS]
        x=negative.profile(y);expected=[F(0)]*20
        expected[0]=x[1];expected[9]=-2*x[2]+1;expected[6]=2*x[3]
        expected[1]=expected[3]=expected[16]=x[4];expected[17]=1-x[4]
        expected[12]=expected[13]=expected[19]=1-2*x[5]
        expected[5]=expected[7]=expected[14]=2*x[6]
        expected[11]=1
        self.assertEqual(measured,expected)

    def test_refutation_status(self):
        self.assertEqual(self.result['status'],'CERTIFIED_REGISTERED_K1_K2_K3_DUALS_ALL_FAIL')

    def test_all_three_registered_witnesses_retained(self):
        self.assertEqual([x['K'] for x in self.result['witnesses']],[1,2,3])

    def test_every_refutation_upper_endpoint_negative(self):
        for row in self.result['witnesses']:
            self.assertLess(F(row['early_branch_gap_interval'][1]),0)

    def test_root_contraction_strict(self):
        self.assertLess(F(self.result['contraction_upper']),1)

    def test_full_optimizer_flag_stays_false(self):
        self.assertIs(self.result['full_three_coordinate_optimizer_certified'],False)

    def test_base_hash_is_live(self):
        self.assertEqual(negative.sha256(negative.BASE.read_bytes()).hexdigest(),negative.BASE_SHA)

    def test_bool_K_is_not_a_registered_integer(self):
        self.assertTrue(all(type(row['K']) is int for row in self.result['witnesses']))


if __name__=='__main__':unittest.main()
