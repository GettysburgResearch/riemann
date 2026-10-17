"""Independent arithmetic anchors and separate-process negative controls."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from fractions import Fraction as Q
import verify

ROOT=Path(__file__).resolve().parent
class CertificateTests(unittest.TestCase):
    def setUp(self): self.p=verify.read_parameters(ROOT/'parameters.json')
    def test_new_seven_margins(self):
        expected={'theta':Q(17,400),'principal_w':Q(10299971,200000000),
          'principal_z':Q(524999,10000000),'small':Q(2158349,10000000),
          'exceptional':Q(8410759,200000000),'good':Q(8479981,200000000),
          'large':Q(507999,100000)}
        self.assertEqual(verify.margins(self.p),expected)
    def test_original_CT_table(self):
        p=dict(self.p)
        p.update(alpha=Q(67,100),beta=Q(151,400),w_line=Q(3,25),
          sigma_good=Q(8801,10000),exception_exponent=Q(317,500),
          small_cutoff=Q(1,5),large_cutoff=Q(3301,10000),large_z=Q(50000))
        expected=[Q(1,32),Q(37749867,10**9),Q(384999,10**7),
            Q(471999,10**7),Q(2617,80000),Q(7949,250000),Q(1481,2500)]
        self.assertEqual(list(verify.margins(p).values()),expected)
    def test_density_and_growth_anchors(self):
        r=verify.validate(self.p)
        self.assertEqual(r['density']['maximum'],Q(2563,4267))
        self.assertEqual(r['density']['height_coefficient_in_d'],Q(9,68))
        self.assertEqual(r['scales']['f_growth'],Q(37,120))
        self.assertEqual(r['scales']['zero_free_boundary'],Q(23,24))
    def test_convex_domain_segments(self):
        # Independent points inside each of the three coordinate moves.
        x=Q(8201,10000);y=Q(181,1000);z=Q(2,5)
        for j in range(21):
            t=Q(j,20)
            for xyz in [(4+t*(x-4),Q(4),Q(2)),(x,Q(4),2+t*(z-2)),(x,4+t*(y-4),z)]:
                self.assertGreater(min(verify.domain(*xyz).values()),0)
    def test_density_height_uniform_in_degree(self):
        # Algebraic bound: rho*Hd <= (lambda-g)/16 by (9); no finite-degree inference.
        gap=Q(601,1000)-Q(2563,4267)
        eta=gap/16
        self.assertLess(eta+gap/16+eta*Q(1,10**6),gap)
    def test_normal_and_optimized_outputs(self):
        a=subprocess.check_output([sys.executable,str(ROOT/'verify.py')])
        b=subprocess.check_output([sys.executable,'-O',str(ROOT/'verify.py')])
        self.assertEqual(a,b)
        self.assertEqual(a,(ROOT/'CHECKS.json').read_bytes())
    def test_duplicate_and_float_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'p.json'
            p.write_text('{"alpha":"1/2","alpha":"2/3"}')
            with self.assertRaises(verify.CertificateError): verify.read_parameters(p)
            raw=json.loads((ROOT/'parameters.json').read_text());raw['alpha']=.55
            p.write_text(json.dumps(raw))
            with self.assertRaises(verify.CertificateError): verify.read_parameters(p)
    def test_six_actual_mutated_optimized_processes(self):
        bad={'no_density':('exception_exponent','1'),
             'old_good_line':('sigma_good','8801/10000'),
             'old_normalization':('normalization','61/100'),
             'no_large_gap':('large_cutoff','9/20'),
             'invalid_w_domain':('w_line','17/100'),
             'unpaid_saving':('claimed_saving','1/20')}
        raw=json.loads((ROOT/'parameters.json').read_text())
        for name,(key,value) in bad.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                p=Path(td)/'bad.json'; data=dict(raw);data[key]=value;p.write_text(json.dumps(data))
                run=subprocess.run([sys.executable,'-O',str(ROOT/'verify.py'),'--parameters',str(p)],capture_output=True)
                self.assertNotEqual(run.returncode,0)
                self.assertIn(b'REJECTED:',run.stderr)

if __name__=='__main__': unittest.main(verbosity=2)
