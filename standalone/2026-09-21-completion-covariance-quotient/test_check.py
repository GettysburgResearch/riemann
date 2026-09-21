#!/usr/bin/env python3
"""CQT32 regression and actual altered-report CLI controls."""
import copy
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import importlib.util

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cqt32_check',ROOT/'check.py')
if spec is None or spec.loader is None:
    raise RuntimeError('cannot load local checker')
c=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=c
spec.loader.exec_module(c)

class Tests(unittest.TestCase):
    def cli(self,path):
        return subprocess.run([sys.executable,'-I','-S','-B',
            *(['-O'] if sys.flags.optimize else []),str(ROOT/'check.py'),
            '--check',str(path)],capture_output=True,text=True,timeout=90)

    def test_full_report(self):
        p=self.cli(ROOT/'results.json')
        self.assertEqual(p.returncode,0,p.stderr)
        self.assertIn('"status": "PASS"',p.stdout)

    def test_actual_cli_mutations(self):
        expected=json.loads((ROOT/'results.json').read_text())
        altered=[]
        x=copy.deepcopy(expected); x['status']='RH_proved'; altered.append(x)
        x=copy.deepcopy(expected); x['full_repo_validator_run']=True; altered.append(x)
        x=copy.deepcopy(expected); x['three_point'][0]['J_h']='0'; altered.append(x)
        x=copy.deepcopy(expected); x['closed_packets'][-1]['last_value']='0'; altered.append(x)
        x=copy.deepcopy(expected); x['rectangular'][0]['endpoint']+=1; altered.append(x)
        x=copy.deepcopy(expected); x['graph'][-1]['minimum_perturbation_energy']='0'; altered.append(x)
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'bad.json'
            for x in altered:
                with self.subTest(fields=x):
                    path.write_text(json.dumps(x))
                    p=self.cli(path)
                    self.assertEqual(p.returncode,2,p.stdout+p.stderr)
                    self.assertIn('REFUSED: report mismatch',p.stderr)
            path.write_text('{"schema":1,"schema":1}')
            p=self.cli(path)
            self.assertEqual(p.returncode,2,p.stdout+p.stderr)
            self.assertIn('duplicate JSON key',p.stderr)

    def test_direct_harmonic_double_sum(self):
        # Different summation order from coefficient-of-1*c*d evaluation.
        a=c.complete(7); b=c.complete(15); end=127
        h=c.H_table(end); actual=c.harmonic_output(a,b,end)
        for k in range(end+1):
            direct=sum((x*y*F(1,i*j)*h[k//(i*j)]
                       for i,x in a.items() for j,y in b.items()),F(0))
            self.assertEqual(actual[k],direct)

    def test_wrong_three_point_sign_rejected(self):
        a,h,ps=c.three_point(31)
        p=ps[0]; h[2*p]=-h[2*p]
        self.assertNotEqual(c.U(c.add(a,h),p),0)
        with self.assertRaisesRegex(ValueError,'unbalanced'):
            c.energy(h)

    def test_endpoint_really_fails(self):
        b=8; h={b:F(b),b+1:F(-b-1)}
        out=c.harmonic_output(h,h,b*b)
        self.assertEqual(out[b*b-1],0)
        self.assertEqual(out[b*b],1)

    def test_full_eight_denominator_closure(self):
        p,r=11,13
        z=c.convolution({p:F(-1),2*p:F(2)}, {r:F(-1),2*r:F(2)})
        z={n:2*v for n,v in z.items()}
        expected={}
        for d in (1,p,r,p*r):
            expected[2*d]=-F(2,p*r); expected[4*d]=F(2,p*r)
        actual={q:c.U(z,q) for q in range(1,4*p*r+1)}
        actual={q:v for q,v in actual.items() if v}
        self.assertEqual(actual,expected)

    def test_singular_linear_system_refused(self):
        with self.assertRaisesRegex(ValueError,'singular'):
            c.solve([[F(1),F(1)],[F(2),F(2)]],[F(0),F(0)])

    def test_float_free_result_energy(self):
        data=json.loads((ROOT/'results.json').read_text())
        for a in data['graph']:
            self.assertLessEqual(F(a['minimum_perturbation_energy']),
                                 F(a['square_reservoir_perturbation_energy']))
        self.assertFalse(data['construction_uses_future_mobius'])
        self.assertTrue(data['joint_optimizer_is_future_dependent_diagnostic'])

if __name__=='__main__':
    unittest.main()
