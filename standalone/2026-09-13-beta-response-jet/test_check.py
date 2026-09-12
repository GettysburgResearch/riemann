"""Bounded tests and real CLI refusals; successful exit is the controlling result."""
from pathlib import Path
from fractions import Fraction as Q
import copy,json,subprocess,sys,tempfile,unittest
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from check import strict_load,typed_equal
from reconstruct import gamma_weight_certificate,coefficient_controls,endpoint_coefficients,endpoint_response
from interval_core import C

class Tests(unittest.TestCase):
    def test_global_majorant_algebra(self):
        r=gamma_weight_certificate()
        self.assertEqual(r['weighted_operator_cap'],'2/3')
        self.assertTrue(all(x>0 for x in r['majorant_numerator_ascending']))
    def test_independent_source_derivative(self):
        r=coefficient_controls()
        self.assertEqual(r['raw_moment_comparisons'],41)
    def test_second_endpoint_truncation(self):
        # A second degree checks enclosure agreement, not independent primitives.
        z,e=endpoint_response(C(Q(1,4),Q(4)),384)
        y,f=endpoint_response(C(Q(1,4),Q(4)),512)
        self.assertLess(max(z.re.lo,y.re.lo),min(z.re.hi,y.re.hi))
        self.assertLess(max(z.im.lo,y.im.lo),min(z.im.hi,y.im.hi))
        self.assertLess(f,e)
    def test_strict_parser_types(self):
        with self.assertRaises(ValueError):strict_load('{"a":1,"a":2}')
        with self.assertRaises(ValueError):strict_load('{"a":1.0}')
        self.assertFalse(typed_equal({'a':True},{'a':1}))
    def test_actual_cli(self):
        base=strict_load((ROOT/'result.json').read_text())
        command=[sys.executable,'-I','-S','-B']
        if not __debug__:command.append('-O')
        command += [str(ROOT/'check.py'),'--check']
        accept=subprocess.run(command+[str(ROOT/'result.json')],capture_output=True,text=True)
        self.assertEqual(accept.returncode,0,accept.stderr)
        cases=[]
        def edit(path,value):
            r=copy.deepcopy(base);d=r
            for key in path[:-1]:d=d[key]
            d[path[-1]]=value;cases.append(json.dumps(r))
        edit(['rh_proved'],True)
        edit(['unbounded_zero_confinement_proved'],True)
        edit(['native_double_collision_computed'],True)
        edit(['weighted_operator','weighted_operator_cap'],'1/3')
        edit(['weighted_operator','response_cap'],'3')
        edit(['weighted_operator','analytic_radius'],'1/4')
        edit(['weighted_operator','majorant_numerator_ascending'],[1]*10)
        edit(['native_initial_response','velocity_witness'],['-3','-2'])
        edit(['native_initial_response','root_is_xi_zero'],True)
        edit(['native_initial_response','series_degree'],True)
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'altered.json'
            for i,text in enumerate(cases):
                p.write_text(text)
                with self.subTest(case=i):
                    run=subprocess.run(command+[str(p)],capture_output=True,text=True)
                    self.assertNotEqual(run.returncode,0,'accepted altered record '+str(i))
                    self.assertIn('REJECT_BJR26',run.stderr)
        print('EXECUTED_CLI_ACCEPTANCES=1 EXECUTED_CLI_REFUSALS=10',flush=True)

if __name__=='__main__':unittest.main(verbosity=2)
